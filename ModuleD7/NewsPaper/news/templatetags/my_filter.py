from django import template

register = template.Library()

string_dict = ['дурак']

@register.filter(name='Censor')
def Censor(arg):
    for i in string_dict:
        if i in arg:
            return "Недопустимая речь"
    return arg
