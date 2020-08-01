from django import template
import datetime
import pytz

ist = pytz.timezone("Asia/Kolkata")

register = template.Library()


@register.simple_tag
def convert_time(time_stamp):
    timestamp = datetime.datetime.fromtimestamp(time_stamp, ist)
    return timestamp.strftime('%d-%m-%Y %H:%M')


@register.simple_tag
def get_count(tagcount, tag):
    out = [tagcount[tag]]
    return out


@register.simple_tag
def get_ABC_count(tagcount, tag):
    out = [tagcount[tag]]
    return out[0]


@register.simple_tag
def date_count(datecount, date):
    out = [datecount[date]]
    return out[0]


@register.simple_tag
def get_vcount(verdict_count, tag):
    out = [verdict_count[tag]]
    return out
