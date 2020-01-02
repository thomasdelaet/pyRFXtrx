# This file is part of pyRFXtrx, a Python library to communicate with
# the RFXtrx family of devices from http://www.rfxcom.com/
# See https://github.com/woudt/pyRFXtrx for the latest version.
#
# Copyright (C) 2012  Edwin Woudt <edwin@woudt.nl>
#
# pyRFXtrx is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyRFXtrx is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pyRFXtrx.  See the file COPYING.txt in the distribution.
# If not, see <http://www.gnu.org/licenses/>.

import sys
sys.path.append("../")

import RFXtrx
import time

def print_callback(event):
    print(event)

rfxcom_device = '/dev/serial/by-id/usb-RFXCOM_RFXtrx433XL_DO2ZW4OB-if00-port0'

try:
    conn = RFXtrx.Connect(rfxcom_device, print_callback, debug=True)
    print (conn)
    fan = RFXtrx.get_device(0x17, 0x03, "005545")

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line.startswith('/seav_fan/t'):
            command = line.lstrip('/seav_fan/t')[0]
        if command == '1':
            fan.send_high(conn.transport)
        elif command == '2':
            fan.send_medium(conn.transport)
        elif command == '3':
            fan.send_low(conn.transport)
        elif command == '4':
            fan.send_off(conn.transport)
        time.sleep(3)
finally:
    conn.close_connection()
