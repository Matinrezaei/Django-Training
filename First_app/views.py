from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from First_app.models import AccessRecord, Topic, Webpage
from First_app.forms import NewFormUser, FormName, UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def other(request):
    return render(request, 'other.html')

def relative(request):
    return render(request, 'relative.html')

def help(request):

    mydict = {'helper': 'im helper'}
    return render(request, 'help.html', context=mydict) 

def Lists(request):
    
    MyList = AccessRecord.objects.order_by('date')
    mydict = {'Access_Record': MyList}
    return render(request, 'index.html', context=mydict)


def form_name_view(request):

    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])


    return render(request, 'form.html', context= {'form': form})



def users(request): 

    form = NewFormUser()    

    if request.method == 'POST':
        form = NewFormUser(request.POST)

        if(form.is_valid()):
            form.save(commit= True)
            return index(request)
        else:
            print("Erroe Validitions !")
    
    return render(request, 'form.html', context= {'form': form})


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)

            profile_form.instance.user = user
            # profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True


        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'register.html',
                {'registered' : registered,
                  'user_form': user_form,
                  'profile_form' : profile_form})


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        print('fucking...')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("someone tried to login and faild");
            print("username: {} and password: {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
        
    else:
        return render(request, 'login.html', {})
