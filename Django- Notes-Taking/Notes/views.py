from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User,Note
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from .forms import NoteForm
from django.contrib import messages

# Create your views here.

def signup(request):
    password_not_match=""
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        email = request.POST.get('email')
        password=request.POST.get('password')
        print(password)
        confirm_password=request.POST.get('confirmpassword')
        print(confirm_password)
        if password != confirm_password:
            password_not_match=('Password do not match!')
            # return redirect('signup')
        else:
            passwords=make_password(password)
            user = User.objects.create(username=username, email=email, password=passwords)
            user.save()
            # messages.success(request,'Account created successfully')
            return redirect('login-page')
    return render(request, 'Notes/Signup.html', {'password_not_match': password_not_match})


def homepage(request):
    if request.user.is_authenticated:
        return redirect('note-home')
    else:
        return render(request,'Notes/Home.html')

def user_login(request):
    credential_error=""
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('note-home')
        else:
            credential_error=('Invalid login credentials')
    return render(request,'Notes/Login.html',{
                'credential_error':credential_error
            })

@login_required
def notes(request):
    
    notes=Note.objects.filter(user=request.user)
    return render(request,'Notes/User_View.html',{
        'notes':notes
    })

@login_required
def add_notes(request):
    if request.method == 'POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.save()
            messages.success(request,'Note Created Successfully')
            return redirect('note-home')
    else:
        form=NoteForm()
        return render(request,'Notes/Add_Notes.html',{
            'form':form
        })

@login_required
def view_notes(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'Notes/view_note.html', {
        'note': note
    })


@login_required
def note_delete(request,id):
    note=get_object_or_404(Note,id=id)
    note.delete()
    return redirect('note-home')
@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')

@login_required
def edit_note(request,id):
    note=get_object_or_404(Note, id=id, user=request.user)
    if request.method=='POST':
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('note-home'))
    else:
        form=NoteForm(instance=note)
    return render(request,'Notes/Edit_Notes.html',{
        'form':form,
        'note':note,
    })