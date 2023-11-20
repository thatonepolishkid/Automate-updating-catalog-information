#!/usr/bin/env python3
import psutil
import shutil
import os
import socket
import emails

sender = 'automation@example.com'
receiver = '34.125.88.200@example.com'.format(os.environ.get('USER'))
body = 'Please check your system and resolve the issue as soon as possible.'
