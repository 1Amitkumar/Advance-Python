import logging
import sys

##################################################################
# it writes messages to text file
l1 = logging.getLogger('ex1')
l1.addHandler(logging.FileHandler('log1.log', mode='w'))
l1.setLevel(logging.INFO)
l1.info('message for log 1')
##################################################################

##################################################################
# formats timestamp and writes to standard error stream
l2 = logging.getLogger('ex2')
handler = logging.StreamHandler(sys.stderr)
l2.addHandler(handler)
fmt='%(asctime)s | MY LOG MESSAGE IS: %(message)s'
handler.setFormatter(logging.Formatter(fmt, datefmt='%m/%d/%Y %I:%M:%S %p'))
l2.setLevel(logging.WARNING)
l2.warning('message for log 2')
###################################################################


###################################################################
# level of log 1 is still INFO
l1.info('another message for log 1')
