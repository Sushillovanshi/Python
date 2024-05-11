x={10,10,30,40,50} 
# unique contan 
print(x)

x={10,20,30,40,'sushil'}
# contan some many order different value.
print(x)

x={ 'sushil' 'sushant' 'neeraj'}
# 
print(x)

# creating a set 
s={10,20,30,40}
print(s)
print(type(s))


# creating a set with different element
s={10,'20','sushil',234.56,True}
print(s)
print(type(s))

# certing a set using range function
s=set(range(5))
print(s)

# duplicate not allowed
s={10,20,30,40,10,20}
print(s)
print(type(s))

# creting an empty set
s=set()
print(s)
print(type(s))

#  methods in  set 

s={ 10,20,30,}
s.add(40)
print(s)

# update function
s={10,20,30}
l=[40,50,60,10]
s.update(l)
print(s)

s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)

# copy set
s={10,20,30,20}
s1=s.copy()
print(type(s))

# pop

s={40,10,20,30}
print(s)
print(type(s))

# remove
s={40,10,30,20}
s.remove(30)
print(s)

# discard
s={10,20,30}
s.discard(10)
print(s)

# clear
s={10,20,30}
print(s)
s.clear()
print(s)

# mathematical

x={10,20,30,40}
y={30,40,50,60}
print(s.union(y))

# intersection

x={10,20,30,40}
y={30,40,50,60}
print(x.intersection(y))
print(s&y)
print(y.intersection)
print(y&x)

