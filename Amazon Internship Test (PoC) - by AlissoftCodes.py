"""
Description:
	This is a "Proof of Concept" script I created
	as a solution to one of the Amazon internship tests.

Source:
	https://github.com/AlissoftCodes

"""

def getMinModEfficiency(d: list, s: list, n: int) -> dict:

	"""
	Description:
		A function that calculates developing project-assignments
		based on the Minimum Mod-Efficiency formula.
	Args:
		d (list): list of integers describing the complexity of a task
		s (list): list of integers describing the skill level of a developer
		n (int): integer number of developers to whom such tasks will be assigned to

	Returns:
		dict: dictionary containing an array (python list) to the optimal assigment
		in the format {item_id:[difficulty, skill, result]} of the mod-efficiency calculation.
	"""

	# The constraints are that 1 <= n <=n 2*10**5
	if 1 <= n <= 2*10**5:
		# For this demo we're creating a Python Dictionary <class 'dict'>
		# in order to assign an id-like system to store the arrays (Python List) <class 'list'>
		mme = {} # mme as in Minimum Mod-Efficiency
		for i in range(n):
			# Populating the mme dict with empty lists to be able
			# to work with its contents even when the length is 0
			mme[i] = []
			for j in range(n):
				# applying the formula
				m = (d[i] + s[j]) % n

				# Verifying how many developers have already been assigned to a project,
				# because one developer cannot be in two or more projects at the same time
				assigned = len([mme[x][1] for x in mme if len(mme[x]) > 0 and mme[x][1] == s[j]])
				
				# Verifying how many developers with the
				# currently processed skill status exist
				devs = s.count(s[j])

				# Making sure of the availability of
				# developers to assign to the project
				if len(mme[i]) == 0:
					if devs >= assigned+1:
						mme[i] = [d[i], s[j], m]

				elif devs > assigned and m < mme[i][2]:
					mme[i] = [d[i], s[j], m]

		# Returning format = {item_id: [difficulty, skill, mod_result], ...} for demonstration purposes
		return mme
		# In order to output the solutions as required in the challenge, comment line 58 and uncomment line 60:
		# return [mme[i][2] for i in mme]
	else:
		# Throwing an error message when n does not satisfy the requirements
		raise ValueError('n should be between 1 and 200000.')


def run_tests():
	"""
	Description:
		This function is made to check if all
		the answers match the required criteria.
	"""
	# 1
	d1, s1, n1 = [0,1,2], [2,1,0], 3
	ex1 = getMinModEfficiency(d1, s1, n1)

	# 2
	d2, s2, n2 = [0,1,1], [0,1,0], 3
	ex2 = getMinModEfficiency(d2, s2, n2)

	# 3
	d3, s3, n3 = [0,1,2,1], [1,3,2,3], 4
	ex3 = getMinModEfficiency(d3, s3, n3)


	# the expected answers -> [(difficulty, skill, mod_result), ...]
	# 1 -> [(0, 0, 0), (1, 2, 0), (2, 1, 0)]
	# 2 -> [(0, 0, 0), (1, 0, 1), (1, 1, 2)]
	# 3 -> [(0, 1, 1), (1, 3, 0), (2, 2, 0), (1, 3, 0)]


	# All that would lead us to this:
	for x, ex in enumerate([ex1, ex2, ex3]):
		# Disclaimer: do not use the <built-in function eval> unless you apply filters,
		# because it could potentially make your code vulnerable to malicious inputs.
		# In this example I'm using it merely for making this piece of code shorter
		# and this code is for demonstration purposes only.
		print(f'\n\nFor n = {eval("n"+str(x+1))}, difficulties = {eval("d"+str(x+1))} and skills = {eval("s"+str(x+1))}, the operations leading to the optimal solution are:')
		for i in ex:
			print(f'• Assign difficulty {ex[i][0]} to skill {ex[i][1]}\n\t- Minimum Mod-Efficiency result: {ex[i][2]}')

		print(f'\nThe lexicographically minimum mod-efficiency array is {[" + ".join([str(ex[i][0]), str(ex[i][1])]) + f" % {len(ex)} = {ex[i][2]}" for i in ex]}')


	# Printing out just the expected output:
	for x, ex in enumerate([ex1, ex2, ex3]):
		print(f'\nExpected output #{x+1}:')
		for i in ex:
			print(ex[i][2])


# Mitigating the requested samples
run_tests()
