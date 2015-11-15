# -*- coding: utf-8 -*-
from django.conf import settings

MALE = 'MAL'
FEMALE = 'FEM'
NOT_DEFINED = 'NON'

DEFAULT_GENDERS = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (NOT_DEFINED, ''),
)

GENDERS = getattr(settings, 'GENDERS', DEFAULT_GENDERS)