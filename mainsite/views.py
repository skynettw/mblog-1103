from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Post
import random

def homepage(request):
    posts = Post.objects.all()
    return render(request, "index.html", locals())

def lotto(request):
    lucky = random.randint(1, 42)
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1, 42))
    
    return render(request, "lotto.html", locals())
    
