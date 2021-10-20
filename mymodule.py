def greeting(name):
    print("Hello " + name)

def ask(x):
    if x == "what is your name?":
        output = "My name is John"
    elif x == "how old are you?":
        output = "I am 40 year old"
    
    elif x == "are you employed?":
        output = "Yes, I am employed"
    else:
        output = "Ask a valid question"
    print(output)

name = "Mike"

person = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

login = {
    "username": "John3454@test.com",
    "password": 1234567890
}