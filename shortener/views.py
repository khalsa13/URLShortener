from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect,Http404

from django.views import View
from analytics.models import ClickEvent
from .models import deepURL
from .forms import verifyForm


class HomeView(View):
    def get(self,request,*args,**kwargs):
        form=verifyForm()
        context={'form':form}
        return render(request,"shortener/home.html",context)


    def post(self,request,*args,**kwargs):
        form = verifyForm(request.POST)
        context= {'form': form}
        template="shortener/home.html"
        if form.is_valid():
            new_url=form.cleaned_data.get('url')
            obj,created=deepURL.objects.get_or_create(Url=new_url)
            context={
                "object":obj,
                "created":created
            }
            if created:
                template = "shortener/success.html"
            else:
                template="shortener/already-exists.html"

        return render(request,template,context)


class RedirectUrl(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(deepURL, shortcode=shortcode)
        qs=deepURL.objects.filter(shortcode=shortcode)
        if qs.exists():
            obj=qs.first()
            return HttpResponseRedirect(obj.Url)
        return Http404


