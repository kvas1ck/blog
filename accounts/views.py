from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.user.is_authenticated:
        return redirect("acounts:profile")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)
            return redirect("accounts:profile")

    else:
        form = RegisterForm()

    context = {
        'form':form
        }

    return render(request,"accounts/register.html", context)


@login_required
def profile(request):
    return render(request, "accounts/profile.html")

