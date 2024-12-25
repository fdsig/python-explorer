# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 


scream = yell = shout 

print(scream('hello'))

print(f'id of scream: {id(scream)}')
print(f'id of yell: {id(yell)}')
print(f'id of shout: {id(shout)}')

print(f'hash of scream: {hash(scream)}')
print(f'hash of yell: {hash(yell)}')
print(f'hash of shout: {hash(shout)}')

print(f'bytes of scream: {scream.__code__.co_code}')
print(f'bytes of yell: {yell.__code__.co_code}')
print(f'bytes of shout: {shout.__code__.co_code}')

