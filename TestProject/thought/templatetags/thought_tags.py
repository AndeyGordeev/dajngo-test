from django import template

from thought.forms import ThoughtForm

register = template.Library()


@register.inclusion_tag('thought/_form.html')
def thought_form():
    form = ThoughtForm()
    return {'form': form}