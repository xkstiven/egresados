from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

def principal(request):
	return render(request,'principal.html')