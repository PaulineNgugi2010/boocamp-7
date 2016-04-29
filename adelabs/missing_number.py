
def find_missing(list1, list2):
  sum_list1 = 0
  sum_list2 = 0
  for i in list1:
    sum_list1 += i
    
  for j in list2:
    sum_list2 += j
    
  if sum_list1 > sum_list2:
    return sum_list1 - sum_list2
  else:
    return sum_list2 - sum_list1