
# Celsius↔Fahrenheit↔Kelvin, plus km↔miles

c="Celsius"
f="Fahrenheit"
k="Kelvin"
km="Kilometer"
mi="Miles"

def celsius_to_fahrenheit(v):
  return v*9/5+32

def celsius_to_kelvin(v):
  return v+273.15

def fahrenheit_to_celsius(v):
  return (v-32)*5/9

def fahrenheit_to_kelvin(v):
  return (v-32)*5/9+273.15

def kelvin_to_celsius(v):
  return v-273.15

def kelvin_to_fahrenheit(v):
  return (v-273.15)*9/5+32

def kilometer_to_miles(v):
  return v*0.621371

def miles_to_kilometer(v):
  return v/0.621371

converters={
  "1": celsius_to_fahrenheit,
  "2": celsius_to_kelvin,
  "3": fahrenheit_to_celsius,
  "4": fahrenheit_to_kelvin,
  "5": kelvin_to_celsius,
  "6": kelvin_to_fahrenheit,
  "7": kilometer_to_miles,
  "8": miles_to_kilometer,
}

temperature_limit={
  "1": -273.15,
  "2": -273.15,
  "3": -459.67,
  "4": -459.67,
  "5": 0,
  "6": 0,
  "7": 0,
  "8": 0,
}

while(True):
  print("Select an operation:")
  print("Temperature:")
  print(f"0: Quit")
  print(f"1: {c}->{f}")
  print(f"2: {c}->{k}")
  print(f"3: {f}->{c}")
  print(f"4: {f}->{k}")
  print(f"5: {k}->{c}")
  print(f"6: {k}->{f}")
  print(f"7: {km}->{mi}")
  print(f"8: {mi}->{km}")
  
  raw=input("Operation (0-8): ")

  try:
    op=int(raw)
  except ValueError:
    print("\nInappropriate value.\n\n")
    continue

  if op==0:
    break
    
  if not (op>=1 and op<=8):
    print("\nOut of range.\n\n")
    continue

  try:
    v = float(input("Value: "))
  except ValueError:
    print("\nInappropriate value.\n\n")
    continue
  
  if v < temperature_limit[str(op)]:
    print("\nInappropriate value.\n\n")
    continue
  
  result=round(converters[str(op)](v),2)

  print(f"\nResult: {result}\n\n")
  

  


