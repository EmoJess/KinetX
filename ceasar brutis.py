def last13(memes):
    return (((ord(memes)+12)%122)+96)
def first13(uber):
    return chr(ord(uber)+12)
def whyudodis(cruel):
    why=['n','o','p','q','r','s','t','u','v','w','x','y','z']
    if(cruel in why):
        return True
def ceasar(PT):
    if(whyudodis(PT)):
        return chr(((ord(PT)+12)%122)+96)
    else:
        return first13(PT)
