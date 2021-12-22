from django.conf.urls import url
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view()
# def questions(request):
#     question = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
#     r = requests.get(question)
#     s = r.json()
#     return render(request,'base.html',{'s':s})

# Create your views here.

def questions(request):
    qus = request.GET.get('qus')
    url = f'https://api.stackexchange.com/2.3/search?intitle={qus}&site=stackoverflow'
    r = requests.get(url)
    s = r.json()
    return render(request,'base.html',{'s':s})
