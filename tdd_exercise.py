def longestCommonSubstring(s1: str, s2: str) -> str:
	D = [[] for i in range(len(s1))]

	common = ""
	for i in range(len(D)):
		if i < len(s1) and i < len(s2) and s1[i] == s2[i]:
			common += s1[i]
		else:
			return common
	return common


import unittest

param_list = [('aa', 'aa', 'aa'), ('aa', 'aa3', 'aa'), ('3aa', '0aa', 'aa')]
class TestStringMethods(unittest.TestCase):

	def test_start(self):
		for p1, p2, res in param_list:
			with self.subTest(msg="Checking if lcs( p1, p2 ) = res", p1=p1, p2=p2, res=res):
				self.assertEqual(longestCommonSubstring(p1, p2), res)

if __name__ == "__main__":
	unittest.main()
