from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import UploadFile
from .serializers import FileSerializer
from rest_framework import generics
from .paginations import CustomPagination

# Create your views here.
def view_profile(request):
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
#6 using generics
#6.1 GET POST
class GenericsList(generics.ListCreateAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = FileSerializer
    pagination_class = CustomPagination

#6.2 GET PUT DELETE
class GenericsBk(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = FileSerializer