from django.shortcuts import render, redirect # app views.py
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        print(new_user.password)
        request.session['first_name'] = new_user.first_name
        request.session['user_id'] = new_user.id
        return redirect('/wishes')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        logged_user = User.objects.filter(email=request.POST['email'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['first_name'] = logged_user.first_name
                request.session['user_id'] = logged_user.id
                return redirect('/wishes')
            return redirect('/')
    return redirect('/')

def wishes(request):
    context = {
        'all_wishes': Wish.objects.all(),
        'wishlist': Grant.objects.all()
    }
    return render(request, "wishes.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')

def stats(request):
    user_count = User.objects.count()
    wishlist = Grant.objects.count()
    pending = Wish.objects.count()
    context = {
        'user_count':user_count,
        'wishlist':wishlist,
        'pending':pending,
    }
    return render(request, 'stats.html', context)

def new_wish(request):
    return render(request, 'new.html')

def add_wish(request):
    if request.method =='POST':
        errors = Wish.objects.validator(request.POST)
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/wishes/new')
        new_wish = Wish.objects.create(item=request.POST['item'], description=request.POST['description'], poster = User.objects.get(id=request.session['user_id']))
        return redirect('/wishes')
    return redirect('/wishes') 

def edit_wish(request, id):
    one_wish = Wish.objects.get(id=id)
    if request.method == 'POST':
        one_wish.item = request.POST['item']
        one_wish.description = request.POST['description']
        one_wish.save()
        return redirect('/wishes')
    context = {
        'edit_wish': one_wish
    }
    return render(request, 'edit.html', context)

def delete_wish(request, id):
    Wish.objects.get(id=id).delete()
    return redirect('/wishes')

def grant_wish(request, id):
    poster = User.objects.get(id=request.session['user_id'])
    item = Wish.objects.get(id=id)
    message = Wish.objects.get(id=id)
    Grant.objects.create(item=item, poster=poster, message=message)
    return redirect('/wishes')

def add_like(request, id):
    liked_wish = Wish.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_wish.likes.add(user_liking)
    return redirect('/wishes')