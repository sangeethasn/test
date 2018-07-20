def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

a=raw_input('Enter the phrase')
a=' '.join(unique_list(a.split()))
print(a)
