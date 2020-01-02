#!/bin/bash
mosquitto_sub -h 192.168.3.39 -t '/seav_fan/#' -v | python3 command_line.py