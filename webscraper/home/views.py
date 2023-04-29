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
            subject_ = "Data Extraction Enquiry Received"

            body = render_to_string(
                "home/emails/confirmation_email_body.txt",
                {
                    "name": request.POST["name"],
                    "contact_email": request.POST["email"],
                    "description": request.POST["description"],
                },
            )

            send_mail(
                subject_,
                body,
                DEFAULT_FROM_EMAIL,
                ["zahurmeerun@hotmail.com"],  # to mail
            )

            body_ = render_to_string(
                "home/emails/confirmation_email_client.txt",
                {
                    "name": request.POST["name"],
                    "contact_email": request.POST["email"],
                    "description": request.POST["description"],
                },
            )

            send_mail(
                "Data Extraction Enquiry",
                body_,
                DEFAULT_FROM_EMAIL,
                [request.POST["email"]],  # to mail
            )

            messages.success(request, "Thank you, your enquiry has been received")
            return redirect(reverse("home"))

        except Exception as e:
            print(e)
            messages.success(request, "Error, Please try again!")
            return redirect(reverse("home"))
