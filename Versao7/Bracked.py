def bracked(string,feedback=False):
    sub_string=""
    for i in string:
        if i in "[]{}()":
            sub_string+=i
    for i in range(len(sub_string)):
        sub_string=sub_string.replace("[]","")
        sub_string=sub_string.replace("{}","")
        sub_string=sub_string.replace("()","")

    if feedback and len(sub_string) != 0:
        limitadores={}
        for i in sub_string:
            if i in "()":
                limitadores["P"]=limitadores.get("P",0) + 1 if i == "(" else -1
            elif i in "[]":
                limitadores["Co"]=limitadores.get("Co",0) + 1 if i == "[" else -1
            elif i in "{}":
                limitadores["Ch"]=limitadores.get("Ch",0) + 1 if i == "{" else -1

        
            
            
        return False,limitadores
        
    return len(sub_string) == 0

if __name__=="__main__":
  print(bracked("([][]("))
  print(bracked("([][])"))
  print(bracked("{"),True)
  print(bracked("}",True))
  print(bracked("{}"))
  print(bracked("((([()])))"))
  print(bracked("((([(]))))",True))
  print(bracked("()[]()"))
  print(bracked(")(())(()",True))
  print(bracked("{](",True))
  print(bracked("})[",True))
  
