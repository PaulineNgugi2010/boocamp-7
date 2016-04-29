def find_max_min(anum):
	max_num , min_num = anum[0], anum[1]
	for i in anum:
		if min_num < i:
			min_num = i
		if min_num > i:
			max_num = i
	if max_num == min_num:
		return [len(anum)]
	return [max_num, min_num]

print find_max_min([1, 3, 4, 5])