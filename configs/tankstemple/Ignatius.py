_base_ = '../default.py'

expname = 'dvgo_Ignatius'
basedir = './logs/tanks_and_temple'

data = dict(
    datadir='./data/TanksAndTempleBG/Train',
    dataset_type='nsvf',
    load2gpu_on_the_fly=True,
    white_bkgd=True,
)

coarse_train = dict(
    pervoxel_lr_downrate=2,
)

