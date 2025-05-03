from django.shortcuts import render
from .models import Profile
import openpyxl
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        degree=request.POST.get("degree","")

        profile=Profile(name=name,email=email,phone=phone,degree=degree)
        profile.save()

    return render(request,'excel/accept.html')


def excel(request, id):
    user_profile = Profile.objects.get(pk=id)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Details"

    ws.append(["Name", user_profile.name])
    ws.append(["Email", user_profile.email])
    ws.append(["Phone number", user_profile.phone])
    ws.append(["Degree", user_profile.degree])
    # Add more fields here

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=details.xlsx'
    wb.save(response)
    return response
    

def list(request):
    profiles=Profile.objects.all()
    return render(request,'excel/list.html',{'profiles':profiles})
