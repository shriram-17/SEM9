def check_pizza(count):
    if 1 <= count <= 10:
        return "Success"
    elif count > 10 or count < 1:
        return "Invalid order quantity"
    else:
        return "Invalid input"