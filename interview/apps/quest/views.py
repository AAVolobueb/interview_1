from django.http import HttpResponse

def index(request):
    return HttpResponse("Тут пусто, всё через API")