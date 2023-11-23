with open("numbers.txt", "r") as file:
    numbers = [line.strip() for line in file]
maxSum=0
secondSum=0
thirdSum=0
sum=0
i=0
while i<len(numbers):
    if(numbers[i] !=''):
        sum+=int(numbers[i]) 
        i+=1
    else:
        if(sum>maxSum):
            thirdSum=secondSum
            secondSum=maxSum
            maxSum=sum
        elif(sum>secondSum):
            thirdSum=secondSum
            secondSum=sum
        elif(sum>thirdSum):
            thirdSum=sum         
        sum=0
        i+=1
     
print(maxSum+secondSum+thirdSum)