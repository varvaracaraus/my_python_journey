# Pizza Order Processor
# This script processes a series of pizza orders, organizing them by customer name and tallying the
# quantities for each type of pizza ordered.

def process_orders() -> None:
    """
    Processes and displays customer orders for pizzas, organizing them by customer name and pizza type.
    """
    n = int(input("Enter the number of orders: "))
    orders = {}

    # Gathering and processing orders
    for i in range(n):
        order_info = input(f"Enter information about the {i + 1} order: ").split()
        customer, pizza, quantity = order_info[0], order_info[1], int(order_info[2])

        # Organizing orders by customer and pizza type
        if customer not in orders:
            orders[customer] = {}
        if pizza not in orders[customer]:
            orders[customer][pizza] = 0
        orders[customer][pizza] += quantity

    # Displaying the processed orders
    customers = sorted(orders.keys())
    for customer in customers:
        print(f"{customer}:")
        for pizza, quantity in sorted(orders[customer].items()):
            print("     ", f"{pizza}: {quantity}")


# Running the order processing function
process_orders()
