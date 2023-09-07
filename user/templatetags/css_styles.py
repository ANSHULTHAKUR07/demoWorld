from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    print("decorator check",arg)
    return value.as_widget(attrs={'class': arg})