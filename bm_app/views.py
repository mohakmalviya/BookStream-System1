from django.shortcuts import render, get_object_or_404, redirect

from .models import Books
from .forms import transaction_form

#Showing main page
def main_page(request):
    return render(request,'bm_app/main.html',{})

# showing login page
def login_page(request):
    return render(request,'bm_app/login.html',{})

# showing signup page
def signup_page(request):
    return render(request,'bm_app/signup.html',{})

# showing home page
def home_page(request):
    return render(request,'bm_app/home.html',{})

# New Transaction form

def new_transaction_view(request):
    my_form = transaction_form()
    context = {
        'form' : my_form
    }
    return render(request, 'bm_app/new_transaction.html', context)


    




