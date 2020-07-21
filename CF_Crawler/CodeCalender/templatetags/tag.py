from django import template
import datetime

register = template.Library()


@register.simple_tag
def convert_time(time_stamp):
    timestamp = datetime.datetime.fromtimestamp(time_stamp)
    return timestamp.strftime('%d-%m-%Y %H:%M')
