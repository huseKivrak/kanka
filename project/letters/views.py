from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Letter, mailbox_count_for
from .forms import LetterForm

User = get_user_model()

@login_required
def create(request):
    if request.method == "POST":
        form = LetterForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
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
        form = LetterForm()

    users = User.objects.all()
    context = {
        "users": users,
        "form": form,
    }
    return render(request, "letter_create.html", context)

@login_required
def detail(request, pk):
    letter = Letter.letters.get(pk=pk)
    return render(request, "letter_detail.html", {"letter": letter})

@login_required
def mailbox(request):
    user = request.user
    mailbox_count = mailbox_count_for(user)
    context = {
        'user': user,
        'mailbox_count': mailbox_count
    }
    return render(request, "mailbox.html", context)

@login_required
def drafts(request):
    user = request.user
    drafts = Letter.letters.drafts().filter(author=user)


    return render(request, "letter_drafts.html", {"drafts": drafts})