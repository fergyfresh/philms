from django.http import HttpResponse
from django.shortcuts import render, redirect

from game.models import Game
from .forms import GameCodeForm


def join_form_view(request, template_name="index.html", form_class=GameCodeForm):
    if request.method == "POST":
        code = request.POST.get("code")
        name = request.POST.get("name")
        form = form_class(request.POST)
        if form.is_valid() and Game.objects.filter(code=code, is_open=True).exists():
            return redirect("game/" + code, kwargs={name: name})
    else:
        form = form_class()
    return render(request, template_name, {"form": form})


def index(request):
    return join_form_view(request)


def game(request, code):
    print(vars(request))
    return HttpResponse("joined game: " + code)
