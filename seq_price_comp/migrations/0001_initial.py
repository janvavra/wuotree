# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-20 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.currency
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('winning_price', otree.db.models.CurrencyField(choices=[(otree.currency.Currency('0.30'), otree.currency.Currency('0.30')), (otree.currency.Currency('0.40'), otree.currency.Currency('0.40')), (otree.currency.Currency('0.60'), otree.currency.Currency('0.60')), (otree.currency.Currency('0.80'), otree.currency.Currency('0.80')), (otree.currency.Currency('1.00'), otree.currency.Currency('1.00'))], null=True)),
                ('winning_demand', otree.db.models.PositiveIntegerField(choices=[(600, 600), (480, 480), (360, 360), (240, 240), (120, 120)], null=True)),
                ('price1', otree.db.models.PositiveIntegerField(null=True)),
                ('price2', otree.db.models.PositiveIntegerField(null=True)),
                ('price3', otree.db.models.PositiveIntegerField(null=True)),
                ('price4', otree.db.models.PositiveIntegerField(null=True)),
                ('price5', otree.db.models.PositiveIntegerField(null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seq_price_comp_group', to='otree.Session')),
            ],
            options={
                'db_table': 'seq_price_comp_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('price', otree.db.models.CurrencyField(choices=[(otree.currency.Currency('0.30'), otree.currency.Currency('0.30')), (otree.currency.Currency('0.40'), otree.currency.Currency('0.40')), (otree.currency.Currency('0.60'), otree.currency.Currency('0.60')), (otree.currency.Currency('0.80'), otree.currency.Currency('0.80')), (otree.currency.Currency('1.00'), otree.currency.Currency('1.00'))], null=True)),
                ('is_a_winner', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('has_chosen', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('player1id', otree.db.models.StringField(max_length=10000, null=True)),
                ('player2id', otree.db.models.StringField(max_length=10000, null=True)),
                ('demand', otree.db.models.IntegerField(default=0, null=True)),
                ('order', otree.db.models.StringField(max_length=10000, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seq_price_comp.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seq_price_comp_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seq_price_comp_player', to='otree.Session')),
            ],
            options={
                'db_table': 'seq_price_comp_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seq_price_comp_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'seq_price_comp_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seq_price_comp.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seq_price_comp.Subsession'),
        ),
    ]
