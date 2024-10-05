#2

def dubl(str):
    str_set = set(str)
    if len(str) == len(str_set):
        return True
    else:
        return False


print(dubl('home'))
print(dubl('apple'))



#3

def dic(str):
    set_str = set(str)
    dict = {}
    for i in set_str:
        if i in str:
            dict [i] = str.count(i)
    return dict
                 
print(dic('hello'))


#4

def rev(str):
    return str[:: -1]

print(rev('lower'))
