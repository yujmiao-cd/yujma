# python  sort 
def sort(alias):
    for j in range(len(alias)-1,0,-1):
       count = 0
       for i in range(0, j):
           if alias[i] > alias[i+1]:
               alias[i],alias[i+1]=alias[i+1],alias[i]
               count+=1
               print(alias)
       if count == 0:
          return

alias = [1, 2, 6, 9, 7, 3]
print(alias)
print("sort-------")
sort(alias)
