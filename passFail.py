'''This module will contain the functions that handle success and fail rates
when starforcing. It will change the star level accordingly depending on
pass, fail, or destruction.'''

import random
import sys
import mesoCost as meso


sys.setrecursionlimit(10 ** 6)

def randomNumbers():
    '''This function simulates a random number generator which will be
        used to determine if an instance of starforcing passes, fails,
        or booms.'''
    #generating a number between 1 through 1000 because the rates of
    #starforcing have decimals, so increasing the range makes it easier
    #to work with
    value = random.randint(1, 1000)

    return value

def Pass(starLevel):
    '''This function raises the starforce level by 1 if executed.'''
    level = starLevel
    #passing increases starforce level by 1
    level += 1
    return level, 0

def fail(starLevel, failCount):
    '''This function simulates failing the starforcing by either
        staying the same level or dropping 1 star based on the
        number of stars'''
    
    level = starLevel
    if level < 11 or level == 15 or level == 20:
        level = level
        failCount = 0
        return level, failCount

    else:
        level = level - 1
        failCount += 1
        return level, failCount

def boom():
    #booming an equip brings it back to 12 stars
    return 12, 0

def simulate(starLevel, failCount):
    '''This function simulates a single starforce attempt at a given star.
        As starforce level increases, success rate decreases and fail/boom
        chance increases.'''
    
    level = starLevel

    if failCount == 2 and level > 10:
        return Pass(level)
        
    elif level < 3:
        failChance = 50 + 50 * level
        success = 1000 - failChance
        value = randomNumbers()
        if value < failChance + 1:
            return fail(level, failCount)

        elif value > failChance:
            return Pass(level)

    elif level == 3:
        value = randomNumbers()
        if value < 151:
            return fail(level, failCount)
        elif value > 150:
            return Pass(level)

    elif level < 12 and level > 3:
        failChance = 50 * level
        success = 1000 - failChance
        value = randomNumbers()
        if value < failChance + 1:
            return fail(level, failCount)

        elif value > failChance:
            return Pass(level)

    elif level == 12:
        #boomChance = 0.6%
        #failChance is 59.4%
        #success is 40%
        value = randomNumbers()

        if value < 7:
            return boom()

        elif value > 6 and value < 601:
            return fail(level, failCount)

        elif value > 600:
            return Pass(level)

    elif level == 13:
        #boomChance is 1.3%
        #failChance is 63.7%
        #success = 35%
        value = randomNumbers()

        if value < 14:
            return boom()

        elif value > 13 and value < 651:
            return fail(level, failCount)

        elif value > 650:
            return Pass(level)

    elif level == 14:
        #boomChance is 1.4%
        #failChance is 68.6%
        #success is 30%
        value = randomNumbers()

        if value < 15:
            return boom()

        elif value > 14 and value < 701:
            return fail(level, failCount)

        elif value > 700:
            return Pass(level)

    elif level == 15 or level == 16 or level == 17:
        #boomChance is 2.1%
        #failChance is 67.9%
        #success is 30%
        value = randomNumbers()

        if value < 22:
            return boom()

        elif value > 21 and value < 701:
            return fail(level, failCount)

        elif value > 700:
            return Pass(level)

    elif level == 18 or level == 19:
        #boomChance is 2.8%
        #failChance is 67.2%
        #success is 30%
        value = randomNumbers()

        if value < 29:
            return boom()

        elif value > 28 and value < 701:
            return fail(level, failCount)

        elif value > 700:
            return Pass(level)

    elif level == 20 or level == 21:
        #boomChance is 7%
        #failChance is 63%
        #success is 30%
        value = randomNumbers()

        if value < 71:
            return boom()

        elif value > 70 and value < 701:
            return fail(level, failCount)

        elif value > 700:
            return Pass(level)

    #-------------------------------------------------------------#
    #starforcing past 22 stars is not realistic because of how unlikely
    #it is. The lines of code below are only for theoretical purposes.

    elif level == 22:
        #boomChance is 19.4%
        #failChance is 77.6%
        #success is 3%
        value = randomNumbers()

        if value < 195:
            return boom()

        elif value > 194 and value < 971:
            return fail(level, failCount)

        elif value > 970:
            return Pass(level)

    elif level == 23:
        #boomChance is 29.4%
        #failChance is 68.6%
        #success = 2%
        value = randomNumbers()

        if value < 295:
            return boom()

        elif value > 294 and value < 981:
            return fail(level, failCount)

        elif value > 980:
            return Pass(level)

    elif level == 24:
        #boomChance is 39.6%
        #failChance is 59.4%
        #success is 1%
        value = randomNumbers()
        if value < 397:
            return boom()

        elif value > 396 and value < 991:
            return fail(level, failCount)

        elif value > 990:
           return Pass(level)

def experimentalTrial(start, end, server, safeguard, equipLevel,
                      failCount=0, cost=0):
    '''This function simulates a trial of starforcing from start to finish.
        It will count how many mesos it takes to achieve the end result.'''
    level = start
    last = end
    mesoCost = cost
    if start == last:
        return int(mesoCost)

    else:
        updatedLevel = simulate(level, failCount)
        if server == 'GMS':
            mesoCost = mesoCost + meso.mesoCostGMS(level, equipLevel, safeguard)
            return experimentalTrial(updatedLevel[0], last, server,
                              safeguard, equipLevel, updatedLevel[1], mesoCost)

        elif server == 'KMS':
            mesoCost = mesoCost + meso.mesoCostKMS(level, equipLevel, safeguard)
            return experimentalTrial(updatedLevel[0], last, server,
                              safeguard, equipLevel, updatedLevel[1], mesoCost)

def manyTrials(start, end, server, safeguard, equipLevel, trials, cost=0):
    '''This function will conduct many trials to find the average amount
        of mesos to get to the desired starforce level.'''

    count = 0
    mesoList = []
    while count != trials:
        trialCost = experimentalTrial(start, end, server,
                                      safeguard, equipLevel, cost=0)
        
        mesoList.append(trialCost)

        count += 1

    print('The expected meso cost is: {:,}'.format(sum(mesoList) / trials))

    print('Range of meso cost: {:,} - {:,}'.format(min(mesoList), max(mesoList)))

    
#if __name__ == '__main__':



    
