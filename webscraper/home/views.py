from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from webscraper.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string
from django.contrib import messages


# Create your views here.
def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")


def send_mail_to(request):
    if request.method == "POST":
        
        try:
            subject_ = 'Request Received'
            body_ = request.POST['description']

            send_mail(
                subject_,
                body_,
                DEFAULT_FROM_EMAIL,
                ['zahurmeerun@hotmail.com'] #to mail
            )
            
            messages.success(request, "Thanks for your order!")
            return redirect(reverse("home"))

        except:
            return redirect(reverse("home"))
