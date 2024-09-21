# accounts/accounts.py
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# function to signup new users  
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # getting the signup form
        if form.is_valid(): # checking if the form is valid , if yes user will be saved and logged in and movies list will appear
            user = form.save()
            login(request, user)
            return redirect('movies:list')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {"form":form})

# function to login   
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST) # getting the login form
        if form.is_valid(): # checking if the form is valid , if yes user will be logged in and movies list will appear
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST :
                return redirect(request.POST.get('next'))
            else:
                return redirect('movies:list')
    else :
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

# function to logout
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect ('movies:list')