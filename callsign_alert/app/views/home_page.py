from django.http import HttpResponse


def indexPageView(_request):
    return HttpResponse("Hello World!")
