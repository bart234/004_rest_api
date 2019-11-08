from rest_framework import generics, mixins
from app_p1.models import BlogPost
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializers
from django.db.models import Q

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView   ): #detail viev
    look_up = 'pk'
    serializer_class = BlogPostSerializers
    # queryset = BlogPost.objects.all()
    
    #wyszukiwanie
    def get_queryset(self):
        qs =BlogPost.objects.all()
        query = self.request.GET.get("q") # q do wyszukiwania ma byc przekazywane jako parametr w url ?q=5
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|
                        Q(content__icontains=query)).distinct()
        return qs


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args,**kwargs) #this create methos is from mixin models

  
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): #detail viev
    look_up = 'pk'
    serializer_class = BlogPostSerializers  
    permission_classes = [IsOwnerOrReadOnly]
    # queryset = BlogPost.objects.all()
    
    def get_queryset(self):
        return BlogPost.objects.all()