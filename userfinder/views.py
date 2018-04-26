from django.shortcuts import render, redirect
from django.contrib import messages
import requests
# Create your views here.

def index(request):
    base_url = "https://api.github.com/users/"

    if request.method == "POST":
        username = request.POST.get("githubname")
        user_info = requests.get(base_url + username)
        user_info = user_info.json()

        if "message" in user_info:
            messages.error(request, "Böyle bir kullanıcı bulunmuyor !")
            return render(request, "index.html")
        else:
            repos_info = requests.get(base_url + username + "/repos")
            repos_info = repos_info.json()
            return render(request, "index.html", {"profile":user_info, "repos":repos_info})
    else:
        return render(request, "index.html")