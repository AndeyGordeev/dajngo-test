from django import template

from thought.forms import ThoughtForm
from ..models import Thought
import datetime
from django.utils import timezone
import json

register = template.Library()


@register.inclusion_tag('thought/_form.html')
def thought_form():
    form = ThoughtForm()
    return {'form': form}


@register.simple_tag(takes_context=True)
def chart_data(context):
    user = context['user']
    ten_days_ago = timezone.now() - datetime.timedelta(days=10)
    thought = user.thought.filter(recorded_at__gte=ten_days_ago)
    return json.dumps({
        'labels': [thought.recorded_at.strftime('%Y-%m-%d') for thought in thought],
        'series': [[thought.conditions*-1 for thought in thought]]
    })
