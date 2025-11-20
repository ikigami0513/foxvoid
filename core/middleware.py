import zoneinfo
from django.utils import timezone
from django.http import HttpRequest
from authentication.models import User


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        user: User = request.user

        if user.is_authenticated:
            tzname = user.timezone
            if tzname:
                timezone.activate(tzname)
            else:
                timezone.deactivate()
        else:
            timezone.deactivate()

        response = self.get_response(request)

        return response
    