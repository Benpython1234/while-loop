i = 1
while i<6:
    print(i)
    i+=1
    
n = int(input("Enter the number: "))

sum = 0
i=1

while i<=n:
    sum = sum+i*i
    print(sum)
    i = i+1
    
print(f"Your sum is equal to : {sum}")

n = int(input("Enter the number: "))

sum = 0 
temp = n
while temp>0:
    digit = temp % 10 
    sum = sum+digit**3
    temp = temp//10 

if n == sum:
    print("The number is Armstrong number")
else:
    print("The number is not Armstrong number")

#score board update

target_score = 250
current_score = 0
while current_score<target_score:
    runs = int(input("Enter the amount of runs score in this Ball: "))
    current_score = current_score+runs
    print(f"your current score is : {current_score} / {target_score}")
print("Target reached you WON THE MATCH!!!")

