from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CONDITIONS = (
    (1, 'Joy'),
    (5, 'Passionate'),
    (10,'Happy'),
    (15,'Positive'),
    (20,'Content'),
    (25,'Bored'),
    (30,'Pessimistic'),
    (35,'Overheated'),
    (40,'Worried'),
    (45,'Angry'),
    (50,'Guilty'),
    (55,'Deepens'),
)

class Thought(models.Model):
    user = models.ForeignKey(User, related_name='thought')
    recorded_at = models.DateTimeField(default=timezone.now, editable=False)
    conditions = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return '{} : {}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'),self.get_conditions_display())