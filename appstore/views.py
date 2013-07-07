# Create your views here.
from models import UserInfo, TransactionDetails, AppFactory
from forms import UserInfoForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def app_description(request, appId):
    if request.method == 'GET':
        form = UserInfoForm()
        return render_to_response('app_desc.html',{'form':form}, context_instance=RequestContext(request))
    else:
        form = UserInfoForm(request.POST)
        if form.is_valid():
            import pdb;pdb.set_trace();
            form = form.save(commit=False)
            app = AppFactory.objects.filter(id=appId)
            if app:
                form.app = app[0]
                form.save()
                return render_to_response('app_desc.html',{'form':form,'done':'done'}, context_instance=RequestContext(request))
        else:
            return render_to_response('app_desc.html',{'form':form,'done':'app not exist'}, context_instance=RequestContext(request))
        
    
def home_page(request):
    app_banner = AppFactory.objects.filter(isBigBanner=True)[0]
    web_apps = AppFactory.objects.filter(isBigBanner=False, appType=1)
    mob_apps = AppFactory.objects.filter(isBigBanner=False, appType=2)
    return render_to_response('index.html',{'web_apps':web_apps,'app_banner':app_banner, 'mob_apps':mob_apps}, context_instance=RequestContext(request))