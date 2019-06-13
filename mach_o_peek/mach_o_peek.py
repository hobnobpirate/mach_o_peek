# -*- coding: utf-8 -*-
"""macho_o_peek, Mach-O reader

Copyright (c) 2019 Hobnobpirate <hobnonpirate@gmail.com>
"""

import struct
from pprint import pprint

class Header:

    def __init__(self, infile):
        self.file = infile

    def read_header(self):
        with open(self.file, "rb") as f:
            self.magic = self.get_value(f.read(4)) # loader.h
            self.cputype = self.get_value(f.read(4)) # machine.h
            self.cpusubtype = self.get_value(f.read(4)) # machine.h
            self.filetype = self.get_value(f.read(4)) # loader.h
            self.ncmds = self.get_value(f.read(4)) # loader.h
            self.sizeofcmds = self.get_value(f.read(4)) # loader.h

    def get_value(self, hexin):
        decoded = struct.unpack("<I", hexin)[0]
        return hex(decoded), decoded

if __name__ == "__main__":
    header = Header("Sample/cat")
    header.read_header()
    d = header.__dict__
    pprint(d, indent=4, width=80)