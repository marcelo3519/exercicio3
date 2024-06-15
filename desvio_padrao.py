from statistics import stdev

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900,7000]

def dp (e1,e2,e3,e4):

    e1=empresa1
    e2=empresa2
    e3=empresa3
    e4=empresa4
    dp=stdev(e1, e2, e3, e4)
    
    print(dp)