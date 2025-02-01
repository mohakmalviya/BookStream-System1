from django.shortcuts import render, get_object_or_404, redirect
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

    if request.method == 'POST':
        print(request.POST)
        my_form = transaction_form(request.POST) #to be used according to the Form/ModelForm used
        if my_form.is_valid():
            my_form.save()
            return redirect('home')
        
    else:
        my_form = transaction_form()
        # context = {
        #     'form' : my_form
        # }
    return render(request, 'bm_app/new_transaction.html', {'form' : my_form})

def login_view(request):
    return render(request = )



    
    


