"""Project-wide re-usable helper functions"""

import os
import random
import string

from datetime import date, datetime

from django.core.validators import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def get_age(birth_date, death_date=None):
    """returns the age of thing/person or else from its birth_date"""
    today = timezone.now()

    if death_date and isinstance(death_date, (date, datetime)):
        today = death_date

    if birth_date:
        if isinstance(birth_date, (date, datetime)):
            age_computed = today.year - birth_date.year - (
                (today.month, today.day) < (
                    birth_date.month, birth_date.day))
            return age_computed
        elif isinstance(birth_date, (int,)):
            age_computed = int(today.year) - birth_date
            return age_computed
    return ''


def get_extension(filename):
    """Returns the extension of a file."""
    return os.path.splitext(filename)


def random_chars(counts):
    """Generates 'counts' number random chars consisting of letters 
    and numbers.
    TODO: a higher performance way?
    """
    return ''.join(['{}'.format(
        random.choice(string.ascii_lowercase + string.digits))
        for _ in range(counts)])
