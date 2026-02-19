from django.http import HttpResponse

def login(request):
    return HttpResponse("ok login")

def register(request):
    return HttpResponse("ok register")

def logout(request):
    return HttpResponse("ok logout")

def user_view(request, user_id):
    return HttpResponse(f"ok user {user_id}")