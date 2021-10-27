from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Profile, Post,Rate
from .forms import SignupForm, PostForm, UpdateUserForm, UpdateUserProfileForm, RatingsForm

# Create your views here.
def index(request):
    form = PostForm
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'post': post[::-1],
        'form': form,
        'users': users,
        'form':PostForm
    except Post.DoesNotExist:
        posts = None
    }
    return render(request, 'index.html', params)

@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')

@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'user_profile.html', params)

@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'edit_profile.html', params)


@login_required(login_url='login')
def project(request, post):
