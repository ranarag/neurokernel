# use of 0.0 instead of 0 where float is expected

RET_INPUTS = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6']
MED_INPUTS = ['C2', 'C3', 'Mi1, 'Tm1', 'Tm2']
NEURON_LIST = [
    {'name':'R1', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R2', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R3', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R4', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R5', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R6', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    #
    {'name':'C2', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'C3', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'Mi1', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'Tm1', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'Tm2', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},

    #
    {'name':'L1', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-47.54, 'initn':0.3525, 'offset':0.0},
    {'name':'L2', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-53.04, 'initn':0.3525, 'offset':0.0},
    {'name':'L3', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-48.57, 'initn':0.3525, 'offset':0.0},
    {'name':'L4', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-5.0, 'V2':25.0, 'V3':20.0, 'V4':35.0,
    'V_l':-60.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':2.0, 'G_k':16.0,
    'phi':0.001, 'initV':-58.4155, 'initn':0.0104, 'offset':0.0},
    {'name':'L5', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-5.0, 'V2':25.0, 'V3':20.0, 'V4':35.0,
    'V_l':-60.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':2.0, 'G_k':16.0,
    'phi':0.001, 'initV':-50.98, 'initn':0.0104, 'offset':0.0},
    {'name':'T1', 'model':'MorrisLecar_a', 'columnar':True, 'output':False,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-5.0, 'V2':25.0, 'V3':20.0, 'V4':35.0,
    'V_l':-60.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':2.0, 'G_k':16.0,
    'phi':0.001, 'initV':-59.64, 'initn':0.0104, 'offset':0.0},
    {'name':'Am', 'model':'MorrisLecar_a', 'columnar':True, 'output':False,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-48.57, 'initn':0.3525, 'offset':0.0}
]

# use of 0.0 instead of 0 where float is expected
SYNAPSE_LIST = [
    {'prename':'R1', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':40, 'mode':0},
    {'prename':'R2', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':43, 'mode':0},
    {'prename':'R3', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':37, 'mode':0},
    {'prename':'R4', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':38, 'mode':0},
    {'prename':'R5', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':38, 'mode':0},
    {'prename':'R6', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':45, 'mode':0},
    {'prename':'R1', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':46, 'mode':0},
    {'prename':'R2', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':45, 'mode':0},
    {'prename':'R3', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':39, 'mode':0},
    {'prename':'R4', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':41, 'mode':0},
    {'prename':'R5', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':39, 'mode':0},
    {'prename':'R6', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':47, 'mode':0},
    {'prename':'R1', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.02', 'power':1.0, 'saturation':10.0,
    'scale':11, 'mode':0},
    {'prename':'R2', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.02', 'power':1.0, 'saturation':10.0,
    'scale':10, 'mode':0},
    {'prename':'R3', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.02', 'power':1.0, 'saturation':10.0,
    'scale':4, 'mode':0},
    {'prename':'R4', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.02', 'power':1.0, 'saturation':10.0,
    'scale':8, 'mode':0},
    {'prename':'R5', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.02', 'power':1.0, 'saturation':10.0,
    'scale':6, 'mode':0},
    {'prename':'R6', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.02', 'power':1.0, 'saturation':10.0,
    'scale':12, 'mode':0},
    {'prename':'L1', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.01', 'power':0.1, 'saturation':10.0,
    'scale':100, 'mode':0},
    {'prename':'L5', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-58.5, 'slope':0.1', 'power':0.1, 'saturation':5.0,
    'scale':20, 'mode':0},
    {'prename':'L2', 'postname':'L4', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.1', 'power':0.1, 'saturation':10.0,
    'scale':4, 'mode':0},
    {'prename':'L2', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.1', 'power':0.1, 'saturation':10.0,
    'scale':35, 'mode':0},
    {'prename':'L1', 'postname':'C2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':52, 'mode':0},
    {'prename':'L1', 'postname':'C3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':61, 'mode':0},
    {'prename':'L5', 'postname':'C2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-58.5, 'slope':0.01', 'power':1.0, 'saturation':5.0,
    'scale':12, 'mode':0},
    {'prename':'L5', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-58.5, 'slope':0.01', 'power':1.0, 'saturation':5.0,
    'scale':5, 'mode':0},
    {'prename':'C2', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-54.9, 'slope':0.02', 'power':1.0, 'saturation':3.0,
    'scale':44, 'mode':0},
    {'prename':'C2', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-54.9, 'slope':0.04', 'power':1.0, 'saturation':3.0,
    'scale':36, 'mode':0},
    {'prename':'C2', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-54.9, 'slope':0.02', 'power':1.0, 'saturation':3.0,
    'scale':29, 'mode':0},
    {'prename':'C2', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-54.9, 'slope':0.02', 'power':1.0, 'saturation':3.0,
    'scale':15, 'mode':0},
    {'prename':'C3', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-53.9, 'slope':0.02', 'power':1.0, 'saturation':3.0,
    'scale':42, 'mode':0},
    {'prename':'C3', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-53.9, 'slope':0.02', 'power':1.0, 'saturation':3.0,
    'scale':9, 'mode':0},
    {'prename':'R1', 'postname':'a1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':19, 'mode':0},
    {'prename':'R2', 'postname':'a1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':16, 'mode':0},
    {'prename':'R2', 'postname':'a2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':22, 'mode':0},
    {'prename':'R3', 'postname':'a2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':18, 'mode':0},
    {'prename':'R3', 'postname':'a3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':20, 'mode':0},
    {'prename':'R4', 'postname':'a3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':16, 'mode':0},
    {'prename':'R4', 'postname':'a4', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':17, 'mode':0},
    {'prename':'R5', 'postname':'a4', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':26, 'mode':0},
    {'prename':'R5', 'postname':'a5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':10, 'mode':0},
    {'prename':'R6', 'postname':'a5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':14, 'mode':0},
    {'prename':'R6', 'postname':'a6', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':22, 'mode':0},
    {'prename':'R1', 'postname':'a6', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':17, 'mode':0},
    {'prename':'a1', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':1, 'mode':0},
    {'prename':'a2', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':1, 'mode':0},
    {'prename':'a3', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':1, 'mode':0},
    {'prename':'a4', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':3, 'mode':0},
    {'prename':'a5', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':5, 'mode':0},
    {'prename':'a6', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':1, 'mode':0},
    {'prename':'a1', 'postname':'T1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':8, 'mode':0},
    {'prename':'a2', 'postname':'T1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':6, 'mode':0},
    {'prename':'a3', 'postname':'T1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':7, 'mode':0},
    {'prename':'a4', 'postname':'T1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':12, 'mode':0},
    {'prename':'a5', 'postname':'T1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':3, 'mode':0},
    {'prename':'a6', 'postname':'T1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':13, 'mode':0},
    {'prename':'a5', 'postname':'L4', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-50.0, 'slope':0.01', 'power':1.0, 'saturation':10.0,
    'scale':3, 'mode':0},
    {'prename':'L4', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':3, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':2, 'mode':0},
    {'prename':'L4', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':3, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':4, 'mode':0},
    {'prename':'L4', 'postname':'L4', 'model':'power_gpot_gpot_sig',
    'cart':3, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':1, 'mode':0},
    {'prename':'L4', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':3, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':2, 'mode':0},
    {'prename':'L4', 'postname':'L2', 'model':'power_gpot_gpot_sig',
    'cart':2, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':3, 'mode':0},
    {'prename':'L4', 'postname':'L3', 'model':'power_gpot_gpot_sig',
    'cart':2, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':1, 'mode':0},
    {'prename':'L4', 'postname':'L4', 'model':'power_gpot_gpot_sig',
    'cart':2, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':2, 'mode':0},
    {'prename':'L2', 'postname':'L4', 'model':'power_gpot_gpot_sig',
    'cart':6, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.04', 'power':1.0, 'saturation':10.0,
    'scale':4, 'mode':0},
    {'prename':'L2', 'postname':'L4', 'model':'power_gpot_gpot_sig',
    'cart':5, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.04', 'power':1.0, 'saturation':10.0,
    'scale':2, 'mode':0},
    {'prename':'L4', 'postname':'L4', 'model':'power_gpot_gpot_sig',
    'cart':4, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.04', 'power':1.0, 'saturation':5.0,
    'scale':2, 'mode':0}
]
