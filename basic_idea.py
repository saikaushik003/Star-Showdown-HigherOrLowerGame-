import pandas as pd
from collections import defaultdict
import random
from PIL import Image
import urllib.request
from io import BytesIO 

insta_followers = pd.read_csv('insta.csv')
actor_names = insta_followers['actor_name'].tolist()
actors_data = defaultdict(list)
for actor, img, foll in zip(actor_names, insta_followers['image_link'].tolist(), insta_followers['followers'].tolist()):
    if foll[-1] == 'M':
        foll_i = float(foll[:-1]) * 1000000
        actors_data[actor] = [img, foll_i, foll]
    elif foll[-1] == 'K':
        foll_i = float(foll[:-1]) * 1000
        actors_data[actor] = [img, foll_i, foll]

actor1 = random.choice(list(actors_data))
a1_img = actors_data[actor1][0]
a1_foll_i = actors_data[actor1][1]
a1_foll = actors_data[actor1][2]
del actors_data[actor1]

res = True
score = 0
while res and actors_data:
    actor2 = random.choice(list(actors_data))
    a2_img = actors_data[actor2][0]
    a2_foll_i = actors_data[actor2][1]
    a2_foll = actors_data[actor2][2]
    print(actor1 +" vs "+ actor2)

    url = a1_img
    with urllib.request.urlopen(url) as url:
        img1 = Image.open(BytesIO(url.read()))

    url = a2_img
    with urllib.request.urlopen(url) as url:
        img2 = Image.open(BytesIO(url.read()))

    
    display(img1, img2)
    
    print(a1_foll + " vs " + "???")
    user_input = input()
    if user_input == "higher":
        if a2_foll_i < a1_foll_i:
            print(a2_foll)
            res = False
        else:
            score += 1
            print("Score: ", score)
    elif user_input == 'lower':
        if a2_foll_i > a1_foll_i:
            print(a2_foll)
            res = False
        else:
            score += 1
            print("Score: ", score)
    actor1 = actor2
    a1_img = a2_img
    a1_foll_i = a2_foll_i
    a1_foll = a2_foll
    del actors_data[actor2]
print("Final Score:", score)
