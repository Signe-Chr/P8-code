import scipy.io
mat = scipy.io.loadmat('TestData/S02_session_1_block_8_processed.mat') 

#Laver ændring
# Data structure:
# dict_keys(['__header__', '__version__', '__globals__', 'cfg'])
# 'cfg': 
#   'blockProperties',
        # 'SNR', 
        # 'LE', 
        # 'SU', 
        # 'SU_all', 
        # 'Task'
#   'EEGLAB', 
        # 'EEG', 
        # 'ICremoved'
#   'trial'
        # 'intervalEEG',




cfg = mat['cfg']
#print(type(cfg))
#print(cfg.shape)

#cfg = cfg[0, 0]
#print(cfg.dtype.names)
#('blockProperties', 'EEGLAB', 'trial')

bp = cfg['trial'][0, 0]
print(bp.dtype.names)
