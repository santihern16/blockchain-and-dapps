#segundo archivo 0108 agosto

t = ()

t += (1,)

t = ()
t = (*t, 11, 12)
print(t)

lst = list(t)
lst.append(13)
t = tuple(lst)

print(lst)
print(t)
