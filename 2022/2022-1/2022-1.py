with open("numbers.txt", "r") as file:
    numbers = [line.strip() for line in file]
maxSum=0
sum=0
i=0
while i<len(numbers):
    if(numbers[i] !=''):
        sum+=int(numbers[i]) 
        i+=1
    else:
        if(sum>maxSum):
            maxSum=sum
        sum=0
        i+=1
        
print(maxSum)
