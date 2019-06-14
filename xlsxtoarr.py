'''
    Convert Excel Column to Array.
'''

import getopt, sys
import xlrd
import re
from xlrd import open_workbook

# read commandline arguments, first
fullCmdArguments = sys.argv
# - further arguments
argumentList = fullCmdArguments[2:]

# i for input file and n  for the column number
unixOpt = "c:r:h"  
gnuOpt = ['col','row','help'] 

try:  
    arguments, values = getopt.getopt(argumentList, unixOpt, gnuOpt)
except getopt.error as err:  
    # output error, and return with an error code
    # print (str(err))
    sys.exit(str(err))

errMsgs = {
        0: 'Invalid file Sis/Bro',
    }
def errPrints(key):    
    sys.stderr.write(errMsgs[0]+'\n')
array = []
if __name__ == "__main__":
    colnum = 0
    rownum = 1
    
    # Check the extension of the file input
    if re.match('^.*(\.xlsx)$',sys.argv[1]) is None:
        errPrints(0)
    else:
        filepath = sys.argv[1]
    
    # Attempt to load in the file contents
    try:
        wb = open_workbook(filepath)
    except:
        sys.exit("The file at:{} couldn't be loaded".format(filepath))

    # Get the first sheet of the workbook
    try:
        ws = wb.sheet_by_index(0)
    except expression as identifier:
        sys.exit("Sheet couldn't be loaded")


    for curArg, curVal in arguments:  
        colnum = int(curVal if curArg in ("-c", "--col") else colnum)
        rownum = int(curVal if curArg in ("-r", "--row") else rownum)
    
    for _ in range(rownum, ws.nrows):
        array.append( ws.row(_)[colnum].value )
    
    sys.stdout.write(str(array)+'\n')
