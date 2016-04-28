from A.classes import Animal, Poacher,Tourist
from A.functions import word_count, sum_of_digits
#Another way
import A.functions as funct
import A.classes as classes

print Animal, word_count
print classes.Animal, funct.word_count

# {
# 	#Example of a namespace, which is this case it has a dictionary
# 	# 'Animal': <class>,
# 	# 'Poacher': <class>,
# 	# 'Tourist': <class>,
# 	# 'word_count': <func>,
# 	# 'sum_of_digits': <func>,
# 	# 'func': {
# 	# 	'word_count': <func>,
# 	# 	'poacher':	<>

# 	}

# }