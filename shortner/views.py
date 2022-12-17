import uuid
from django.shortcuts import redirect, render

from shortner.models import Url

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]  #to generate unique ID
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request,pk): #to get the website after url is shortened
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)