""" a function for generating odd numbered sequences """

odd_generator = lambda lower_bound, upper_bound: (x for x in range(lower_bound, upper_bound) if x % 2)  # we're gonna want an odd num generator for testing
