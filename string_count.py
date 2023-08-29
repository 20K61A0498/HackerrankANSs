sentence=input()
sub_str=input()
l=len(sub_str)
c=0
i=0
for i in range(len(sentence)):
    s=sentence[i:i+l]
    if s==sub_str:
        c+=1
if sub_str not in sentence:
    print("enter a valid word")
print(c)
