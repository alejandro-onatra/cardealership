# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext
from datetime import datetime, timedelta

# TODO: Add custom choices in admin support
MODEL_CHOICES = (
    ( 'AUDI', 'Audi' ),
    ( 'MERCEDES', 'Mercedes' ),
    ( 'BMW', 'BMW' ),
    ( 'FERRARI', 'Ferrari' ),
    ( 'SKODA', 'Skoda' ),
    ( 'KIA', 'Kia' )
)


class Car(models.Model):

    brand = models.CharField( choices=MODEL_CHOICES, blank=False, default='', max_length=50 )
    year = models.DateField( gettext('year'), default=datetime.now().year, blank=False )
    model = models.TextField( max_length=60, blank=False, default='Other' )


class Rental(models.Model):

    start_date = models.DateField( gettext('Start Date'), default=datetime.now().date(), blank=False )
    end_date = models.DateField( gettext('End Date'), default=datetime.now().date() + timedelta(days=1), blank=False )
    cost = models.IntegerField( default =0, blank=False )
    car = models.ForeignKey( Car, on_delete=models.CASCADE, blank=False )


