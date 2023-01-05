from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # blogs/
    path("", views.index, name='index'),
    path("blogs/", views.blogList, name='blogList'),
    path("blog/<str:slug>-<int:pk>", views.blogDetail, name='blogDetail'),

    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
