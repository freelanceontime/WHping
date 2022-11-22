import requests
from bs4 import BeautifulSoup
import time
import json

# take second element for sort
system = 'A-SJ8X'
jumpswithin = 15
webhookchannelurl = ""

def thera():
    url = "http://www.eve-scout.com/api/wormholes?systemSearch=" + system

    page = requests.get(url)
    result = page.json()

    systems = (len(result))

    regions = []
    solarsystems = []
    jumps = []

    for i in range(systems):
        if result[i]['jumps'] == 0:
            continue
        else:
            regions.append(result[i]['destinationSolarSystem']['region']['name'])
            solarsystems.append(result[i]['destinationSolarSystem']['name'])
            jumps.append(result[i]['jumps'])

    # print(regions)
    # print(solarsystems)
    # print(jumps)

    jumpsandsys = dict(zip(jumps, zip(solarsystems, regions))) #Create a dictionary
    #print(jumpsandsys.items())
    jumpsandsys = sorted(jumpsandsys.items(), key=lambda item: item[0]) # Sort the dictionary by prices
    #print(jumpsandsys)

    url3 = "http://www.eve-scout.com/api/wormholes?systemSearch=Jita"

    page3 = requests.get(url3)
    result3 = page3.json()

    systems3 = (len(result3))

    regions3 = [] 
    solarsystems3 = []
    jumps3 = []

    for i in range(systems3):
        if result[i]['jumps'] == 0:
            continue
        else:
            regions3.append(result3[i]['destinationSolarSystem']['region']['name'])
            solarsystems3.append(result3[i]['destinationSolarSystem']['name'])
            jumps3.append(result3[i]['jumps'])


    jumpsandsys3 = dict(zip(jumps3, zip(solarsystems3, regions3))) #Create a dictionary
    jumpsandsys3 = sorted(jumpsandsys3.items(), key=lambda item: item[0]) # Sort the dictionary by prices

    #print(jumpsandsys3) 

    systemtest = jumpsandsys3[0][1]
    first_value = jumpsandsys3[0][0]  
    second_value = systemtest[0]
    third_value = systemtest[1]

    # print('Jumps:', jumpsandsys3[0][0])
    # print('System: ', systemtest[0])
    # print('Region' , systemtest[1])

    time.sleep(200)

    url2 = "http://www.eve-scout.com/api/wormholes?systemSearch=" + system

    page2 = requests.get(url2)
    result2 = page2.json()

    systems2 = (len(result2))

    regions2 = []
    solarsystems2 = []
    jumps2 = []

    for i in range(systems2):
        if result2[i]['jumps'] == 0:
            continue
        else:
            regions2.append(result2[i]['destinationSolarSystem']['region']['name'])
            solarsystems2.append(result2[i]['destinationSolarSystem']['name'])
            jumps2.append(result2[i]['jumps'])


    jumpsandsys2 = dict(zip(jumps2, zip(solarsystems2, regions2))) #Create a dictionary
    #print(jumpsandsys2.items())
    jumpsandsys2 = sorted(jumpsandsys2.items(), key=lambda item: item[0]) # Sort the dictionary by jumps
    #print(jumpsandsys2)

    compare1set = dict(jumpsandsys)
    compare2set = dict(jumpsandsys2)

    compare1 = compare1set.items()
    compare2 = compare2set.items()

    # print(compare1)
    # print(compare2)

    diff = compare2 - compare1

    s = [money for (money,(id, test)) in diff if money < 68]
    t = [id for (money,(id, test)) in diff if money < 68]
    j = [test for (money,(id, test)) in diff if money < 68]

    #print(diff)

    try:
        if diff != set():
            if int(s[0]) < jumpswithin:
                from discord import SyncWebhook
                webhook = SyncWebhook.from_url(webhookchannelurl)    
                webhook.send("Thera Connection in System " + str(t) + " in region " + str(j) + " ," + str(s) + " Jumps from [" + system + "],\nThe closest connection to Jita is ['" + str(second_value) + "'] in region ['" + str(third_value) + "'], [" + str(first_value) + "] Jumps from Thera")
                            
            else:
                print(str(t) + " in " + str(j) + " is not less than [" + str(jumpswithin) + "] jumps it is " + str(s))
    except IndexError:
        print("Failure")

while True:
    try:
        thera()
    except:
        print("error")
        pass
