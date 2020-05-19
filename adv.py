from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)


# * --------------------------- Traversing Path -------------------------------
def dft(current_room):
    opposites = {
        'n': 's',
        'e': 'w',
        's': 'n',
        'w': 'e'
    }
    path = []
    visited = set()
    def search(current_room, last_direction_traveled=None):
        # Get all of the current rooms exits it looks like ['n', 's', 'w', 'e']
        exits = current_room.get_exits()
        # Add room to the visited set
        visited.add(current_room)
        # Chooses the first direction in the list   
        for direction in exits:
            # Getting the room that is in that direction
            next_room = current_room.get_room_in_direction(direction)
            # If the next room hasn't been visited
            if next_room not in visited:
                # Add that direction to the path
                path.append(direction)
                # Search for a new room to travel to. Update the last direction traveled 
                search(next_room, direction)
        # If this runs we hit a dead end and the only way to go is backwards which is the opposite    
        if last_direction_traveled is not None:
            # Traversing if the room has already been visited and there are no more directions to go reveals a deadend
            path.append(opposites[last_direction_traveled])
   
    search(current_room)
    return path
    
# * ------------------------------------------------------------------------

# Fill this out with directions to walk
# traversal_path = ['n', 's', 'e', 'w']
traversal_path = dft(player.current_room) 


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
