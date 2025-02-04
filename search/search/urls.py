"""search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
import search

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^search$', search.search),
	url(r'^result', search.result),
	# url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
	#     {'document_root': settings.STATIC_PATH, 'show_indexes': True})
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )