from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"todos.html",{'username' : 'Spruha' ,'todos': [{'football': 'completed'}, {'django': 'pending'}]})