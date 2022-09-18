import re

begin_comm = ["#", "“ ” ”", "‘’’"]
boolop = ["and", "or", "not"] 
compop = ["==", "!=", "<", ">", "<=", ">="]
boolvak = ["false", "true"]
intop = ["+", "-", "*", "/"]
assignop = ["="]
int = [0,1,2,3,4,5,6,7,8,9]
reservword = ["print", "False", "class",	"is", "return", "None",	"continue",	"lambda", "try", "True", "def",	"nonlocal",	"while", "and",	"del", "not", "with", "as",	"elif",	"or", "yield", "assert", "else", "pass", "break", "except",	"raise"]
delimop = ["{", "}", "[", "]"]
may = '^[A-Z]*($|\s)'
min = '^[a-z]*($|\s)'
num = '^[0-9]*($|\s)'

def encontrar_elemento(elemento, lista):
    if elemento in lista: 
        return True
    return False

def getchar(indice, cadena): #retuen siguiente, lo mueve
    indice = indice+1
    return cadena[indice], indice
    

def peekchar(indice, cadena): #return sig sin mover
    return cadena[indice+1], indice


def calculadora(cur_char, cadena, indice):

    if encontrar_elemento(cur_char, delimop):
        devuelvo = "CLOSE_PAR [",cur_char, "] found"
        return devuelvo

    if cur_char == ":":
        a = peekchar(indice, cadena)
        if a == "=":
            devuelvo = "ASSIGN_OP  [=] found"
            return devuelvo

        else:
            devuelvo = "ERROR found"
            return devuelvo
            
    if cur_char == "/":
        a = peekchar(indice, cadena)
        if ((a == "*") or (a== "/")):
            return 0        ##################

        else:
            devuelvo = "DIVISION_OP [/] found"
            return devuelvo                


    if cur_char == ".":
        a = peekchar(indice, cadena)
        if re.match(num, a):
            dev_num = []
            dev_num.append(a)
            while(True):
                a = peekchar(indice, cadena)
                if re.match(num, a):
                   dev_num.append(a) 

                else:
                    break
            devuelvo = "Numero",dev_num, "found"
            return devuelvo 
        else:
            devuelvo = "ERROR found"
            return devuelvo

    if re.match(num,cur_char) == True:  
        a = peekchar(indice, cadena) 
        dev_num = []
        dev_num.append(a)
        while(True):
            a = peekchar(indice, cadena)
            if re.match(num, a):
                dev_num.append(a) 

            else:
                break
        devuelvo = "Numero",dev_num, "found"
        return devuelvo    

    if (re.match(min,cur_char) == True) or (re.match(may,cur_char) == True): 
        a = peekchar(indice, cadena) 
        dev_car= []
        dev_car.append(a)
        while(True):
            a = peekchar(indice, cadena)
            if (re.match(num, a) == True) or (re.match(min,cur_char) == True) or (re.match(may,cur_char) == True):
                dev_car.append(a) 

                if (dev_car == "read") or (dev_car == "write"):
                    devuelvo = "RESERVEDWORD",dev_car, "found"
                    return devuelvo 

            else:
                break
        devuelvo = "ID",dev_car, "found"
        return devuelvo
    else:
        devuelvo = "ERROR found"
        return devuelvo

    





with open(r'C:\Users\Paul\Desktop\Compiladores\scanner\archivo.txt', 'r', encoding="utf8") as f:
    lines = f.readlines()

lines = [line.replace(r'\n', ' ').replace(r'\r', '') for line in lines]

with open(r'C:\Users\Paul\Desktop\Compiladores\scanner\archivo1.txt', 'w', encoding="utf8") as f:
    f.writelines(lines)


cadena_tres = "a = 2 +7\nprint (a)$"

cadena_tres = " ".join(cadena_tres.split())
cadena_tres = cadena_tres.replace(" ", "")
cadena_tres.rstrip()
print(cadena_tres)
print("INFO SCAN - Start scanning…")



tamaño = len(cadena_tres)
i =0
while(cadena_tres[i]!="$"):
    token = calculadora(cadena_tres[i], cadena_tres, i)
    print(token)

print("INFO SCAN - Completed with 0 errors")