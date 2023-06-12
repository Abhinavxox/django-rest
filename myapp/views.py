from django.http import JsonResponse

def hello_world(request):
    data = {
        'message': 'Hello, world!'
    }
    return JsonResponse(data)
