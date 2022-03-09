from django.shortcuts import render
from songs.models import Movie, Audio, Video
from django.contrib import messages
from django.db.models import Q
from songs.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #retrieve the content of the form
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        content = request.POST.get('content')

        #email
        subject = 'Enquiry from madsongs.com user'
        message = content
        from_email = settings.EMAIL_HOST_USER
        user_email = email
        to_lst = [user_email,from_email]
        send_mail(subject,message, from_email, to_lst, fail_silently = False)
        return HttpResponseRedirect('thankyou')

    return render(request,'contactus.html', {'form':form})
def thankyou(request):
    res = HttpResponse()
    res.write("<h1>Thanks for contacting madsongs.com</h1>")
    res.write("<h2>We have sent a mail to you. please check.</h2>")
    return res

def movies(request):
    qs=Movie.objects.all()
    return render(request,'movies.html', {'mlst':qs})

def movie_details(request, x):
    m=Movie.objects.get(id=x)
    lst1=Audio.objects.all()
    lst2=Video.objects.all()
    return render(request,'movie_details.html', {'m':m, 'alist':lst1, 'vlist':lst2})

def audio(request):
    lst=Audio.objects.all()
    return render(request, 'audios.html', {'alist':lst})

def video(request):
    lst=Video.objects.all()
    return render(request, 'videos.html', {'vlist':lst})

def search_list(request):
    q=request.GET.get('query')
    if q:
        match1 = Movie.objects.filter(Q(title__icontains = q) | Q(director__icontains = q))
        match2 = Audio.objects.filter(Q(title__icontains = q))
        match3 = Video.objects.filter(Q(title__icontains = q))
        if match1 or match2 or match3:
            return render(request, 'search_list.html',{'m1':match1, 'm2':match2, 'm3':match3})

        else:
            messages.error(request, 'No result found')
    else:
        return HttpResponseRedirect('/search_list')
    return render(request, 'search_list.html')