import re

from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        patterns = getattr(
            settings,
            "LOGIN_REQUIRED_EXEMPT_URLS",
            [
                r"^/accounts/",
                r"^/admin/",
                r"^/static/",
                r"^/media/",
                r"^/api/",
            ],
        )
        self.exempt = [re.compile(p) for p in patterns]

    def __call__(self, request):
        if request.user.is_authenticated:
            return self.get_response(request)
        path = request.path
        for pattern in self.exempt:
            if pattern.match(path):
                return self.get_response(request)
        return redirect(settings.LOGIN_URL)
