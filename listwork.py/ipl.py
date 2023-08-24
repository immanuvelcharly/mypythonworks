users=("sachin","kohli","seheag","rahul","dhoni","raina")
sachin_followers=("kohli","sehwag","rahul")
suggetion=[]

for user in users:
    if user !="sachin"and user not in sachin_followers:
        suggetion.append(user)
        print("friend request suggetion for sachin")
        for request in suggetion:
            print(request)
        