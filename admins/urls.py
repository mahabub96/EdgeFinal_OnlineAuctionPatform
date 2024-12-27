from django.urls import path
from . import views

urlpatterns = [
    path('api/admin/overview/', views.AdminOverviewView.as_view(), name='admin_overview'),
    path('api/admin/auctions/', views.ManageAuctionsView.as_view(), name='manage_auctions'),
    path('api/admin/auctions/<int:item_id>/', views.ManageAuctionsView.as_view(), name='update_auction'),
    path('api/admin/users/', views.ManageUsersView.as_view(), name='manage_users'),
    path('api/admin/users/<int:user_id>/', views.ManageUsersView.as_view(), name='update_user'),
    path('api/admin/categories/', views.ManageCategoriesView.as_view(), name='manage_categories'),
    path('api/admin/categories/<int:category_id>/', views.ManageCategoriesView.as_view(), name='update_category'),
    path('api/admin/logs/', views.AdminLogsView.as_view(), name='admin_logs'),
    path('api/admin/notifications/', views.AdminNotificationsView.as_view(), name='admin_notifications'),
]





# from django.urls import path
# from .views import (
#     AdminOverviewView,
#     ManageAuctionsView,
#     ManageUsersView,
#     ManageCategoriesView,
#     AdminLogsView,
#     AdminNotificationsView,
# )

# # Template-based URLs
# template_urlpatterns = [
#     path('dashboard/', AdminOverviewView.as_view(), name='admin-dashboard'),
#     path('manage-auctions/', ManageAuctionsView.as_view(), name='template-manage-auctions'),
#     path('manage-users/', ManageUsersView.as_view(), name='template-manage-users'),
#     path('manage-categories/', ManageCategoriesView.as_view(), name='template-manage-categories'),
#     path('logs/', AdminLogsView.as_view(), name='template-logs'),
#     path('notifications/', AdminNotificationsView.as_view(), name='template-notifications'),
# ]

# # API-based URLs
# api_urlpatterns = [
#     path('api/overview/', AdminOverviewView.as_view(), name='api-admin-overview'),
#     path('api/manage-auctions/', ManageAuctionsView.as_view(), name='api-manage-auctions'),
#     path('api/manage-auctions/<int:item_id>/', ManageAuctionsView.as_view(), name='api-update-auction'),
#     path('api/manage-users/', ManageUsersView.as_view(), name='api-manage-users'),
#     path('api/manage-users/<int:user_id>/', ManageUsersView.as_view(), name='api-update-user'),
#     path('api/manage-categories/', ManageCategoriesView.as_view(), name='api-manage-categories'),
#     path('api/manage-categories/<int:category_id>/', ManageCategoriesView.as_view(), name='api-update-category'),
#     path('api/logs/', AdminLogsView.as_view(), name='api-logs'),
#     path('api/notifications/', AdminNotificationsView.as_view(), name='api-notifications'),
# ]

# urlpatterns = template_urlpatterns + api_urlpatterns

# from django.urls import path
# from .views import (
#     AdminOverviewView, ManageAuctionsView, ManageUsersView,
#     ManageCategoriesView, AdminLogsView, AdminNotificationsView,AddCategoryView
# )


