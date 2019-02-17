# -*- coding: utf-8 -*-
import subprocess

class ariaClass:

    def __init__(self):
        pass

    def torrent_dld(self, name):
        self.name = name
        cmd = f".\\bin\\aria2c.exe -T {name}"
        print(cmd)
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        data = proc.communicate()
        for line in data:
            print(line)

    def magnet_dld(self, name):
        self.name = name
        return f'.\\bin\\aria2c.exe {name}'