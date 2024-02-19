from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', views.feed_page),
    path('publicate/', views.publicate_page, name='publicate_page'),
    path('home/', views.index),
    path('post/<int:id>', views.post_page),
    path('', views.index)

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)