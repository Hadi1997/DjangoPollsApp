from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

def index(request):
	question_list = Question.objects.all()
	context = {'question_list': question_list}
	return render(request, 'votings/index.html', context)

	# return HttpResponse(question_list[0])

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'votings/details.html', {'question': question})

def result(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'votings/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
		return render(request, 'votings/details.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('result', args=(question.id,)))


# Create your views here.
