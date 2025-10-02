for i in range(0, 101, 18):
    print(i)
    
for i in range(100, -1, -18):
    print(i)
    
count=1
while count<=10:
    print("Hello, World!")
    count +=4

for i in range(1,10):
    if i%2==0:
        continue
    print(i)

for i in range(1,11):
    print(i)
    
####################################33
table = 7

for i in range(1,11):
    print(f"{table}x{i}={table*i}")
#######################################
count=1

while count>=10:
    print(count)
    count -=1
########################################
num=0
for i in range(1,101):
    num += i
print(num)



print(sum(range(1,101)))


for i in range(1,51):
    if i%2==0:
        print(i)


count = 100

while count>=2:
    if(count%2!=0):
     print(count)
    count -=1