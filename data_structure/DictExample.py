#define a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)

#access dictionary
carModel = car["model"]
carYear = car.get("year")

print(carModel, carYear) # Mustang 1964

# add new / change value
car["year"] = 2008
car["price"] = 1000000
print(car)

# Loop
for key in car:
    print(key, car.get(key))

for key, value in car.items():
    print(key, value)

# check if key exists in dict
if "model" in car:
    print("Yes, key model exists")

modelValue = car.pop("model")
print(modelValue)
print(car)
