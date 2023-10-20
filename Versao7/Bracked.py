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
        limitadores=[None,None,None]
        r=""
        for i in sub_string:
            if i in "()":
                if limitadores[0] == None:
                    limitadores[0]=0
                limitadores[0]+=1 if i == "(" else -1
            elif i in "[]":
                if limitadores[1] == None:
                    limitadores[1] = 0
                limitadores[1]+=1 if i == "[" else -1
            elif i in "{}":
                if limitadores[2] == None:
                    limitadores[2]=0
                limitadores[2]+=1 if i == "{" else -1

        siglas=["P","Co","Ch"]
        for i,_ in enumerate(limitadores):
            if limitadores[i] == None:
                continue
            if limitadores[i] < 0:
                r+=f"{siglas[i]}(F{-limitadores[i]}),"
            elif limitadores[i] > 0:
                r+=f"{siglas[i]}(A{limitadores[i]}),"
            else:
                r+=f"{siglas[i]}(P),"
            
            
        return False,r
        
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
  
