from django.shortcuts import render, HttpResponse
from .models import LogsCount

# Create your views here.
def home(request):
    return render(request,"home.html")

def count(request):
    items = LogsCount.objects.all()
    return render (request, "count.html", {"count": items })

