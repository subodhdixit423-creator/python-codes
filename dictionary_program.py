#create and access dictionay elements 
student={
    "roll_no":101,
    "name":"Amit"
    "marks":85
}

print("dictionary:",student)
print("name:",student["name"])
print("marks:",student.get("marks"))
print()

#update dictionary
print("2.update dictionary")
student["marks"]=90
student["grade"]="A"
print("updated dictionary:",student)
print()

#removing elements
print("3.removing elements")
removed_value=student.pop("grade")
print("removed value:",removed_value)
print("after removing 'grade':",student)

student.popitem()
print("After.popitem():",student)
print()

#merging dictionaries
print("4.merging dictionaries")
dict1={ "a":1,"b":2}
dict2={"c":3,"d":4}

merged_dict=dict1|dict2
print("first ditionary:",dict1)
print("second dictionary:",dict2)
print("merged dictionary:"merger_dict)
