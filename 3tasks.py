#Task!
random_list=[2, 67, 43, 3, 7]
e=random_list

while e==random_list:
    print(random_list)

#Task2
letters=["a", "b", "c", "f", "g", "d", "e"]
index=0

while index < len(letters):
    if letters[index] in ["f", "g"]:
        index+=1
        continue 
    print(letters[index])
    index += 1


#Task3
n=int(input("Enter number: "))
c=0
while c<=n:
    print(c)
    c+=1

#Task4
password=["alex777"]
chances=3

for code in range(chances):
    log_in=input("Enter password: ")
    if log_in in password:
        print("accessed")
        break
    else:
        chances-=1
        if chances==0:
         print("Blocked for 24 hours")
        else:
            print("Password is wrong, available chances: ", {chances})
        

    



    