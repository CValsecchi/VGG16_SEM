![repo version](https://img.shields.io/badge/Version-v.%201.1-green)
![python version](https://img.shields.io/badge/python-v.2.6-blue)
![license](https://img.shields.io/badge/license-CC_BY_4.0-orange)

# CNN for SEM Images

![Screenshot](VGG16_CNNSEM.png)

This repository contains all the necessary files to fine tune a pretrained VGG16 CNN starting from custom images and to predict SEM images of calcareous red algae using saved models.
For more information regarding the method, have a look at:
REF

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following prerequisites are needed:

*[Python 3.6*](https://www.python.org/download/releases/3.6/)


### Creation of the Conda environment

Install conda from the [official website](https://www.anaconda.com/download/). Once conda is installed, it can be used to generate the environment saved in the environment.yml file.

The environment can be created with conda as follows (after saving the environment.yml file in the working directory):
```
conda env create -f environment.yml
```
Activate jupyter notebook inside the environment as follows:

```
conda activate env
jupyter notebook
```
Now go to the notebooks directory.

## Using the notebook
There are two notebooks allowing to reproduce the work in REF.
1. "CNN_SEM_VGG16_MODEL" allows to replicate the training and prediction in the Internal validatione and External test setups.
2. "EXPLANATION" allows to load the saved models, predict custom images and return the explanation in terms of LIME, GradCAM and saliency.


## Authors

* **Cecile Valsecchi** (https://github.com/grisoniFr)
* **Gabriele Sottocornola** (https://github.com/grisoniFr)
* **Giulia Piazza**

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
See the [LICENSE.md](LICENSE.md) file for additional details. 
