from django.shortcuts import render

def bot_list(request):
    return render(request, "bots/bot_list.html", {})