from django.shortcuts import render, reverse, HttpResponseRedirect
from ghost_app.models import Boast_Roast
from ghost_app.forms import PostForm

def index(request):
    all_posts = Boast_Roast.objects.filter().order_by('-id')
    return render(request, 'index.html', {'title': 'Ghost Post', 'all_posts': all_posts})


def boasts_view(request):
    boasts = Boast_Roast.objects.filter(post_type=True).order_by('-id')
    return render(request, 'boasts.html', {'b_title': 'Boasts', 'boasts': boasts})


def roasts_view(request):
    roasts = Boast_Roast.objects.filter(post_type=False).order_by('-id')
    return render(request, 'roasts.html', {'r_title': 'Roasts', 'roasts': roasts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Boast_Roast.objects.create(content = data.get('content'), post_type = data.get('post_type'))
            return HttpResponseRedirect(reverse('homepage'))

    form = PostForm()
    return render(request, 'form.html', {'form': form, 'a_title': 'Add Post'})


def upvote(request, post_id):
    post = Boast_Roast.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, post_id):
    post = Boast_Roast.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def votes_view(request):
    votes = sorted(Boast_Roast.objects.all(), key=lambda votes: votes.num_votes)[::-1]
    return render(request, 'votes.html', {'votes': votes, 'v_title': 'Sorted by Votes'})