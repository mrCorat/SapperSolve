import random
from secrets import choice
import unittest
from wsgiref.validate import validator
from include.Minefield import *
from numpy import choose
cells_value = (0,0)
cells_answer_neigbour = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1), (1,0), (1,1)]
class Test_moore_dist_func(unittest.TestCase):
    def test_neigbours_positive(self):
        self.assertEqual(moore_dist(cells_value), cells_answer_neigbour)
    def test_non_correct_type(self):
        self.assertEqual(moore_dist((1.1, 'carra')), [])
    def test_int_in_float_variables(self):
        self.assertEqual(moore_dist((0.0, 0.0)), [])
    def test_more_elements(self):
        self.assertEqual(moore_dist((0, 0, 0)), [])
    def test_less_elements(self):
        self.assertEqual(moore_dist(0), [])

variable_sets = {'x', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8'}
class Test_validation_class(unittest.TestCase):
    def setUp(self):
        self.valide = Validator(variable_sets)
    def test_random_generate_int(self):
        self.assertTrue(self.valide.is_correct_symbols(chr(ord('0') + random.randint(0,8))))
    def test_additional_values(self):
        self.assertTrue(self.valide.is_correct_symbols('x') and self.valide.is_correct_symbols('?'))
    def test_9(self):
        self.assertFalse(self.valide.is_correct_symbols('9'))
    def test_string_non_symbol_test(self):
        self.assertFalse(self.valide.is_correct_symbols('Hi'))
    def test_string_with_element_number(self):
        self.assertFalse(self.valide.is_correct_symbols('0x'))
    def test_ASCII_test(self):
        self.assertFalse(self.valide.is_correct_symbols(ord('0')))

def generate_with_divider_string(pattern, divider_range, divider = " "):
    answer = ""
    for i in range(len(pattern)):
        answer += divider*random.choice(divider_range) + pattern[i]
    answer += divider*random.choice(divider_range) + '/n'
    return answer
#This function does not get correct for Sapper rules elements, but can
#generate field, that should get in correct value or get exceptions, that can be predictable
def Generator(pattern = ['?', '0'], default_len = random.randint(0,10), default_unique_height = [random.randint(0,10) for i in range(10)], size_pattern = range(10)):
    example = ""
    answer = []
    for i in range(len(default_unique_height)):
        pattern_last_string = "".join([random.choice(pattern) for i in range(default_len)])
        for j in range(default_unique_height[i]):
            answer.append(pattern_last_string)
            example += generate_with_divider_string(pattern_last_string, size_pattern)
    return example, answer


class Test_Minefield_Test(unittest.TestCase):
#Steps of testing
#1. Generating with correction
#2. Getting input values
#3. Get value from field
#4. Changing element and test corrects
    def test_positive_minefield_correct_field(self):
        example, answer = Generator(default_len=10, default_unique_height=[1 for i in range(10)], size_pattern=[1])
        correct_minefield = Minefield(example, 0)
        self.assertEquals(correct_minefield.get_table(), answer)
if __name__ == "__main__":
  unittest.main()