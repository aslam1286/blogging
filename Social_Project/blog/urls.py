
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_home'),

    path('post/<int:pk>/detail/', views.PostDetailView.as_view(),
         name='post_detail'),

    path('post/new/', views.PostCreateView.as_view(),
          name='post_create'),

    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),
         name='post_update'),

    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),
         name='post_delete'),

    path('user/<str:username>', views.UserPostListView.as_view(),
           name='user_posts'),


    path('about/', views.about_view, name='blog_about'),

    path('latest_posts/', views.Latest_Posts_View, name='latest_posts'),

    path('python_info/', views.Python_Info_View, name='python_info'),

    path('django_info/', views.Django_Info_View, name='django_info'),

    path('pythonque/', views.pythonque, name='pythonque'),

    path('courses/', views.Our_Courses, name='courses'),

    #

    path('learnpy/', views.Learn_Python, name='learn_python'),

    path('learndj/', views.Learn_Django, name='learn_django'),

    path('learnml/', views.Learn_ML, name='learn_ml'),

    path('learnds/', views.Learn_DS, name='learn_ds')

]