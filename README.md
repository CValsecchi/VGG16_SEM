![repo version](https://img.shields.io/badge/Version-v.%201.1-green)
![python version](https://img.shields.io/badge/python-v.3.6-blue)
[![License](https://img.shields.io/github/license/italia/bootstrap-italia.svg)](https://github.com/italia/bootstrap-italia/blob/master/LICENSE)

# VGG16 for SEM images
Pretrained VGG16 adapted to classify SEM images of coralline algae

![Screenshot](VGG16_CNNSEM.png)

This repository contains all the necessary files to fine tune a pretrained VGG16 CNN starting from custom images and to predict SEM images of calcareous red algae using saved models.
For more information regarding the method, have a look at:
REF

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following prerequisites are needed:

*[Anaconda Python 3.8*](https://www.anaconda.com/products/individual)

Install conda from the [official website](https://www.anaconda.com/products/individual). Once conda is installed, it can be used to generate the environment saved in the environment.yml file.

The environment can be created with conda as follows (after saving the environment.yml file in the working directory):

```
conda env create -f environment.yml
```

Activate jupyter notebook inside the environment as follows:

```
conda activate kerasclonenv
jupyter notebook
```

Now go to the notebooks directory.

## Using the notebook

There are two notebooks allowing to reproduce the work in REF.
1. "CNN_SEM_VGG16_MODEL" contains the code used for the training and prediction in the Internal validatione and External test setups.
2. "EXPLANATION" allows to load the saved models, predict custom images and return the explanation in terms of LIME, GradCAM and saliency.

Example images are present in the "images" folder.
