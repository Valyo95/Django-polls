from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions that are not published in the future."""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Should only return question published in the past
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		# the F objects refers to the column value in the DB
		# it is used to generate an SQL expression that is executed by the DB itself
		# this way we solve race condition
		selected_choice.votes = F('votes') + 1
		selected_choice.save()
		
		# selected_choice.refresh_from_db()
		# print(selected_choice.votes)
		# if print without reloading selected_choice.votes will have the value: "F('votes') + Value(1)"
		# we must reload from db to get the updated value

		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from beign posted twice
		# if the user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))