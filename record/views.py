from django.shortcuts import render, redirect
from .models import DataBase
from .forms import EntryForm


def CreateView (request):
    try:
        if request.method == 'POST':
            form = EntryForm(request.POST)
            if form.is_valid():
                form.save()
                form = EntryForm()
        else:
            form = EntryForm()
        data = DataBase.objects.all()
    except:
        pass
    return render (request,'createntry.html',{'form':form, 'data':data})

def DeleteView (request, id):
    try:
        if request.method == "POST":
            data = DataBase.objects.get(pk=id)
            data.delete()
            return redirect ('/')
    except:
        pass

def UpdateView(request,id):
    try:
        if request.method == 'POST':
            data = DataBase.objects.get(pk=id)
            form = EntryForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect ('/')
        else:
            data = DataBase.objects.get(pk=id)
            form = EntryForm(instance=data)
    except:
        pass
    return render(request, "updateview.html", {'form': form})