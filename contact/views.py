from django.views import View
from .models import *
from django.shortcuts import render, redirect,reverse
from django.utils.decorators import method_decorator


# Create your views here.
class PivotoraIndex(View):
    template_name = "index.html"

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

