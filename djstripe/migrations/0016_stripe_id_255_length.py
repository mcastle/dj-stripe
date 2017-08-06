# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-25 22:40
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import migrations
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0015_upcoming_invoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='charge',
            name='source_stripe_id',
            field=djstripe.fields.StripeIdField(help_text='The payment source id.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='charge',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='stripesource',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='destination',
            field=djstripe.fields.StripeIdField(help_text='ID of the bank account, card, or Stripe account the \
            transfer was sent to.', max_length=255),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='destination_payment',
            field=djstripe.fields.StripeIdField(help_text='If the destination is a Stripe account, this will be the \
            ID of the payment that the destination account received for the transfer.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='source_transaction',
            field=djstripe.fields.StripeIdField(
                help_text='ID of the charge (or other transaction) that was used to \
                fund the transfer. If null, the transfer was funded from the available balance.',
                max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='stripe_id',
            field=djstripe.fields.StripeIdField(max_length=255, unique=True),
        ),
    ]
