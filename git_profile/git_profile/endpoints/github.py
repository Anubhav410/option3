import logging

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from git_profile.external_systems.github import Github

logger = logging.getLogger()


class GithubCallback(APIView):
    def get(self, request):
        if 'code' not in request.GET:
            return Response("Not authorized")

        code = request.GET['code']
        # access_token = '40ffe9c548c5ecca1e30266d79aa843a6ef4cc40'
        github_service = Github(code)
        github_service.get_access_token()
        repos = github_service.get_repositories()
        return render(request, "repos.html", context={"repos": repos})
