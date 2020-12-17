


def eval_expr(s,d={}):

    s=s.split()
    n=len(s)
    zasobnik=[]

    for i in range(n):

        if s[i] in d:
        
            zasobnik.append(int(d[s[i]]))

        if s[i].isdigit():

            zasobnik.append(int(s[i]))

        elif s[i]=="+":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(a)+int(b))

        elif s[i]=="-":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(a)-int(b))

        elif s[i]=="*":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(a)*int(b))

        elif s[i]=="/":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(a)/int(b))

    return zasobnik.pop()


def to_infix(s):
    
    s=s.split()
    stack=[]
    n=len(s)
    
    for i in range(n):

        if s[i].isdigit():

            stack.append(int(s[i]))

        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            string="( {} + {} )".format(a,b)
            stack.append(string)

        elif s[i]=="-":
            a=stack.pop()          
            b=stack.pop()
            string="( {} - {} )".format(a,b)
            stack.append(string)

        elif s[i]=="*":
            a=stack.pop()                                                                                           
            b=stack.pop()                                                                                           
            string="( {} * {} ) ".format(a,b)
            stack.append(string)
        
        elif s[i]=="/":
            a=stack.pop()                                                                                           
            b=stack.pop()                                                                                           
            string=" ( {} / {} ) ".format(a,b)
            stack.append(string)

    return stack.pop()
        





