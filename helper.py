##
#   Project: shoeBot
#   Filename: helper.py
#   Author: Daniel Takyi
#   Purpose:
##

#
def organizeShoes(one, two, three, rack):
    i = 0
    checklist = []
    foundShoes = []
    for shoeBox in rack:
        shoe = shoeBox.text.strip()
        if one in shoe:
            print(shoe)
            checklist.append(1)
            foundShoes.append(shoe)
        elif two in shoe:
            print(shoe)
            checklist.append(1)
            foundShoes.append(shoe)
        elif three in shoe:
            print(shoe)
            checklist.append(1)
            foundShoes.append(shoe)
        else:
            checklist.append(0)
        i += 1
    
    return checklist, foundShoes
    
#
def organizePrices(checklist, priceList):
    i = 0
#    j = 0
    foundPrices = []
    for shoePrice in priceList:
        if checklist[i] == 1:
            price = shoePrice.text.strip()
            print(price)
            foundPrices.append(price)
        i += 1
    
    return foundPrices

#
def conjoin(foundShoes, foundPrices):
    catalogue = []
    i = 0
    for i in range(len(foundShoes)):
        catalogue.append(tuple((foundShoes[i], foundPrices[i])))
    print(catalogue)
    return catalogue

#
def checkForUpdate(pages, catalogue):
    i = 0
    for page in pages:
        for record in page:
            if catalogue[i][0] in str(record['fields']):
                print(record['fields'])
            else:
                #alert me and rewrite database
                ##alert()
                ##rewrite()
                break
            i += 1

