# PyRPG - CTCL 2025
# File: src/map.py
# Purpose: Provide functions for loading and processing map files
# Created: March 11, 2025
# Modified: March 12, 2025

import os
import pytiled_parser 
import pathlib
from PIL import Image, ImageDraw
from typing import List

class Tileset:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.tsx = pytiled_parser.parse_tileset(self.path)
        print(self.tsx.properties())


# Apparently naming this "Map" clobbers something else?
class GameMap: 
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.tmx = pytiled_parser.parse_map(self.path)
        tilesets = self.tmx.tilesets

        

        # "floor" is the only layer drawn here
        for layer in self.tmx.layers:
            if layer.name == "floor":
                floor = layer
                break
        

        mapsize = (self.tmx.tile_size[0] * self.tmx.map_size[0], self.tmx.tile_size[1] * self.tmx.map_size[1])
        im = Image.new("RGBA", mapsize, color = (0,0,0,0))
 
        mapimage = 




def loadmaps() -> List[GameMap]:
    mapfiles = ["maps/" + f for f in os.listdir("maps/") if f.endswith(".tmx") and os.path.isfile("maps/" + f)]
    maps = [GameMap(m) for m in mapfiles]
    return maps

