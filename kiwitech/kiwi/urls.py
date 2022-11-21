
from django.urls import path
from . import views
from rest_framework import routers

from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

 
router = routers.SimpleRouter()
# router.register(r'', views.PostViewSet),
# router.register(r'', views.StudentViewSet),
# router.register(r'',views.MusicianViewSet)
urlpatterns = [
    path('home',views.home,name='home'),
    path('about/<int:aboutid>',views.about,name='about'),
    path('hello',views.helloView.as_view()),
     path('go-to-django/', views.RedirectView.as_view(url='https://www.djangoproject.com/'), name='go-to-django'),
    path('<pk>/', views.PostDetailView.as_view()),
     path('wdwd', views.PostList.as_view()),
      path('<pk>/update', views.PostUpdateView.as_view()),
      path("book/",views.BookApiView.as_view()),
      path('charge',views.charge,name='charge'),
      path('index',views.index,name='index'),
      path('restaurants/', views.Restaurants.as_view()),
    path('restaurants/<str:restaurant_id>/', views.RestaurantDetail.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/', views.Recipes.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/', views.RecipeDetail.as_view()),
     path('', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    
 
      
]
urlpatterns += router.urls
