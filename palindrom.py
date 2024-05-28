num=int(input("enter a number:"))
print(num)
temp=num
rev=0

while num!=0:
    
    dgt=num%10
    rev=(rev*10)+dgt 
    
    num=int(num/10) 
    

print(rev)

if rev==temp:
    print("the number is palindrome")
else:
    print("the number is not palindrome")
