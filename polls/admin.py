from django.contrib import admin

#imports question from models.py
from .models import Choice, Question

# Register your models here.

#class that allows you to add 3 choices to a question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#Makes the question model in admin have the published date and the question in the model with none and Date info as title
class QuestionAdmin(admin.ModelAdmin):

    #displays field names as columns on the change list page for the object
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None, {'fields': ['question_text']}),
        #the classes collapse under the pub_date
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


    inlines = [ChoiceInline]

    #allows admin to filter questions by their pub_date on the change list
    list_filter = ['pub_date']

    #adds a search bar on top of the change list
    search_fields = ['question_text']

#Puts the Question class in the admin site.
#Registers the Question class with the QuestionAdmin format in the admin site
admin.site.register(Question, QuestionAdmin)
