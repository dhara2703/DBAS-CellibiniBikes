from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            # log the user in
            return redirect('customers:homepage')
    else:
        signupForm = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': signupForm})
