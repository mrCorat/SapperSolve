from numpy import true_divide
from pyparsing import Char


moore_pattern =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1), (1,0), (1,1)]
def moore_dist(cell):
    if isinstance(cell, tuple) and len(cell) == 2 and isinstance(cell[0], int) and isinstance(cell[1], int):
        return [(cell[0] + element[0], cell[1] + element[1]) for element in moore_pattern]
    else:
        return []

validat_element_with_modify = {'x', '1', '2', '3', '4', '5', '6', '7', '8'}
validat_element_at_start = {'0', '?', ' ', '/n'}
class Validator:
    def __init__(self, set_elements):
        self.dictionary = set(set_elements)
    def is_correct_symbols(self, char_element):
        return char_element in self.dictionary and isinstance(char_element, str)
    ##   return isinstance(other_validation, set) and len(other_validation - self.dictionary) > 0
  #  def input_new_elements(self, element):
   #     if isinstance(element, set):
    #        self.dictionary = self.dictionary + element
     #   elif isinstance(element, str) and len(element) == 1:
      #      self.dictionary.add(element)
    #def remove_elements(self, element):
     #   if isinstance(element, set):
      #      self.dictionary = self.dictionary - element
       # elif isinstance(element, str) and len(element) == 1:
        #    self.dictionary.remove(element)
        
class NotPositiveNumber(Exception):
    pass
class NotCorrectChar(Exception):
    pass
class NonRectangleString(Exception):
    pass
class IsEmptySet(Exception):
    pass
class OutOfFields(Exception):
    pass
class Minefield:
    def __init__(self, minefield, number_of_bombs):
        try:
            Dictionary = set(minefield)
            if len(Dictionary - validat_element_at_start) >0:
                raise NotCorrectChar()
            correct_filter_minefield = minefield.replace(" ","").split('\n')
            if len(correct_filter_minefield) == 0:
                raise IsEmptySet()
            flag_of_correct_rect = True
            for i in range(len(self.minefield) - 1):
                if len(correct_filter_minefield[i]) != len(correct_filter_minefield[i+1]):
                    flag_of_correct_rect = False
                    break
            if not flag_of_correct_rect:
                raise NonRectangleString()
            if len(correct_filter_minefield == ""):
                raise IsEmptySet()
            if not isinstance(number_of_bombs, int):
                raise NotPositiveNumber()
            if number_of_bombs < 0:
                raise NotPositiveNumber() 
            self.unopened_bombs = number_of_bombs
            self.Vocabulary = Validator()
        except NotCorrectChar:
            print("there is other chars, except special numbers")
        except NonRectangleString:
            print("not correct rectangle")
        except IsEmptySet:
            print("Field is Empty")
        finally:
            self.minefield = minefield.replace(" ","").split('\n')
            self.unopened_bombs = number_of_bombs
            self.Vocabulary = Validator(validat_element_with_modify)
    def get_table(self):
        return self.minefield
    def get_value(self, cell):
        return self.minefield[cell[0]][cell[1]]
    def get_entrance(self):
        result = {}
        for i in range(len(self.minefield)):
            for j in range(len(self.minefield[i])):
                if(self.minefield[i][j] != '?'):
                    result.add((i,j))
        try:
            if len(result) == 0:
                raise  NotCorrectChar()
        except NotCorrectChar:
            print("No Entrance points")
        else:
            return result
    def change_value(self,cell, new_value):
        try:
            if not self.Vocabulary.is_correct_symbols(new_value):
                raise NotCorrectChar()
        except NotCorrectChar:
            print ('changing data not correct')
        else:
            self.minefield[cell[0]] = self.minefield[cell[0]][:cell[1]] + new_value + self.minefield[cell[0]][cell[1] + 1 : ]
    def cell_in_field(self, cell):
        return -1 < cell[0] < len(self.minefield) and -1 < cell[1] < len(self.minefield[cell[0]])            
    def cell_is_free(self, cell):
        try:
            if self.cell_in_field(cell):
                raise OutOfFields()
        except OutOfFields:
            print("Out of field cells")
        else:
            return self.minefield[cell[0]][cell[1]] == '?'       
    def neighbour_cells(self, cell):
        result = []
        try:
            if self.cell_in_field(cell):
                raise OutOfFields()
        except OutOfFields:
            print("Out of field cells")
        else:
            for simple_cell in moore_dist(cell):
                if self.cell_in_field(simple_cell) and self.cell_is_free(simple_cell):
                    result.append(simple_cell)
            if result != []:
                return result