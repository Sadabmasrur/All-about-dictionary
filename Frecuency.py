test_dict={
    'Codingal':1,
    'is':2,
    'best':2,
    'for':2,
    'Coding':1
}

print("The original dictionarey: ", test_dict)

k=2
res=0

for key in test_dict:
    
    if test_dict[key]==k:
        res=res+1
        
print("Frequency of k is : ",res)        