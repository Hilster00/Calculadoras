
def limpagem(lista):
    r=[]
    for i in lista:
        if type(i) != str:
            r.append(limpagem(i))
        elif i in ["+","/","*","-","r","sen","cos","tan","sen'","cos'","tan'","som","log","ln",'lg',"fat","%","^","!","π","e"]:
            r.append(i)
        elif ("." in i) or ("#" in i):
            if "#" in i:
                i = "inf"
            r.append(float(i))
        else:
            r.append(int(i))
          
    if r[0] == "-" or r[0] == "+":
        r.insert(0,0)
    return r
