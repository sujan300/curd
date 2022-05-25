from django import forms
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from blog.models import Post
from blog.forms import PostForm

# Create your views here.


def post_view(request):
    form = PostForm()
    if request.method =="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            print("##############################yes valid !!!!!!!!!!!1")
            form.save()
            form = PostForm()


    posts = Post.objects.all()
    return render(
        request,
        'index.html',
        {
            'posts':posts,
            'form':form,
            'home':True,
        }
    )




# this is for post details #################
def post_details(request,id):
    each_post = get_object_or_404(Post,id =id)
    return render(
        request,
        "post_detail.html",
        {
            'each_post':each_post,
        },
    )




# this function for deleting post

def delete_view(request,id):
    post = Post.objects.get(id =id)
    post.delete()
    return HttpResponseRedirect("/")



# this view is for editing posts
def edit_view(request,id):
    post = get_object_or_404(Post,id =id)

    print("hsbdhshdjsdjvsdvjsvdjvsjdjhbsdjsjbdhiuehiwjodjcbbjbjhvbjhbcs c[[[[[[[",request.POST)
    
    if request.method !='POST':
        form = PostForm(instance=post)
        print("=========================",request.FILES)

    else:
        form = PostForm(data =request.POST,files=request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    # else:
    #     form = PostForm(instance=post)

    posts = Post.objects.all()
    return render(
        request,
        'index.html',
        {
            'form':form,
            'posts':posts,
            'home':True,
        }
    )


