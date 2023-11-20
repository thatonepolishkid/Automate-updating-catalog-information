import os
import shutil
import sys
import socket
import psutil


def check_disk_full(disk, min_gb, min_percent):
    """Checks if there is enough disk space."""
    du = shutil.disk_usage(disk)

    percent_free = 100 * du.free / du.total

    gigabytes_free = du.free / 2**30

    return gigabytes_free < min_gb or percent_free < min_percent


def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=0.5, min_percent=20)


def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("localhost")
        return False
    except Exception:
        return True

def check_virtual_memory():
    return psutil.virtual_memory() >= 500

def check_cpu_usage():
    """Checks cpu usage over 2 seconds, and gets the average. If cpu usage under 80% returns True, else returns False"""
    usage = psutil.cpu_percent(2)
    print(usage)
    return usage > 80


def main():
    checks = [
        (check_root_full, "Error - Available disk space is less than 20%"),
        (check_no_network, "Error - localhost  cannot be resolved to [127.0.0.1]"),
        (check_cpu_usage, "Error - cpu usage is over 80%"),
        (check_virtual_memory, "Error - Available memmory is less than 500MB")
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False
    if not everything_ok:
        sys.exit(1)
    print("Nothing wrong")


if __name__ == '__main__':
    main()
