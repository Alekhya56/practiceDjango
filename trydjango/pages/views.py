from django.shortcuts import render
# Create your views here.
def home_view(requset, *args, **kwargs):
    # print(requset)
    # print(args, kwargs)
    # print("usser",requset.user)
    # return HttpResponse("<h1> Hai Santosh </h1>")
    return render(requset, "home.html", {} )
    
def contact_view(request,*args, **kwargs):
    my_context ={
        "my_title" : "This is a title",
        "my_details" : [10, 1996, 2019, 2708,'Alekhya'],
        "my_value" : 26,
        "heading" : "<h1>This is heading of the contcat page</h1>"
    }
    return render (request,"contact.html", my_context)
def about_view(request, *args, **kwargs):
    return render(request,"about.html",{})
