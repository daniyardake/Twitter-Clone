from django.shortcuts import render
from .models import Account
from twits.models import Twit


def register(request):
    context = dict()
    if (request.method == 'POST'):
        login = request.POST['login']
        password = request.POST['password']
        try:
            image = request.FILES['image']
            has_image = True
        except:
            has_image = False
        
        if (len(login)>30 or len(password)>30 or len(login) < 2 or len(password)<5):
            context['error_data'] = True
            return render(request, 'general/register.html', context)
        else:
            try:
                potential_duplicate = Account.objects.get(login = login)
                context['error_login'] = True
                return render(request, 'general/register.html', context)
            except:
                #Correct input
                if (has_image):
                    user = Account(login = login, password = password, image = image)
                else:
                    user = Account(login = login, password = password)
                user.save()
                request.session['user'] = login
                return render(request, 'app/users.html', context)

    
    return render(request, 'general/register.html', context)

def login(request):
    context = dict()
    if (request.method == 'POST'):
        login = request.POST['login']
        password = request.POST['password']
        
        try:
            potential_user = Account.objects.get(login = login)
            if (potential_user.password == password):
                request.session['user'] = login
                return render(request, 'app/users.html', context)
            else:
                context['error_password'] = True
                return render(request, 'general/login.html', context)
        except:
            context['error_login'] = True
            return render(request, 'general/login.html', context)
    return render(request, 'general/login.html', context)

def signout(request):
    context = dict()
    request.session['user'] = None
    return render(request, 'general/index.html', context)

def user(request, login):
    context = dict()
    try:
        user = Account.objects.get(login = login)
        context['user'] = user
        me = Account.objects.get(login = request.session['user'])
        context['button'] = not (user in me.follows.all())
        if (request.method == 'POST'):
            me.follows.add(user)
            me.save()

        try:
            twits = Twit.objects.filter(author = user)
            context['twits'] = twits
        except:
            context['twits'] = []


        follows = user.follows.all()
        context['follows'] = follows
        

        
        return render(request, 'app/user.html', context)
    except:
        return render(request, 'general/404.html', context)

    return render(request, 'app/user.html', context)


def my_account(request):
    context = dict()
    try:
        login = request.session['user']
        user = Account.objects.get(login = login)
        context['user'] = user
        try:
            twits = Twit.objects.filter(author = user)
            context['twits'] = twits
        except:
            context['twits'] = []
        return render(request, 'app/user.html', context)
    except:
        return render(request, 'general/404.html', context)

    return render(request, 'app/user.html', context)
    



def users(request):
    context = dict()
    users = Account.objects.all()
    context['users'] = users
    return render(request, 'app/users.html', context)
