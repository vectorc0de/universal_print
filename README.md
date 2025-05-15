# 🗂️🏢 Universal Print Management & Tracking (Django)

This Django-based application provides a structured way to manage and track printers within organizations, focusing on integration with Universal Print. It allows for the organization of users, groups, and printers, along with detailed logging of print jobs.

## ✨ Project Highlights

This project offers a foundational structure for managing your printing infrastructure, particularly when leveraging Universal Print. Key aspects include:

* **🏢 Organization Management:** Define and manage different organizations within the system.
* **👥 Group Management:** Organize users into logical groups for easier permission management or reporting.
* **👤 User Management:** Register and manage user accounts, associating them with specific organizations and groups.
* **🖨️ Printer Inventory:** Maintain a detailed inventory of printers, including their names, owners, driver details, port information, and the organization they belong to. Tracks registration and last seen times.
* **📄 Print Job Tracking:** Log details of each print job, including the document name, status, size, total pages, the local user who printed it, the printer used, and the user who uploaded the job.

## 🚀 Getting Started

Follow these steps to set up and explore this print management application.

### Prerequisites

Ensure you have:

* **Python:** (version 3.x recommended)
* **pip:** (Python package installer)
* **Django:** (latest stable version recommended)

### Installation

1.  **Clone the repository (if available on GitHub):**
    ```bash
    git clone git@github.com:vectorc0de/universal_print.git
    cd printer_cloud
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install django
    # Install any other required Django packages
    ```

4.  **Make migrations:**
    ```bash
    python manage.py makemigrations
    ```

5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    Access the application at `http://127.0.0.1:8000/` and the admin interface at `http://127.0.0.1:8000/admin/`.

### Models Overview

Here's a look at the Django models that structure the application's data:

* **`Organization`:** Represents a distinct organization.
    * `name`: The name of the organization (CharField, max length 16).

* **`Groupo`:** Represents a group of users.
    * `name`: The name of the group (CharField, max length 16).

* **`User`:** Represents a user within the system.
    * `name`: The name of the user (CharField, max length 16).
    * `local_id`: A local user identifier (CharField, max length 128).
    * `password`: User's password (CharField, max length 16).
    * `groups`: Foreign key linking the user to a `Groupo` (on_delete=models.CASCADE).
    * `organization`: Foreign key linking the user to an `Organization` (on_delete=models.CASCADE).

* **`Printer`:** Represents a managed printer.
    * `name`: The name of the printer (CharField, max length 16).
    * `owner`: The owner of the printer (CharField, max length 16).
    * `driver_name`: The printer driver name (CharField, max length 64).
    * `port_name`: The printer port name (CharField, max length 64).
    * `organization`: The organization the printer belongs to (CharField, max length 16).
    * `registered_in`: The date and time the printer was registered (DateTimeField).
    * `last_seen`: The last time the printer was seen or active (CharField, max length 16).

* **`PrinterOuts`:** Represents a record of a printed document.
    * `registered_in`: The date and time the print job was recorded (DateTimeField).
    * `document_name`: The name of the printed document (CharField, max length 256).
    * `job_status`: The status of the print job (IntegerField, default=0). You might need to define specific integer codes for different statuses (e.g., 0: pending, 1: completed, 2: failed).
    * `size`: The size of the printed document (IntegerField, default=0).
    * `total_pages`: The total number of pages in the document (IntegerField, default=0).
    * `local_user_name`: The username on the local machine that initiated the print job (CharField, max length 32).
    * `printer_name`: The name of the printer used for the job (CharField, max length 64).
    * `upload_by`: Foreign key linking the print job to the `User` who initiated it (on_delete=models.CASCADE).

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## 📄 License

GPL v3