from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:list')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {"form":form})