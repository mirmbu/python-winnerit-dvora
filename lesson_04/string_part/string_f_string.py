#f-string.
name = "Dvora"
proffeional = "QA and automation"
expirience = 5

print("Name: ", name, "Proffeional: ", proffeional, "Exprience: ", expirience)

#error - can only concatenate str (not "int") to str
#print("Name: "+ name, "Proffeional: "+ proffeional, "Exprience: "+ expirience)

print(f"Name: {name}. Proffeional: {proffeional}. Expirience: {expirience}.")
print(f"Name: {name.upper()}. Proffeional: {proffeional.lower()}. Expirience: {expirience * 3}.")
print(f"{name=}. {proffeional=}. {expirience=}.")
print(f"{name=}. {proffeional = }. {expirience= }.")

BASE_URL = "www.example.com"
BASE_API_URL = f"{BASE_URL}/api/v1"
BASE_ITEMS_URL = f"{BASE_API_URL}/items"
print(BASE_URL)
print(BASE_API_URL)
print(BASE_ITEMS_URL)