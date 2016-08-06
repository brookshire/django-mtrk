#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.shortcuts import render, render_to_response

def home_page(request):
    return render_to_response('home.html')
