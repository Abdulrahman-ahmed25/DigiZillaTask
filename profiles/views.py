from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import UploadFile

# Create your views here.
def view_profile(request):
    # if request.method == 'POST':
    #     uploaded_file = request.FILES['document']
    #     fs = FileSystemStorage()
    #     fs.save(uploaded_file.name, uploaded_file)
    context={
        'user':request.user
    }
    return render(request, 'profiles/profile_view.html', context)

def file_list(request):
    files = UploadFile.objects.all()
    return render(request, "profiles/file_list.html", {
        'files':files
    })

def file_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()  
    return render(request, "profiles/file_upload.html", {
        'form': form
    })