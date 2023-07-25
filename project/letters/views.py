from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Letter, mailbox_count_for
from .forms import LetterForm


User = get_user_model()


@login_required
def create(request, pk=None):
    """
    Create a new letter or edit an existing one.
    """
    letter = None
    if pk:
        letter = Letter.letters.drafts().get(pk=pk)

    if request.method == "POST":
        form = LetterForm(data=request.POST, instance=letter)
        if form.is_valid():
            if letter:
                form.save()
            else:
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()

            if 'send_button' in request.POST:
                letter.send()
                messages.info(request, f'letter sent to {letter.recipient.username}!')
            else:
                messages.info(request, f'"{letter.title}" saved as draft!')
            return redirect("/")

    else:
        form = LetterForm(instance=letter)

    users = User.objects.all()
    context = {
        "users": users,
        "form": form,
        "letter": letter,
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

    return render(request, "mailbox.html", {'mailbox_count': mailbox_count})


@login_required
def drafts(request):
    user = request.user
    drafts = Letter.letters.drafts().filter(author=user)

    return render(request, "letter_drafts.html", {"drafts": drafts})
