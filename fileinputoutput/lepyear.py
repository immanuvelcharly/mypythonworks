f=open("C:\Users\IMMANUEL\Desktop\python\fileinputoutput\data.txt","w")
year=[2000,2024,1991,1995,1200,1400,1234]
#centery year divicible by 100 and 400

#non centery %100 !=0 and dividable by 4
# year="value"
# if(year %100==0 and year %400==0):




for y in year:
    if(y %100==0 and y%400==0):
        f.write(str(y)+"\n")
    elif(y %100 !=0 and y %4==0):
        f.write(str(y)+"\n")






for y in year:
    if(y %100==0 and y%400==0):
        print(y)
    elif(y %100 !=0 and y %4==0):
        print(y)
