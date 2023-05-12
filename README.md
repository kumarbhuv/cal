## Fine Grained Image Classification: A study on effect of causality on prediction


Implementation of CAL and Testing from the repo raoyongming/CAL
The credit for original implementation goes to Yongming Rao.

## Datasets
The instructions to download and install FGVC datasets is given below:-

<b> CUB Dataset </b>

Caltech-UCSD Birds (CUB) dataset is provided by Caltech Vision Lab. The dataset can be downloaded from this [link](https://www.vision.caltech.edu/datasets/cub_200_2011/).
The CUB-200 dataset consists of 11,788 images of 200 bird species, with each species having between 30 to 60 images.
The dataset folder should have the following structure:

```
CUB_dataset_root_folder/
    └─ images
    └─ image_class_labels.txt
    └─ train_test_split.txt
    └─ ....
```
<b> FGVC-Aircraft Dataset </b>

The FGVC-Aircraft-2013 dataset contains 10,000 images of airplanes, with each category having between 80 to 100 images. The Dataset is provided by Oxford Univeristy under the [link](https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/). 

The dataset folder should have the following structure:

```
aircraft_dataset_root_folder/
    └─ data
        └─ images
            ├─ 0034309.jpg
            ├─ 0034958.jpg
            ├─ ...
        ├─ families.txt
        ├─ images_box.txt
        ├─ ...
    ├─ evaluation.m
    ├─ example_evaluation.m
    ├─ ...

```

## Training & Evaluation
- Modify `config_train.py` to run experiments on different datasets
- Run `bash run.sh` to train models.
- Set configurations in ```config_infer.py``` and run  `python infer.py` to conduct multi-crop evaluation.

## Requirements
* Python 3
* PyTorch 1.6+


