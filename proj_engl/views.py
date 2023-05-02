from django.shortcuts import render
from django.core.cache import cache
from . import words_work


def index(request):
    return render(request, "index.html")


def words_list(request):
    words = words_work.get_words()
    return render(request, "words_list.html", context={"words": words})

