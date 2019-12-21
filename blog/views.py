from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#from django.http import HttpResponse


def posts_list(request):
    names = ['Billi', 'Garri', 'Sara', 'Kelli']
    return render(request, 'blog/index.html', context={'names': names})
