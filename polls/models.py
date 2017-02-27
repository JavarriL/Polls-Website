from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

#models.Models makes the class base the formatting off of the admin site
#gives each field its appropriate HTML widget
class Question(models.Model):
    #creates a character field with a max length of 200 and sets it to question_text
    question_text = models.CharField(max_length=200)

    #creates a date and time field that says the date that the question was published
    pub_date = models.DateTimeField('date published')

    #method that returns the question. Used for the object name when in a list of objects
    def __str__(self):
        return self.question_text

    #returns the published date of questions that have been published less than or equal to one day ago
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    #Tells Django that choice is related to question. When it's deleted, run a CASCADE animation
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    #creates a character field with a max length of 200
    choice_text = models.CharField(max_length=200)

    #creates an integer field set to a default value of 0
    votes = models.IntegerField(default=0)

    #method that returns the question. Used for the object name when in a list of objects
    def __str__(self):
        return self.choice_text
