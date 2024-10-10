from django.shortcuts import render, redirect
from .models import Profiledetails
from .forms import ProfileForm
# Create your views here.

#Read, Create, Update, Delete

#Read
def profiles(request):
    profiles = Profiledetails.objects.all()
    #render( request,template_name, context, content_type, status, using)
    return render(request, 'profiles/profile_list.html',{'profiles': profiles})
    #render(request, template name, context)

#Create
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
        return render(request, 'profiles/profile_form.html',{'form': form})
    
#Update
def profile_update(request, pk):
    profile = Profiledetails.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.post, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        profile = Profiledetails(instance = pk)
        return render(request, 'profiles/profile_form.html',{'form': form})

#Delete
def profile_delete(request, pk):
    profile = Profiledetails.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'profiles/profile_list.html',{'profile': profile})