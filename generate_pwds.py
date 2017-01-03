#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  generate_pwds.py
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
import base64
import os

masterkey = 'abcdef'

log_level = logging.INFO
FORMAT = '%(levelname)-8s %(message)s'


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
        logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    else:
        logging.basicConfig(level=log_level, format=FORMAT)

    if args.p:
        logging.debug('master key set: ' + args.p)
        global masterkey
        masterkey = args.p

    if args.i:
        process_csv_file(args.i,'output.csv')


def process_csv_file(infile,outfile):
    logging.debug(sys._getframe().f_code.co_name)
    os.remove(outfile)
    try:
        f = open(infile, 'rt')
        reader = csv.reader(f)
        for row in reader:
            if row[0].strip()[:1] != '#':
               pwd = generate_passwords(row[0].strip(), row[1].strip())
               try:
                   f = open(outfile, 'a')
                   f.write(pwd+os.linesep)
               except FileNotFoundError:
                   logging.error(infile + ': File not found')
    except FileNotFoundError:
        logging.error(infile + ': File not found')



def generate_passwords(domainname, username, n=3,length = 16):
    logging.debug(sys._getframe().f_code.co_name + ': ' + domainname + ', ' + username)
    pwd_raw = domainname[:n] + username[:n] + masterkey
    logging.debug('hashing: ' + pwd_raw)
    pwd = hashlib.sha256(pwd_raw.encode('utf-8')).hexdigest()
    logging.debug('Password: '+ pwd)
    ascii_string=''.join(chr(int(pwd[i:i + 2], 16)%92+33) for i in range(0, len(pwd), 2))
    ascii_string = ascii_string.replace("'","-")
    ascii_string = ascii_string.replace("`","$")
    ascii_string = ascii_string.replace('"', "£")
    ascii_string = ascii_string[:length]
    ascii_string = '"' + domainname + '","'+ username + '","'+ ascii_string +'"'
    logging.info(ascii_string)
    return  ascii_string

parse_arguments(addparser_init())

def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
