import os

data_root = "data/ade/ADEChallengeData2016"
anno_file = "sceneCategories.txt"
cate_list = ['factory_outdoor', 'warehouse_outdoor', 'sinkhole', 'quonset_hut_outdoor', 'mesa', 'brewery_indoor', 'pharmacy', 'steel_mill_indoor', 'performance', 'riding_arena', 'road', 'athletic_field_outdoor', 'pumping_station', 'recycling_plant_indoor', 'mobile_home']

if __name__ == "__main__":
    train_dict = {}
    val_dict = {}
    test_dict = {}
    num = 0

    with open(os.path.join(data_root, anno_file), "r") as f:
        annos = f.readlines()
        for anno in annos:
            file_name, category_id = anno.strip().split(" ")
            if "val" not in file_name:
                continue

            if category_id not in val_dict:
                val_dict[category_id] = 1
            else:
                val_dict[category_id] += 1
    
    with open(os.path.join(data_root, anno_file), "r") as f:
        annos = f.readlines()
        for anno in annos:
            file_name, category_id = anno.strip().split(" ")
            if "train" not in file_name:
                continue

            if category_id not in val_dict:
                if category_id in cate_list:
                    if category_id not in train_dict:
                       train_dict[category_id] = 1
                    else:
                       train_dict[category_id] += 1

                    if train_dict[category_id] <= 1:
                        os.system("cp {} {}".format(os.path.join(data_root, "images/training", file_name+".jpg"), os.path.join(data_root, "images/partraining", file_name+".jpg")))
                        os.system("cp {} {}".format(os.path.join(data_root, "annotations/training", file_name+".png"), os.path.join(data_root, "annotations/partraining", file_name+".png")))
                        num += 1
                continue

            if category_id not in train_dict:
                train_dict[category_id] = 1
            else:
                train_dict[category_id] += 1

            if train_dict[category_id] <= val_dict[category_id]:
                os.system("cp {} {}".format(os.path.join(data_root, "images/training", file_name+".jpg"), os.path.join(data_root, "images/partraining", file_name+".jpg")))
                os.system("cp {} {}".format(os.path.join(data_root, "annotations/training", file_name+".png"), os.path.join(data_root, "annotations/partraining", file_name+".png")))
                num += 1

    print(num)
