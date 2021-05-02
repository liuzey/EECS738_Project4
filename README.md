# EECS738_Project4 Treasure Hunters Inc.
EECS738 Machine Learning course project4. In this project, dynamic programming with different policies is used to solve a GridWorld task. Specifically, two policies are implemented: policy iteration and value iteration. The problem is to let the robot move towards the distination and collect rewards by taking moves in the square grids. Every move indicates a reward varying in actions, and the route is along with accumulative rewards. So the action is taken by assessing the current situation and make optimal choices. Underlying principles of dynamic programming is Markov Decision Process (MDP).

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
* **-a**: Length of the grid.
* **-b**: Width of the grid.
* **-t**: A string of termination states coordinates, e.g. '6532' for two states (6,5) (3,2). Due to the implementation, the coordiante should be less than  10. For coordinates bigger than 10, please modify [here](https://github.com/liuzey/EECS738_Project4/blob/2a882a7c39ec8b418773b8f5cd6b161002c9d32f/main.py#L23) into a list of coordiante in format \[\[x1,y1\],\[x2,y2\],\[x3,y3\]...\].
* **-s**:

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

