from .models import Notification

def notifications_context(request):
    if request.user.is_authenticated:
        # Assuming staff/admins can see all notifications for simplicity,
        # or you can filter by `user=request.user` or `user__isnull=True`
        qs = Notification.objects.filter(user=request.user) | Notification.objects.filter(user__isnull=True)
        unread_count = qs.filter(is_read=False).count()
        recent_notifications = qs.order_by('-created_at')[:5]
        return {
            'unread_notifications_count': unread_count,
            'recent_notifications': recent_notifications,
        }
    return {
        'unread_notifications_count': 0,
        'recent_notifications': [],
    }
