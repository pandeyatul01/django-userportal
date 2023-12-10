from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import logout


from .models import UploadedFile, UserProfile
from .forms import FileUploadForm,UserRegisterForm, UserProfileForm

def home(request):
    return render(request,"home.html")

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('files-list')
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})

@login_required
def file_list(request):
    print("HERE")
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})
@login_required
def view_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'view_profile.html', {'form': form})



class CreateUserView(View):
    template_name = "register.html"

    def get(self, request):
        form = UserRegisterForm()
        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

        context = {"form": form}
        return render(request, self.template_name, context)
    

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect("home")