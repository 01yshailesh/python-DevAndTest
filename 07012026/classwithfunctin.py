set1 = {1, 2, 3, 4, 5}  
set2 = {4, 5, 6, 7, 8, 9, 10, 11, 12}
aset={'Apple', 'Banana', 'Cherys', 'Mango'}
fset = frozenset(['Apple', 'Banana', 'Cherys', 'Mango'])
class setclass:
    def func(self):
        return "Hello, Welcome to set operations"
    
    def print_sets(self):
        print("Set 1:", set1)
        print("Set 2:", set2)
        print("A Set:", aset)
    # adding an element to the set
    def add_element(self, element):
        el = input("Enter element to add to set: ")
        aset.add(el)
        print(aset)
#=========================================================
# adding multiple elements to the set
    def add_many_elements(self, elements):
        aset.update(['Grapes', 'Pineapple'])    
        print(aset)

# removing an element from the set
    def remove_element(self, element):
        aset.remove('Banana')   
        print(aset)

# removing an element using discard (no error if not found)
    def discard_element(self, element):
        aset.discard('Kiwi')
        print(aset)

# popping an arbitrary element from the set
    def pop_element(self):
        popped_element = aset.pop()
        print(aset)

    # displaying the popped element
    def display_popped_element(self):
        popped_element = aset.pop()
        print(f'Popped element: {popped_element}')

    # clearing the set
    def clear_set(self):
        aset.clear()

    # displaying the cleared set
    def display_cleared_set(self):
        print(aset)

    # creating a frozenset (immutable set)
    def create_frozenset(self):
        print(fset) 

    # trying to add an element to the frozenset (will raise an error)
    #fset.add('Orange')  # Uncommenting this line will raise an AttributeError 
    #print(fset)

    # trying to remove an element from the frozenset (will raise an error)
    #print(fset.remove('Banana'))  # Uncommenting this line will raise an AttributeError

    #print(fset) 
    def display_frozenset_type(self):
        print(type(fset))

    # displaying the length of the frozenset
    def display_frozenset_length(self):
        print(len(fset))

    # checking membership in the frozenset
    def check_membership_in_frozenset(self):
        el = input("Enter element to check in frozenset: ")
        print('{el}' in fset)  

    # iterating through the frozenset
    def iterate_frozenset(self):
        for item in fset:
            print(item) 
        print(fset)

    # creating a frozenset (immutable set)
    def create_and_display_frozenset_and_set(self):    
        print(fset)

    # displaying the type of the frozenset
    def display_types_and_lengths(self):          
        print(fset)
        # displaying the type of the set
        print(type(aset))
        print(len(aset))
        print(aset)
        # displaying the length of the frozenset
        print(type(fset))
        print(len(fset))
        
    # iterating through the frozenset
    def iterate_frozenset_and_set(self):
        for item in fset:
            print(item) 
        print(fset)
        for item in aset:
            print(item)     
        print(aset)
#=========================================================
# demonstrating set operations
class math_operations:
    print(f'Set 1: {set1}')
    print(f'Set 2: {set2}')
  # union
    def union_set(self):
        us = set1.union(set2)
        print(f'Union: {us}')
# intersection
    def intersection_set(self):
        intersection_set = set1.intersection(set2)      
        print(f'Intersection: {intersection_set}')
# difference
    def difference_set(self):
        difference_set = set1.difference(set2)
        print(f'Difference (Set1 - Set2): {difference_set}')
# symmetric difference
    def symmetric_difference_set(self):
        symmetric_difference_set = set1.symmetric_difference(set2)
        print(f'Symmetric Difference: {symmetric_difference_set}')
# demonstrating subset and superset
# checking subset   
    def subset(self):
        is_subset = set1.issubset(set2)
        print(f'Is Set A a subset of Set B? {is_subset}')   
# checking superset
    def superset(self):
        is_superset = set2.issuperset(set1)
        print(f'Is Set B a superset of Set A? {is_superset}') 
# checking disjoint
    def disjoint_det(self):
        are_disjoint = set1.isdisjoint(set2)
        print(f'Are Set X and Set Y disjoint? {are_disjoint}')  
# demonstrating set comprehension
    def squared_set(self):
        squared_set = {x**2 for x in range(1, 6)}
        print(f'Squared Set: {squared_set}')
# demonstrating frozenset comprehension
    def squared_fset(self):
        squared_fset = frozenset(x**2 for x in range(1, 6))
        print(f'Squared Frozenset: {squared_fset}')


obj = setclass()
obj2 = math_operations()
print(obj.func())
print(f"1: Prints Sets" )
print(f"2: Add Element to Set" )
print(f"3: Add Many Elements to Set" )
print(f"4: Remove Element from Set" )
print(f"5: Discard Element from Set" )
print(f"6: Pop Element from Set" )
print(f"7: Display Popped Element from Set" )
print(f"8: Clear Set" )
print(f"9: Display Cleared Set" )
print(f"10: Create Frozenset" )
print(f"11: Display Frozenset Type")
print(f"12: Display Frozenset Length")
print(f"13: Check Membership in Frozenset")
print(f"14: Iterate through Frozenset")
print(f"15: Create and Display Frozenset and Set")
print(f"16: Display Types and Lengths of Frozenset and Set")
print(f"17: union of Sets")
print(f"18: intersection of Sets")
print(f"19: difference of Sets")
print(f"20: symmetric difference of Sets")
print(f"21: Check Subset")
print(f"22: Check Superset")
print(f"23: disjoint_det")
print(f"24: squared_set")
print(f"25: squared_fset")



op = input(f"Select Any One option to perform set operations: ")
if op == '1':
    print(f"{obj.print_sets()}")
elif op == '2':
    print(f"{obj.add_element('Orange')}")   
elif op == '3':
    el = input("Enter elements to add (comma separated): ")
    print(f"{obj.add_many_elements(el.split(','))}")  
elif op == '4':
    print(f"{obj.remove_element('Banana')}")
elif op == '5':
    print(f"{obj.discard_element('Kiwi')}")
elif op == '6':
    print(f"{obj.pop_element()}")
elif op == '7':
    print(f"{obj.display_popped_element()}")
elif op == '8':
    print(f"{obj.clear_set()}")
elif op == '9':
    print(f"{obj.display_cleared_set()}")
elif op == '10':
    print(f"{obj.create_frozenset()}")
elif op == '11':
    print(f"{obj.display_frozenset_type()}")
elif op == '12':
    print(f"{obj.display_frozenset_length()}")
elif op == '13':
    print(f"{obj.check_membership_in_frozenset()}")
elif op == '14':
    print(f"{obj.iterate_frozenset()}")
elif op == '15':
    print(f"{obj.create_and_display_frozenset_and_set()}")
elif op == '16':
    print(f"{obj.display_types_and_lengths()}")
elif op == '17':
    print(f"{obj2.union_set()}")
elif op == '18':
    print(f"{obj2.intersection_set()}")
elif op == '19':
    print(f"{obj2.difference_set()}")
elif op == '20':
    print(f"{obj2.symmetric_difference_set()}")
elif op == '21':
    print(f"{obj2.subset()}")
elif op == '22':
    print(f"{obj2.superset()}")
elif op == '23':
    print(f"{obj2.disjoint_det()}")
elif op == '24':
    print(f"{obj2.squared_set()}")
elif op == '25':
    print(f"{obj2.squared_fset()}")
else:
    print("Invalid Option Selected")

