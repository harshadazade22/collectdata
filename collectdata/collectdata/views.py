from django.http import HttpResponse
from django.shortcuts import render
from formdata.models import Saveform
def Savedata(request):
    if request.method=="POST":
        name=request.POST.get('NAME')
        email=request.POST.get('EMAIL')
        todata=Saveform(name=name,email=email)
        todata.save()

    return render(request,"form.html")