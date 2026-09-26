"""Reusable HTTP client wrapping Python's requests library."""

import requests
from config.config import TIMEOUT


class APIClient:
    """Simple, reusable HTTP client for API testing."""

    def __init__(self, base_url, headers=None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)
        self.last_response = None

    def _url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, params=None):
        self.last_response = self.session.get(
            self._url(endpoint), params=params, timeout=TIMEOUT
        )
        return self.last_response

    def post(self, endpoint, json=None):
        self.last_response = self.session.post(
            self._url(endpoint), json=json, timeout=TIMEOUT
        )
        return self.last_response

    def put(self, endpoint, json=None):
        self.last_response = self.session.put(
            self._url(endpoint), json=json, timeout=TIMEOUT
        )
        return self.last_response

    def patch(self, endpoint, json=None):
        self.last_response = self.session.patch(
            self._url(endpoint), json=json, timeout=TIMEOUT
        )
        return self.last_response

    def delete(self, endpoint):
        self.last_response = self.session.delete(
            self._url(endpoint), timeout=TIMEOUT
        )
        return self.last_response