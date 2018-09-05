import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

        input = """int main () {
            putIntLn(4);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

        input = """int main (int a,b,c;float y,x,d) {
            putIntLn(4);
            a = b + c;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))


    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.test(input,expect,203))

        """incorrect variable declaration 3"""
        input = """float a,c,d"""
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.test(input,expect,303))