
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def home(request):
    return render(request,"1.html")

def get_student(request):
    queryset=student.objects.all()

    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(student_name=search)
    
    paginator = Paginator(queryset, 20)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,"student.html",{'queryset':page_obj})

# Create your views here.
