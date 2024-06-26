# Semantic Segmentation with VPD-MT
## Getting Started 

1. Install the [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) library and some required packages.

```bash
pip install openmim
mim install mmcv-full
mim install mmsegmentation
```

2. Follow the guide in [mmseg](https://github.com/open-mmlab/mmsegmentation/blob/master/docs/dataset_prepare.md) to prepare the ADE20k dataset.


## Results and Fine-tuned Models

| Model | Config | Head | Crop Size | Lr Schd | mIoU |
|:---:|:---:|:---:|:---:|:---:| :---:|:---:|:---:|
| ```VPDSeg_SD-1-5``` | [config](configs/fpn_vpd_sd1-5_512x512_gpu8x2_ade2k_seq.py) | Semantic FPN | 512x512 | 8K | 41.5 |

## Training
```
bash dist_train.sh <CONFIG_PATH> <NUM_GPUS>
```
We use 8 GPUs by default.

## Evaluation
Command format:
```
bash dist_test.sh <CONFIG_PATH> <CHECKPOINT_PATH> <NUM_GPUS> --eval mIoU
```
To evaluate a model with multi-scale and flip, run
```
bash dist_test.sh <CONFIG_PATH> <CHECKPOINT_PATH> <NUM_GPUS> --eval mIoU --aug-test
```
