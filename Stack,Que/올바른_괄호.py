# def solution(s):
#     if s[0]==")" or s[-1]=="(" or len(s)%2!=0 :
#         return False
#     else:
#         while(len(s)>2):
#             s=s.replace("()","")
#         if s=="()" or s =="":
#             return True 
#         else:
#             return False

# def solution(s):
#     while (s[0]!=")" and s[-1]!="(" and len(s)%2==0):
#         s=s.replace("()","")
#         if s=="":
#             return True
#     return False

s="(())()"	
list=[]
def solution(s):
    for i in s:
       if i=="(":
           list.append(i)
       else:
           if list==[]:
               return False
           else:
               list.pop()
    return print(list==[])
           
        
    
    
solution(s)