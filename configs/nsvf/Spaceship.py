_base_ = '../default.py'

expname = 'dvgo_Spaceship'
basedir = './logs/nsvf_synthetic'

data = dict(
    datadir='./data/Synthetic_NSVF/Spaceship',
    dataset_type='nsvf',
    white_bkgd=True,
)

