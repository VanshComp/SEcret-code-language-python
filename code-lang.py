import random
i="c"
#coding
while i=="c":
    choice=input("Enter \"code\" to form code language or \"decode\" to decode your coded language: ")
    if(choice=="code"):
        print("Instructions: if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end\nelse:   simply reverse the string")
        t= list(input("Enter your text: "))
        if len(t) == 3:
            t[0],t[2]=t[2],t[0]
            t1="".join(t)
            t2="".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",k=3))
            t3="".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",k=3))
            print( ("%s%s%s") % (t2,t1,t3))
        else:
            t.reverse()
            t1="".join(t)
            print(t1)
#decoding
    elif(choice=="decode"):
        print("Instruction: if the word contains less than 3 characters, reverse it\nelse: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning")
        r= list(input("Enter your text: "))
        if len(r) < 3:
            r.reverse()
            r1="".join(r)
            print(r1)
   
        else:
            r1=r[3:-3]
            r1[0],r1[2]=r1[2],r1[0]
            r2="".join(r1)
            print(r2)
    else:
        print("You selected wrong path....Please choose again")
    i=input("Press c to continue else q to quit: ")
print("Successfully exited from program")