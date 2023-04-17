def union():
  a={1,2,3}
  b={2,3,4}
  print(a.union(b))
 
def intersection():
  a={1,2,3}
  b={2,3,4}
  print(a.intersection(b))
def difference():
  a={1,2,3}
  b={2,3,4}
  print(a-b)
def symmetric_difference():
  a={1,2,3,4}
  b={3,4,5,6}
  print(a.union(b)-a.intersection(b))
union()
intersection()
difference()
symmetric_difference()
        
   
