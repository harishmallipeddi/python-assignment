l = [
      {"a":["hockey","volley ball","foot ball"],
       "b": ("pushpa","dragon","Varanasi","aarya")},
      True,
      "67890",
      "5678.897",
      [78,False]
    ]
print(l[3][3:6])
l[4][0]=79
print(l[4][0])
print(l[0]['b'][0:2:1])
print(l[0]['b'][2][4:])
l[4][0]=78
print(l[4])
print(l[0]['a'][1][4:10:2])
print(l[0]['a'][0][3:])
print(l[0]['b'][0][::-1])
print(l[0]['a'][2][0:4])
print(l[1])