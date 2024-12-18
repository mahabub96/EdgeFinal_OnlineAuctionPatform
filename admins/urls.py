from django.urls import path
from .views import (
    AdminOverviewView,
    ManageAuctionsView,
    ManageUsersView,
    ManageCategoriesView,
    AdminLogsView,
    AdminNotificationsView,
)

# Template-based URLs
template_urlpatterns = [
    path('dashboard/', AdminOverviewView.as_view(), name='admin-dashboard'),
    path('manage-auctions/', ManageAuctionsView.as_view(), name='template-manage-auctions'),
    path('manage-users/', ManageUsersView.as_view(), name='template-manage-users'),
    path('manage-categories/', ManageCategoriesView.as_view(), name='template-manage-categories'),
    path('logs/', AdminLogsView.as_view(), name='template-logs'),
    path('notifications/', AdminNotificationsView.as_view(), name='template-notifications'),
]

# API-based URLs
api_urlpatterns = [
    path('api/overview/', AdminOverviewView.as_view(), name='api-admin-overview'),
    path('api/manage-auctions/', ManageAuctionsView.as_view(), name='api-manage-auctions'),
    path('api/manage-auctions/<int:item_id>/', ManageAuctionsView.as_view(), name='api-update-auction'),
    path('api/manage-users/', ManageUsersView.as_view(), name='api-manage-users'),
    path('api/manage-users/<int:user_id>/', ManageUsersView.as_view(), name='api-update-user'),
    path('api/manage-categories/', ManageCategoriesView.as_view(), name='api-manage-categories'),
    path('api/manage-categories/<int:category_id>/', ManageCategoriesView.as_view(), name='api-update-category'),
    path('api/logs/', AdminLogsView.as_view(), name='api-logs'),
    path('api/notifications/', AdminNotificationsView.as_view(), name='api-notifications'),
]

urlpatterns = template_urlpatterns + api_urlpatterns

# from django.urls import path
# from .views import (
#     AdminOverviewView, ManageAuctionsView, ManageUsersView,
#     ManageCategoriesView, AdminLogsView, AdminNotificationsView,AddCategoryView
# )

# # Template Routes
# template_urlpatterns = [
#     path("overview/", AdminOverviewView.as_view(), name="template-admin-overview"),
#     path("manage-auctions/", ManageAuctionsView.as_view(), name="template-manage-auctions"),
#     path("manage-users/", ManageUsersView.as_view(), name="template-manage-users"),
#     path("manage-categories/", ManageCategoriesView.as_view(), name="template-manage-categories"),
#     path('add-category/', AddCategoryView.as_view(), name='add_category'),  # This is the one that should match
#     path("admin-logs/", AdminLogsView.as_view(), name="template-admin-logs"),
#     path("admin-notifications/", AdminNotificationsView.as_view(), name="template-admin-notifications"),
# ]

# # API Routes
# api_urlpatterns = [
#     path("api/overview/", AdminOverviewView.as_view(), name="api-admin-overview"),
#     path("api/manage-auctions/", ManageAuctionsView.as_view(), name="api-manage-auctions"),
#     path("api/manage-auctions/<int:item_id>/", ManageAuctionsView.as_view(), name="api-manage-auction-item"),
#     path("api/manage-users/", ManageUsersView.as_view(), name="api-manage-users"),
#     path("api/manage-users/<int:user_id>/", ManageUsersView.as_view(), name="api-manage-user"),
#     path("api/manage-categories/", ManageCategoriesView.as_view(), name="api-manage-categories"),
#     path("api/manage-categories/<int:category_id>/", ManageCategoriesView.as_view(), name="api-manage-category"),
#     path("api/admin-logs/", AdminLogsView.as_view(), name="api-admin-logs"),
#     path("api/admin-notifications/", AdminNotificationsView.as_view(), name="api-admin-notifications"),
# ]

# # Combine URL patterns
# urlpatterns = template_urlpatterns + api_urlpatterns
