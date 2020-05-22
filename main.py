from get_project import getproject
print("Please enter the directories to be compared: ")
print("Directory 1:")
d1 = input()
# d1 = 'attendee-profiler-master/*.py'
# d2 = 'Attendance-using-Face-master/*.py'
# l1 = "https://github.com/lakshaydeepak/attendee-profiler"
# l2 = "https://github.com/satinder147/Attendance-using-Face"
print("Directory 2:")
d2 = input()
print("Please enter the online github repository links if any: ")
print("Repository 1:")
l1 = input()
print("Repository 2:")
l2 = input()
getproject(d1,d2,l1,l2)
