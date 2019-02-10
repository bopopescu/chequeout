from django.shortcuts import render
from django.http import HttpResponse
from . import models
from hashlib import sha256
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        print("yea")
        form_data = request.POST
        username = form_data['username']
        first_name = form_data['first_name']
        last_name = form_data['last_name']
        password = sha256(form_data['password'].encode()).hexdigest()
        account_number = form_data['account_number']
        card_number = form_data['card_number']
        cvv = form_data['cvv']
        address = form_data['address']
        account = models.Account(
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
            account_number = account_number,
            card_number = card_number,
            csv = cvv,
            address = address,
        )
        print(username)
        account.save()
        return render(request, 'account/login.html', {})
    return render(request, 'account/register.html',{})

def login(request):
    # add proper password checks
    if request.method == 'POST':
        form_data = request.POST
        print(request.POST)
        user = models.Account.objects.filter(username=form_data['username'])
        if user:
            return redirect('../../chat/message')
    return render(request, 'account/login.html', {})
