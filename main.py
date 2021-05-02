import numpy as np
import argparse
from algorithm import DP
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

parser = argparse.ArgumentParser()
parser.add_argument("-a", type=int, default=6, help='Map size: length.')
parser.add_argument("-b", type=int, default=5, help='Map size: width.')
parser.add_argument("-t", type=str, default='00', help='List of locations of rewards.')
parser.add_argument("-s", type=str, default='00', help='Bot start location.')
args = parser.parse_args()

A = args.a
B = args.b
START = [int(args.s[0]), int(args.s[1])]
LOCATIONS = [[int(args.t[2 * i]), int(args.t[2 * i + 1])] for i in range(0, len(args.t)//2)]
GAMMA = 0.5

def visual(route):
    local = LOCATIONS[:]
    ax = plt.subplot(111)
    plt.ion()
    for item in route:
        ax.cla()
        x1 = np.arange(item[0], item[0]+2)
        ax.fill_between(x1, item[1], item[1]+1, facecolor='green')
        for reward in local:
            x2 = np.arange(reward[0], reward[0]+2)
            ax.fill_between(x2, reward[1], reward[1]+1, facecolor='red')

        plt.xlim(0, A)
        plt.ylim(0, B)

        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.grid(True, which='major')
        ax.yaxis.grid(True, which='major')
        plt.pause(1)

        if item in local:
            local.remove(item)

if __name__ == '__main__':
    init_V = np.zeros((A, B))
    dp = DP.DynamicProgramming(gamma=GAMMA, term_states=LOCATIONS)
    route = dp.policy_iter(np.copy(init_V), START)
    visual(route)