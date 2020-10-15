
import math
#funkcija koja izračunava ekuklidsku udaljenost svakog parametra za svaku lokaciju
def euclidDistance(userProfile, locations, locationName):
    
    userBusiness = userProfile['Business']
    userFamily = userProfile['Family']
    userAdventure = userProfile['Adventure']
    userCasual = userProfile['Casual']
    
    locationBusiness = locations[locationName]['Business']
    locationFamily = locations[locationName]['Family']
    locationAdventure = locations[locationName]['Adventure']
    locationCasual = locations[locationName]['Casual']
    
    euclid = (userBusiness - locationBusiness) ** 2 + (userFamily - locationFamily) ** 2 + (userAdventure - locationAdventure) ** 2 + (userCasual - locationCasual) ** 2
    
    euclid = math.sqrt(euclid)
    
    return euclid


print ("In the next 5 questions, enter the number in front of the option that answers it the best")

#dictionary sa tipovima koji će se koristit kasnije
tripTypes = {1 : 'Business',
         2 : 'Family',
         3 : 'Adventure',
         4 : 'Casual'}

answer1 = int(input("During the last 5 years, Your trips were mostly done as: 1: Business trips, 2: Family trips, 3: Adventures with friends, 4: Relaxing vacations "))

answer2 = int(input("When You choose to eat outside, what do you take into consideration when choosing the place? 1: Ratings, 2: Is it Family friendly, 3: I like to try out new places, 4: Cozy and quiet "))

answer3 = int(input("When sightseeing, what places do You like to visit?  1: Areas with hustle and bustle, shopping malls etc, 2: ZOOs, Amusement parks and etc., 3: Areas with lots of activities, adrenaline parks, 4: I like to take it slow, see some landmarks, learn about history and etc. "))

answer4 = int(input("How do You choose to traverse around your destination 1: Rent a car, 2: We bring our own transportation, 3: Public transport or rent a bicycle, 4: Just take it slow and walk everywhere "))

answer5 = int(input("What brings You to Osijek? 1: Business, 2: Family vacation, 3: Trip with friends/Erasmus, 4: Friend recommendation for relaxing vacation "))

answers = [answer1, answer2, answer3, answer4]


#zapisivanje prva 4 odgovora u listu
answerTypes = []
for i in answers:
    for key in tripTypes:
        if (i==key):
            answerTypes.append(tripTypes[key])
            break




userProfile = {'Business' : 0,
               'Family' : 0,
               'Adventure' : 0,
               'Casual' : 0}


#stvaranje user profila
for i in answerTypes:
    for key in userProfile:
        if (i==key):
            userProfile[key] = userProfile[key] + 25
            break


#overridanje jednog parametra user profila ovisno o dogovoru 5, 
#odnosno ovisno o razlogu puta, jer se može dogodit da iako je korisnik inače casual na putovanjima
#u ovom slučaju razlog putovanja može biti poslovni 
if (answer5 == 1):
    userProfile['Business'] = 100
    
elif (answer5 == 2):
    userProfile['Family'] = 100
    
elif (answer5 == 3):
    userProfile['Adventure'] = 100
    
elif (answer5 == 4):
    userProfile['Casual'] = 100
    

#popis lokacija
locations = {'ZOO Osijek' : {'Business' : 0,
                   'Family' : 94,
                   'Adventure' : 37,
                   'Casual' : 15},
             'Citadel - Old town Tvrđa' : {'Business' : 5,
                          'Family' : 35,
                          'Adventure' : 15,
                          'Casual' : 50},
             'Restaurant Zimska Luka' : {'Business' : 80,
                              'Family' : 40,
                              'Adventure' : 20,
                              'Casual' : 30},
             'Movie Theater Urania' : {'Business' : 0,
                                       'Family' : 70,
                                       'Adventure' : 10,
                                       'Casual' : 80},
             'European Avenue Secession Row' : {'Business' : 0,
                                                'Family' : 15,
                                                'Adventure' : 30,
                                                'Casual' : 70},
             'Kopika Beach' : {'Business' : 0,
                               'Family' : 87,
                               'Adventure' : 70,
                               'Casual' : 80},
             'Mlin - Watermill on Drava' : {'Business' : 0,
                                            'Family' : 86,
                                            'Adventure' : 45,
                                            'Casual' : 94},
             'Main Square - Ante Starčević' : {'Business' : 60,
                                               'Family' : 35,
                                               'Adventure' : 20,
                                               'Casual' : 70},
             'Promenade' : {'Business' : 5,
                            'Family' : 67,
                            'Adventure' : 80,
                            'Casual' : 100},
             'Park of King Tomislav' : {'Business' : 0,
                                        'Family' : 50,
                                        'Adventure' : 90,
                                        'Casual' : 77},
             'St. Peter and St. Paul Co-cathedral' : {'Business' : 0,
                               'Family' : 40,
                               'Adventure' : 5,
                               'Casual' : 60},
             'Chapel of the Stoney Cross' : {'Business' : 15,
                                             'Family' : 30,
                                             'Adventure' : 40,
                                             'Casual' : 70},
             'Red Fićo' : {'Business' : 0,
                           'Family' : 46,
                           'Adventure' : 55,
                           'Casual' : 96},
             'HNK - Theater' : {'Business' : 60,
                                'Family' : 30,
                                'Adventure' : 0,
                                'Casual' : 70},
             'Kopački rit' : {'Business' : 20,
                              'Family' : 100,
                              'Adventure' : 100,
                              'Casual' : 70},
             'Gallery of Fine Arts' : {'Business' : 70,
                                       'Family' : 0,
                                       'Adventure' : 0,
                                       'Casual' : 40},
             'Museum of Slavonia' : {'Business' : 40,
                                     'Family' : 40,
                                     'Adventure' : 20,
                                     'Casual' : 87},
             'Principovac - Ilok' : {'Business' : 80,
                                     'Family' : 45,
                                     'Adventure' : 60,
                                     'Casual' : 50},
             'Erdut Winery' : {'Business' : 76,
                               'Family' : 36,
                               'Adventure' : 65,
                               'Casual' : 50},
             'Ethno Village Karanac' : {'Business' : 16,
                                        'Family' : 100,
                                        'Adventure' : 100,
                                        'Casual' : 56}}

locationsEuclid = {}

locationList = []


#određivanje euklidske udaljenosti za svaku lokaciju u odnosu na parametre user profila, te zatim zapisivanje gdje je key broj, a value lokacija
for key in locations:
    rating = euclidDistance(userProfile, locations, key)
    locationsEuclid[rating] = key
#uzlazno sortiranje samo lokacija u listu 
for key in sorted (locationsEuclid):
    locationList.append(locationsEuclid[key])
    
    
print ("For Your visit to Osijek we suggest You visit these locations: ", locationList[:5])