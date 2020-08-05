  
def list_yello(yello):
    list = ''
    for i in range(len(yello)):
        list += str(i + 1) + '. ' + yello[i] + '\n'
    return list