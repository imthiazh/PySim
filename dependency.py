import ast
from pprint import pprint
from getcmnt import cmt_input

def graph_gen(f1,f2):
    with open(f1, "r+") as myfile:
        source = myfile.read()
    with open(f2, "r+") as myfile2:
        source2 = myfile2.read()

    tree = ast.parse(source)
    #astpretty.pprint(ast.parse(expr))
    analyzer = Analyzer()
    analyzer.visit(tree)
    rp1 = analyzer.report()
    imp1 = rp1["import"]
    from1 = rp1["from"]
    tree2 = ast.parse(source2)
    # astpretty.pprint(ast.parse(expr))
    analyzer = Analyzer()
    analyzer.visit(tree2)
    rp2 = analyzer.report()
    imp2 = rp2["import"]
    from2 = rp2["from"]
    print()
    print("----- Dependency Graph Analysis of " + f1 + " & " + f2 + " -----")
    print()
    print("Imports identified in " + f1)
    # print(imp1)
    count = 1
    flag = 0
    for i in imp1:
        print(str(count) + ". " + str(i))
        count += 1
        flag = 1
    if (flag == 0): print("None found")
    print()
    print("Imports identified in " + f2)
    # print(imp2)
    count = 1
    flag = 0
    for i in imp2:
        print(str(count) + ". " + str(i))
        count += 1
        flag = 1
    if (flag == 0): print("None found")
    print()
    print("Similar Imports Report :")

    count = 1
    flag = 0
    for i in imp1:
        for j in imp2:
            if(i==j):
                print(str(count) + ". ", end='')
                print(i,end='')
                count += 1
                flag=1
                print()
    if(flag==0): print("None found")
    print()

    print("Incoming from imports identified in " + f1)
    # print(from1)
    count = 1
    flag = 0
    for i in from1:
        print(str(count) + ". " + str(i))
        count += 1
        flag = 1
    if (flag == 0): print("None found")
    print()
    print("Incoming from imports identified in " + f2)
    # print(from2)
    count = 1
    flag = 0
    for i in from2:
        print(str(count) + ". " + str(i))
        count += 1
        flag = 1
    if (flag == 0): print("None found")
    print()


    print("Similar Imports Report :")
    count = 1
    flag = 0
    for i in from1:
        for j in from2:
            if (i == j):
                print(str(count) + ". ", end='')
                print(i, end='')
                count += 1
                flag = 1
                print()
    if (flag == 0): print("None found")
    cmt_input(f1, f2)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"import": [], "from": []}

    def visit_Import(self, node):
        for alias in node.names:
            self.stats["import"].append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.stats["from"].append(alias.name)
        self.generic_visit(node)

    def report(self):
        return self.stats

def main():
    graph_gen("face_detection.py", "faceDetection.py")

if __name__ == "__main__":
    main()





