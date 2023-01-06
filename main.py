import json


with open('followers.json') as f:
    with open('following.json') as fo:
        with open('pending_follow_requests.json') as pfr:
            followers_file = json.load(f)
            following_file = json.load(fo)
            pending_requests_file = json.load(pfr)


people_not_following_back = []
followers = []
following = []
pending_requests = []


for follower in followers_file['relationships_followers']:
    username = follower['string_list_data'][0]['value']

    followers.append(username)

for follower in following_file['relationships_following']:
    username = follower['string_list_data'][0]['value']

    following.append(username)

for follower in pending_requests_file['relationships_follow_requests_sent']:
    username = follower['string_list_data'][0]['value']

    pending_requests.append(username)

for follower in following:
    if follower not in followers:
        people_not_following_back.append(follower)


def display(arr):
    for follower in arr:
        print('username :', follower, '||  instgram_url :',
              'https://www.instagram.com/'+follower)


while True:
    print('''
1 - followers 
2 - following
3 - people that do not follow you back
4 - pending requests
    ''')

    choice = ''
    try:
        choice = int(input('Enter 1,2,3,4 or 5 for quitting : '))
    except ValueError:
        print("==> please make sure to enter a number ")
        continue
    if choice == 1:
        print('==> You have', len(followers), 'followers')
        print()
        display(followers)
    elif choice == 2:
        print('==> You are following', len(following), 'people')
        print()
        display(following)
    elif choice == 3:
        print('==> People that do not follow you back are',
              len(people_not_following_back))
        print()
        display(people_not_following_back)
    elif choice == 4:
        print('==> Pending requests are ', len(pending_requests))
        print()
        display(pending_requests)
    elif choice == 5:
        print('==> exiting..')
        break
    else:
        print('==> Invalid')
