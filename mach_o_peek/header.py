#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""header.py, Mach-O reader

This class defines the header for a Mach O file.
Currently, only 64-bit Mach O files are processed.

Copyright (c) 2019 Hobnobpirate <hobnonpirate@gmail.com>
"""

import struct

MAGICTYPES = {
    3199925962: "fat_le",
    3405691582: "fat_be",
    3472551422: "macho_le_x86",
    3489328638: "macho_le_x64",
    4277009102: "macho_be_x86",
    4277009103: "macho_be_x64",
}

CPUTYPES = {
    1: "vax",
    2: "romp",
    4: "ns32032",
    5: "ns32332",
    7: "i386",
    8: "mips",
    9: "ns32532",
    11: "hppa",
    12: "arm",
    13: "mc8800",
    14: "sparc",
    15: "i860",
    16: "i860_little",
    17: "rs6000",
    18: "powerpc",
    16777216: "abi64",
    16777223: "x86_64",
    16777228: "arm6464",
    16777234: "powerpc64",
    4294967295: "any",
}

FILETYPES = {
    1: "object",
    2: "executable",
    3: "fvmlib",
    4: "core",
    5: "preload",
    6: "dylib",
    7: "dylinker",
    8: "bundle",
    9: "dylib_stub",
    10: "dsym",
    11: "kext_bundle",
}


class Header:
    """This class parses the header of a Mach O executable"""

    def __init__(self, infile):
        self.file = infile

    def read_header(self):
        """Check the first 4 bytes of an executable for the magic number"""
        with open(self.file, "rb") as f:
            try:
                self.magic = f.read(4)
                if self.magic == b"\xcf\xfa\xed\xfe":
                    self.fmt = "<I"
                    self.process_macho(f)
                elif self.magic == b"\xca\xfe\xba\xbe":
                    pass
            except:
                pass

    def process_macho(self, f):
        """Process a Mach O binary header"""
        self.magic = MAGICTYPES[self.get_value(self.magic)]
        self.cputype = CPUTYPES[self.get_value(f.read(4))]  # machine.h
        self.cpusubtype = self.get_value(f.read(4))  # machine.h
        self.filetype = FILETYPES[self.get_value(f.read(4))]  # loader.h
        self.ncmds = self.get_value(f.read(4))  # loader.h
        self.sizeofcmds = self.get_value(f.read(4))  # loader.h

    def get_value(self, hexin):
        """Decode a hex value"""
        decoded = struct.unpack(self.fmt, hexin)[0]
        return decoded
