# View for user
def register_menu():
    print("\n=== REGISTER ACCOUNT ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    return username, password

def login_menu():
    print("\n=== LOGIN ===")    
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    return username, password

def show_message(message):
    print(message)