#!/usr/bin/env python

import numbers

import numpy as np
import pycuda.driver as drv
import pycuda.elementwise as elementwise
import pycuda.gpuarray as gpuarray
from pycuda.tools import dtype_to_ctype

# List of available numerical types provided by numpy: 
num_types = [np.typeDict[t] for t in \
             np.typecodes['AllInteger']+np.typecodes['AllFloat']]

# Numbers of bytes occupied by each numerical type:
num_nbytes = dict((np.dtype(t), t(1).nbytes) for t in num_types)

def set_realloc(x_gpu, data):
    """
    Transfer data into a GPUArray instance.

    Copies the contents of a numpy array into a GPUArray instance. If
    the array has a different type or dimensions than the instance,
    the GPU memory used by the instance is reallocated and the
    instance updated appropriately.
    
    Parameters
    ----------
    x_gpu : pycuda.gpuarray.GPUArray
        GPUArray instance to modify.
    data : numpy.ndarray
        Array of data to transfer to the GPU.

    Examples
    --------
    >>> import pycuda.gpuarray as gpuarray
    >>> import pycuda.autoinit
    >>> import numpy as np
    >>> import misc
    >>> x = np.asarray(np.random.rand(5), np.float32)
    >>> x_gpu = gpuarray.to_gpu(x)
    >>> x = np.asarray(np.random.rand(10, 1), np.float64)
    >>> set_realloc(x_gpu, x)
    >>> np.allclose(x, x_gpu.get())
    True
    
    """

    # Only reallocate if absolutely necessary:
    if x_gpu.shape != data.shape or x_gpu.size != data.size or \
        x_gpu.strides != data.strides or x_gpu.dtype != data.dtype:
        
        # Free old memory:
        x_gpu.gpudata.free()

        # Allocate new memory:
        nbytes = num_nbytes[data.dtype]
        x_gpu.gpudata = drv.mem_alloc(nbytes*data.size)
    
        # Set array attributes:
        x_gpu.shape = data.shape
        x_gpu.size = data.size
        x_gpu.strides = data.strides
        x_gpu.dtype = data.dtype
        
    # Update the GPU memory:
    x_gpu.set(data)

def bufint(a):
    """
    Return buffer interface to GPU array.

    Parameters
    ----------
    a : pycuda.gpuarray.GPUArray
        GPU array.

    Returns
    -------
    b : buffer
        Buffer interface to array.
    """

    assert isinstance(a, gpuarray.GPUArray)
    return a.gpudata.as_buffer(a.nbytes)

def set_by_inds(dest_gpu, ind, src_gpu, ind_which='dest'):
    """
    Set values in a GPUArray by index.

    Parameters
    ----------
    dest_gpu : pycuda.gpuarray.GPUArray
        GPUArray instance to modify.
    ind : pycuda.gpuarray.GPUArray or numpy.ndarray
        1D array of element indices to set. Must have an integer dtype.
    src_gpu : pycuda.gpuarray.GPUArray
        GPUArray instance from which to set values.
    ind_which : str
        If set to 'dest', set the elements in `dest_gpu` with indices `ind`
        to the successive values in `src_gpu`; the lengths of `ind` and
        `src_gpu` must be equal. If set to 'src', set the
        successive values in `dest_gpu` to the values in `src_gpu` with indices
        `ind`; the lengths of `ind` and `dest_gpu` must be equal.

    Notes
    -----
    Only supports 1D index arrays.

    May not be efficient for certain index patterns because of lack of inability
    to coalesce memory operations.
    """

    # Only support 1D index arrays:
    assert len(np.shape(ind)) == 1
    assert dest_gpu.dtype == src_gpu.dtype
    assert issubclass(ind.dtype.type, numbers.Integral)
    N = len(ind)
    if ind_which == 'dest':
        if N != len(src_gpu):
            raise ValueError('len(ind) == %s != %s == len(src_gpu)' % (N, len(src_gpu)))
    elif ind_which == 'src':
        if N != len(dest_gpu):
            raise ValueError('len(ind) == %s != %s == len(dest_gpu)' % (N, len(dest_gpu)))
    else:
        raise ValueError('invalid value for `ind_which`')
    data_ctype = dtype_to_ctype(dest_gpu.dtype)
    ind_ctype = dtype_to_ctype(ind.dtype)
    if not isinstance(ind, gpuarray.GPUArray):
        ind = gpuarray.to_gpu(ind)
    v = "{data_ctype} *dest, {ind_ctype} *ind, {data_ctype} *src".format(data_ctype=data_ctype, ind_ctype=ind_ctype)
    if ind_which == 'dest':
        func = elementwise.ElementwiseKernel(v, "dest[ind[i]] = src[i]")
    else:
        func = elementwise.ElementwiseKernel(v, "dest[i] = src[ind[i]]")
    func(dest_gpu, ind, src_gpu, range=slice(0, N, 1))
