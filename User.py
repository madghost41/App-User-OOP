# your User class goes hereclass User:
class User():
    def __init__(self, name, email, address, password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
    
    def __str__(self):
        return f"I am {self.name} and my email is {self.email}"

   

kurt = User('k.angle', 'kangel@gmail.com', '123 Drury Lane', 'password123')
print(kurt)
