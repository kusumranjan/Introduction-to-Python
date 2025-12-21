from django.http import JsonResponse, request, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


def hello(request):
    return JsonResponse({'message': 'Hello world'})

def check(request):
    return JsonResponse({'message': 'Checked'})

def status(request):
    return JsonResponse({'message': 'check done'})



@csrf_exempt
def get_request(request):
    if request.method == "GET":
        return JsonResponse({"message": "GETTING REQUEST"})
    return HttpResponse("Checking")


@csrf_exempt
def post_request(request):
    if request.method == "POST":
        return JsonResponse({"message": "POST REQUEST"})
    return HttpResponse("ok")


@csrf_exempt
def put_request(request):
    if request.method == "PUT":
        return JsonResponse({"message": "PUT REQUEST"})
    return HttpResponse("ok")


@csrf_exempt
def del_request(request):
    if request.method == "DELETE":
        return JsonResponse({"message": "DELETE REQUEST"})
    return HttpResponse("ok")



@api_view(['GET', 'POST', 'PUT', 'DELETE'])

def api_view(request):
    if request.method == "GET":
        return JsonResponse({"message": "GET REQUEST"})
    elif request.method == "POST":
        return JsonResponse({"message": "POST REQUEST"})
    elif request.method == "PUT":
        return JsonResponse({"message": "PUT REQUEST"})
    elif request.method == "DELETE":
        return JsonResponse({"message": "DELETE REQUEST"})
        
--------------------------------       -- -----------------------------------
-------------------------------        --------------------------------------


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle
import json
@csrf_exempt
def vehicle(request):
    if request.method == 'GET':
        data = list(Vehicle.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        body=json.loads(request.body)
        Vehicle.objects.create(
            number_plate=body['number_plate'],
            vehicle_type=body['vehicle_type'],
            manufacturer=body['manufacturer'],
            year=body['year'],
        )
        return JsonResponse({'success':True})

    if request.method == 'PUT':
        try:
            body = json.loads(request.body.decode('utf-8'))
            p = Vehicle.objects.get(id=body['id'])
            p.number_plate = body['number_plate']
            p.vehicle_type = body['vehicle_type']
            p.manufacturer = body['manufacturer']
            p.year = body['year']

            p.save()
            return JsonResponse({'success': True})
        except Exception as e:
            print(e)
    if request.method == 'DELETE':
        body=json.loads(request.body)
        p=Vehicle.objects.get(id=body['id'])
        p.delete()
        return JsonResponse({'success':True})

    return JsonResponse({'success':False})
