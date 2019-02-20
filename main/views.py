from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout

from .GetDetails import getDetails

# Create your views here.

def home(request):
	print("Route Hit")
	if request.is_ajax():
		print("hello")
		print("post data : ", request.POST)
		# name = data["name"]
		name = "name"

		detail = getDetails(name)

		return HttpResponse(detail)
	else:
		print("main")
		return render(request, "main/index.html")
