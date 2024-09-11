import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


try:
    length = int(input("Enter the desired length for the password: "))
    if length < 1:
        print("Please enter a positive integer for the length.")
    else:
        generated_password = generate_password(length)
        
        print(f"Generated password: {generated_password}")
except ValueError:
    print("Please enter a valid integer for the length.")
