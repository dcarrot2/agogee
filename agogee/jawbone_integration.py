import urllib
import json
import requests

def main():
    workout_url = 'https://jawbone.com/nudge/api/users/@me/moves'

    #authorization codes for 4 users
    header1 = {
        'Authorization': 'Bearer b6_3pfGGwEjLGQwKcc35Ru0-Al13wvvmkdMJNNjUQ0eHD4Ce7f5WhAmKfv_1EyUa8EvaJSumcI0GoYT-V9UbpVECdgRlo_GULMgGZS0EumxrKbZFiOmnmAPChBPDZ5JP'
    }

    header2 = {
        'Authorization': 'Bearer b6_3pfGGwEhQeA-iexyKuPFK59dIENPZkdMJNNjUQ0eHD4Ce7f5WhApDdojKJArz8EvaJSumcI0GoYT-V9UbpVECdgRlo_GULMgGZS0EumxrKbZFiOmnmAPChBPDZ5JP'
    }

    header3 = {
        'Authorization': 'Bearer b6_3pfGGwEhQeA-iexyKuDiwm81cuT3GkdMJNNjUQ0eHD4Ce7f5WhGqd6Uyz2SdX8EvaJSumcI0GoYT-V9UbpVECdgRlo_GULMgGZS0EumxrKbZFiOmnmAPChBPDZ5JP'
    }

    header4 = {
        'Authorization': 'Bearer b6_3pfGGwEiGq-jKynKSFO0-Al13wvvmkdMJNNjUQ0eHD4Ce7f5WhJpFxMafL32D8EvaJSumcI0GoYT-V9UbpVECdgRlo_GULMgGZS0EumxrKbZFiOmnmAPChBPDZ5JP'
    }

    #retrives all information for each usr
    user1 = requests.get(workout_url, headers = header1)
    user2 = requests.get(workout_url, headers = header2)
    user3 = requests.get(workout_url, headers = header3)
    user4 = requests.get(workout_url, headers = header4)

    #four users
    firstUser  = "Art"
    secondUser = "Katie"
    thirdUser  = "Daniel"
    fourthUser = "Rivka"

    # counts for active time
    userOneTime    =  get_active_minutes(user1)
    userTwoTime    =  get_active_minutes(user2)
    userThreeTime  =  get_active_minutes(user3)
    userFourTime   =  get_active_minutes(user4)

    #counts for calories burned
    userOneBurnedCalories     =  get_calories_burned(user1)
    userTwoBurnedCalories     =  get_calories_burned(user2)
    userThreeBurnedCalories   =  get_calories_burned(user3)
    userFourBurnedCalories    =  get_calories_burned(user4)

    #Get total points for active time and burned calories
    userOneTime    = int(userOneTime   / 60 + userOneBurnedCalories)
    userTwoTime    = int(userTwoTime   / 60 + userTwoBurnedCalories)
    userThreeTime  = int(userThreeTime / 60 + userThreeBurnedCalories)
    userFourTime   = int(userFourTime  / 60 + userFourBurnedCalories)

    #Create lists of array for each user
    listOfUsers = [userOneTime,userTwoTime,userThreeTime,userFourTime]
    rankUsers   = [firstUser,secondUser,thirdUser,fourthUser]

    #ranks the users
    bubble_sort(listOfUsers,rankUsers)

    #prints the ranking
    #print "Time in order(minutes) and calories burned"    
    #print listOfUsers

    #print "Ranking for users"
    #print rankUsers

def get_active_minutes(user):
    temp_min = 0
    for x in range(0,user.json()['data']['size']):
        temp_min += user.json()['data']['items'][x]['details']['active_time']
        #print 'Day ' + str(x + 1) + ' ' + str(user.json()['data']['items'][x]['details']['active_time']  / 60) + ' active minutes'

    #print
    #print('Total time: ' + str(temp_min / 60) + ' minutes')
    #print

    return temp_min / 60

def get_calories_burned(user):
    temp_cal = 0
    for x in range(0,user.json()['data']['size']):
           temp_cal += user.json()['data']['items'][x]['details']['calories']
           #print 'Day ' + str(x + 1) + ' calories burned: ' + str(user.json()['data']['items'][x]['details']['calories'])

    #print
    #print('Total calories burned ' + str(int(temp_cal)))
    #print

    return temp_cal
    
def bubble_sort(listOfUsers,rankUsers):
    # Sort the sequence from greatest to least
    for i in reversed(range(len(listOfUsers))):
        finished = True
        for j in range(i):
            if listOfUsers[j] < listOfUsers[j + 1]:
                listOfUsers[j], listOfUsers[j + 1] = listOfUsers[j + 1], listOfUsers[j]
                rankUsers[j], rankUsers[j + 1] = rankUsers[j + 1], rankUsers[j]
                finished = False
        if finished:
            break

main()
