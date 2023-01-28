cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
cars[0] = "Toyota"
x = len(cars)
for x in cars:
  print(x)
cars.append("Honda")
cars.pop(1)
cars.insert(2, "Volvo")
cars.remove("Volvo")
for x in cars:
  print(x)

