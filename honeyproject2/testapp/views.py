from django.shortcuts import render,get_object_or_404,redirect
from testapp.models import Video,Comment,Profile
from testapp import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required
def videoslist_view(request):
    videos_list=Video.objects.all()
    return render(request,'testapp/video_list.html',{'videos_list':videos_list})

def videodetail_view(request,year,month,day,post):
    video=get_object_or_404(Video,status='post',slug=post,publish__year=year,publish__month=month,publish__day=day)
    comments=video.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.video=video
            new_comment.save()
            csubmit=True
    else:
        form=forms.CommentForm()
    return render(request,'testapp/video_detail.html',{'video':video,'form':form,'csubmit':csubmit,'comments':comments})

def SignUpView(request):
    form=forms.SignUpform()
    if request.method=='POST':
        form=forms.SignUpform(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return redirect('/procreate')
    return render(request,'testapp/signup.html',{'form':form})

def logout_view(request):
    return render(request,'testapp/logout.html')

def profile_view(request):
    profiles=Profile.objects.all()
    return render(request,'testapp/profile.html',{'profiles':profiles})

def profilecreate_view(request):
    form=forms.ProfilecreateForm()
    if request.method=='POST':
        form=forms.ProfilecreateForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('/profile')
    return render(request,'testapp/procreate.html',{'form':form})

def postcreate_view(request):
    form=forms.PostcreateForm()
    if request.method=='POST':
        form=forms.PostcreateForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('/watchnjoy')
    return render(request,'testapp/postcreate.html',{'form':form})
