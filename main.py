#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2016 Tillo Bosshart <ti.bo@hotmail.ch>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import logging
import Colorer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i',
                    action='store_true',
                    help='input csv file')
parser.add_argument('-e')

parser.add_argument('--debug',
                    action='store_true',
                    help='set logging level to ERROR')
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.ERROR)

if args.i:
    print('bla')

def main(args):
    call_path = args[0]
    args = args[1:]
    logging.info(str(args))
    logging.debug(str(args))
    logging.error(str(args))
    return 0

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
