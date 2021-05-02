import numpy as np

class DynamicProgramming:
    def __init__(self, gamma=0.9, p_r=0.25, p_s=0.25, reward=-1, term_states=None):
        self.gamma = gamma
        self.p_r = p_r
        self.p_s = p_s
        self.reward = reward
        self.term_states = term_states[:]

    def per_policy_iter(self, v):
        E_r = 4 * self.reward * self.p_r
        k = 0
        while True:
            print('k: {}'.format(k))
            print(v)
            print('\n')
            v_new = np.copy(v)
            for i in range(v.shape[0]):
                for j in range(v.shape[1]):
                    if [i, j] in self.term_states:
                        continue
                    v_new[i, j] = E_r + self.gamma * (self.p_s * v[max(i-1, 0), j] + self.p_s * v[i, max(j-1, 0)] \
                                               + self.p_s * v[min(i+1, v.shape[0]-1), j] + self.p_s * v[i, min(j+1, v.shape[1]-1)])
            if np.max(np.abs(v_new-v)) < 0.001:
                print('k: {}'.format(k+1))
                print(v_new)
                print('\nConverged.\n')
                return v_new
            else:
                v = v_new
            k += 1

    def policy_iter(self, v, s):
        start = s[:]
        final_print = ''
        final_route = []
        while len(self.term_states) > 0:
            v_new = self.per_policy_iter(v[:])
            start, print_out, route = self.go(start, v_new)
            self.term_states.remove(start)
            final_print += print_out[:-10]
            final_route.extend(route)
        final_print += print_out[-10:]
        print('Final route: \n' + final_print[:-4])
        return final_route

    def per_value_iter(self, v):
        k = 0
        while True:
            print('k: {}'.format(k))
            print(v)
            print('\n')
            v_new = np.copy(v)
            for i in range(v.shape[0]):
                for j in range(v.shape[1]):
                    if [i, j] in self.term_states:
                        continue
                    v_new[i, j] = max(self.reward + self.gamma * v[max(i-1, 0), j], self.reward + self.gamma * v[i, max(j-1, 0)],
                                      self.reward + self.gamma * v[min(i+1, v.shape[0]-1), j], self.reward + self.gamma * v[i, min(j+1, v.shape[1]-1)])
            if (v_new == v).all():
                print('k: {}'.format(k+1))
                print(v_new)
                print('\nConverged.\n')
                return v_new
            else:
                v = v_new
            k += 1

    def value_iter(self, v, s):
        start = s[:]
        final_print = ''
        final_route = []
        while len(self.term_states) > 0:
            v_new = self.per_value_iter(v[:])
            start, print_out, route = self.go(start, v_new)
            self.term_states.remove(start)
            final_print += print_out[:-10]
            final_route.extend(route)
        final_print += print_out[-10:]
        print('Final route: \n' + final_print[:-4])
        return final_route

    def go(self, s, v):
        start = s[:]
        printout = ''
        new_start = start[:]
        i = 0
        route = [start, ]
        while i == 0 or new_start != start:
            start = new_start[:]
            a_ = max(start[0]-1, 0)
            b_ = min(start[0]+1, v.shape[0]-1)
            c_ = max(start[1]-1, 0)
            d_ = min(start[1]+1, v.shape[1]-1)
            printout += str(start) + ' -> '
            neighbors = [[start[0], start[1]], [a_, start[1]], [b_, start[1]], [start[0], c_], [start[0], d_]]
            neighbors_v = [v[start[0], start[1]], v[a_, start[1]], v[b_, start[1]], v[start[0], c_], v[start[0], d_]]
            new_start = neighbors[neighbors_v.index(max(neighbors_v))]
            route.append(new_start)
            i += 1
        print(printout[:-4], '\n')
        return new_start, printout, route


if __name__ == '__main__':
    init_V = np.zeros((5, 6))
    start = [1, 1]
    dp = DynamicProgramming(term_states=[[0, 0], [0, 5], [1, 3]])
    route = dp.policy_iter(np.copy(init_V), start)
