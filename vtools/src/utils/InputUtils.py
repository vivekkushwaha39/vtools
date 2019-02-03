def readmultiline():
    data = ''
    chunk = ''
    while(chunk != '__' ):
        chunk = raw_input()
        if chunk != '__':
            data = data+chunk
            
    return data