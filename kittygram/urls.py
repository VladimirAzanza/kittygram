from django.urls import path

from cats.views import cat_list
# from cats.views import APICat
# from cats.views import CatList, CatDetail

# LOW LEVEL:
# path('cats/', APICat.as_view()),

urlpatterns = [
   path('cats/', cat_list),
   # HIGH LEVEL:
   # path('cats/', CatList.as_view()),
   # path('cats/<int:pk>/', CatDetail.as_view())
]
