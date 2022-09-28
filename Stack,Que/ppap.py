"""
Case 1 
시간초과
"""
# import sys
# str= str(sys.stdin.readline().strip())
# while('PPAP' in str):
#     str = str.replace('PPAP','P')
# if str=='P':
#     print('PPAP')
# else:
#     print('NP') 

"""
Case2 
시간초과 
str으로 비교
"""
# import sys
# str= str(sys.stdin.readline().strip())

# new=''
# for i in str:
#     new+=i
#     if len(new)>=4 and new[-4:]=='PPAP':
#         new=new[:-3]
# if new=='P' or new=='':
#     print('PPAP')
# else:
#     print('NP') 

#------------------------------
import sys
str= str(sys.stdin.readline().strip())

new=[]
for i in str:
    new.append(i)
    if len(new)>=4 and new[-4:]==['P','P','A','P']:
        for j in range(3):
            new.pop()
        # new=new[:-3]
if new==['P'] :
    print('PPAP')
else:
    print('NP') 
    
#new=new[:-3] 보다 pop3번하는게 빠른가보네 배워 갑니다 