import random


class Matrix:
    # create the check to see if the matrix has the same amount of items per row
    def __init__(self, argInput):
        self.input = argInput

    def getListOfLists (self):
        """makes the object printable"""
        return (self.input)

    def transpose (self):
        """inverts the matrix"""
        transposed_input = list(map(list, zip(*self.input)))
        return transposed_input

    def shapeCheck(self):
        """Checks if all rows in a matrix have the same amount of items"""
        row_nr = 0
        base_row_length = len(self.input[0])
        for item in self.input:
            rows_col = len(self.input[row_nr])
            if base_row_length != rows_col:
                print(f'Error in {self.input} {item}')
                return False
            row_nr += 1
        return True

    def __mul__(self, other): # determine the rules to multiply the matrix
        """"""
        pass
