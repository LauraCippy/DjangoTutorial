from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.template.context_processors import request
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

def index(request):
    lista_domande = Question.objects.order_by("domanda")
    template = loader.get_template("mia_app/index.html")
    context = {
        "question_list": lista_domande,
    }
    return HttpResponse(template.render(context, request))

class DetailView(generic.DetailView):
    model = Question
    template_name = "mia_app/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "mia_app/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "mia_app/detail.html",
            {
                "question": question,
                "error_message": "Non hai scelto una risposta",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("mia_app:results", args=(question.id,)))
