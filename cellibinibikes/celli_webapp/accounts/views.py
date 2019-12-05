from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee, Customer
from . import forms
from .forms import DefaultUserForm, CustomerUserForm, CreateEmployeeAccountForm, CreateCustomerAccountForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
                return redirect('tasks:list')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
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
        form = DefaultUserForm()
        create_customer = CreateCustomerAccountForm()
    return render(request, 'accounts/customer_create.html', {'form': form, 'create_customer': create_customer})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer_list.html', {'customers': customers})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'accounts/employee_list.html', {'employees': employees})
















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
