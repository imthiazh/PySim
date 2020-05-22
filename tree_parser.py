import ast
import astpretty
import astdump

from simMatrix import simMatrix

def parse_tree(f1,f2):
    with open(f1, "r+") as myfile:
        source = myfile.read()
    with open(f2, "r+") as myfile2:
        source2 = myfile2.read()

    module_tree = ast.parse(source)
    module_tree2 = ast.parse(source2)
    # astpretty.pprint(module)
    # print("----------------------")
    # astpretty.pprint(module2)
    fndetails = []
    fnnames1 = []
    function_segments = [node for node in ast.walk(module_tree) if isinstance(node, ast.FunctionDef)]
    for f in function_segments:
        details = []
        details.append(f.name)
        fnnames1.append(f.name)
        details.append([a.arg for a in f.args.args])
        returnstatements = [node for node in ast.walk(module_tree) if isinstance(node, ast.Return)]
        for b in returnstatements:
            new = [a.id for a in b.value.elts]
            details.append(new)
        s = str(astdump.indented(f, printres=False))
        stri = s.split()
        details.append(stri)
        fndetails.append(details)
    fndetails2 = []
    fnnames2 = []
    function_segments2 = [node for node in ast.walk(module_tree2) if isinstance(node, ast.FunctionDef)]
    for f in function_segments2:
        details2 = []
        details2.append(f.name)
        fnnames2.append(f.name)
        details2.append([a.arg for a in f.args.args])
        for b in f.body:
            if isinstance(b, ast.Return):
                new = [a.id for a in b.value.elts]
                details2.append(new)
        s = str(astdump.indented(f, printres=False))
        stri = s.split()
        details2.append(stri)
        fndetails2.append(details2)

    return fndetails,fndetails2,fnnames1,fnnames2,f1,f2


if __name__ == "__main__":
    main()