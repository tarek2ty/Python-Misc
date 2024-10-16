import asn1tools
import os

def ASN1Decoder(file,ASN1DecoderFile):
    ASN1decoder = asn1tools.compile_files(ASN1DecoderFile, 'ber')
    #print("loaded module")
    with open(file, "rb") as encoded:
        content = encoded.read()
    Schema = bytearray()
    Schema.extend(content) #MeasDataCollection
    Data = ASN1decoder.decode('', content, check_constraints=False)  # output is type(dict)
    return(Data)    #^^^ put the first type dict or the appropriate one

DataDict = {}
ASN1DecoderFile = ""  #put privided schema file
dir = 'input'
for file in os.listdir(dir): #must have an input/ dir containing the .ber files
    try:
        decodedDict = ASN1Decoder(f'{dir}/{file}', ASN1DecoderFile)
    except Exception as e:
        print(f'failed to decode {file} due to {e}')
        continue
    print(decodedDict)

