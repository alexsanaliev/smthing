# Tasl1
height=float(input("Enter your height: "))

if height==155:
    print("Your ideal weight range is: 43-48 kilos ")

elif height==165:
    print("Your ideal weight range is: 50-57 kilos ")

elif height==175:
    print("Your ideal weight range is: 60-65")

elif height==190:
    print("Your ideal weight range is: 70-77")

else:
    print("Your ideal weight range is: 85-95") #Sərtdə formuldan istifadə qeyd olunmayib, ona gore bir təhər hesablayir,
# yada butun cəki və boy araliglari əhatə etmə uchun daha uzun kod alinir 
    

# Task2
shopping_list={
    "t-shirt": 28,
    "trousers": 52,
    "shoes": 77,
    "glasses": 12, 
    "cap": 22}
shopping_cart=[]
print("Available products: ", shopping_list)
choice=input("Add products to the shopping cart using comma: ").split(",")
for items in choice:

 if items in shopping_list:
    shopping_cart.append(items)
 else:
     print("This product is not available in stock")

print("Added to the cart", shopping_cart) 

print("Total cost including taxes: ",)
# UNFORTUNATELY DIDN`T COMPLETE THIS ONE, i`LL APRECIATE IT, IF YOU GONNA HELP ME

# Task3
car=0.50
bus=1
truck=2
fuel=1

wehicle=input("Type of wehicle? ")
distance=float(input("Enteк covered distance in km`s "))

if wehicle=="car":
  print(distance*car, "$")
elif wehicle=="bus":
  print(distance*bus, "$")
else:
  print(distance*truck, "$")