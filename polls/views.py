from django.shortcuts import render
from django.http import HttpResponse

def index(request):
# {
    return HttpResponse("Hello friend, you're at the polls index. Wellcome!")
# }

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
# {
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response % question_id)
# }

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")