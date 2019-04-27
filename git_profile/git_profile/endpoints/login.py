from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView


class Login(APIView):
    def get(self, request):
        context = dict(github_client_id=settings.GITHUB_CLIENT_ID, github_base=settings.GITHUB_BASE)
        return render(request, "login.html", context=context)