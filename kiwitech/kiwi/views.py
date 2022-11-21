from datetime import timezone
from locale import currency
from symbol import return_stmt
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,RedirectView,DetailView,ListView,UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import PostSerializer,BookSerializer, StudentSerializer
from .models import Post, Student
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.http import JsonResponse,HttpResponse
from django.conf import settings
import stripe
from django.contrib.auth.hashers import make_password,check_password
from .task import *
from kiwi import serializers 

from rest_framework import generics
from .models import Snippet,Musician
from .serializers import SnippetSerializer



from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Restaurant, Recipe, Ingredient
from django.http import Http404
from rest_framework import status
#function based view 
def home(request):
    # return HttpResponse('hello')
    def get_context_data(self,**kwargs):
     context = super().get_context_data(**kwargs)
     context['key']=settings.STRIPE_PUBLISHABLE_KEY
    return render(request,'home.html',{'name':'Chirag'})


def charge(request):
    if request.method == "POST":
      charge= stripe.Charge.create(
        amount=500,
        currency='usd',
        description='A Django Charge',
        source=request.POST['stripeToken']
      )
      return render(request,'charge.html')




def about(request,aboutid):
    return HttpResponse(aboutid)

#TemplateView using class based view example
class helloView(TemplateView):
      paginate_by = 2
      model = Post
      template_name = "hello.html"

def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
            
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context



#RedirectView 
class PostCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Post, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)    


#Detailview

class PostDetailView(DetailView):
    # specify the model to use
    model = Post

#Listview 
class PostList(ListView):
 
    # specify the model for list view
    model = Post  

#updateview 
class PostUpdateView(UpdateView):
    # specify the model you want to use
    model = Post
  
    # specify the fields
    fields = [
        "title",
        "author"
    ]    


#viewset
class PostViewSet(viewsets.ModelViewSet):
      queryset = Post.objects.all()
      serializer_class = PostSerializer



#apiview



class PostApiView(APIView):

    def get(self,request):
        allPost = Post.objects.all()
        return Response({'Message':"List of Post","Post List": allPost})
   


    def post(self,request):

        Post.objects.create(
                           title=request.data["title"],
                           content=request.data["content"],
                           author=request.data["author"]

        )
        post = Post.objects.filter(title=request.data["title"]).values()
        return JsonResponse({'Message': " new  Post"})


class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List of Books", "Book List":allBooks})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=BookSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Book.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author")
                            )

        book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":book})



class StudentViewSet(viewsets.ModelViewSet):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer



      def retrieve(self, request,pk=None):
          queryset = Student.objects.all()
          student=get_object_or_404(queryset,pk=pk)
          serializer_class = StudentSerializer(student)
          return Response(serializers.data)

         


    #   print(make_password) 
    #   print(check_password('chirag','0x7fb6f0d3c5e0'))    



def index(request):
#    send_mail_without_celery()
    sleepy()
    return HttpResponse("hello celery")


def send_mail_without_celery():
    send_mail(
    'CELERY WORKED',
    'Here is the message.',
    'chiragsaxena001@gmail.com',
    ['chiragsaxena001@gmail.com'],
    fail_silently=False,
)         
    return None


#   pagination

from django.shortcuts import render
from django.core.paginator import Paginator 

from .models import Book

def index(request):
    books = Book.objects.all()

    book_paginator = Paginator(books, 5)

    page_num = request.GET.get('page')

    page = book_paginator.get_page(page_num)

    context = {
        'count' : book_paginator.count,
        'page' : page
    }
    return render(request, 'index.html', context)


class Restaurants(APIView):

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = serializers.RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):

    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        serializer = serializers.RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def delete(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Recipes(APIView):

    def get(self, request, restaurant_id):
        recipes = Recipe.objects.filter(restaurant__id=restaurant_id)
        serializer = serializers.RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_id):
        try:
            Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404

        serializer = serializers.RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant_id=restaurant_id, ingredients=request.data.get("ingredients"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):

    def get(self, request, restaurant_id, recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant__id=restaurant_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        serializer = serializers.RecipeSerializer(recipe)
        return Response(serializer.data)

    def delete(self, request, restaurant_id, recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant__id=restaurant_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer        



class MusicianViewSet(viewsets.ModelViewSet):
      queryset = Musician.objects.all()
      serializer_class = StudentSerializer


 

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        context['count'] = context['task'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task'] = context['task'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    # fields = ['title', 'description']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('task')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage, self).get(*args, *kwargs)
     