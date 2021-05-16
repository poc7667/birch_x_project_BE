import pdb
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

# def order(request):
#     return order
def skus(request):
    with open('./data/skus.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)

def reviews(request):
    with open('./data/reviews.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)

@csrf_exempt
def orders(request):
    if request.method == 'POST':
        # post_data = json.loads(request.body.decode("utf-8"))
        return JsonResponse('', safe=False)
    elif request.method == 'GET':
        with open('./data/orders.json') as f:
            jsonDataResponse = json.load(f)
        return JsonResponse(jsonDataResponse, safe=False)

def shipments(request):
    with open('./data/shipments.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)


def employees(request):
    with open('./data/employees.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)



def payments(request):
    with open('./data/payments.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)


def customers(request):
    with open('./data/customers.json') as f:
        jsonDataResponse = json.load(f)
    return JsonResponse(jsonDataResponse, safe=False)
