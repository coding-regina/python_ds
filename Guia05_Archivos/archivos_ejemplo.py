data = 'Sextos contenidos'
with open('archivo.txt','r') as f:
    #f.write(data)
    f.seek(20) #posiciona al inicio del archivo
    print(f.read())
    print(f.tell())
    f.close()