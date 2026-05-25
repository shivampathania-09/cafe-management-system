# Django Cafe Management System

## Project Overview
The Django Cafe Management System is a comprehensive web application designed to streamline the day-to-day operations of a modern cafe or restaurant. 
The purpose of this system is to replace manual paper-based tracking with an efficient, digital platform that handles menu inventory, point-of-sale operations, order tracking, and sales analytics in a centralized hub.

**Main Objectives:**
- Simplify order taking and automated billing (including GST calculation).
- Provide real-time inventory tracking to prevent stockouts.
- Offer staff an intuitive interface for order lifecycle management.
- Generate actionable insights through a robust analytics dashboard.
- Export financial and operational data for accounting purposes.

## Features
- **Authentication:** Secure staff login and registration system with role-based access control.
- **Dashboard:** An interactive dashboard featuring summary metrics, low stock alerts, and visual charts (using Chart.js) for revenue and orders.
- **Menu Management:** Full CRUD (Create, Read, Update, Delete) capabilities for menu items, pricing, and availability.
- **Order Management:** Point-of-Sale interface to quickly add items, calculate totals with GST, and assign orders to specific tables.
- **Billing and PDF Invoice:** Automated calculation of subtotals, GST (18%), and dynamic generation of downloadable PDF invoices using `xhtml2pdf`.
- **Order Status Tracking:** Track order lifecycles dynamically from "Pending" -> "Preparing" -> "Ready" -> "Delivered".
- **Inventory Management:** Real-time stock deductions upon order creation, preventing negative stock, and auto-disabling out-of-stock items.
- **Data Export:** Export detailed Orders, Inventory, and Sales reports in both `.csv` and true `.xlsx` (Excel) formats.
- **Recent Activity:** An activity ledger logging crucial events like menu updates, inventory warnings, and order status changes.
- **Notifications:** Integrated Django messages framework with auto-dismissing Bootstrap alerts for success, error, and low-stock warnings.
- **Responsive UI:** A clean, mobile-friendly interface built with Bootstrap 5.

## Tech Stack
- **Backend:** Python 3.x, Django 5.x
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Chart.js
- **Database:** SQLite (Default, configurable to PostgreSQL/MySQL)
- **Libraries/Packages used:** 
  - `django` (Web Framework)
  - `xhtml2pdf` (PDF Invoice generation)
  - `openpyxl` (Excel report generation)

## Installation Steps
Follow these steps to set up the project locally:

1. **Clone the project**
   ```bash
   git clone <repository-url>
   cd Cafe_Management_System
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django xhtml2pdf openpyxl
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/` in your browser.

## Screenshots

> *Note: Replace these placeholders with actual screenshots of the application.*

- **Login Page**  
  ![Login Page](docs/screenshots/login.png)

- **Dashboard**  
  ![Dashboard](docs/screenshots/dashboard.png)

- **Menu Page**  
  ![Menu Page](docs/screenshots/menu.png)

- **Order Page**  
  ![Order Page](docs/screenshots/order.png)

- **Billing Page / Invoice**  
  ![Billing Page](docs/screenshots/billing.png)

- **Inventory Page**  
  ![Inventory Page](docs/screenshots/inventory.png)

## Database Schema
The database architecture revolves around five core models:

1. **User (Custom Model):** Extends Django's `AbstractUser` to include a `role` field (e.g., Customer, Staff).
2. **MenuItem:** Represents products available for sale. Contains `name`, `description`, `price`, `stock_quantity`, `low_stock_threshold`, and boolean `is_available`.
3. **Order:** Represents a customer's transaction. Linked to a `User` (staff who took the order). Tracks `status`, `table_number`, `subtotal`, `gst_amount`, and `total_price`.
4. **OrderItem:** The bridge table establishing a Many-to-Many relationship between `Order` and `MenuItem`. Records the `quantity` ordered for a specific item within an order.
5. **Activity:** An audit trail model. Logs a text `message` and categorized `activity_type` (e.g., `inventory_updated`, `order_status`) with a timestamp.

## Additional Sections

### Future Enhancements
- **Customer Facing Portal:** A separate interface allowing customers to scan a QR code, view the digital menu, and place orders directly from their tables.
- **Payment Gateway Integration:** Seamless integration with Stripe or Razorpay to process digital payments directly within the app.
- **Advanced Staff Permissions:** Granular control separating Kitchen Staff views (only seeing pending orders) from Management views (financial reports).

### Challenges Faced
- **PDF Generation Consistency:** Ensuring CSS styles translated correctly into the `xhtml2pdf` generated invoices required careful inline styling and table layouts.
- **Concurrency in Inventory Tracking:** Ensuring stock quantities don't drop below zero if multiple staff members place orders for a low-stock item simultaneously.

### Conclusion
This Cafe Management System serves as a robust foundation for modernizing restaurant workflows. By prioritizing a clean user interface alongside critical business logic like inventory tracking and billing automation, it significantly reduces operational overhead.

> *A Django-based Cafe Management System project developed for my internship purpose.*
