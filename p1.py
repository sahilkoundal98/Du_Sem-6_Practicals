import pandas as pd
import matplotlib.pyplot as plt
f = pd.read_csv("people.txt") 
import numpy as np 
f.index
len(f)
temp = pd.read_csv("people.txt") 
temp.dropna(inplace = True) 
temp
def check_age_range(f) : 
    print("Age Check")
    age_range = lambda r : r in range(151) 
    print(f["Age"].apply(age_range))

check_age_range(f)

def check_age_rangeN(f) :
    print("Age Check")
    age_range = lambda r : r in range(151)
    a=np.array(f["Age"].apply(age_range))
    print("Number Of valid Values:",sum(a))
    print("Number Of invalid Values:",len(a)-sum(a))
    a=sum(a)
    return a
#####################
def check_age(f) :
    print("Years Married")
    age_check = lambda r : r[0] > r[1] 
    print(f[["Age","yearsMarried"]].apply(age_check,axis=1))

check_age(f)

f.Status
def check_ageN(f) :
    print("Years Married")
    age_check = lambda r : r[0] > r[1]
    a = np.array(f[["Age","yearsMarried"]].apply(age_check,axis=1))
    print("Number Of valid Values:",sum(a))
    print("Number Of invalid Values:",len(a)-sum(a))
    a=sum(a)
    return a
##################

def check_status(f) :
    print("Status(Married)")
    status=set(f.Status)

    status_check = lambda r : r in status
    print(f["Status"].apply(status_check))

check_status(f)

def check_statusN(f) :
    print("Status(Married)")
    status=set(f.Status)
    status_check = lambda r : r in status
    a=np.array(f["Status"].apply(status_check))
    print("Number Of valid Values:",sum(a))
    print("Number Of invalid Values:",len(a)-sum(a))
    a=sum(a)
    return a
##########
def check_group(f) :
    print("Group Check")
    def group_check(x) :
        if (x[0] in range(18) and x[1]=="child") or (x[0] in range(18,66) and x[1]=="adult") or (x[0]>65 and x[1]=="elderly") :
            return True
        else :
            return False
    print(f[["Age","AgeGroup"]].apply(group_check,axis=1))
check_group(f)
f.describe()


def check_groupN(f) :
    def group_check(x) :
        if (x[0] in range(18) and x[1]=="child") or (x[0] in range(18,66) and x[1]=="adult") or (x[0]>65 and x[1]=="elderly") :
            return True
        else :
            return False
    a=np.array(f[["Age","AgeGroup"]].apply(group_check,axis=1))

    print("Age Group(Class")
    print("Number Of valid Values:",sum(a))
    print("Number Of invalid Values:",len(a)-sum(a))
    a=sum(a)
    return a

###################

E = {"check_age_range" : check_age_rangeN, "check_age" : check_ageN, "check_status": check_statusN, "check_group" : check_groupN}

print("xxxxxxxxxxxxx---Summary--xxxxxxxxxxxxx")
x=[]
for i in E.keys() :
    print("-----")
    x.append(E[i](f))

plt.bar(E.keys(),x)
plt.show()