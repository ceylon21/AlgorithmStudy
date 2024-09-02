# 굳이 list로 구성하지 않아도 된단 생각이 들었다
# step2에서 not in 사용, step3에서 while문 사용 등등 다시 풀어보기
import re 
def solution(new_id):
    id = []
    answer = ''
    
    # step 1
    id = list(new_id.lower())
    
    # step 2
    # re 라이브러리를 사용했다가 실전에서는 사용하기 어려울 것 같다 생각
    # 가독성을 위해 중첩 조건문으로 작성 - 연산자 주의하기 ! 
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