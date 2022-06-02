def is_vowel(a):
    if a in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

def is_consonant(a):
    if not isinstance(a, str):
        raise TypeError(f"{a} is an invalid argument type. Argument takes in str type.")
    elif is_vowel(a) == True:
        return False
    else: 
        return True

def apply_discount(price, discount_amount):
    discount_amount = discount_amount / 100
    return (f"The after discount price is ${(price) - (price * discount_amount)}")

def calculate_tip(tip_amount, total_bill_amount): 
    tip_amount = tip_amount / 100 
    return (f" The tip amount should be ${total_bill_amount * tip_amount}") 
