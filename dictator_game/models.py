from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'Dictator'
    players_per_group = 2
    num_rounds = 1
    endowment = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0.1, max=Constants.endowment,
        verbose_name='I will keep (from 0 to %i)' % Constants.endowment
    )

    given = models.CurrencyField(min=0, max=Constants.endowment,
                                 doc="The amount kept by the dictator")

    def set_payoffs(self):
        self.kept = Constants.endowment - self.given
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = self.kept
        p2.payoff = self.given


class Player(BasePlayer):
    pass
