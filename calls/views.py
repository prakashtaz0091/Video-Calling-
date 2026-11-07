from django.shortcuts import render, redirect


def home(request):
    if request.method == "POST":
        room = request.POST.get("room", "").strip()
        if room:
            return redirect("room", room_name=room)
    return render(request, "calls/home.html")


def room(request, room_name):
    return render(request, "calls/room.html", {"room_name": room_name})