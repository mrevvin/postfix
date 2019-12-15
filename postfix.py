def drje(n):
    if n=="^":
        n=4
    elif n=="*" or n=="/":
        n=3
    elif n=="-" or n=="+":
        n=2
    return(n)
inf=input("plz enter infix : ")
amlgr=[]
pos=[]
post=""
for item in inf:
    if item != "+" and item !="^" and item !="*" and item !="-" and item !="(" and item !=")" and item !="/":
        post=post+item
    elif amlgr==[]:
        amlgr.append(item)
    elif item=="(":
        amlgr.append(item)
    elif item==")":
        while item!="(":
            post=post+amlgr.pop()
            item=amlgr[len(amlgr)-1]
            if(item=="("):
                amlgr.pop()
                break
    elif item!="(" and amlgr[len(amlgr)-1]!="(":
        while(amlgr!=[] and drje(amlgr[len(amlgr)-1])>=drje(item)):
            if item!="(" and amlgr[len(amlgr)-1]!="(":
                post=post+amlgr.pop()
            else:
                break
            break
        amlgr.append(item) 
    else: 
        amlgr.append(item)
while amlgr!=[]:
    post=post+amlgr.pop()
print(post) 
while(True):  
    ans=input("do yo want to test:y/n   ")
    if ans=="n" or ans=="N":
        exit()
    elif ans=="y" or ans=="Y":
        for item in post:
            if item != "+" and item !="^" and item !="*" and item !="-" and item !="(" and item !=")" and item !="/":
                pos.append(int(input(item+": ")))   
            else:
                if item=="^":
                    pos[len(pos)-2]=pos[len(pos)-2]^pos[len(pos)-1]
                    pos.pop()
                elif item=="+":
                    pos[len(pos)-2]=pos[len(pos)-2]+pos[len(pos)-1]
                    pos.pop()
                elif item=="-":
                    pos[len(pos)-2]=pos[len(pos)-2]-pos[len(pos)-1]
                    pos.pop()
                elif item=="*":
                    pos[len(pos)-2]=pos[len(pos)-2]*pos[len(pos)-1]
                    pos.pop()
                elif item=="/":
                    (pos[len(pos)-2])=(pos[len(pos)-2])/(pos[len(pos)-1])
                    pos.pop()
        print(pos[0])
        exit()
    else:
        print("plz try again...")