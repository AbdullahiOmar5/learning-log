from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Create a new user."""

    if request.method != "POST":
        # Display blank form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("learning_logs:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)


# Create your views here.
