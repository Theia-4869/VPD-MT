# Depth Estimation with VPD-MT
## Getting Started  

1. Install the [mmcv-full](https://github.com/open-mmlab/mmcv) library and some required packages.

```bash
pip install openmim
mim install mmcv-full
pip install -r requirements.txt
```

2. Prepare NYUDepthV2 datasets following [GLPDepth](https://github.com/vinvino02/GLPDepth) and [BTS](https://github.com/cleinc/bts/tree/master).

```
mkdir nyu_depth_v2
wget http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/nyu_depth_v2_labeled.mat
python extract_official_train_test_set_from_mat.py nyu_depth_v2_labeled.mat splits.mat ./nyu_depth_v2/official_splits/
```

Download sync.zip provided by the authors of BTS from this [url](https://drive.google.com/file/d/1AysroWpfISmm-yRFGBgFTrLy6FjQwvwP/view) and unzip in `./nyu_depth_v2` folder. 

Your dataset directory should be:

```
│nyu_depth_v2/
├──official_splits/
│  ├── test
│  ├── train
├──sync/
```

## Results and Fine-tuned Models

|  | RMSE | d1 | d2 | d3 | REL  | log_10 |
|-------------------|-------|-------|--------|--------|--------|-------|
| **VPD-MT** | 0.313 | 0.938 | 0.993 | 0.998 | 0.085 | 0.037 |

## Training

Run the following instuction to train the VPD-Depth model. We recommend using 8 NVIDIA A100 GPUs to train the model with a total batch size of 24. 

```
bash train2k.sh <LOG_DIR>
```

## Evaluation
Command format:
```
bash test.sh <CHECKPOINT_PATH>
```