# Elon Musk Laptop Store

A simple console-based inventory and shopping cart application for a laptop store, built with Python. This project provides both Admin and Buyer interfaces to manage, display, and purchase laptop inventory, with user-friendly table displays using the `tabulate` library.

## Features

### Admin Features
- **Admin Login**: Secure admin access with username and password.
- **Display Laptops**: View all available laptops in a formatted table.
- **Add Laptop**: Add new laptops to the inventory.
- **Delete Laptop**: Remove laptops from inventory (with a recycle bin for recovery).
- **Update Laptop**: Edit laptop details.
- **Recycle Bin**: View and restore deleted laptops.

### Buyer Features
- **View Laptops**: Browse the list of laptops for sale.
- **Add to Cart**: Select laptops with quantity to add to the shopping cart.
- **View/Edit Cart**: View, update, or remove items from the cart.
- **Payment**: Complete payment with automatic total calculation and change.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `tabulate` library

Install the required library:
```bash
pip install tabulate
```

### Running the Application

1. Save the provided Python script into a file, for example `main.py`.
2. Run the script:
    ```bash
    python main.py
    ```

## Usage

When you run the program, the main menu will appear:
- Choose to enter as **Admin** or **Buyer**.
- Follow the on-screen instructions.
- All interactions are handled through the terminal/command line.

### Admin Credentials
- **Username:** `admin`
- **Password:** `123`

### Example Display

```text
Welcome to Elon Musk Laptop Store
Would you like to enter as:
1. Buyer (or type "buyer")
2. Admin (or type "admin")
3. Exit (or type "exit" or "keluar")
Choose (1/2/3):
```

## Code Structure

- **Admin Mode:** Inventory management (add, edit, delete, restore).
- **Buyer Mode:** Shopping, add to cart, checkout, and modify cart.
- **Database:** Uses Python lists (no persistent storage).
- **UI:** Command-line interface, neat tables with `tabulate`.

## Authors

- Ardinata  
  *Feel free to add your contact information or GitHub profile.*

## License

This project is for educational purposes and is free to use or modify.

---
