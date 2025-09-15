from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Video,UserPassword

def home(request):
    return render(request,'home.html')

def base(request):
    try:
        if request.session['user_id']:
            return render(request,'base.html')
    except:
        return redirect('login')


def get_user(request):
    users = User.objects.all()
    name = request.GET.get('name')
    if name:
        users = users.filter(name__iexact=name)
    return render(request,'list_u.html',{'users':users})

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        User.objects.create(name=name, surname=surname, email=email, photo=photo)
        return redirect('get_u')
    return render(request,'cr_user.html')

def update_user(request,id):
    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.surname = request.POST.get('surname')
        user.email = request.POST.get('email')
        user.photo = request.FILES.get('photo')
        user.save()
        return redirect('get_u')
    return render(request,'cr_user.html')

def delete_user(request,id):
    user = get_object_or_404(User,id=id)
    user.delete()
    return redirect('get_u')

def details_user(request,id):
    user = get_object_or_404(User,id=id)
    return render(request,'details_u.html',{'user':user})



def get_video(request):
    videos = Video.objects.all()
    title = request.GET.get('title')
    if title:
        videos = videos.filter(video_title__iexact=title)
    return render(request,'list_v.html',{'videos':videos})



def add_video(request):
    try:
        if request.session['user_id']:
            users = User.objects.all()
            if request.method == 'POST':
                video_title = request.POST.get('video_title')
                video_description = request.POST.get('video_description')
                video_file = request.FILES.get('video_file')
                user_id = request.session.get('user_id')
                Video.objects.create(video_title=video_title, video_description=video_description, video_file=video_file, user=User.objects.get(id=user_id))
                return redirect('get_v')
        return render(request,'cr_video.html',{'users':users})
    except:
        return redirect('login')
    

def update_video(request,id):
    video = get_object_or_404(Video,id=id)
    users = User.objects.all()
    if request.method == 'POST':
        video.video_title = request.POST.get('video_title')
        video.video_description = request.POST.get('video_description')
        video.video_file = request.FILES.get('video_file')
        user_id = request.POST.get('user')
        if user_id:
            video.user = get_object_or_404(User,id=user_id)
        video.save()
        return redirect('get_v')
    return render(request,'cr_video.html',{'video':video,'users':users})

def delete_video(request,id):
    video = get_object_or_404(Video,id=id)
    video.delete()
    return redirect('get_v')

def details_video(request,id):
    video = get_object_or_404(Video,id=id)
    return render(request,'details_v.html',{'video':video})

def user_videos(request, user_id):
    user = get_object_or_404(User, id=user_id)
    videos = Video.objects.filter(user=user)
    return render(request, 'user_videos.html', {'user': user, 'videos': videos})

def video_exclude_user(request, user_id):
    videos = Video.objects.exclude(user__id=user_id)
    return render(request, 'list_v.html', {'videos': videos})


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password!=confirm:
            return render(request, 'register.html',{'context': 'password are note same'})
        try:
           user = User.objects.create(name=name, surname=surname, email=email)
           UserPassword.objects.create(user=user, password=password)
           return redirect('login')
        except:
            return render(request,'register.html',{'context':'this username or email already taken'})
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_password = UserPassword.objects.get(user=user)

            if user_password.password == password:
                request.session['user_id'] = user.id
                return redirect('base')
        except:
            return render(request,'login.html',{'context':'wrong email or password'})
    return render(request,'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')
