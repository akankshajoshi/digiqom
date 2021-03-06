# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UserInfoForm
from models import AppFactory, HomePageText, Banner

def submit_userinfo(request, appId):
    if request.method == 'GET':
        form = UserInfoForm()
        return render_to_response('userinfo.html',{'form':form}, context_instance=RequestContext(request))
    else:
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            app = AppFactory.objects.filter(id=appId)
            if app:
                form.app = app[0]
                form.save()
                return render_to_response('userinfo.html',{'form':form,'done':'done'}, context_instance=RequestContext(request))
        else:
            return render_to_response('userinfo.html',{'form':form,'done':'app not exist'}, context_instance=RequestContext(request))
        
    
def home_page(request):
    hometext = HomePageText.objects.all()[0]
    web_apps = AppFactory.objects.filter(appType=1)
    banners = Banner.objects.all()
    return render_to_response('index.html', {'web_apps':web_apps, 'hometext':hometext,'banners':banners}, context_instance=RequestContext(request))

def app_description(request, appId):
    if request.method == 'GET':
        app = AppFactory.objects.filter(id=appId)[0]
        return render_to_response('inside.html', {'app':app}, context_instance=RequestContext(request))
#     else:
#         if form.is_valid():
#             import pdb;pdb.set_trace();
#             form = form.save(commit=False)
#             app = AppFactory.objects.filter(id=appId)
#             if app:
#                 form.app = app[0]
#                 form.save()
#                 return render_to_response('index.html', {'form':form, 'done':'done'}, context_instance=RequestContext(request))
#         else:
#             return render_to_response('index.html', {'form':form, 'done':'app not exist'}, context_instance=RequestContext(request))
