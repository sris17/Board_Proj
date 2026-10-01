import random

company_shares=10
investor1=20
investor2=14
misc=0
price_per_stock=100
condition="loss"

print("Investor 1","\t","Investor 2","\t","Misc")
print(investor1,"\t"*2,investor2,"\t"*2,misc)

if condition=="loss":
    n1=random.randint(3,8)
    n2=random.randint(4,10)
    investor1-=n1
    investor2-=n2
    misc=n1+n2

elif condition=="profit":
    



print(investor1,"\t"*2,investor2,"\t"*2,misc)

