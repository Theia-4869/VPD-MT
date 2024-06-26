# VPD-MT

This repository contains PyTorch implementation for <ins>**V**</ins>isual <ins>**P**</ins>erception <ins>**D**</ins>iffusion Models with <ins>**M**</ins>ultiple <ins>**T**</ins>imestamps. VPD-MT is a framework that leverages the high-level and low-level knowledge of a pre-trained text-to-image diffusion model to downstream visual perception tasks.

## Installation
Clone this repo, and run
```
git submodule init
git submodule update
```
Download the checkpoint of [stable-diffusion](https://github.com/runwayml/stable-diffusion) (we use `v1-5` by default) and put it in the `checkpoints` folder. Please also follow the instructions in [stable-diffusion](https://github.com/runwayml/stable-diffusion) to install the required packages.

## Semantic Segmentation with VPD-MT
Equipped with a lightweight Semantic FPN and trained for 8K iterations on $512\times512$ crops, our VPD-MT can achieve 41.5 mIoU on ADE2K.

Please check [segmentation.md](./segmentation/README.md) for detailed instructions.

## Depth Estimation with VPD-MT
VPD obtains 0.313 RMSE on NYUv2k depth estimation benchmark, establishing the new state-of-the-art.

|  | RMSE | d1 | d2 | d3 | REL  | log_10 |
|-------------------|-------|-------|--------|--------|--------|-------|
| **VPD-MT** | 0.313 | 0.938 | 0.993 | 0.998 | 0.085 | 0.037 |

Please check [depth.md](./depth/README.md) for detailed instructions on training and inference.

## License
MIT License

## Acknowledgements
This code is based on [stable-diffusion](https://github.com/CompVis/stable-diffusion), [mmsegmentation](https://github.com/open-mmlab/mmsegmentation), [VPD](https://github.com/wl-zhao/VPD), and [DatasetDM](https://github.com/showlab/DatasetDM).
