from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import registration, login 

class loadtemplateview(TemplateView):
    template_name = 'Home/home.html'

def registrationview(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        reg_email = request.POST.get('email')

        Username = request.POST.get('Username')
        log_email = request.POST.get('email')
        password = request.POST.get('password')

        if name and phone and address and reg_email:
            reg_form = registration(name=name, phone=phone, address=address, email=reg_email)
            reg_form.save()

        if Username and log_email and password:
            log_form = login(Username=Username, email=log_email, password=password)
            log_form.save()

        return redirect('details')


    return render(request, 'Home/login.html')


def details_view(request):
    context = {
        'registration_details': registration.objects.all(),
        'login_details': login.objects.all(),
    }
    return render(request, 'Home/details.html', context=context)
