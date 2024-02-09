## Authorization Decorator: 
# Create a decorator called authorize that can be applied to 
# functions requiring authorization. It should take a username 
# and password as arguments and only execute the function if the 
# provided credentials match predefined values. 
# Otherwise, it should raise an UnauthorizedError

definedUser = "Danny"
definedPass = "123"

def authorize(func):
    def wrapper(username, password):
        if (username == definedUser and password == definedPass):
            func(username, password)
        else:
            raise Exception("Unauthorized Error")
    return wrapper

@authorize
def login(username, password):
    print("You have successfully logged in!")

login("Danny", "123")
login("Danny", "1234")
