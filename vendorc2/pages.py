from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class question(Page):
    form_model = 'player'
    form_fields = ['sex','age','siblings','born_vienna']

page_sequence = [question]

