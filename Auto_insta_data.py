from instagrapi import Client

user_id = cl.user_id_from_username("pi_lover314")


cl = Client()
cl.login(USERNAME,PASSWD)


user_id = cl.user_id_from_username("pi_lover314")
medias = cl.user_medias(user_id, 20)

 media = cl.photo_upload(
    "train.jpg",
    "Hello peeps",
)
