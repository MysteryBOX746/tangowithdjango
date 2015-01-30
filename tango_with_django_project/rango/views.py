from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'message': "This tutorial has been put together by Vladimir Nikolov 2082042"}
	return render(request,'rango/about.html', context_dict)