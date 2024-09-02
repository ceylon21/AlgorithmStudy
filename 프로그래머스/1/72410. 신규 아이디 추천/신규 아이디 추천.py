import re
def solution(new_id):
    id = []
    answer = ''
    
    # step 1
    id = list(new_id.lower())
    
    # step 2
    for i in range(len(id)) : 
        q = ord(id[i])
        if (q < ord('a')) or (q > ord('z')) :
            if (q < ord('0')) or (q > ord('9')) :
                if (id[i] != "-") and (id[i] != "_") and (id[i] != ".") :
                    id[i] = ''
    
    id = ''.join(id)
    id = list(id)
    
    # step 3
    cnt = 0
    for i in range(len(id)) : 
        if id[i] == '.' : 
            cnt += 1
            if cnt > 1 : 
                id[i] = ''
        else : cnt = 0

    id = ''.join(id)
    id = list(id)
    
    # step 4
    if len(id) > 0 and id[0] == '.' : 
        id = id[1:]
    if len(id) > 0 and id[-1] == '.' :
        id = id[:-1]
    
    # step 5
    id = ''.join(id)
    if id == '' : id = 'a'
    
    # step 6
    if len(id) >= 16 : id = id[:15]
    if id[-1] == '.' :
        id = id[:-1]
    
    # step 7
    if len(id) <= 2 : 
        for i in range(3-len(id)) : 
            id += id[-1]
    
    return id