import requests
import pandas as pd

file = pd.read_csv("Ratings.csv")
contestants_IITRPR = [i.lower() for i in file['Codeforces Username']]
month = input("Month: ")
monthStartContestId = int(input("Month's starting contest ID: "))
ratings = []

base = 'https://codeforces.com/api/user.rating?handle='

for i, contestent in enumerate(contestants_IITRPR):
    URL = base + contestent.strip()
    monthMaxRating = 0
    otherMaxRating = 0
    data = requests.get(url=URL, timeout=60).json()
    if data['status'] == 'OK': 
        data = data['result']
        monthRatings = []
        otherRatings = []
        for contest in data:
            if contest['contestId'] >= monthStartContestId:
                monthRatings.append(contest['newRating'])
            else:
                otherRatings.append(contest['newRating'])
        if len(monthRatings):
            monthMaxRating = max(monthRatings)
        if len(otherRatings):
            otherMaxRating = max(otherRatings)
    ratings.append(monthMaxRating - otherMaxRating)
    print(contestent, monthMaxRating - otherMaxRating)
    
file[month] = ratings
file.to_csv('Ratings.csv')