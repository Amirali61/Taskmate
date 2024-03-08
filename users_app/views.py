from django.shortcuts import redirect, render
from users_app.forms import CostumeRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        registration_form = CostumeRegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request,"New User created, Login to continue")
            return redirect('login')
        else:
            return render(request,'register.html',{'registration_form':registration_form})
    else:
        registration_form = CostumeRegisterForm()
        return render(request,'register.html',{'registration_form':registration_form})