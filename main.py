import pickle
import random
import os
from icrawler.builtin import GoogleImageCrawler
from instagrapi import Client

import shutil
from PIL import Image

DIRECTORY = f"C:\\M\\Heck99!"

f=open('math_tags.pkl','rb')
math_tag = random.choice(pickle.load(f))
keyword = math_tag
print(math_tag)

f.close()



def save_photos(DIR,keyword,amount=10):
    
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': DIR})
    google_crawler.crawl(keyword=f'math meme + {keyword}', max_num=amount, file_idx_offset=0)


def png2jpg(DIR):
    '''
    converts images that are png or other styles to jpg
    '''

    for i in os.listdir(DIRECTORY):
        j=os.path.join(DIRECTORY,i)

        if i.split(".")[-1] != 'jpg':
            #print(i)

            new_name = "".join(i.split(".")[:-1])
            new_name = new_name + ".jpg"
            #print (new_name)
            im = Image.open(j)
            path=os.path.join(DIRECTORY,new_name)
            im.convert('RGB').save(path)
            del im
            os.remove(j)
            #print(path)

'''
def checker(DIR):
    #returns how many jpg images are there in a dir
    count = 0
    for i in os.listdir(DIR):
        if i.split(".")[-1] == 'jpg':
            count+=1 
    return count


save_photos(DIRECTORY,keyword,amount=10)
while checker(DIRECTORY) < 3:
    amount+=10
    save_photos(DIRECTORY,keyword,amount)
    
print(f"There are more than 3 : namely {checker(DIRECTORY)} jpg images")

'''
#cl = Client()
#cl.login("pi_lover314", "Pi=2580!")


save_photos(DIRECTORY,keyword,amount=5)

png2jpg(DIRECTORY)

posts=5

p = 0
for i in os.listdir(DIRECTORY):
    p+=1
    j=os.path.join(DIRECTORY,i)
    if p <=  posts:
        if i.split(".")[-1] == 'jpg':
            cl.photo_upload(j,f"#{math_tag}")
            print(f"photo no :{p} uploaded!")

shutil.rmtree(DIRECTORY, ignore_errors=True)
    

