from django.shortcuts import render


def index(request):
    context = dict()
    return render(request, 'general/index.html', context)

def about(request):
    context = dict()
    return render(request, 'general/about.html', context)