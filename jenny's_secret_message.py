def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
## Esto ya es mio. Jeje
input_name = input("Enter your name: ")
name = input_name.strip()
message = greet(name)
print(message)