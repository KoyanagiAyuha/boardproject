from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        newusername = request.POST['username']
        newpassword = request.POST['password']
        try:
            User.objects.get(username=newusername)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:

            user = User.objects.create_user(newusername, '', newpassword)
    return render(request, 'login.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})



def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    postuser = request.user.get_username()
    if postuser in post.readuser:
        return redirect('list')
    else:
        post.read += 1
        post.readuser = post.readuser + ' ' + postuser
        post.save()
        return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = {'title', 'content', 'author', 'images'}
    success_url = reverse_lazy('list')