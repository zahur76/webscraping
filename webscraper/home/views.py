from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def send_mail(request):

    if request.method == "POST":

        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('description'))

        return redirect(reverse("home"))