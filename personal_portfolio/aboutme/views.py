from django.shortcuts import render
from .models import aboutme

def aboutme_index(request):
    about = aboutme.objects.all()
    context = {
        'about': aboutme
    }
    return render(request, 'aboutme_index.html', context)


def aboutme_detail(request, pk):
    about = aboutme.objects.get(pk=pk)
    context = {
        'about': aboutme
    }
    return render(request, 'aboutme_detail.html', context)

