from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from.models import place
from.models import person
def demo(request):
    obj=place.objects.all()
    obj1 = person.objects.all()
    return render(request,"index.html",{'result':obj,'resul':obj1})





# def addtn(request):
#
#    x = int(request.GET.get('no1'))
#    y = int(request.GET.get('no2'))
#
#    res = x+y
#
#    return render(request, "result.html", {'result': res})
#
# def inp(request):
#    return render(request, "input.html")


