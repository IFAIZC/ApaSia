from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Posting
from .forms import UserProfileForm, PostForm
from django.http import JsonResponse


@login_required(login_url='login_user')
def home(request):
    posts = Posting.objects.all().order_by('-created_at')
    return render(request, "home.html", {'posts': posts})

@login_required(login_url='login_user')
def profile_page(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = UserProfileForm(instance=user_profile)
        
    context = {
        'form': form,
        'user_profile': user_profile
    }
    return render(request, 'profile_page.html', context)

@login_required(login_url='login_user')
def posting(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()
            return redirect('home')
    else:
        form = PostForm()
        
    posts = Posting.objects.all().order_by('-created_at')

    return render(request, 'posting.html', {'form': form, 'posts': posts})

@login_required(login_url='login_user')
def delete_post(request, pk):
    posting = get_object_or_404(Posting, pk=pk)
    if request.method == 'POST':    
        posting.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'posting': posting})

@login_required(login_url='login_user')
def edit_post(request, pk):
    posting = get_object_or_404(Posting, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=posting)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=posting)
        
    return render(request, 'edit_post.html', {'form': form, 'posting': posting})

@login_required(login_url='login_user')
def update_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = UserProfileForm(instance=user_profile)
        
    context = {
        'form': form,
        'user_profile': user_profile
    }
    return render(request, 'update_profile.html', context)

@login_required(login_url='login_user')
def like_post(request, pk):
    posting = get_object_or_404(Posting, pk=pk)
    liked = False
    if posting.likes.filter(id=request.user.id).exists():
        posting.likes.remove(request.user)
    else:
        posting.likes.add(request.user)
        liked = True
    
    # Check if the request is an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'likes': posting.total_likes(), 'liked': liked})

    return redirect('home')