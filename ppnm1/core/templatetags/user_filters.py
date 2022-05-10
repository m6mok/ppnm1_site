import datetime

from django import template


register = template.Library()


@register.filter()
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter()
def settype(field, type):
    return field.as_widget(attrs={'type': type})


@register.filter()
def next_day(date):
   return date + datetime.timedelta(days=1)


@register.filter()
def previous_day(date):
   return date - datetime.timedelta(days=1)


@register.filter()
def to_hour_format(num):
    return f'{num:02}:00'


@register.filter()
def rus_money(num):
    if num is not '':
        return f'{num} руб.'
    return


@register.filter()
def description_add(str):
    if str is not '':
        return str + '...'
    return
