from django.shortcuts import render
from chat import models
from hashlib import sha256
import random

# Create your views here.
def confirmation(request):
    return render(request, 'pay/confirmation.html', {})

def processing(request):
    # store in a csv, then process it using blockchain
    with open('pay/transaction.csv', 'w') as f:
        text = "Elton Pinto" + ',' + "Amazon" + ',' + sha256(str(random.randrange(1,10)).encode()).hexdigest() + ',' +sha256("epinto6".encode()).hexdigest()+ ',' +sha256("123456789".encode()).hexdigest()+ ',' +sha256("234567891".encode()).hexdigest() + ','+sha256("019".encode()).hexdigest()
        f.write(text)
        print(text)

    print("did it")
    return render(request, 'pay/processing.html', {})

def success(request):
    return render(request, 'pay/success.html', {})
