"""
URL configuration for AuctionPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include app-specific URLs
    path('users/', include('users.urls')),              # URLs for the 'users' app
    path('auction-items/', include('auction_items.urls')),  # URLs for the 'auction_items' app
    path('bids/', include('bids.urls')),                # URLs for the 'bids' app
    path('payments/', include('payments.urls')),        # URLs for the 'payments' app
    path('notifications/', include('notifications.urls')),  # URLs for the 'notifications' app
    path('logs/', include('logs.urls')),                # URLs for the 'logs' app
    path('files/', include('files.urls')),              # URLs for the 'files' app
    path('categories/', include('categories.urls')),    # URLs for the 'categories' app
    path('transactions/', include('transactions.urls')),# URLs for the 'transactions' app
    path('admins/', include('admins.urls')),

    # Add authentication endpoints for REST API (JWT)
    #path('api/token/', include('rest_framework_simplejwt.urls')),  
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

