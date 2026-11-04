class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      S =[]
      for token in tokens:
           operator=['+','-','*','/']
           if token not in operator:
                 S.append(int(token))
           else:
               b=S.pop()
               a=S.pop()
               if token =='+':
                   S.append(a+b)
               elif token =='-':
                    S.append(a-b)
               elif token =='*':
                    S.append(a*b)
               elif token =='/':
                    S.append(int(a/b))
      return S[-1]                     

            

        
                       
                  
    
