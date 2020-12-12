from django.shortcuts import render
from accounts.models import Account
from .models import Twit, Comment

def twits(request):
    context = dict()
    user = Account.objects.get(login = request.session['user'])
    friends = user.follows.all()
    print(friends)
    twits = []
    all_twits = Twit.objects.all()
    for twit in all_twits:
        if twit.author in friends:
            twits.append(twit)
    context['twits'] = twits
    return render(request, 'app/twits.html', context)

def twit(request, pk):
    context = dict()
    twit = Twit.objects.get(pk = pk)
    context['twit'] = twit
    if (request.method == 'POST'):
        content = request.POST['comment']
        user = Account.objects.get(login = request.session['user'])
        comment = Comment(author = user, content = content, twit = twit)
        comment.save()
    comments = Comment.objects.filter(twit = twit)
    context['comments'] = comments
    
    return render(request, 'app/twit.html', context)


def add_twit(request):
    context = dict()
    if (request.method == 'POST'):
        user = Account.objects.get(login = request.session['user'])
        content = request.POST['content']
        try:
            image = request.FILES['image']
            has_image = True
        except:
            has_image = False
        
        if (has_image):
            twit = Twit(author = user, content = content, image = image)
        else:
            twit = Twit(author = user, content = content)
        twit.save()
        context['success'] = True
        return render(request, 'app/add_twit.html', context)
    else:
        return render(request, 'app/add_twit.html', context)
    return render(request, 'app/add_twit.html', context)