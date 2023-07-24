from django.shortcuts import render
from letters.models import mailbox_count_for

def index(request):
    if request.user.is_authenticated:
        user = request.user
        mailbox_count = mailbox_count_for(user)
        context = {
            'user': user,
            'mailbox_count': mailbox_count
        }
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")