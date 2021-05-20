from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .forms import SignupForm
# Create your views here.

def signup_view(request):
    if request.method == 'POST' : #and request.is_ajax():
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            # return JsonResponse({
            #     'msg':'success'
            # })
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})
