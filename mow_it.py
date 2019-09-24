from enum import Enum
from exceptions import *
import argparse
import os


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        ret_str = ""
        ret_str += "".join([str(self.x), " ", str(self.y)])
        return ret_str


class Directions(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Map:
    def __init__(self):
        self.height = 0
        self.width = 0

    def init_surface(self, text):
        """Initiate Map surface."""
        try:
            surface = tuple(int(x) for x in text.split(" "))
        except ValueError:
            raise MapSurfaceException("Bad position values")

        if surface[0] <= 0 or surface[1] <= 0:
            raise MapSurfaceException("Map height and width should be upper than 0")

        if len(surface) != 2:
            raise MapSurfaceException("Map should have height and width")
        self.height = surface[0]
        self.width = surface[1]

    def is_valid_position(self, position):
        """Validate mower new position in map surface."""
        if position.x >= 0 and position.x <= self.width and position.y >= 0 and position.y <= self.height:
            return True
        return False


class Mower:
    def __init__(self):
        self.position = None
        self.direction = None
        self.movement_instructions = ""
        self.map = None

    def start(self):
        for movement_instruction in self.movement_instructions:
            self.execute_instruction(movement_instruction)
        print(self.position.__str__() + " " + self.direction.value)

    def init_position(self, text):
        items = text.split(" ")
        if len(items) != 3:
            return None
        try:
            position = Position(int(items[0]), int(items[1]))
            self.direction = Directions(items[2])
            
        except ValueError:
            raise MowerPositionException("Mower position parameer error")
        if self.map.is_valid_position(position) :
            self.position=position
        else :
            raise MowerPositionException("Mower position out of map")

    def execute_instruction(self, instruction):
        """If instruction is D or G rotate mower else move front."""
        if instruction in ["G", "D"]:
            self.rotate(instruction)
        elif instruction == "A":
            try:
                self.move()
            except MowerMapOverException as e:
                print(e)

    def rotate(self, direction):
        directions = [x.value for x in list(Directions)]
        if direction is "D":
            self.direction = Directions(directions[(directions.index(self.direction.value) + 1) % len(directions)])
        elif direction is "G":
            self.direction = Directions(directions[(directions.index(self.direction.value) - 1) % len(directions)])
        else:
            raise MowerRotationException("Rotation direction %s is incorrect" % direction)

    def move(self):
        if self.direction is Directions.NORTH:
            new_position = Position(self.position.x, self.position.y + 1)
        elif self.direction is Directions.SOUTH:
            new_position = Position(self.position.x, self.position.y - 1)
        elif self.direction is Directions.EAST:
            new_position = Position(self.position.x + 1, self.position.y)
        elif self.direction is Directions.WEST:
            new_position = Position(self.position.x - 1, self.position.y)
        if self.map.is_valid_position(new_position):
            self.position = new_position
        else:
            raise MowerMapOverException("new position %s is over map limit" % new_position)


def init_mowers_from_file(file_path):
    instructions = None
    if not os.path.exists(file_path):
        raise InstructionFileDoesNotExist
    with open(file_path, "r") as f:
        instructions = f.read().splitlines()
    map = Map()
    map.init_surface(instructions[0])
    mowers = []
    for i in range(1, len(instructions), 2):
        mower_position = instructions[i]
        mower_movements = instructions[i + 1]
        mower = Mower()
        mower.map = map
        mower.init_position(mower_position)
        mower.movement_instructions = mower_movements
        mowers.append(mower)
    return mowers


if __name__ == "__main__":
    '''Entry point for the player'''
    # Create the argument parser
    parser = argparse.ArgumentParser()
    # Path to the instruction filr
    parser.add_argument('-f', '--file', dest='instruction_file', default=None,
                        help='path of the instruction file.')
    args = parser.parse_args()
    instruction_file = args.instruction_file
    if instruction_file is None:
        print(b"The --file option is mandatory")
        exit(1)
    try:
        init_mowers_from_file(instruction_file)
        mowers = init_mowers_from_file(instruction_file)
        for mower in mowers:
            mower.start()
    except MowItException as e:
        print(e)
        exit(1)
