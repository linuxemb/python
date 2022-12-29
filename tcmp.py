##############################################   To do =======================

# map board name to column
    # this is incomplete - only supports HDMx
columnIndexDict = {"HDMx": {"MAIN-1-BOARD": 3, "STIC-1-BOARD": 5, "MAIN-1-PAN": 6, "MAIN-1-THBLT-1":7, "Sample": 9},    # "MAIN-1-THBLT-1":7 == pusherplate 0    but   Heater 0 ??  RTD  ?? 

#### to do   ??? 
                   #"TCC3": {"MAIN-1-BOARD": 3, "MAIN-1-PAN": 6, "MAIN-1-THBLT-1":7, "LV-TH-1-16" : ??, "Device Kit" : ?     Sample": 9},     


                   "HST": {"MAIN-1-BOARD": 3, "STIC-1-BOARD": 5, "MAIN-1-PAN": 6, "MAIN-1-THBLT-1":7, "Sample": 9},  
                    "HST": {"MAIN-1-BOARD": 3, "STIC-1-BOARD": 5, "MAIN-1-PAN": 6, "MAIN-1-THBLT-1":7, "Sample": 9},  

                       }
#######################################################################
    # Based on I-Ninja-BLT-Format.pdf   
bltFieldsDict = {
                #                                          HDMx  --owned hw items
                #                  type    HBI     HST     TCC     CME     STIC    PAN     PUSHER  PSTPOC Sample
                "LANGUAGE"      : ["INT",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "1"],
                "MFGDATE"       : ["DATE", "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "2021.08.30-08.36"],
                "MFGID"         : ["STR",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "HDMX-TCC2.x"],
                "PRODNAME"      : ["STR",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "HDMx"],
                "SERIALNUM"     : ["STR",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "049683-97687"],
                "PARTNUM"       : ["STR",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "249"],
                "FRUFILEID"     : ["INT",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "79"],
                "MACADDR"       : ["MAC",  "YES",  "YES",  "YES",  "YES",  "NO",   "NO",   "NO",   "NO",  "01-03-02-98-34-23" ],
                "MACADDR2"      : ["MAC",  "YES",  "NO",   "NO",   "NO",   "NO",   "NO",   "NO",   "NO",  "01-03-02-98-34-24"  ], 
                "HWREV"         : ["REV",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "2.5.0"],
                "FPGAREV"       : ["REV",  "YES",  "YES",  "YES",  "NO",   "NO",   "NO",   "NO",   "NO",  "43.5.0" ],
                "FWREV"         : ["REV",  "YES",  "YES",  "YES",  "YES",  "NO",   "NO",   "NO",   "YES", "34.2.7"],
                "PLDREV"        : ["REV",  "NO",   "YES",  "YES",  "NO",   "NO",   "NO",   "NO",   "NO",  "12.3.2"],
                "LIFECYCLECNT"  : ["INT",  "YES",  "YES",  "NO",   "NO",   "NO",   "YES",  "YES",  "NO",  "87"],
                "PMDATE"        : ["DATE", "YES",  "YES",  "NO",   "NO",   "NO",   "YES",  "YES",  "NO",  "2021.08.30-08.36"],
                "PMCYCLECNT"    : ["INT",  "YES",  "YES",  "NO",   "NO",   "NO",   "YES",  "YES",  "NO",  "42"],
                "REPLCYCLECNT"  : ["INT",  "YES",  "YES",  "NO",   "NO",   "NO",   "NO",   "YES",  "NO",  "98"],
                "CLEANCYCLECNT" : ["INT",  "YES",  "YES",  "NO",   "NO",   "NO",   "NO",   "YES",  "NO",  "63"],
                "FLAGS"         : ["INT",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES",  "YES", "0"],  
                "OFAPURGE"      : ["INT",  "YES",  "NO",   "NO",   "NO",   "NO",   "YES",  "NO",   "NO",  "0" ],
                }



bltFieldsList = list(bltFieldsDict.keys())
print(f'bltFireldList:{bltFieldsList}\n')

def buildCmd( tcmpCmd, cmd, target, sequence, fieldList):
    """ Build a TCMP command with the given parameters.
    
    Typical command will look like:
    <REQ:GET-BLT:MAIN-1-BOARD::FIELD=LANGUAGE>

    Returns: String containing command
    """
    cmdList = [tcmpCmd, cmd, target, sequence, fieldList]

    return "<{cmd}>".format(cmd=":".join(cmdList))

def buildReq(cmd, target, sequence, fieldList):
    """ Build a TCMP REQ command with the given parameters.
    
    Typical command will look like:
    <REQ:GET-BLT:MAIN-1-BOARD::FIELD=LANGUAGE>

    Returns: String containing command
    """
    return buildCmd("REQ", cmd, target, sequence, fieldList)


def getColumnIndex(boardName, bltName):
    """Get the columen index in bltFieldsDict for boardName and bltName.
    """
    boardDict = columnIndexDict[boardName]
    columnIndex = boardDict[bltName]

    return columnIndex

def getSampleColumnList( platformTarget):
    """ Return the sample values for each entry as a list.

    Returns: List of list containing [[<field name>, <sample value>], ...]
    """
    print(f'columnIndexDict: {columnIndexDict}')
    columnIndex = getColumnIndex(platformTarget, 'Sample')
    print(f' columnIndex:{columnIndex}')
    columnList = []
    for key, val in bltFieldsDict.items():
        columnList.append([key, val[columnIndex]])

    return columnList

##################
def getSupportedColumnList( platformTarget, target, unifiedBLT=False):
        """This function pulls out a 'supported' column from the bltFieldsDict.
        """
        if unifiedBLT:
            columnList = [[key, "YES"] for key in bltFieldsDict.keys()]
        else:
            columnIndex = getColumnIndex(platformTarget, target)
       
            columnList = []
            breakpoint()
            for key, val in bltFieldsDict.items():
                columnList.append([key, val[columnIndex]])

        return columnList

targetListDict = {"TCC3": ["MAIN-1-BOARD",] + ["ARRAY-{x}-BOARD".format(x=x) for x in range(1, 5)] + ["TH-{x}-BOARD".format(x=x) for x in range(1, 17)],
                      "HST": ["MAIN-1-BOARD", "TIE-1-BOARD", "MAIN-1-THBLT-1", "MAIN-1-THBLT-2", "MAIN-1-THBLT-3", "MAIN-1-THBLT-4"],
#                      "HDMx": ["MAIN-1-BOARD"],
                      "HDMx": ["MAIN-1-BOARD", "MAIN-1-PAN", "MAIN-1-THBLT-1", "STIC-1-BOARD"],
#                      "HDMx": ["MAIN-1-BOARD", "MAIN-1-PAN",],
                      }




# test =============================

getCommand = "GET-BLT"
fieldName = 'MFG'
value = 'fidus'
fieldList = "FIELD={fn},VALUE={val}".format(fn=fieldName, val=value)

req  = buildReq(getCommand, 'Main-1-board', '11', fieldList )
req1  = buildReq(getCommand, 'Main-1-board', '', fieldList )
print(req1)
# <REQ:GET-BLT:Main-1-board:11:FIELD=MFG,VALUE=fidus>
platformTarget =  'HDMx'
#columnList = getSampleColumnList(platformTarget)
#print(f'columnList: {columnList}')  

targetList = targetListDict[platformTarget]   # targetList=['MAIN-1-BOARD']
print(f'targetList={targetList}')

""" columnIndex:9
columnList: [['LANGUAGE', '1'], ['MFGDATE', '2021.08.30-08.36'], ['MFGID', 'HDMX-TCC2.x'], ['PRODNAME', 'HDMx'], ['SERIALNUM', '049683-97687'], ['PARTNUM', '249'], ['FRUFILEID', '79'], ['MACADDR', '01-03-02-98-34-23'], ['MACADDR2', '01-03-02-98-34-24'], ['HWREV', '2.5.0'], ['FPGAREV', '43.5.0'], ['FWREV', '34.2.7'], ['PLDREV', '12.3.2'], ['LIFECYCLECNT', '87'], ['PMDATE', '2021.08.30-08.36'], ['PMCYCLECNT', '42'], ['REPLCYCLECNT', '98'], ['CLEANCYCLECNT', '63'], ['FLAGS', '0'], ['OFAPURGE', '0']]
"""
#print(getSupportedColumnList(platformTarget, 'MAIN-1-BOARD', True))
print(getSupportedColumnList(platformTarget, 'MAIN-1-THBLT-1"', True))


#targetList=['MAIN-1-BOARD', 'MAIN-1-PAN', 'MAIN-1-THBLT-1', 'STIC-1-BOARD']    --- for HDMx
# [['LANGUAGE', 'YES'], ['MFGDATE', 'YES'], ['MFGID', 'YES'], ['PRODNAME', 'YES'], ['SERIALNUM', 'YES'], ['PARTNUM', 'YES'], ['FRUFILEID', 'YES'], ['MACADDR', 'YES'], ['MACADDR2', 'YES'], ['HWREV', 'YES'], ['FPGAREV', 'YES'], ['FWREV', 'YES'], ['PLDREV', 'YES'], ['LIFECYCLECNT', 'YES'], ['PMDATE', 'YES'], ['PMCYCLECNT', 'YES'], ['REPLCYCLECNT', 'YES'], ['CLEANCYCLECNT', 'YES'], ['FLAGS', 'YES'], ['OFAPURGE', 'YES']]

print('-----getSupportedColumnList===')
print(getSupportedColumnList(platformTarget, 'MAIN-1-THBLT-1'))  #  --- for HDMx
#[['LANGUAGE', 'YES'], ['MFGDATE', 'YES'], ['MFGID', 'YES'], ['PRODNAME', 'YES'], ['SERIALNUM', 'YES'], ['PARTNUM', 'YES'], ['FRUFILEID', 'YES'], ['MACADDR', 'YES'], ['MACADDR2', 'NO'], ['HWREV', 'YES'], ['FPGAREV', 'YES'], ['FWREV', 'YES'], ['PLDREV', 'YES'], ['LIFECYCLECNT', 'NO'], ['PMDATE', 'NO'], ['PMCYCLECNT', 'NO'], ['REPLCYCLECNT', 'NO'], ['CLEANCYCLECNT', 'NO'], ['FLAGS', 'YES'], ['OFAPURGE', 'NO']]
