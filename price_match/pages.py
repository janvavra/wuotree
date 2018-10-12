from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class PriceMatching(Page):
    form_model = 'player'
    form_fields = ['price_matching']

class Decide(Page):
    form_model = 'player'
    form_fields = ['price']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.non_zero()
        self.group.store_old_price()
        self.group.set_payoffs()

class WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.count_price_matching()

class MyWaitPage(WaitPage):
    pass


class Results(Page):
    timeout_seconds = 60

    def vars_for_template(self):
        return {
            'my_price': self.player.price,
            'price_choice_1': self.group.price1,
            'price_choice_2': self.group.price2,
            'price_choice_3': self.group.price3,
            'price_choice_4': self.group.price4,
            'price_choice_5': self.group.price5,
            'price_1': Constants.prices[0],
            'price_2': Constants.prices[1],
            'price_3': Constants.prices[2],
            'price_4': Constants.prices[3],
            'price_5': Constants.prices[4],
            'winning_price': self.group.winning_price,
            'winning_demand': self.group.winning_demand,
            'my_demand': self.player.demand,
            'my_cost': Constants.cost,
            'my_profit': self.player.payoff
        }

page_sequence = [PriceMatching,
                 MyWaitPage,
                 Decide,
                 ResultsWaitPage,
                 Results]

