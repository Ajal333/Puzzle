import random

list1 = []
list2 = []
list3=[]
list4=[]
for i in range(12,98):
    for j in range(1,9):
        if len(str(i*j))>2:
            list1.append('{0}*{1}'.format(i,j))
            list2.append('{}'.format(i*j))

for i in range(0,len(list1)-1) :
    for j in range((i+1),len(list1)):
        if list2[i] == list2[j]:
            if str(list2[i])[0] !='0' and str(list2[i])[1] != '0' and str(list2[i])[2] != '0' :
                if str(list2[i])[0] != str(list2[i])[1] and str(list2[i])[0] != str(list2[i])[2] and str(list2[i])[2] != str(list2[i])[1]:
                    list3.append('{0}={1}={2}'.format(list1[i],list2[i],list1[j]))
                    
for i in range(0,len(list3)) :
    f=0
    for j in range(0,13) :
        for k in range(0,13):
            if list3[i][k] != '=' and list3[i][k] != '*':
                if list3[i][j] == list3[i][k] and j!=k:
                    f=f+1
                else :
                    continue
            else :
                continue
    if f == 0 :
        list4.append(list3[i])

print(list4)

