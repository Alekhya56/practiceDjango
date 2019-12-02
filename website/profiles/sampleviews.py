def register_view(request):
    if request.method == 'POST':
        print("I am POST method")
        #print(request.POST['first_name'])
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['Username']
        email      = request.POST['Email']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password =password1, email= email, first_name = first_name, last_name= last_name )
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, "register.html")

def login_view(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info (request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    auth.logout(requset , user)
    return redirect('/')