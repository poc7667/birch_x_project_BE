import pdb
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
#
def index(request):
    # todo_list = Todo.objects.order_by('id')
    #
    # form = TodoForm()
    #
    # context = {'todo_list' : todo_list, 'form' : form}
    with open('./data/index.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)

def skus(request):
    with open('./data/skus.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)

def reviews(request):
    with open('./data/reviews.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)

#
# def reviews(request):
#     # todo_list = Todo.objects.order_by('id')
#     #
#     # form = TodoForm()
#     #
#     # context = {'todo_list' : todo_list, 'form' : form}
#     with open('./data/index.json') as f:
#         jsonDataResponse = json.load(f)
#     return JsonResponse(jsonDataResponse, safe=False)
# @require_POST
# def addTodo(request):
#     form = TodoForm(request.POST)
#
#     if form.is_valid():
#         new_todo = Todo(text=request.POST['text'])
#         new_todo.save()
#
#     return redirect('index')
#
# def completeTodo(request, todo_id):
#     todo = Todo.objects.get(pk=todo_id)
#     todo.complete = True
#     todo.save()
#
#     return redirect('index')
#
# def deleteCompleted(request):
#     Todo.objects.filter(complete__exact=True).delete()
#
#     return redirect('index')
#
# def deleteAll(request):
#     Todo.objects.all().delete()
#
#     return redirect('index')