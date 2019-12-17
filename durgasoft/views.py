from django.http import HttpResponse
from django.views.generic import View

class BaseClass(View):
    greetings = "Good morning"

    def get(self, request):
        return HttpResponse(self.greetings)


class ChildClass(View):
    greetings = "Good afternoon"

    def get(self, request):
        return HttpResponse(self.greetings)