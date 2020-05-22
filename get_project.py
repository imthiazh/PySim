from tree_parser import parse_tree
from kmp_module import kmp_compare
from dependency import *
from simMatrix import simMatrix
from repo_stargazers import stargazer_comparison
import glob
import sys
import os


class Logger(object):
    def __init__(self, filename="Red.Wood", mode="a"):
        self.stdout = sys.stdout
        self.file = open(filename, mode)
        sys.stdout = self

    def __del__(self):
        self.close()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def write(self, message):
        self.stdout.write(message)
        self.file.write(message)

    def flush(self):
        self.stdout.flush()
        self.file.flush()
        os.fsync(self.file.fileno())

    def close(self):
        if self.stdout != None:
            sys.stdout = self.stdout
            self.stdout = None

        if self.file != None:
            self.file.close()
            self.file = None

def getproject(d1,d2,l1,l2):
    my_console = Logger("my_console_file.txt")  # you can change the file's name
    list1 = glob.glob(d1)
    list2 = glob.glob(d2)

    for (i,j) in zip(list1,list2):
        print("--------------------------------------------------------------")
        fndetails1,fndetails2,fnnames1,fnnames2,f1,f2 = parse_tree(i,j)
        simMatrix(fndetails1, fndetails2, fnnames1, fnnames2, f1, f2)
        graph_gen(i, j)
        kmp_compare(i, j)
    stargazer_comparison()
    kmp_compare("attendee-profiler-master/README.md", "Attendance-using-Face-master/README.md")

    my_console.close()
