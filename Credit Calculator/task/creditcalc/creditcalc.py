import math
import argparse


class CreditCalculator:
    def __init__(self):
        self.args = None

    def sol_num_month(self):
        nomi_interest = self.args[3] / 12 / 100
        self.args[2] = math.log(self.args[4] / (self.args[4] - nomi_interest * self.args[1]), 1 + nomi_interest)
        self.args[2] = math.ceil(self.args[2])
        year = self.args[2] // 12
        month = self.args[2] % 12
        if year == 0 and month == 1:
            print(f'You need {month} month to repay this credit!')
        elif year == 1 and month > 1:
            print(f'You need {year} year and {month} months to repay this credit!')
        elif year > 1 and month == 1:
            print(f'You need {year} years and {month} month to repay this credit!')
        else:
            print(f'You need {year} years and {month} months to repay this credit!')
        print(f'Overpayment = {self.overpayment()}')

    def sol_annui_pay(self):
        nomi_interest = self.args[3] / 12 / 100
        self.args[4] = self.args[1] * (nomi_interest * (1 + nomi_interest) ** self.args[2]) / (
                (1 + nomi_interest) ** self.args[2] - 1)
        self.args[4] = math.ceil(self.args[4])
        print(f'Your annuity payment = {self.args[4]}!')
        print(f'Overpayment = {self.overpayment()}')

    def sol_principal(self):
        nomi_interest = self.args[3] / 12 / 100
        self.args[1] = self.args[4] / ((nomi_interest * (1 + nomi_interest) ** self.args[2]) / (
                (1 + nomi_interest) ** self.args[2] - 1))
        self.args[1] = math.floor(self.args[1])
        print(f'Your credit principal = {self.args[1]}!')
        print(f'Overpayment = {self.overpayment()}')

    def sol_diff(self):
        nomi_interest = self.args[3] / 12 / 100
        pay_sum = 0
        for i in range(1, self.args[2] + 1):
            month_pay = self.args[1] / self.args[2] + nomi_interest * (
                        self.args[1] - self.args[1] * (i - 1) / self.args[2])
            month_pay = math.ceil(month_pay)
            pay_sum += month_pay
            print(f'Month {i}: paid out {month_pay}')
        print(f'\nOverpayment = {int(pay_sum - self.args[1])}')

    def overpayment(self):
        return int(self.args[4] * self.args[2] - self.args[1])

    def start(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--type', type=str, default=None)
        parser.add_argument('--principal', type=float, default=None)
        parser.add_argument('--periods', type=int, default=None)
        parser.add_argument('--interest', type=float, default=None)
        parser.add_argument('--payment', type=float, default=None)
        self.args = vars(parser.parse_args())
        self.args = list(self.args.values())
        if self.args.count(None) > 1:
            print('Incorrect parameters.')
        elif self.args[0] == 'diff' and self.args[3] is None:
            print('Incorrect parameters.')
        elif self.args[0] == 'diff':
            self.sol_diff()
        elif self.args[0] == 'annuity' and self.args[4] is None:
            self.sol_annui_pay()
        elif self.args[0] == 'annuity' and self.args[1] is None:
            self.sol_principal()
        elif self.args[0] == 'annuity' and self.args[2] is None:
            self.sol_num_month()


calculator1 = CreditCalculator()
calculator1.start()
