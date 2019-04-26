from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings

class Login(APIView):
    def get(self, request):
        context = dict(github_client_id=settings.GITHUB_CLIENT_ID, github_base=settings.GITHUB_BASE)
        return render(request, "login.html", context=context)