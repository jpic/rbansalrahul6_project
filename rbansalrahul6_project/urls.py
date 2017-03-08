"""rbansalrahul6_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.models import User, Group
from django.views import generic
from django import forms

from dal import autocomplete


class GroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return Group.objects.all()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = dict(
            groups=autocomplete.ModelSelect2Multiple('group_autocomplete'),
        )
        exclude = []


class UserUpdate(generic.UpdateView):
    model = User
    form_class = UserForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'user/(?P<pk>\d+)/$', UserUpdate.as_view()),
    url(r'group/$', GroupAutocomplete.as_view(), name='group_autocomplete'),
]
