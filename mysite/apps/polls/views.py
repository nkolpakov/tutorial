from django.http.response import HttpResponse


def index(request, *args, **kwargs):
    return HttpResponse('Hello, world! You\'re in a polls index.')
