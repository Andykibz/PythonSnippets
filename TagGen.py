"""
    This is a simple script that is used to create a JSON file of PLC Tag Names
    and their corresponding addresses. This is don by converting a list of tag names to 
    a Dictionary and evenntually dumping that Dictionary as a JSON file
    The addresses are created automatically and in an incremental fashion i.e
    I0.0,I0.1, ...,I0.7, I1.0, I1.2, .... etc
    It requires definition of the following by its user
        1. Name of the Json File
        2. List of Tag Names.
    Afterwards the user needs to call the convertToDict function which takes in
        1. A list of tag names
        2. The PLC Area alphanumeric symbol i.e I -> inputs, ! -> Outputs
        3. The Start Byte
        4. The Start Bit
    The converDict may be called a number of times however it will only update a 
    single dictionary object which will eventually creat the JSON file.
    The output will be something like this:
        {
            "Start": {
                "label": "Start",
                "address": "I0.0"
            },
            "Stop": {
                "label": "Stop",
                "address": "I0.1"
            }
        }
        For this input: convertToDict( ["start", "stop"], I, 0, 0 )
            
"""
# NOTE: The output file will be placed in the directory from where you are calling the 
#       python file and not necesarily where this python script is.

import json
import sys

# Name of the Output json file name
outFileName = "C:IndexingTags.json"

# List of all Input Tags.
InputTagList = [ "Start", "Stop", "Emergency", "Output", "Reset", "Auto","TransferRetracted", 
                "TransferExtended", "CapacitiveSensorB3", "FiberOpticSensorB2", "InductiveSensorB4",
                "CapacitiveSensorB1, StepperMotorReadyb%", "IN1", "IN2" ]

# List of Output Tags
OutputTagList = [ "StartLamp", "ExtendTransfer4M1", "ExtendLift1M1", "RetractLif1M2", "Stepper45", "Stepper90","ReleaseGripper3M1", 
                "CloseGripper3M2", "ExtendRotationCylinder2M1", "RetractRotationCylinder", "OUT1", "OUT2"]

# Initialise a blank Dictionary
tagDict  = dict()

# Populates the instatiated dictionary tagDict
def convertToDict(_tagList, area, bytNum, bitNum):
    for tag in _tagList:
        tagDict[tag] = {"label": tag, "address": f"{area}{bytNum}.{bitNum}" }
        bytNum = bytNum + 1 if( (bitNum+1)%8 == 0 ) else bytNum
        bitNum = (bitNum+1)%8


if __name__ == "__main__":
    convertToDict(InputTagList, "I", 0, 0)
    convertToDict(OutputTagList, "Q", 4, 0)

    with open(outFileName, 'w', encoding ='utf8') as json_file:
        
        try:
            json.dump(tagDict, json_file, ensure_ascii = True)
        except:
            sys.stderr.write("Something did not work out quite right")
        else:
            sys.stdout.write(f"{outFileName} created Successfully!")

