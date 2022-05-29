""" Useful functions """

import datetime


def make_date(date_value):
    """ Convert Stripe value to user friendly date """
    nice_date = datetime.datetime.fromtimestamp(date_value).strftime(
        '%d-%m-%Y')
    return nice_date
