# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Car(models.Model):

    # TODO: Add custom choices in admin support
    MODEL_CHOICES = ('Audi', 'Mercedes', 'BMW', 'Ferrari', 'Skoda', 'Kia')

    brand = models.CharField( choices=MODEL_CHOICES, blank=False, default='' )
    year = models.DateField( _('Date'), auto_now_add=True )
    model = models.TextField( max_length=60, blank=False, default='Other')

