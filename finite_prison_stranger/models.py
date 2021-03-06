from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Jon Wood'

doc = """
Two participants represent a bolt-producing company and compete to sell bolts
over a fixed number of rounds.
"""

class Constants(BaseConstants):
    name_in_url = 'FinitePrisonS'
    players_per_group = 2
    num_rounds = 10
    bolt_prices = (0.08,0.12)
    payoff_dict = {'0.080.08': 12,'0.080.12': 24,'0.120.08': 0,'0.120.12': 17.5}

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    bolt_price = models.FloatField(choices=Constants.bolt_prices,
	                                widget=widgets.RadioSelect())
    def not_zero(self):
        if self.bolt_price not in Constants.bolt_prices:
            self.bolt_price = 0.08

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        self.payoff = Constants.payoff_dict[str(self.bolt_price)+str(self.other_player().bolt_price)]
    pass
