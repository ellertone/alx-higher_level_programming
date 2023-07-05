import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp_1 = Employee('Ellertone', "Ongoki", 1000)

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, "Ellertone.Ongoki@email.com")
        
        self.emp_1.last = 'Manase'
        self.assertEqual(self.emp_1.email, "Ellertone.Manase@email.com")

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, "Ellertone Ongoki")
        
        self.emp_1.last = 'Manase'

        self.assertEqual(self.emp_1.fullname, "Ellertone Manase")

    def test_apply_raise(self):
        
        self.emp_1.apply_raise()

        self.assertEqual(self.emp_1.pay, 1050.0)


if __name__ == '__main__':
    unittest.main()
        
