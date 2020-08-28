'''The functions in this module will calculate the meso cost given
the number of stars and the level of the equip. The functions in this
module only calculate the meso cost for one try and does not calculate
the average cost to reach a certain star.'''

def mesoCostKMS(star, level, safeguard=0):
    '''This function calculates the meso cost for starforcing
        using the formula for Korean Maplestory.'''

    #formulas are found online on strategywiki.org
    if star < 10:
        cost = 1000 + ((level ** 3) * ((star + 1) / 25))
        return cost

    elif star > 9 and star < 15:
        cost = 1000 + ((level ** 3) * (((star + 1) ** 2.7) / 400))
        
        if star == 12 or 13 or 14 and safeguard == 1:
            cost = 2 * cost
            return cost
        
        else:
            return cost

    elif star > 14 and star < 25:
        cost = 1000 + ((level ** 3) * (((star + 1) ** 2.7) / 200))
        
        if star == 15 or 16 and safeguard == 1:
            cost = 2 * cost
            return cost
        
        else:
            return cost

def mesoCostGMS(star, level, safeguard=0):
    '''This function calculates meso cost using the Global Maplestory
        formula.'''
    
    #different formulas are used based on the current starforce level
    if star < 10:
        cost = 1000 + ((level ** 3) * ((star + 1) / 25))
        return cost

    elif star > 9 and star < 15:
        cost = 1000 + ((level ** 3) * (((star + 1) ** 2.7) / 400))
        
        if star == 12 or star == 13 or star == 14 and safeguard == 1:
            cost = 2 * cost
            return cost
        
        else:
            return cost

    elif star > 14 and star < 18:
        cost = 1000 + ((level ** 3) * (((star + 1) ** 2.7) / 120))
        
        if star == 15 or star == 16 and safeguard == 1:
            cost = 2 * cost
            return cost
        
        else:
            return cost

    elif star > 17 and star < 20:
        cost = 1000 + ((level ** 3) * (((star + 1) ** 2.7) / 110))
        return cost

    elif star > 19 and star < 25:
        cost = 1000 + ((level ** 3) * (((star + 1) ** 2.7) / 100))
        return cost

if __name__ == '__main__':

    print(mesoCostKMS(20, 150, 0))
        
