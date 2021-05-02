# EECS738_Project4 Treasure Hunters Inc.
EECS738 Machine Learning course project4. 

## Ideas and Thinking
* 

## Setup
### Environment
* Python 3.9
* MacOS or Linux

### Package
* Recommend setting up a virtual environment. Different versions of packages may cause unexpected failures.
* Install packages in **requirements.txt**.
```bash
pip install -r requirements.txt
``` 

## Usage
### Positional & Optional Parameters
* **data**: Dataset name (task) to choose from 'mnist' and 'gtsrb'.
* **-p**: Whether to load pre-trained model parameters. The parameters for MNIST model is saved in ['./paras'](https://github.com/liuzey/EECS738_Project3/tree/main/paras). The parameters for GTSRB model is saved in ['./paras_save'](https://github.com/liuzey/EECS738_Project3/tree/main/paras_save). (Default: False).
* **-s**: Whether to save the trained model parameters (Default: False).

### Example
```bash
python main.py 'gtsrb' -s 1 -p 1
```
* 'gtsrb': GTSRB recognition task.
* -p: Model parameters are pre-trained and loaded.
* -s: Trained parameters are saved periodically.


## Result Analysis 

## Notes
* 

## Schedule
- [x] Set up a new git repository in your GitHub account
- [x] Pick two datasets from https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research
- [x] Choose a programming language (Python, C/C++, Java) **Python**
- [x] Formulate ideas on how neural networks can be used to accomplish the task for the specific dataset
- [x] Build a neural network to model the prediction process programmatically
- [x] Document your process and results
- [x] Commit your source code, documentation and other supporting files to the git repository in GitHub

## Reference
* 

