import sys, traceback


def printexception():
    tab = sys.exc_info()[2]
    while tab.tb_next:

        tab = tab.tb_next
    frames = tab.tb_frame                      # jump in execution frames
    code = frames.f_code
    print("Frame %s in %s at line %s"%\
              (code.co_name,
               code.co_filename,
               frames.f_lineno))

    for k, v in frames.f_locals.items():                  # print local variables
        print("%20s = %s"%(k,str(v)))

    
try:
    a = 3
    b = "Mango"
    c = a / 0
except ZeroDivisionError:
    printexception()
