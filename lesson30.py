# https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python
# test.assert_equals(block1.get_width(),2)
# test.assert_equals(block1.get_length(),2)
# test.assert_equals(block1.get_height(),2)
# test.assert_equals(block1.get_volume(),8)
# test.assert_equals(block1.get_surface_area(),24)

from typing import List

class Block:
    def __init__(self, dims: List[float]):
        self.width = dims[0]
        self.length = dims[1]
        self.height = dims[2]
        
    def get_width(self) -> float:
        return self.width

    def get_length(self) -> float:
        return self.length

    def get_height(self) -> float:
        return self.height

    def get_volume(self) -> float:
        return self.width * self.length * self.height

    def get_surface_area(self) -> float:
        return 2 * self.length * self.width + 2 * self.length * self.height + 2 * self.height * self.width
    
dims = [2,3,4]
block1 = Block(dims)
assert block1.get_width() == 2
assert block1.get_length() == 3
assert block1.get_height() == 4
assert block1.get_surface_area() == 2*2*3 + 2*2*4 + 2*3*4
assert block1.get_volume() == 2*3*4

