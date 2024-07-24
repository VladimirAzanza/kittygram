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


# urls.py will change if we have a viewset. We have to configure the routers.
'''
from rest_framework.routers import SimpleRouter
from django.urls import include, path
from cats.views import CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
'''
