
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin )
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404

from blog.models import Post


def home_view(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html', context)


def about_view(request):
    return render(request,'blog/about.html')



from django.views.generic import (
    ListView,DetailView,CreateView,UpdateView,DeleteView )

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(
            User, username=self.kwargs.get('username')
        )
        return Post.objects.filter(author=user)



def Latest_Posts_View(request):
    post_list = Post.objects.all().order_by('-date_posted')[:5]
    return render(request,'blog/latest_posts.html',{'post_list':post_list})


def Python_Info_View(request):
    return render(request,'blog/python_info.html')


def pythonque(request):
    return render(request,'blog/pythonque.html')

def Django_Info_View(request):
    return render(request,'blog/django_info.html')

def Our_Courses(request):
    return render(request, 'courses/courses.html')


#Learn Python
def Learn_Python(request):
    return render(request, 'courses/learn_python.html')

#Learn Django
def Learn_Django(request):
    return render(request, 'courses/learn_django.html')

#Learn Machine Learning
def Learn_ML(request):
    return render(request, 'courses/learn_ml.html')

#Learn Data Science
def Learn_DS(request):
    return render(request, 'courses/learn_ds.html')








