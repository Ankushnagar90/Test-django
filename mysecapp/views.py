from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mysecapp/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'mysecapp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mysecapp/detail.html', {'question': question})
def result(request,question_id):
    response="you are looking at the result of question %s."
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("You're voting on question %s."  % question_id)



# detail(request = HttpResponse, question_id=34)