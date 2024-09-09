from random import randrange

shorts = ["Cargos", "Shorts"]
pants = ["Sweats","Khakis", "Jeans"]
light = ["Flannel", "Jacket"]
heavy = ["Hoodie", "Sweater"]

colorKey = {
    "Shirt": ["Blue", "Black", "Green", "Purple","Gray", "White", "Brown","Orange"],
    "Cargos": ["Black", "Gray", "Khaki"],
    "Shorts":["Black", "Blue", "Gray"],
    "Sweats": ["Black","Gray"],
    "Khakis":["Khaki"],
    "Jeans":["Blue","Black"],
    "Flannel": ["Blue","Green","Gray", "Red", "Blue/Red"],
    "Jacket": ["Green"],
    "Hoodie": ["Blue", "Black", "Green", "Purple","Gray", "White", "Brown"],
    "Sweater": ["Light Gray", "Dark Gray"],
    "Shoes":["Black", "White"]
}

tee_weather = 60
shorts_weather = 50
sweater_weather = 43

layer1 = 0
layer2 = 1
layer3 = 2
layer4 = 3



def colorScheme(fit):
    outfit = ""
    for x in fit:
        color = randrange(0,len(colorKey[x]))
        outfit += colorKey[x][color] + " " + x + "\n "
    return outfit 

def layers(temp):
    fit = []
    
    fit.insert(layer2,"Shirt")
    
    if(temp < shorts_weather):
        pantType = randrange(0,len(pants))
        fit.insert(layer1,pants[pantType])
        heavyType = randrange(0,len(heavy))
        fit.insert(layer3,heavy[heavyType])
    else:
        shortType = randrange(0,len(shorts))
        fit.insert(layer1,shorts[shortType])
        #pick shirt
    if((temp < tee_weather and temp > shorts_weather) or temp < sweater_weather):
        lightType = randrange(0,len(light))
        fit.insert(layer4,light[lightType])
        #pick a light jacket

    return colorScheme(fit)
        
            

