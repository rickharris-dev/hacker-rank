#!/usr/bin/python
from datetime import datetime

time = raw_input().strip()
time = datetime.strptime(time,'%I:%M:%S%p')
print datetime.strftime(time, '%H:%M:%S')
