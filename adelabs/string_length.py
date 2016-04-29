def string_length(anything):
 
  if type(anything) == str:
    return [len(anything)]
  else:
    length = []
  
    for i in anything:
     length.append(len(i))
    return length
     
print string_length(['Fairy', 'Tale'])
print string_length('C-Sharp')