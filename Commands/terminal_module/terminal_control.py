#!/usr/bin/env python3
import subprocess
from threading import Thread
from queue import Queue,Empty
import time


class terminal_control():
    def getabit(self):
        for c in iter(lambda:self.process.stdout.read(1),b''):
            self.stdout_queue.put(c)
        self.process.stdout.close()

    def __init__(self):
        self.process = subprocess.Popen('cmd',stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
        self.stdout_queue = Queue()
        self.stdout_thread = Thread(target=self.getabit)
        self.stdout_thread.daemon = True
        self.stdout_thread.start()
    

    def getdata(self):
        r = b''
        while True:
            try:
                c = self.stdout_queue.get(False)
            except Empty:
                break
            else:
                r += c
        return r.decode("BIG5")

    def writedata(self, in_dat):
        self.process.stdin.write(bytes(in_dat,'BIG5'))
        self.process.stdin.write(b'\n')
        self.process.stdin.flush()

    def close(self):
        self.process.kill()
