import unittest
from exceptions import *
from mow_it import *

class TestMap(unittest.TestCase):
    """
        Test the map functions 
    """
    
    def test_new_map_creation_zero_surface_fail(self):
        """
        User tries to create a new map, with 0 surface parameters 
        """
        map = Map()
        self.assertRaises(MapSurfaceException,  map.init_surface, "0 0")
        
    def test_new_map_creation_negative_surface_fail(self):
        """
            User tries to create a new map, with negative surface parameters 
        """
        map = Map()
        self.assertRaises(MapSurfaceException,  map.init_surface, "-1 0")
        
    def test_new_map_creation_bad_surface_parameters_fail(self):
        """
            User tries to create a new map, with one surface parameters 
        """
        map = Map()
        self.assertRaises(MapSurfaceException,  map.init_surface, "0")
        
    def test_new_map_creation_text_surface_parameters_fail(self):
        """
            User tries to create a new map, with letter surface parameters 
        """
        map = Map()
        self.assertRaises(MapSurfaceException,  map.init_surface, "A F")
    
    def test_new_map_creation_pass(self):
        """
            User tries to create a new map, with good parameters 
        """
        map = Map()
        map.init_surface("5 5")
        self.assertEqual(map.height, 5)
        self.assertEqual(map.width, 5)
    
    def test_map_position_out_of_surface_fail(self):
        """
            User tries to set position out of surface
        """
        map = Map()
        map.init_surface("5 5")
        position=Position(6,5)
        self.assertFalse(map.is_valid_position(position))
        
    def test_map_position_in_surface_pass(self):
        """
             User tries to set position insid surface
        """
        map = Map()
        map.init_surface("5 5")
        position=Position(1,3)
        self.assertTrue(map.is_valid_position(position))
        
class TestMower(unittest.TestCase):
    """
        Test the mower creation and functions 
    """
    
    def test_new_mower_initial_position_fail(self):
        """
        User tries to create a new mower, with initial parameters out of map
        """
        map=Map()
        map.init_surface("5 5")
        position=Position(1,3)
        direction=Directions("N")
        mower = Mower()
        mower.map=map
        self.assertRaises(MowerPositionException,mower.init_position, ("1 7 N") )
        
    def test_new_mower_initial_position_pass(self):
        """
        User tries to create a new mower, with initial parameters inside map
        """
        map=Map()
        map.init_surface("5 5")
        expected_position=Position(1,2)
        expected_direction=Directions("N")
        mower = Mower()
        mower.map=map
        mower.init_position("1 2 N")
        self.assertEqual(mower.position.x,expected_position.x)
        self.assertEqual(mower.position.y,expected_position.y)
        self.assertEqual(mower.direction,expected_direction)
    
    def test_mower_rotate(self):
        """
        User rotate mower
        """
        map=Map()
        map.init_surface("5 5")
        expected_position=Position(1,3)
        expected_direction=Directions("E")
        mower = Mower()
        mower.map=map
        mower.init_position("1 3 N")
        mower.rotate("D")
        self.assertEqual(mower.position.x,expected_position.x)
        self.assertEqual(mower.position.y,expected_position.y)
        self.assertEqual(mower.direction,expected_direction)
        
    def test_mower_move(self):
        """
        User move mower
        """
        map=Map()
        map.init_surface("5 5")
        expected_position=Position(2,2)
        expected_direction=Directions("E")
        mower = Mower()
        mower.map=map
        mower.init_position("1 2 E")
        mower.move()
        self.assertEqual(mower.position.x,expected_position.x)
        self.assertEqual(mower.position.y,expected_position.y)
        self.assertEqual(mower.direction,expected_direction)
        
    def test_mover_execute_instruction_rotate_right(self):
        map=Map()
        map.init_surface("5 5")
        expected_direction=Directions("E")
        mower = Mower()
        mower.map=map
        mower.init_position("1 2 N")
        mower.execute_instruction("D")
        self.assertEqual(mower.direction,expected_direction)
    
    def test_mover_execute_instruction_rotate_left(self):
        map=Map()
        map.init_surface("5 5")
        expected_direction=Directions("W")
        mower = Mower()
        mower.map=map
        mower.init_position("1 2 N")
        mower.execute_instruction("G")
        self.assertEqual(mower.direction,expected_direction)
    
    def test_mover_execute_instruction_move(self):
        map=Map()
        map.init_surface("5 5")
        expected_position=Position(2,2)
        expected_direction=Directions("E")
        mower = Mower()
        mower.map=map
        mower.init_position("1 2 E")
        mower.execute_instruction("A")
        self.assertEqual(mower.position.x,expected_position.x)
        self.assertEqual(mower.position.y,expected_position.y)
        
    def test_mover_start(self):
        map=Map()
        map.init_surface("5 5")
        expected_position=Position(1,3)
        expected_direction=Directions("N")
        mower = Mower()
        mower.map=map
        mower.init_position("1 2 N")
        mower.movement_instructions="GAGAGAGAA"
        mower.start()
        self.assertEqual(mower.position.x,expected_position.x)
        self.assertEqual(mower.position.y,expected_position.y)
        self.assertEqual(mower.direction,expected_direction)
        
        

if __name__ == '__main__':
    unittest.main()