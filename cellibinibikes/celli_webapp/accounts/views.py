from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save()
            # log the user in
            login(request, user)
            return redirect('customers:homepage')
    else:
        signupForm = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': signupForm})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('customers:homepage')
        
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
        

def logout_view(request):
    if request.method == 'POST':
        logout(request) 
        return redirect('accounts:login')
