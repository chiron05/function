def most_frequent(string1):
    mydict={}
    for num in string1:
        z= string1.count(num)
        mydict[num]=str(z)
    list1=list(mydict.items())
    tuple1=tuple(list1)
    tuple1=sorted(mydict.items(),reverse=True, key=lambda x: x[1])
    print("Output:\n")
    for x in tuple1:
        print(x[0]+" 0"+x[1])

string=str(input("Please enter a string: "))
most_frequent(string)
