aset={'Apple', 'Banana', 'Cherys', 'Mango'}
print(aset)

# adding an element to the set
aset.add('Orange')
print(aset)

# adding multiple elements to the set
aset.update(['Grapes', 'Pineapple'])    
print(aset)

# removing an element from the set
aset.remove('Banana')   
print(aset)

# removing an element using discard (no error if not found)
aset.discard('Kiwi')
print(aset)

# popping an arbitrary element from the set
popped_element = aset.pop()
print(aset)

# displaying the popped element
print(f'Popped element: {popped_element}')

# clearing the set
aset.clear()

# displaying the cleared set
print(aset)

# creating a set with initial elements
aset = {'Apple', 'Banana', 'Cherys', 'Mango'}   
print(aset)

# creating a frozenset (immutable set)
fset = frozenset(['Apple', 'Banana', 'Cherys', 'Mango'])
print(fset) 

# trying to add an element to the frozenset (will raise an error)
#fset.add('Orange')  # Uncommenting this line will raise an AttributeError 
print(fset)

# trying to remove an element from the frozenset (will raise an error)
#print(fset.remove('Banana'))  # Uncommenting this line will raise an AttributeError

print(fset) 

print(type(fset))

# displaying the length of the frozenset
print(len(fset))

# checking membership in the frozenset
print('Mango' in fset)

print('Kiwi' in fset)   

# iterating through the frozenset
for item in fset:
    print(item) 
print(fset)
# creating a set with initial elements
aset = {'Apple', 'Banana', 'Cherys', 'Mango'}
print(aset)
# creating a frozenset (immutable set)
fset = frozenset(['Apple', 'Banana', 'Cherys', 'Mango'])
print(fset)
# displaying the type of the frozenset
print(type(fset))       
print(fset)
print(type(aset))
print(aset)
# displaying the length of the frozenset
print(len(fset))
print(len(aset))
# checking membership in the frozenset
print('Mango' in fset)
print('Mango' in aset)
print('Kiwi' in fset)   
print('Kiwi' in aset)
# iterating through the frozenset
for item in fset:
    print(item) 
print(fset)
for item in aset:
    print(item)     
print(aset)

# demonstrating set operations
set1 = {1, 2, 3, 4, 5}  
set2 = {4, 5, 6, 7, 8}
print(f'Set 1: {set1}')
print(f'Set 2: {set2}')
# union
union_set = set1.union(set2)
print(f'Union: {union_set}')
# intersection
intersection_set = set1.intersection(set2)      
print(f'Intersection: {intersection_set}')
# difference
difference_set = set1.difference(set2)
print(f'Difference (Set1 - Set2): {difference_set}')
# symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(f'Symmetric Difference: {symmetric_difference_set}')

# demonstrating frozenset operations
fset1 = frozenset([1, 2, 3, 4, 5])  
fset2 = frozenset([4, 5, 6, 7, 8])
print(f'Frozenset 1: {fset1}')      

print(f'Frozenset 2: {fset2}')
# union     
union_fset = fset1.union(fset2)
print(f'Union: {union_fset}')
# intersection
intersection_fset = fset1.intersection(fset2)
print(f'Intersection: {intersection_fset}')
# difference
difference_fset = fset1.difference(fset2)

print(f'Difference (Frozenset1 - Frozenset2): {difference_fset}')
# symmetric difference
symmetric_difference_fset = fset1.symmetric_difference(fset2)

print(f'Symmetric Difference: {symmetric_difference_fset}')

# demonstrating subset and superset
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
print(f'Set A: {setA}')     
print(f'Set B: {setB}')
# checking subset   
is_subset = setA.issubset(setB)
print(f'Is Set A a subset of Set B? {is_subset}')   
# checking superset
is_superset = setB.issuperset(setA)
print(f'Is Set B a superset of Set A? {is_superset}')   
# demonstrating disjoint sets
setX = {1, 2, 3}
setY = {4, 5, 6}
print(f'Set X: {setX}')
print(f'Set Y: {setY}')
# checking disjoint
are_disjoint = setX.isdisjoint(setY)
print(f'Are Set X and Set Y disjoint? {are_disjoint}')  
# demonstrating set comprehension
squared_set = {x**2 for x in range(1, 6)}
print(f'Squared Set: {squared_set}')

# demonstrating frozenset comprehension
squared_fset = frozenset(x**2 for x in range(1, 6))
print(f'Squared Frozenset: {squared_fset}')
