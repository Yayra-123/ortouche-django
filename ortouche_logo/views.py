from django.shortcuts import render
from .models import Logo
# Create your views here.

def logo(request):
    logos =Logo.objects.all()
    context = {
        'logos':logos,
    }
    return render(request,'page_logo.html',context)
