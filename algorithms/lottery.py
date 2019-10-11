import math
import random


class Lottery:

    def lot_1(self, entry, people):
        i_entries = people * entry
        f_prob = (entry / i_entries) * 100
        return f_prob

    ''' Add power ball '''
    def power_ball(self, numbers_a, b_positions):
        n_win_num = numbers_a - b_positions
        n_num_fac = math.factorial(n_win_num)
        pos_fac = math.factorial(b_positions)
        num_fac = math.factorial(numbers_a)
        full_num_com = num_fac / (math.factorial(b_positions)
                                  * math.factorial(numbers_a - b_positions))
        data_1 = []
        data_2 = []
        print(full_num_com)
        for i in range(1, b_positions):
            a = pos_fac / (math.factorial(i) * math.factorial(b_positions-i))
            tmp = b_positions - i
            b = n_num_fac / (math.factorial(tmp)
                             * math.factorial(n_win_num - tmp))
            data_1.append(a)
            data_2.append(b)
        prob = []
        for i in range(len(data_1)):
            a = (data_1[i] * data_2[i]) / full_num_com
            prob.append(a)
        return prob

    def player(self, amount, game):
        games = float(amount / game)
        population = 40000000
        gpp = float(games / population)
        return games, gpp

    ''' Needs work '''

    def game(self, size, numbers):
        a = [0, 0, 0, 0, 0]
        cycle = 0
        # win = [15, 23, 34, 51, 55]
        while (True):
            for i in range(size):
                a[i] = random.randint(1, 69)
                cycle = cycle + 1
                print(a)
                if (cycle > 10000000):
                    return a
