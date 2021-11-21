import glob
import os
flag=0
#print(glob.glob("/home/19110207/code2readme_data//*.py"))
import csv
import pandas as pd
from tqdm import trange
import pickle

l=''
k=''
n=0
code_len, readme_len = 0,0

py=0
cpp=0
c=0
java=0
cs=0
js=0


df = pd.DataFrame(columns =["ENG","FR"])

with open('D:/Sem 5/Natural language processing/code2readme/code2readme_data/dump.tsv', 'wt') as out_file:
  tsv_writer = csv.writer(out_file, delimiter='\t')

  for i in trange(20000):
    # print("file no --> ", i)

    
    path = os.walk("D:/Sem 5/Natural language processing/code2readme/code2readme_data/data/{}".format(i+1))

    for root, directories, files in path:

      for file in files:
        # print(file)
        
        if(".py" in file):
          py += 1
        elif (".cpp" in file):
          cpp += 1
        elif (".c" in file):
          c += 1
        elif (".java" in file):
          java += 1
        elif (".js" in file):
          js += 1

total = py+cpp+c+java+js


print("py --> ",py*100/total)
print("cpp --> ",cpp*100/total)
print("c --> ",c*100/total)
print("java --> ",java*100/total)
print("js --> ",js*100/total)







     









         # print("python")
        # if (".py" in file) or (".cpp" in file) or (".c" in file) or (".java" in file) or (".cs" in file) or (".js" in file) :
        #   try:
        #     # print("yes")
        #     flag=1
        #     # print(file)
        #     os.chdir("D:/Sem 5/Natural language processing/code2readme/code2readme_data/data/{}".format(i+1))
        #     f = open("all_py_{}.txt".format(i+1),"a")
        #     f1 = open(root+"/"+file, "r")
        #     l = f1.read()
        #     l = l+""
        #     f1.close()
        #     #print(l)

        #     f.write(l)
        #     f.close()
        #   except:
        #     pass


        # if "README.md" in file and flag==1:
        #   try:
        #     flag=2
        #     # print("yes")
        #     os.chdir("D:/Sem 5/Natural language processing/code2readme/code2readme_data/data/{}".format(i+1))
        #     a = open("all_readme_{}.txt".format(i+1),"a")
        #     a1 = open(root+"/"+file, "r")
        #     k = a1.read()
        #     k = k+""
        #     a1.close()
        #     #print(l)

        #     a.write(k)
        #     a.close()
        #   except:
        #     # print("pass")
        #     pass

        # else:
        #   continue
          

       


        # if(flag==2):



        #   if(len(l)<= 7000 and len(k) >= 100 and len(l)!=0 and len(k)!=0):
        #     try:
        #       # print(l,k)
        #       l = str(l).replace('\n','AAA')
        #       k = str(k).replace('\n','AAA')
        #       # print(l)
        #       df = df.append({'ENG': str(l).replace('|',''), 'FR':str(k).replace('|','')},ignore_index=True)
        #       # print(df)
        #       # tsv_writer.writerow([r'{}'.format(l), r'{}'.format(k)])
        #       # tsv_writer.writerow(["XXXXXXXXX", "############"])
        #     except Exception as e:
        #       print(e)
          # code_len += len(l)
          # readme_len += len(k)
          # n += 1
# print(len(df))
# with open(r'C:\Users\ANIL KURLE\Desktop\try.pickle', 'wb') as handle:
#     pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
# df.to_csv(r'C:\Users\ANIL KURLE\Desktop\dumksjdbp.csv',index=False,quoting=csv.QUOTE_NONE,escapechar='\\')


# print("avg code len --> ",code_len/n, "avg readme len --> ", readme_len/n)





       
        
      
        
        
        
        
        