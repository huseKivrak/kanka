from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from . models import Letter, mailbox_count_for

User = get_user_model()


def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        author = request.user
        recipient_id = request.POST["recipient"]
        recipient = User.objects.get(id=recipient_id)

        letter = Letter.letters.create(
            title=title,
            body=body,
            author=author,
            recipient=recipient,
        )

        if 'send_button' in request.POST:
            letter.send()

        return redirect(reverse("letters:detail", kwargs={"pk": letter.pk}))


    else:
        users = User.objects.all()
        context = {
            "users": users,
        }
        return render(request, "letter_create.html", context)

def detail(request, pk):
    letter = Letter.letters.get(pk=pk)
    context = {
        "letter": letter,
    }
    return render(request, "letter_detail.html", context)

def mailbox(request):
    user = request.user
    mailbox_count = mailbox_count_for(user)
    context = {
        'user': user,
        'mailbox_count': mailbox_count
    }
    return render(request, "mailbox.html", context)