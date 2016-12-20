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
import csv
import sys
import hashlib

masterkey = 'abcdef'

def addparser_init():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        help='input csv file')
    parser.add_argument('-p',
                        help='master key')
    parser.add_argument('--debug',
                        action='store_true',
                        help='set logging level to DEBUG')
    return parser


def parse_arguments(parser):
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)

    if args.p:
        logging.debug('master key set: ' + args.p)
        global masterkey
        masterkey = args.p

    if args.i:
        read_csv_file(args.i)



def read_csv_file(file):
    logging.debug(sys._getframe().f_code.co_name)
    try:
        f = open(file, 'rt')
        reader = csv.reader(f)
        for row in reader:
            generate_passwords(row[0], row[1])
    except FileNotFoundError:
        logging.error(file + ': File not found')


def generate_passwords(domainname, username, n=3):
    logging.debug(sys._getframe().f_code.co_name + ': ' + domainname + ', ' + username)
    logging.debug('hashing: ' + domainname[:n] + username[:n] + masterkey)


parse_arguments(addparser_init())

def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
