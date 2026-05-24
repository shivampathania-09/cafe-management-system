from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cafe'

urlpatterns = [
    path('login/', views.custom_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    
    # Menu URLs
    path('menu/', views.MenuListView.as_view(), name='menu_list'),
    path('menu/add/', views.MenuCreateView.as_view(), name='menu_add'),
    path('menu/<int:pk>/edit/', views.MenuUpdateView.as_view(), name='menu_edit'),
    path('menu/<int:pk>/delete/', views.MenuDeleteView.as_view(), name='menu_delete'),
    
    # Order & Billing URLs
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/new/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/invoice/', views.order_invoice_pdf, name='order_invoice_pdf'),
    path('orders/<int:order_id>/update-status/', views.order_update_status, name='order_update_status'),
    
    # Export URLs
    path('export/orders/', views.export_orders, name='export_orders'),
    path('export/inventory/', views.export_inventory, name='export_inventory'),
    path('export/sales/', views.export_sales, name='export_sales'),

    # Notifications
    path('notifications/', views.notifications_list, name='notifications_list'),
    path('notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
]
