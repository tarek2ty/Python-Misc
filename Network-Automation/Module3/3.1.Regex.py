# In this Modoule, we will write a parser

import re       #regex

#we need to extract model id for example
#from the text 
# "cisco CSR1000V (VXE) processor (revision VXE) with 31k/32k memory"
# we need "CSR1000V" only

def parse_model(text):
    model_regex = re.compile(r"cisco\s+(?P<model>\S+)\s+\(\S+\)\s+processor\s+")
    #find cisco then \s+ means one white space or more
    #(?P) is capture group on \S+ means one or more non-white spaces
    #put this capture group in a dictionary <model>
    #then skip white spaces and non-white spaces until you find "processor"
    #just to make sure we are on the right line
    #we can just write "cisco\s+(?P<model>\S+)" but we wanted to avoid other variations

    model_match = model_regex.search(text)  #see if your regex is found in the text
    if model_match: # if found, that means the model is stored in a dict key = "model"
        return model_match.group("model")
    return None 

print(parse_model("cisco CSR1000V (VXE) processor (revision VXE) with 31k/32k memory"))