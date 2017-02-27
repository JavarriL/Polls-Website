from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
# Create your views here.

#Creates a function IndexView that runs a generic view with the addition of polls/index.html to localhost website
# and the object_name latest_question_list
#Display a list of objects
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    #function gets the latest 5 questions
    def get_queryset(self):
        

        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

#Creates a function DetailView that runs a generic view with the addition of polls/detail.html to localhost website
# and the model is based on the Question object
#Display a detail page for a particular type of object
class DetailView(generic.DetailView):

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte = timezone.now())

#Creates a function IndexView that runs a generic view with the addition of polls/results.html to localhost website
# and the model is based on the Question object
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#Creates a function that runs if it's requested and takes in the question number
def vote(request, question_id):
    #gets the question object with the same number as the id. If the question_id doesn't exist, it raises a Http404
    #error
    question = get_object_or_404(Question, pk = question_id)
    try:

        #tries to get the input of the choice that you picked on detail.html by getting its id
        selected_choice = question.choice_set.get(pk = request.POST['choice'])

    #if you get an error saying that this choice DoesNotExist
    except (KeyError, Choice.DoesNotExist):

        #return the question along with the error message in the detail.html template
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    #if you do assign something to selected_choice
    else:
        #that choice gets another vote and saves it
        selected_choice.votes += 1
        selected_choice.save()

        #redirects to results webpage with the value of the question_id
        return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))
