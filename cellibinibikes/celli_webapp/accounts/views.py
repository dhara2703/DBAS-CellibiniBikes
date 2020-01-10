from . import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Employee, Customer
from django.contrib.auth.models import User
from .forms import DefaultUserForm, CustomerUserForm, CreateEmployeeAccountForm, CreateCustomerAccountForm
from .render import Render
from django.utils import timezone
from django.views.generic import View




# Create your views here.
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
                return redirect('bike:bikelist')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


@login_required(login_url='/accounts/login/')
def profile(request):
    employee = Employee.objects.get(e_userid=request.user.id)
    print(request.user.id)
    args = {'user':request.user, 'employee':employee}
    return render(request, 'accounts/profile.html', {'args': args})
    

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect('accounts:login')

@login_required(login_url='/accounts/login/')
def employee_create(request):
    if request.method == 'POST':
        form = DefaultUserForm(request.POST or None)
        create_employee = CreateEmployeeAccountForm(request.POST or None)

        if form.is_valid() and create_employee.is_valid():
            request.user.is_staff = True
            user = form.save()
            newemployee = create_employee.save(commit=False)
            newemployee.e_userid = user
            newemployee.save()
            return redirect('tasks:list')
    else:
        form = DefaultUserForm()
        create_employee = CreateEmployeeAccountForm()
    return render(request, 'accounts/employee_create.html', {'form': form, 'create_employee': create_employee})


@login_required(login_url='/accounts/login/')
def customer_create(request):
    if request.method == 'POST':
        form = CustomerUserForm(request.POST or None)
        create_customer = CreateCustomerAccountForm(request.POST or None)

        if form.is_valid() and create_customer.is_valid():
            user = form.save()
            newcustomer = create_customer.save(commit=False)
            newcustomer.c_userid = user
            newcustomer.save()
            return redirect('accounts:clist')
    else:
        form = CustomerUserForm()
        create_customer = CreateCustomerAccountForm()
    return render(request, 'accounts/customer_create.html', {'form': form, 'create_customer': create_customer})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer_list.html', {'customers': customers})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'accounts/employee_list.html', {'employees': employees})


def customer_detail(request, customerid):
    customer = Customer.objects.get(c_customerid = customerid)
    return render(request, 'accounts/customer_detail.html', {'customer': customer})
    
# http://127.0.0.1:8000/accounts/pdf/apprentices
class Pdfapprentices(View):

    def get(self, request):
        today = timezone.now()
        apprentices = Employee.objects.all().filter(e_isapprentice=True)
        return Render.render('accounts/apprentices_report.html', {'today': today, 'apprentices': apprentices, 'user':request.user})












# ----------------------------------------------------------------------------
# No Need with This
# Don't Remove this
# ----------------------------------------------------------------------------
# def signup_view(request):
#     if request.method == 'POST':
#         signupForm = UserCreationForm(request.POST)
#         if signupForm.is_valid():
#             user = signupForm.save()
#             # log the user in
#             login(request, user)
#             return redirect('customers:homepage')
#     else:
#         signupForm = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': signupForm})
