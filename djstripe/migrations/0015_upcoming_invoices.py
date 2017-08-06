# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-25 17:51
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0014_auto_20160625_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingInvoice',
            fields=[
                ('invoice_ptr', models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True,
                    serialize=False, to='djstripe.Invoice')),
            ],
            options={
                'abstract': False,
            },
            bases=('djstripe.invoice',),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='invoice',
            field=models.ForeignKey(help_text='The invoice to which this invoiceitem is attached.',
                                    null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='invoiceitems', to='djstripe.Invoice'),
        ),
    ]
