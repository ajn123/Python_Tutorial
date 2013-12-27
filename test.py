import sys
import unittest

def foo():
    print 'hello world!'

class Case(unittest.TestCase):
    def test_foo(self):
        foo()
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        self.assertEquals(output,'hello world!')

