from pickle import FALSE, TRUE

def vir_size(list):
    s=0
    for a in list:
        if a!=-1:
            s+=1
    return s

def size_term(term):
    s=0
    for a in term:
        if a=="'" :
            continue
        else:
            s+=1
    return s

def term_list(term,size):
    l=[]
    flag=False
    val=-1
    for i in range(size):
        l.append(1)
    for a in term:
        if a=="'":
            l[val]=0
        else:
            val+=1
    return l

def list_term(list):
    s=""
    idx=97
    for a in list:
        if a==-1:
            idx+=1
        elif a==1:
            s+=chr(idx)
            idx+=1
        else:
            s+=chr(idx)+"'"
            idx+=1
    return s


def equal(list1,list2):
    for i in range(len(list)):
        if(list1[i]!=list2[i]):
            return False
    return True


def check_list_terms(True_list,DC_list,list):
    for a in list:
        if a in True_list :
            continue
        else: 
            if a in DC_list:
                continue
            else:
                return False
            # return False
    return True

def create_list(list):
    l=[]
    l.append(list)
    size=len(list)
    for i in range(size):
        new=[]
        for a in l:
            if a[i]==-1:
                temp=a.copy()
                temp[i]=1
                new.append(temp)
                temp=a.copy()
                temp[i]=0
                new.append(temp)
            else:
                new.append(a)
        l=new
    return l

# print(create_list([-1,0,0,-1]))
    
# print(term_list("ab'cde'",5))
# print(list_term([0,0,1,1,0,1]))
# print(size_term("abc'd'e'fg'"))
            


def finali(T_list,DC_list,list,size):
    queue=[]
    i=0
    while i<size:
        queue.append([list.copy(),i])
        i+=1
    min_term=list
    min_size=vir_size(list)
    # print(("hello ",queue))
    while len(queue)!=0:
        (a,b)=queue.pop(0).copy()
        # print("*************************")
        # print((a,b))
        # print("##########################")
        a[b]=-1
        arr=create_list(a)
        # if(b==3):print(arr)
        if check_list_terms(T_list,DC_list,arr):
            # print("True")
            i_curr=b+1
            
            if(min_size>vir_size(a)):
                min_size=vir_size(a)
                min_term=a
            while i_curr<size:
                queue.append([a.copy(),i_curr])
                # print([a,i_curr])
                i_curr+=1
    return min_term


def comb_function_expansion(func_TRUE, func_DC):
    output=[]
    T_list=[]
    DC_list=[]
    if len(func_TRUE)==0:
        return 
    for a in func_TRUE:
        T_list.append(term_list(a,size_term(a)))
    for b in func_DC:
        DC_list.append(term_list(b,size_term(b))) 


    for a in T_list:
        output.append(list_term(finali(T_list,DC_list,a,len(a))))

    return output

# def find_leastterm(func_TRUE,func_DC,term,size_term):
#     T_list=[]
#     DC_list=[]
#     for a in func_TRUE:
#         T_list.append(term_list(a,size_term))
#     for b in func_DC:
#         DC_list.append(term_list(b,size_term)) 
#     # print(T_list)
#     # print(DC_list)
#     y=finali(T_list,DC_list,term,size_term)
#     return y


# func_TRUE = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
# func_DC = ["abc'd"]
func_TRUE = ["a'bc","ab'c'","ab'c"]
func_DC = ["a'b'c'","a'b'c","a'bc'","abc"]


print(comb_function_expansion(func_TRUE,func_DC))
# a=func_TRUE[0]
# print(term_list(a,size_term(a)))
# print(find_leastterm(func_TRUE,func_DC,term_list(a,size_term(a)),size_term(a)))




# print(check_list_terms([[1,1,1],[0,1,1]],[[1,0,1]],[[1,0,1],[1,1,1]]))

