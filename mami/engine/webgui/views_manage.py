from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from ..models import Stream, Multiview

# Homepage
def dashboard(request):
    return render(request, 'manage/home.html')

