from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from .models import  MadminCategory
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.email = request.POST.get('email', '')
        form.password = request.POST.get('password', '')

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['email'], password=cd['password'])
            if user is None:
                return HttpResponse('Invalid login')

            if not user.is_active:
                return HttpResponse('Disabled account')

            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    users = User.objects.all()

    page = request.GET.get('page', 1) # first page
    paginator = Paginator(users, 5) # no of pages

    try:
        user = paginator.page(page)
    except PageNotAnInteger:
        user = paginator.page(1)
    except EmptyPage:
        user = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        form.username = request.POST.get('username', '')
        form.email = request.POST.get('email', '')
        form.password = request.POST.get('password', '')
        form.password2 = request.POST.get('password2', '')
        if form.is_valid():
            user = form.save(commit=False)
            # Set the chosen password
            user.set_password(form.cleaned_data['password'])
            # Save User object
            user.save()
            return redirect('login')
            # return render(request, 'login.html', {'user': user})

    else:
        form = UserRegistrationForm()
    return render(request, 'users.html', {'form': form, 'users': users})


def login_view(request):

    if request.method == 'POST' and request.is_ajax():
        form = LoginForm(request.POST)
        form.email = request.POST.get('email', '')
        form.password = request.POST.get('password', '')

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['email'], password=cd['password'])
            if user is None:
                return HttpResponse('Invalid login')

            if not user.is_active:
                return HttpResponse('Disabled account')

            login(request, user)
            return redirect("home")
            # return HttpResponse('Authenticated successfully')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):

    users = User.objects.all().count()
    category = MadminCategory.objects.all()[:10]

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        form.username = request.POST.get('username', '')
        form.email = request.POST.get('email', '')
        form.password = request.POST.get('password', '')
        form.password2 = request.POST.get('password2', '')

        if form.is_valid():
            user = form.save(commit=False)
            # Set the chosen password
            user.set_password(form.cleaned_data['password'])
            # Save User object
            user.save()
            return render(request, 'login.html', {'user': user})

    else:
        form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form, 'users':users, 'categories':category})


    

def list_categories(request):
    category = MadminCategory.objects.all()
    return render(request, 'categories.html', {'categories':category})



def post(request):
    category = MadminCategory.objects.all() # displaying all categories
    cat = MadminCategory()

    page = request.GET.get('page', 1) # first page
    paginator = Paginator(category, 5) # no of pages

    try:
        cats = paginator.page(page)
    except PageNotAnInteger:
        cats = paginator.page(1)
    except EmptyPage:
        cats = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        cat.title = request.POST.get('title')
        cat.category = request.POST.get('category')
        cat.body = request.POST.get('body')
        cat.date = request.POST.get('date')
        cat.save()
    return render(request, 'posts.html', {'categories':cats})



def comments(request):
    return render(request, 'comments.html')


def logout_view(request):
    logout(request)
    return redirect('login')










   








