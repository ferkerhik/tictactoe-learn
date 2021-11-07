from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth import  login, logout
from .models import Bot, Game
from django.contrib.auth.decorators import  login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CreateUserForm

# Create your views here.
def index(request):
    bots = Bot.objects.all()
    return render(request, 'index.html',{
        'bots' :bots,
    })



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('myapp:index')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html',{
        'form':form,
    })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('myapp:index')

def signup_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:index')
    else:
         form = CreateUserForm()
    return render(request, 'account/singup.html',{
        'form' : form
    })


@login_required
def createGame(request):
    print(Bot.objects.get(bot_id = request.POST['bot']))
    board = Game.objects.create(
                player = request.user,
                status = request.POST['status'],
                bot = Bot.objects.get(bot_id = request.POST['bot']),
                board1 = request.POST['Board'][0],
                board2 = request.POST['Board'][1],
                board3 = request.POST['Board'][2],
                board4 = request.POST['Board'][3],
                board5 = request.POST['Board'][4],
                board6 = request.POST['Board'][5],
                board7 = request.POST['Board'][6],
                board8 = request.POST['Board'][7],
                board9 = request.POST['Board'][8],
            )
    board.save()
    return redirect('/')

@login_required
def profile(request):
    games_list = Game.objects.filter(player = request.user)
    paginator = Paginator(games_list,10)
    page = request.GET.get('page')  
    totalgame = games_list.count()
    wingame = games_list.filter(status="WIN").count()
    losegame = games_list.filter(status="LOSE").count()
    tiegame  = games_list.filter(status="TIE").count()
    winrate = wingame/totalgame*100
    print(wingame)
    try:
        games_list = paginator.page(page)
    except PageNotAnInteger:
        games_list = paginator.page(1)
    except EmptyPage:
        games_list = paginator.page(paginator.num_pages())

    return render(request, 'profile.html',{
        'games' : games_list,
        'totalgame' : totalgame,
        'wingame' : wingame,
        'losegame' : losegame,
        'tiegame' : tiegame,
        'winrate' : winrate
        
    })
def learn(request):
    return render(request, 'learn.html')

def learn_ttt(request):
    return render(request, 'learn_ttt.html')

def learn_profile(request):
    return render(request, 'learn_profile.html')