import scipy.io
mat = scipy.io.loadmat('TestData/S02_session_1_block_8_processed.mat') 
#dict_keys(['__header__', '__version__', '__globals__', 'cfg'])




cfg = mat['cfg']
#print(type(cfg))
#print(cfg.shape)

#cfg = cfg[0, 0]
#print(type(cfg))
#print(cfg.dtype)
#print(cfg.dtype.names)
#('blockProperties', 'EEGLAB', 'trial')

bp = cfg['blockProperties'][0, 0]
print(bp.dtype.names)
