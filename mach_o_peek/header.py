# -*- coding: utf-8 -*-
"""header.py, Mach-O reader

This class defines the header for a Mach O file.
Currently, only 64-bit Mach O files are processed.

Copyright (c) 2019 Hobnobpirate <hobnonpirate@gmail.com>
"""

import struct

class Header:

    def __init__(self, infile):
        self.file = infile

    def read_header(self):
        with open(self.file, "rb") as f:
            try:
                self.magic = self.get_value(f.read(4)) # loader.h
                if self.magic[0] == "0xfeedfacf":
                    self.cputype = self.get_value(f.read(4)) # machine.h
                    self.cpusubtype = self.get_value(f.read(4)) # machine.h
                    self.filetype = self.get_value(f.read(4)) # loader.h
                    self.ncmds = self.get_value(f.read(4)) # loader.h
                    self.sizeofcmds = self.get_value(f.read(4)) # loader.h
            except:
                pass

    def get_value(self, hexin):
        decoded = struct.unpack("<I", hexin)[0]
        return hex(decoded), decoded
