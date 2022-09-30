def message2Command(ctx):
    cmd_str=''
    cmd=[]
    s=[]
    while(len(ctx) > 0):
        if(ctx[0]==' '):
            if(cmd_str != ''):
                cmd.append(cmd_str.lower())
            cmd_str=''
            ctx=ctx[1:]
        elif(ctx[0]=='"'):
            ctx=ctx[1:]
            s_str=''
            while(ctx[0]!='"'):
                s_str+=ctx[0]
                ctx=ctx[1:]
            ctx=ctx[1:]
            s.append(s_str)
        else:
            cmd_str+=ctx[0]
            ctx=ctx[1:]
    if(cmd_str!=''):
        cmd.append(cmd_str)
    return {'command':cmd,'string':s}

def String2Second(Str):
    if((Str.find('d') and Str.find('h') and Str.find('m') and Str.find('s')) != -1):
        s=int(time.time())
        def NumBeforeChar(Str):
            print(Str)
            l=len(Str)
            for i in range(l,0,-1):
                if(not Str[i-2:l-1].isdigit()):
                    break
            return int(Str[i-1:l-1])
        if(Str.find('d') != -1):
            s+=NumBeforeChar(Str[:Str.find('d')+1])*60*60*24
            print(s)
        if(Str.find('h') != -1):
            s+=NumBeforeChar(Str[:Str.find('h')+1])*60*60
            print(s)
        if(Str.find('m') != -1):
            s+=NumBeforeChar(Str[:Str.find('m')+1])*60
            print(s)
        if(Str.find('s') != -1):
            s+=NumBeforeChar(Str[:Str.find('s')+1])
            print(s)
        return s
    elif(Str.count('.') == 2):
        return int( time.mktime(time.strptime(s2,"%Y.%m.%d")) )
    elif(Str.count('.') == 4):
        return int( time.mktime(time.strptime(s3,"%Y.%m.%d.%H.%M")) )