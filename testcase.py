import unittest
def showMsg(msg):
	return "%s"%(msg)
def do_divide(a,b):
	return (a/b)
def ShowTrue(flag):
	return(flag)
class TestSomeFunc(unittest.TestCase):
	def testrun(self):
		self.assertEqual('OK',showMsg('OK'))
		self.assertNotEqual('OK',showMsg('NO'))
		self.assertTrue(do_divide(1,2))
		self.assertIs(int(do_divide(1,2)),1)

if __name__=='__main__':
	unittest.main()
