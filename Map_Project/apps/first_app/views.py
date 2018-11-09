from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import User, Node, Category
from decimal import Decimal
# from .models import User, Message, Comment
# import bcrypt
import random
import datetime

def index(request):
    context = {
        'nodes': Node.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def process(request):
    print(request.POST)
    lat = request.POST['lat']
    long = Decimal(request.POST['long'])
    Node.objects.create(title=request.POST['title'], desc=request.POST['desc'], lat=lat, long=long)
    return redirect('/')
