fp = open("C:\\Users\\aniba\\OneDrive\\Desktop\\texto_ramdom.txt","r", encoding = "UTF-8")

'''

#2 Leer archivo
#datos = fp.read() # si nole coloco nad ame lee todo y si lle coloc un numero solo me lee ese numero determinado
fp.readline()
fp.read(4)
datos = fp.readline(8) # lee hasta cuando solo tenga un enter
#3 Cerrar el achivo
fp.close
print(datos)
'''
for linea in fp:
    print(linea[0], end="s")

fp.close()