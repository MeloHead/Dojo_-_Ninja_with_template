from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    print('-----------this is the index----------')
    
    context ={
        "all_dojos": Dojo.objects.all(),
        "all_ninjas": Ninja.objects.all()
    }
    return render(request,'index.html', context)

def add_dojo(request):
    Dojo.objects.create(
        name=request.GET['dojo_name'], 
        city=request.GET['dojo_city'], 
        state=request.GET['dojo_state'])
    return redirect('/')

def add_ninja(request):
    dojo1 = Dojo.objects.get(id=request.GET['dojo_id'])
    print('**************************', dojo1)
    Ninja.objects.create(
        first_name=request.GET['ninja_first_name'], 
        last_name=request.GET['ninja_last_name'], 
        dojo=dojo1)
    
    return redirect('/')



    #**next steps**
    # when user enters info 
        #create methods to add users
    # add that info into list
        #create a route from both Dojos and Ninjas
