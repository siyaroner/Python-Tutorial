days=["MONDAY","    TUESDAY","   WEDNESDAY","   THURSDAY","    FRIDAY","    SATURDAY","   SUNDAY"]
hours=["08:00","09:00","10:00","11:00","12:00",]
i=0
while i<len(days)  :
    print(days[i],end=" ")
    
    if i==len(days)-1: 
        j=0
        print("\n")
        while j<len(hours):
                z=0
                while z<len(days):
                    print(hours[j],end=" ")
                    y=0
                    l=0
                    while y<len(days[l]):
                        print(end=" ")
                        y+=1
                    l+=1 
                    z+=1
                print("\n")
                j+=1
    else:
        pass
    i+=1
print()
