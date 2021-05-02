# EECS738_Project4 Treasure Hunters Inc.
EECS738 Machine Learning course project4. In this project, dynamic programming with different policies is used to solve a GridWorld task. Specifically, two policies are implemented: policy iteration and value iteration. The problem is to let the robot move towards the distination and collect rewards by taking moves in the square grids. Every move indicates an reduced rewards, varying in actions. So the action is taken by assessing the current situation and make optimal choices. Underlying principles of dynamic programming is Markov Decision Process (MDP).

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
- [x] Think up a map-like environment with treasure, obstacles and opponents
- [x] Choose a programming language (Python, C/C++, Java) **Python**
- [x] Formulate ideas on how reinforcement learning can be used to find treasure efficiently while avoiding obstacles and opponents
- [x] Build one or more reinforcement policies to model situational assessments, actions and rewards programmatically
- [x] Document your process and results
- [x] Commit your source code, documentation and other supporting files to the git repository in GitHub

## Reference
* 

