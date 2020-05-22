def simMatrix(fnarg,fnarg2,fn1,fn2,f1,f2):
    flag = 0
    count = 1
    print("----- Class/Module Analysis of "+f1+" & "+f2+" -----")
    print()
    print("Classes/Modules identified in "+f1)
    print(str(count)+". "+f1)
    print()
    print("Classes/Modules identified in " + f2)
    print(str(count)+". "+f2)
    print()
    print("Similar Class/Module Report :")
    print("[NOTE: Two classes are said to be similar if any function structures are identified to be similar")
    print(", i.e. a similar report for two classes does not necessarily mean that all functions are similar]")
    print(", and a not similar report ensures that no functions were identified as similar")
    print()
    flag = 0
    for i in fnarg:
        for j in fnarg2:
            if(i[-1]==j[-1]):
                count += 1
                flag=1
                print()
            # else:
            #     flag = 0
            #     break
    count =1
    if(flag==0): print("Classes/Modules Identified as Not Similar")
    elif(flag==1): print("Classes/Modules Identified as Similar")
    print()
    print()
    print("----- Function/Method Analysis of " + f1 + " & " + f2 + " -----")
    print()
    print("Functions identified in " + f1 + ":")
    flg = 0
    for i in fn1:
        print(str(count)+". "+str(i))
        count+=1
        flg=1
    if(flg==0): print("None found")
    count=1
    print()
    print("More information about functions in " + f1 + ":")
    print("Fn Name"+"\t\t\t"+" Arguments"+"\t\t\t"+"Return Type""\t\t\t"+"Function Abstract Definition")
    flg = 0
    for i in fnarg:
        print(str(count)+ ". ",end='')
        flg = 1
        for j in i:
            print(j,end='\t')
            # print("\t")
        count+=1
        print()
    if (flg == 0): print("None found")
    count =1

    print()
    flg = 0
    print("Functions identified in " + f2 + ":")
    for i in fn2:
        flg = 1
        print(str(count) + ". " + str(i))
        count += 1
    if (flg == 0): print("None found")
    count = 1
    print()
    flg = 0
    print("More information about functions in " + f2 + ":")
    print("Fn Name"+"\t\t\t"+" Arguments"+"\t\t\t"+"Return Type""\t\t\t"+"Function Abstract Definition")
    for i in fnarg2:
        flg = 1
        print(str(count) + ". ", end='')
        for j in i:
            print(j, end='\t')
        count += 1
        print()
    if (flg == 0): print("None found")
    count = 1
    print()
    flag = 0
    print("Similar Function/Method Report :")
    print("[NOTE: Two functions are said to be similar their function structures are identified to be similar")
    print(",i.e Two functions with differing names, arguments and return type can be similar if they have similar body statements")
    print()
    print("Fn Name"+"\t\t\t"+" Arguments"+"\t\t\t"+"Return Type""\t\t\t"+"Function Abstract Definition")
    for i in fnarg:
        for j in fnarg2:
            if(i[-1]==j[-1]):
                print(str(count) + ". ", end='')
                for a in i:
                    print(a, end='\t')
                print()
                for a in j:
                    print(a, end='\t')
                count += 1
                flag=1
                print()
    count =1
    if(flag==0): print("None found")