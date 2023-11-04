from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'pages/about_me.html')

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email_from = form.cleaned_data['email']


            send_mail("Message from" + name, message, email_from, ['dorothy.schwark@gmail.com'])

            return redirect('home')

    else:

        form = ContactForm()



    return render(request, 'pages/contact.html', {
        'form': form

    })
