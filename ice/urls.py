"""
URL configuration for ice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


from django.http import HttpResponse
import os
import django
from django.core.management import call_command

def run_migrations(request):
    try:
        call_command('migrate')
        return HttpResponse("✅ Migrations ran successfully.")
    except Exception as e:
        return HttpResponse(f"❌ Error running migrations: {str(e)}")


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),  # Include the user management URLs
    # path('', include('django.contrib.auth.urls')),  # Includes built-in login/logout URLs
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('community/', include(('community.urls', 'community'), namespace='community')),
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
    path('chat/', include('chat.urls')),
    path('members/', include('members.urls')),
    path('run-migrations/', run_migrations),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
