def check_age(age):
    if 1 >= age or age <= 100:
        return True
    return False

print(check_age(50))