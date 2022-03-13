from django.contrib import admin
from django.urls import path, include
from app.views import GetMemberView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('members/', GetMemberView.as_view()),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
