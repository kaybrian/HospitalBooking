from django.shortcuts import render



def Index(request):
    context = {}
    return render(request,'landingpage/index.html',context)


def Blog(request):
    context = {}
    return render(request, 'landingpage/blog.html',context)