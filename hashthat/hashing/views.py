from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib
from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST) # POST data contains stuff from form inside of home.html
        if filled_form.is_valid(): # if all data checks out and is ok
            text = filled_form.cleaned_data['text'] # pulling text object into variable
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            # Checking if anyone has already created this hash
            try:
                Hash.objects.get(hash=text_hash) # if exists, don't need to save it
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash', hash = text_hash)
    form = HashForm()
    return render(request, 'hashing/home.html', {'form':form})

def hash(request, hash): # hash param specified in url pats
    hash = Hash.objects.get(hash =hash)
    return render(request, 'hashing/hash.html', {'hash':hash})

def quickhash(request):
    text = request.GET['text']
    return JsonResponse({'hash': hashlib.sha256(text.encode('utf-8')).hexdigest()})