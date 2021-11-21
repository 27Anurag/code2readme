from csv import reader
# open file in read mode
import io
# import requests
import time
from git import Repo
import signal
from threading import Thread
import functools

#github token 
#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

# Path 
# D:\Sem 5\Natural language processing\code2readme\code2readme_data



def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print ('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco


@timeout(10)
def clone(git_url, repo_dir):
    print("cloning repo --> {}".format(repo_name))
    Repo.clone_from(git_url, repo_dir)
    print("cloned")



LIMIT=0
can_download=0
curr = 30000

memo = open("bigdadmemo.txt","a+")


with open('bigdad.csv', 'r', encoding="utf8") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)

    # Iterate over each row in the csv using reader object
    for row in csv_reader:

        LIMIT+=1
        if(LIMIT==50000):
            print("TASK COMPLETED")
            break
        if(LIMIT <= curr):
            continue

        # row variable is a list that represents a row in csv
        # print(row[3])
        repo_name = row[0]
        readme_flag = row[2]



        if(readme_flag != "README.md"):
            continue


            

        # print(readme_flag)
        # print(repo_name)

        #good repo_url --> 
        #https://api.github.com/repos/M-Media-Group/Cartes.io/languages

        repo_url = "https://api.github.com/repos/" + repo_name + "/languages"

        readme = "https://api.github.com/repos/" + repo_name + "/contents/README.md"
        
        repo_dir = "D:/Sem 5/Natural language processing/code2readme/code2readme_data/data/{}".format(LIMIT)
        # repo_dir = "/home/19110207/bigdad_data/{}".format(LIMIT)
        

        git_url = "https://github.com/" + repo_name + ".git"
        # print(git_url)


        # repo_url = "https://api.github.com/repos/00ec454/Ask/languages"
        # flag = 0

        with open('bigdadmemo.txt', 'r') as f:
            for line in f:
                if(line == git_url):
                    print("skipping ...")
                    continue


        try:
            clone(git_url, repo_dir)
            memo.write(git_url + "\n")
        except :
            print("Download failed")
            pass



        can_download+=1
        

        # print("DOWNLOADED {} repos".format(can_download))




       

