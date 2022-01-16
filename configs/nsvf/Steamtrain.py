_base_ = '../default.py'

expname = 'dvgo_Steamtrain'
basedir = './logs/nsvf_synthetic'

data = dict(
    datadir='./data/Synthetic_NSVF/Steamtrain',
    dataset_type='nsvf',
    white_bkgd=True,
)

