#!/usr/bin/env python3

import socket

host = socket.gethostname().lower()

mapping = {
    "orion": "orion",
    "ursa": "ursa",
    "hercules": "hercules",
    "hera": "hera",
    "gaea": "gaeac6",
    "wcoss": "wcoss2",
}

for token, machine in mapping.items():

    if token in host:
        print(machine)
        raise SystemExit(0)

print("unknown")
raise SystemExit(1)
