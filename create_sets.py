set1={1,2,3,4,5}
set2={4,5,6,7,8}
#access set elements (iterate through set)
print("set 1 element")
for elem in set1:
    print(elem,end="")
    print("\nSet 2 elememnts:")
    for elem in set 2:
print(elem,end="")
print()

#union of sets

union_set=set1.union(set2)
print("union of Set1 and Set2:",union_set)

#intersection of sets 
intersection_set=set1.intersectiom(set2)
print("intersection of Set1 and Set2:",
      intersection_set)

#difference of sets(Set1-Set2)
difference_set=set1.difference(set2)
print("difference(Set1-Set2):",difference_set)

#difference of sets(Set2-Set1)
difference_set2=set2.difference(set1)
print("difference(Set2-Set1):",difference_set2)



