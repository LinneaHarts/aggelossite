from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.forms import modelformset_factory
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Company, Job

from .forms import AddJobForm, AddCompanyForm

@login_required(login_url='/jobbidder/accounts/login')
    #?next=/%s/' % company_id)
def detail(request, company_id):
    company = Company.objects.get(id__exact=company_id)
    context = {
        'company': company,
    }
    return render(request, 'jobbidder/detail.html', context)

def index(request):
    company_list = Company.objects.all()
    context = {
        'companies': company_list,
    }
    return render(request, 'jobbidder/index.html', context)

#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        login(request, user)
#        return HttpResponse("Login successful")
#    else:
#        return HttpResponse("Login failed")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            context = {'message': 'New user saved correctly'}
        else:
            context = {'form': form, 'message': 'Problem with registration'}
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'registration/register.html', context)

def adduser(request):
    UserFormSet = modelformset_factory(User, exclude=())
    if request.method == 'POST':
        formset = UserFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            context = {'message': 'User saved successfully'}
        else:
            context = {'message': 'Problem with job'}
    else:
        formset = UserFormSet()
        context = {
            'formset': formset
        }
    return render(request, 'jobbidder/adduser.html', context)

@login_required(login_url='/jobbidder/accounts/login?next=/addjob')
def addjob(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            new_company = form.save()
            context = {'message': 'New job saved correctly'}
        else:
            context = {'formset': formset, 'message': 'Problem with job'}
    else:
        form = AddJobForm()
        context = {'form': form}
    return render(request, 'jobbidder/addjob.html', context)

def addcompany(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        new_company = form.save()
        context = {'message': 'New company saved correctly'}
    else:
        form = AddCompanyForm()
        context = {'form': form}
    return render(request, 'jobbidder/addcompany.html', context)
