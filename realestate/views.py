from django.shortcuts import render
from django.template import RequestContext


def handler404(request, *args, **argv):
    return render(request, 'pages/404.html')