from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random
from decimal import Decimal
from django.contrib.auth import get_user_model
from cafe.models import MenuItem, Order, OrderItem, Activity

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with sample demo data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # 1. Create Users
        admin_user, created = User.objects.get_or_create(username='admin', defaults={
            'email': 'admin@example.com',
            'first_name': 'Admin',
            'last_name': 'User',
            'is_superuser': True,
            'is_staff': True,
            'role': 'staff'
        })
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        staff_user, created = User.objects.get_or_create(username='staff', defaults={
            'email': 'staff@example.com',
            'first_name': 'Staff',
            'last_name': 'User',
            'is_staff': True,
            'role': 'staff'
        })
        if created:
            staff_user.set_password('staff123')
            staff_user.save()

        # 2. Create Menu Items
        menu_data = [
            {'name': 'Cold Coffee', 'price': '90.00', 'stock': 50, 'low_stock': 10},
            {'name': 'Burger', 'price': '120.00', 'stock': 20, 'low_stock': 5},
            {'name': 'Pizza', 'price': '250.00', 'stock': 3, 'low_stock': 5}, # low stock
            {'name': 'Pasta', 'price': '180.00', 'stock': 15, 'low_stock': 5},
            {'name': 'Cappuccino', 'price': '110.00', 'stock': 40, 'low_stock': 10},
            {'name': 'Sandwich', 'price': '80.00', 'stock': 25, 'low_stock': 5},
            {'name': 'French Fries', 'price': '100.00', 'stock': 0, 'low_stock': 5}, # out of stock
            {'name': 'Chocolate Cake', 'price': '150.00', 'stock': 12, 'low_stock': 3},
        ]

        menu_items = []
        for item in menu_data:
            obj, created = MenuItem.objects.get_or_create(
                name=item['name'],
                defaults={
                    'price': Decimal(item['price']),
                    'stock_quantity': item['stock'],
                    'low_stock_threshold': item['low_stock'],
                    'is_available': item['stock'] > 0
                }
            )
            # Update if exists to ensure fresh stock amounts for demo
            if not created:
                obj.price = Decimal(item['price'])
                obj.stock_quantity = item['stock']
                obj.is_available = item['stock'] > 0
                obj.save()
            
            if obj.stock_quantity > 0:
                menu_items.append(obj)
                
        # 3. Create Orders and Activity
        statuses = ['pending', 'preparing', 'ready', 'delivered']
        now = timezone.now()
        
        # Generate orders over the last 7 days to populate charts
        for i in range(40):
            days_ago = random.randint(0, 6)
            order_date = now - timedelta(days=days_ago, hours=random.randint(0, 10))
            
            # Use model fields
            order = Order.objects.create(
                user=staff_user,
                status=random.choice(statuses),
                table_number=str(random.randint(1, 10))
            )
            
            # Since auto_now_add is on created_at, we need to update it after creation
            Order.objects.filter(id=order.id).update(created_at=order_date)
            
            subtotal = Decimal('0.00')
            # Add 1 to 3 items per order
            num_items = random.randint(1, 3)
            selected_items = random.sample(menu_items, num_items)
            
            for m_item in selected_items:
                quantity = random.randint(1, 3)
                OrderItem.objects.create(
                    order=order,
                    menu_item=m_item,
                    quantity=quantity
                )
                subtotal += m_item.price * quantity
            
            gst = subtotal * Decimal('0.18')
            total = subtotal + gst
            order.subtotal = subtotal
            order.gst_amount = gst
            order.total_price = total
            order.save()
            
            # Log some activity
            act_date = order_date + timedelta(minutes=5)
            activity = Activity.objects.create(
                message=f"Order #{order.id} created",
                activity_type='order_created'
            )
            Activity.objects.filter(id=activity.id).update(created_at=act_date)

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with demo data!'))
