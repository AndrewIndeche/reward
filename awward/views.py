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
def user_profile(request, username):

@login_required(login_url='login')
def project(request, post):
