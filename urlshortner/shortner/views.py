from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
from .models import Url

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())
        new_url = Url(link=link, uid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(request, pk):
    url_details = Url.objects.get(uid=pk)
    url_details.clicks += 1
    url_details.save()
    return redirect("https://"+url_details.link)