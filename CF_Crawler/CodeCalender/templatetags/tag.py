from django import template
import datetime

register = template.Library()


@register.simple_tag
def convert_time(time_stamp):
    timestamp = datetime.datetime.fromtimestamp(time_stamp)
    return timestamp.strftime('%d-%m-%Y %H:%M')


@register.simple_tag
def get_count(tagcount,tag):
    out = [tagcount[tag]]
    return out


@register.simple_tag
def get_ABC_count(tagcount,tag):
    out = [tagcount[tag]]
    return out[0]
