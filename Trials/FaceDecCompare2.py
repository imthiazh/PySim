import ast

def main():
    f1 = "face_detection.py"
    f2 = "faceDetection.py"
    with open(f1, "r+") as myfile:
        source = myfile.read()
    with open(f2, "r+") as myfile2:
        source2 = myfile2.read()

    module = ast.parse(source)
    module2 = ast.parse(source2)

    fnarg = []
    print("The functions in 1 are :")
    fn1 = []
    function_definitions = [node for node in ast.walk(module) if isinstance(node, ast.FunctionDef)]
    for f in function_definitions:
        fna = []
        fna.append(f.name)
        fn1.append(f.name)
        fna.append([a.arg for a in f.args.args])
        # fnarg.append(fna)
        for b in f.body:
            if isinstance(b, ast.Return):
                new = [a.id for a in b.value.elts]
                fna.append(new)
        fnarg.append(fna)
    print(fn1)
    print("More information about functions: ")
    for a in fnarg: print(a)

    fnarg2 = []
    print("The functions in 2 are :")
    fn2 = []
    function_definitions2 = [node for node in ast.walk(module2) if isinstance(node, ast.FunctionDef)]
    for f in function_definitions2:
        fna2 = []
        fna2.append(f.name)
        fn2.append(f.name)
        fna2.append([a.arg for a in f.args.args])
        for b in f.body:
            if isinstance(b, ast.Return):
                new = [a.id for a in b.value.elts]
                fna2.append(new)
        fnarg2.append(fna2)
    print(fn2)
    print("More information about functions: ")
    for a in fnarg2: print(a)
    print()
    print()
    print("Similarity Checking")
    simMatrix(fnarg,fnarg2,fn1,fn2,f1,f2)

def simMatrix(fnarg,fnarg2,fn1,fn2,f1,f2):
    flag = 0
    print("Class/module Similarity Verification :")
    print("Classes/Modules in Code")
    print(f1)
    print(f2)
    # print()
    if(fn1==fn2): print("Classes/Modules Identified as Similar ")
    else: print("Classes/Modules Identified as Not Similar")
    print()
    print("Function/Method Similarity Verification : ")
    print()
    print("Function/Method Identified as Similar : ")
    for i in fnarg:
        for j in fnarg2:
            if(i==j):
                flag = 1
                print(i)
    if(flag==0): print("None found")



if __name__ == "__main__":
    main()