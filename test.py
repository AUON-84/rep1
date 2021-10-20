import mymodule as mm
import platform 


ymssg = mm.ask("how old are you?")
emssg = mm.ask("are you employed?")
print(ymssg)
print(emssg)

username = mm.login.get("username")
password = mm.login.get("password")

print(username)
print(password)


name = mm.person['name']
print(name)

age = mm.person['age']
print(age)

country = mm.person['country']
print(country)

dir(platform.system())

name = "JohnDoe"

print(name.removeprefix("John"))

def removeprefix_(x, name):
    pref = len(x)
    x = name[pref:]
    print(x)

print(removeprefix_("John", "JohnDoe"))
