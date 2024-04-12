
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
  return render(request, 'home.html')


def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(
      request, username=username, password=password
    )
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.error(request, "Invalid credentials")
      return redirect('login')
  else:
    return render(request, 'login1.html')


def register_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password1 = request.POST['password1']
    if password == password1:
      if User.objects.filter(email=email).exists():
        messages.error(request, 'Email is already taken')
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.error(request, 'username already taken')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else:
      messages.error(request, "Password does not match")
      return redirect('register')  # redirect send you to a diff page from root directory itself
  else:
    return render(request, 'register1.html')
def logout_view(request):
  logout(request)
  return redirect('home')  # Redirect to login page after logout