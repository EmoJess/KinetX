def isvowel(stuff):
     v=['a','e','i','o','u']
     if(stuff in v):
         return True
        
def iscon(jebus):
    c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    if(jebus[0] and jebus[1] in c):
        return True



def pigg(pig):
     end='ay'
     if(isvowel(pig[0])):
         return pig + "way"
     if(isvowel(pig[1])):
         pig=pig[1:]+pig[0]+'ay'
         return pig
     if(iscon(pig)):
         pig=pig[2:]+pig[:2]+'ay'
         return pig
    # print pig
   #  if(
     #   
    #    print pig

print pigg('cream')
print pigg('cone')

