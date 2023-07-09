import os

cmd = "netsh wlan show profile"
mostrar_redes = os.popen(cmd)
print(mostrar_redes.read())

with open("wifi.txt", "a") as archivo:
    red = input("Ingresar la red: ")
    codigo = "netsh wlan show profile "+red+" key=clear"
    res = os.popen(codigo)
    mi_archivo2 = archivo.write(res.read())
    print(f"Se procesó la red: {red}")






































