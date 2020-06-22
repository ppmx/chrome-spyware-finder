#!/usr/bin/env python3

import os
import glob
import sys

path_chromium = os.path.expanduser("~/.config/chromium/")

with open("GalComm-Malicious-Chrome-Extensions-Appendix-B.txt") as f:
    malformed = f.read().split("\n")

for profile_path in glob.glob(os.path.join(path_chromium, "Profile*")):
    print("[+] Profile Path:", profile_path)

    extensions_path = os.path.join(profile_path, "Extensions")

    if not os.path.exists(extensions_path):
        continue

    for extension in os.listdir(extensions_path):
        if extension in malformed:
            print("   ALERT: malicious extension found:", extension)
    

