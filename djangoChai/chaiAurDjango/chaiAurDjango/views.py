from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthCheckAPIView(APIView):
    def get(self, request):
        return Response(
            {"status": "ok", "message": "Service is healthy"},
            status=status.HTTP_200_OK
        )

def home(request):
    # return HttpResponse("Hello, Worlds. You are at chai aur Django Home Page")
    return render(request, "website/index.html")

def about(request):
    # return HttpResponse("Hello, Worlds. You are at chai aur Django About Page")
    return render(request, "website/about.html")

def contact(request):
    # return HttpResponse("Hello, Worlds. You are at chai aur Django Contact Page")
    return render(request, "website/contact.html")
