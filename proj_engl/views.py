from django.shortcuts import render
from django.core.cache import cache
from . import words_work
import re


def index(request):
    return render(request, "index.html")


def words_list(request):
    words = words_work.get_words()
    return render(request, "words_list.html", context={"words": words})


def word_add(request):
    return render(request, "word_add.html")


def word_request(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_word = request.POST.get("new_word", "")
        new_translation = request.POST.get("new_translation", "")
        context = {"user": user_name}
        eng_match = re.search(r'[a-zA-z]+', new_word)
        ru_match = re.search(r'[а-яА-я]+', new_translation)
        if len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        elif len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Слово должно быть не пустым"
        elif eng_match is None:
            context["success"] = False
            context["comment"] = "Слово должно быть на английском"
        elif ru_match is None:
            context["success"] = False
            context["comment"] = "Перевод должен быть на русском"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            words_work.write_word(new_word, new_translation)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "word_request.html", context)
    else:
        return word_add(request)

