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
* **-a**: Length of the grid. Default value is 6.
* **-b**: Width of the grid. Default value is 5.
* **-t**: A string of termination states coordinates, e.g. '6532' for two states (6,5) (3,2). Due to the implementation, the coordiante should be less than 10. For coordinates bigger than 10, please modify [here](https://github.com/liuzey/EECS738_Project4/blob/2a882a7c39ec8b418773b8f5cd6b161002c9d32f/main.py#L23) directly into a list of coordiante pairs in format \[\[x1,y1\],\[x2,y2\],\[x3,y3\]...\].
* **-s**: A string of Starting position of the robot, e.g. '65' for start point at (6,5). Similar as **-t**, for coordinates bigger than 10, please modify [here](https://github.com/liuzey/EECS738_Project4/blob/06cf92b103c795e21c1fb0925556c04a4f60404c/main.py#L22) directly into coordiante pair in format \[x0,y0\].

### Example
```bash
{python main.py -a 10 -b 10 -t 004578616367699397 -s 11} 
```
* A grid task of 10\*10.
* Bot starts in position (1,1).
* Multiple destinations: (0,0) (4,5) (7,8) (6,1) (6,3) (6,7) (6,9) (9,3) (9,7).


## Results

![](https://github.com/liuzey/EECS738_Project4/blob/main/pics/all.gif)

## Notes
* After reaching each destination, the situation is evaluated again. Thus, the bot makes a optimal set of choices step after step for the current situation. In this way, the final route may not be the globally optimal route.
* Adding obstacles follows the same logic, but treating obstacle cells as walls. It is easy to implement but comlicated in different parameters in dynamic programming, thus it is not included.

## Schedule
- [x] Set up a new git repository in your GitHub account
- [x] Think up a map-like environment with treasure, obstacles and opponents
- [x] Choose a programming language (Python, C/C++, Java) **Python**
- [x] Formulate ideas on how reinforcement learning can be used to find treasure efficiently while avoiding obstacles and opponents
- [x] Build one or more reinforcement policies to model situational assessments, actions and rewards programmatically
- [x] Document your process and results
- [x] Commit your source code, documentation and other supporting files to the git repository in GitHub

## Reference
* EECS 690 Introduction to Machine Learning Course Materials.
* numpy.arange - Numpy APIs. https://numpy.org/doc/stable/reference/generated/numpy.arange.html
* matplotlib.pyplot.ion - Matplotlib Documentation. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html

