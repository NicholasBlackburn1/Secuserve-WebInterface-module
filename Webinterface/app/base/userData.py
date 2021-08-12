"""
class should turn list into Array to be looped trhough
for flask
"""



def turnListToArray(face,num):
    user = []
    image = []
    i = 0
    
    while i > int(num):
        user.append(face[i].user)
        image.append(face[i].image)
        i+=1
        
    return user,image
    
    