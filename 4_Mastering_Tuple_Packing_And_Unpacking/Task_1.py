# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),
]

# Function to process and print order details
def process_orders(order_list):
    for order in order_list:
        # Unpack the tuple
        customer_name, product, quantity = order
        
        # Print the order details
        print(f"Customer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")

# Process and print the sample orders
process_orders(orders)
