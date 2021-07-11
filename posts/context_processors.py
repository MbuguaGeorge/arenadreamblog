from BlogSettings.models import *
from posts.models import Post

def postfooter(request):
    footerposts=Post.objects.order_by('-timestamp')[:3]
    return {'fposts':footerposts}

def gallery(request):
    galimgs=Gallery.objects.order_by('-timestamp')[:8]
    return {'galimgs':galimgs}

def customname(request):
    customname=Customblogname.objects.all()
    return {'custom':customname}

def overviewtext(request):
    ov=OverViewtext.objects.all()
    return {'overviewtext':ov}

def blogintroheading(request):
    bh=Blogintroheading.objects.all()
    return {'bintroheading':bh}

def site_intro_context(request):
    stin=Site_intro_context.objects.all()
    return {'sitein_context':stin}

def site_random_context(request):
    strn=Site_intro_context.objects.all()
    return {'siterandom_context':strn}

def subscribe_newslater_description(request):
    sb=Subscribe_newslater_description.objects.all()
    return {'Sub_description':sb}

def helpdesk(request):
    desk_details=Helpdesk.objects.all()
    return {'desk_details':desk_details}