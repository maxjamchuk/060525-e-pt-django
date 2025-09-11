from django.contrib import admin
from django.urls import path, include

from news import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('about/', views.about),
    path('news/', include('news.urls'))
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.main),
#     path('info/', views.info),
#     path('news/', views.get_all_news),
#     path('news/faq/', views.faq),
#     path('news/<int:news_id>/, views.get_news_by_id)
# ]
