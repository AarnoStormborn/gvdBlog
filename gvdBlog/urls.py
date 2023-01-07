from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

admin.site.site_header = "Genius Vision Digital Blog Admin"
admin.site.site_title = "Genius Vision Digital Blog Admin site"
admin.site.index_title = "GVD Blog Admin"
