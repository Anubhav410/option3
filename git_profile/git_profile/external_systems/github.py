import logging

import requests
from django.conf import settings

logger = logging.getLogger()


class Github:
    GITHUB_LOGIN_PATH = '/login/oauth/access_token'
    REPOSITORIES_PATH = '/user/repos'

    def __init__(self, code, access_token=None):
        self.code = code
        self.access_token = access_token

    def get_access_token(self):
        if not self.code:
            logger.error("Empty authorization code")
            raise Exception("Empty authorization code")
        try:
            url = "{base}{login_path}".format(base=settings.GITHUB_BASE, login_path=self.GITHUB_LOGIN_PATH)
            data = dict(client_id=settings.GITHUB_CLIENT_ID, client_secret=settings.GITHUB_CLIENT_SECRET,
                        code=self.code)
            headers = {"Accept": "application/json"}
            response = requests.post(url, data, headers=headers)
            logger.info("Github status: {status}".format(status=response.status_code))
            response.raise_for_status()
            self.access_token = response.json()['access_token']
        except Exception as e:
            logging.exception(e.message)
            raise

    def get_repositories(self):
        if not self.access_token:
            raise Exception("Please generate access token first")
        url = "{base}{repo_path}".format(base=settings.GITHUB_API_BASE, repo_path=self.REPOSITORIES_PATH)
        try:
            headers = {"Authorization": "token {}".format(self.access_token), "Accept": "application/json"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.exception(e.message)
            raise
