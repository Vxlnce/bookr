from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = request.GET.get("name") or "World"
    return render(request, "base.html", {"name" : name})

def search_results(request):
    search_text = request.GET.get("search")
    return render(request, "search.html", {"search": search_text})