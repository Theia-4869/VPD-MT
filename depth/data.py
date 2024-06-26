import os
import numpy as np

np.random.seed(0)


filenames_pth = "dataset/filenames/nyudepthv2/train_list.txt"

if __name__ == '__main__':
    with open(filenames_pth, 'r') as f:
        filenames = f.readlines()

    part_filenames = np.random.choice(filenames, 2000, replace=False)

    part_filenames_pth = filenames_pth.replace('train_list', 'part_list')
    print("save part_filenames to {}".format(part_filenames_pth))

    with open(part_filenames_pth, 'w') as f:
        f.writelines(part_filenames)
