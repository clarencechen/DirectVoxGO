_base_ = '../default.py'

expname = 'dvgo_Robot'
basedir = './logs/nsvf_synthetic'

data = dict(
    datadir='./data/Synthetic_NSVF/Robot',
    dataset_type='nsvf',
    white_bkgd=True,
)

