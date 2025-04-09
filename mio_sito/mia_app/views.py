from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
    question_list = Question.objects.order_by("domanda")
    context = {"question_list": question_list}
    return render(request, "mia_app/index.html", context)

def detail(request, question_id):
    domanda = get_object_or_404(Question, pk=question_id)
    return render(request, "mia_app/detail.html", {"question": domanda})

def results(request, question_id):
    response = "Stai vedendo il risultato della domanda: %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("stai votando la domanda %s." % question_id)
