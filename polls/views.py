# from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.urls import reverse

# Create your views here.
def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list":latest_question_list
    # }
    # return HttpResponse(template.render(context,request))
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list":latest_question_list
    }
    return render(request,"polls/index.html",context)


def home(request):
    return HttpResponse("Hello, Welcome Home!")


def detail(request,question_id):
    # try :
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist")
    # return render(request,"polls/detail.html",{"question":question})
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{"question":question})


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question":question,"error_message":"选项错误"})
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
