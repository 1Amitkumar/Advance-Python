def param(obligatory, optional=77, *args, **kwargs):
    print("obligatory: ", obligatory)
    print("optional  : ", optional)
    print("args      : ", args)
    print("kwargs    : ", kwargs)
    print()


param(True)
param(True, 99)
param(True, 99, 77)
param(True, 99, 77, 55)
param(True, 99, 77, 55, a=33, b=11)
