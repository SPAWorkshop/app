from django.conf import settings
import time


class DebugDelayMiddleware:

    def process_request(self, request):
        delay = getattr(settings, 'REQUEST_DELAY', 0)
        if delay and settings.DEBUG:
            print(" => Applying delay to the request (%ss)" % delay)
            time.sleep(delay)
        return None
