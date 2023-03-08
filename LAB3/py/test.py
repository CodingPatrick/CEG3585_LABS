def decoding(message):
    output = []
    outString = ''
    for x in message:
        if x == "0":
            output.append(0)
        elif x == "1":
            output.append(1)
        elif x == "+" or x == "-":
            output.append(0)
    outString = ''.join(str(e) for e in output)
    return outString

def encoding(message):
    output = []
    outString = ''
    b = message
    change = 1
    i=0
    while(i<len(b)):
        if(i<=(len(b)-8) and b[i]=='0' and 
           b[i+1]=='0' and b[i+2]=='0' and 
           b[i+3]=='0' and b[i+4]=='0' and 
           b[i+5]=='0' and b[i+6]=='0' and 
           b[i+7]=='0' and i!=0  ):
            if change==-1:
                output.append(0)
                output.append(0)
                output.append(0)
                output.append('+')
                output.append('-')
                output.append(0)
                output.append('-')
                output.append('+')
                i+=8
            else:
                output.append(0)
                output.append(0)
                output.append(0)
                output.append('-')
                output.append('+')
                output.append(0)
                output.append('+')
                output.append('-') 
                i+=8
        elif (b[i] == '0'):
            output.append(0)
            i+=1
        else:
            if change ==-1:
                output.append('-')
            elif change == 1:
                output.append('+')
            i+=1
            if(change == 1):
                change = -1
            else:
                change = 1
    outString = ''.join(str(e) for e in output)
    return outString

print(1100000000110000010)
print(encoding('1100000000110000010'))
print(decoding('1100000000110000010'))