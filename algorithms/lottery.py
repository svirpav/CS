import math
import random


class Lottery:

    def lot_1(self, entry, people):
        i_entries = people * entry
        f_prob = (entry / i_entries) * 100
        return f_prob

    def power_ball(self, numbers, b_positions):
        fac_numbers = math.factorial(numbers)
        fac_positions = math.factorial(b_positions)
        fac_combinations = math.factorial(numbers - b_positions)
        un_combinations = fac_numbers / (fac_positions * fac_combinations)
        print("factorial for unique combinations %d " % un_combinations)
        prob = []
        num = []
        for i in range(1, b_positions):
            a = numbers - i
            b = b_positions - i
            a_fac = math.factorial(a)
            b_fac = math.factorial(b)
            ab_fac = math.factorial(a - b)
            comb = float(a_fac / (b_fac * ab_fac))
            prob.append(float((comb / un_combinations) * 100))
            num.append(i)
        prob.append(float((1.0 / un_combinations) * 100))
        num.append(b_positions)
        return num, prob

    def player(self, amount, game):
        games = float(amount / game)
        population = 40000000
        gpp = float(games / population)
        return games, gpp

    def game(self, size, numbers):
        a = [0, 0, 0, 0, 0]
        cycle = 0
        win = [15, 23, 34, 51, 55]
        while (True):
            for i in range(size):
                a[i] = random.randint(1, 69)
                cycle = cycle + 1
                if (a == win):
                    return a
