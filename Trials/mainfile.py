from tree_parser import parse_tree
from kmp_module import kmp_compare
from dependency import *
from simMatrix import simMatrix
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

def getproject(d1,d2):
    my_console = Logger("my_console_file.txt")  # you can change the file's name
    list1 = glob.glob(d1)
    list2 = glob.glob(d2)
    # list1 = glob.glob("proj1/*.py")
    # list2 = glob.glob("proj2/*.py")
    # for (i,j) in list1,list2:
    #     print(i)
    #     print(j)
    files = []
    # for i in list1:
#attendee-profiler-master/*.py  Attendance-using-Face-master/*.py
    #n = len(list1)
    for (i,j) in zip(list1,list2):
        print("--------------------------------------------------------------")
        # fnarg,fnarg2,fn1,fn2,f1,f2 = parse_tree(i,j)
        # simMatrix(fnarg, fnarg2, fn1, fn2, f1, f2)
        # kmp_compare("attendee-profiler-master/face_detection.py", "Attendance-using-Face-master/faceDetection.py")
        kmp_compare(i, j)
        # graph_gen(i, j)
          #  cmt_input(i, j)


    # parse_tree("proj1/face_detection.py","proj2/faceDetection.py")
    # cmt_input("face_detection.py","faceDetection.py")
    # graph_gen("face_detection.py","faceDetection.py")
    # compare("faceDetection.py")
    # print(list1)
    # print(list2)
    my_console.close()
