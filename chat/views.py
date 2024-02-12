from django.shortcuts import render, redirect


def chatPage(request):
    if not request.user.is_authenticated:
        return redirect("LOGIN")
    context = {}
    return render(request, "chat/chatPage.html", context)
