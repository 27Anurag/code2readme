import glob
import os
flag=0
#print(glob.glob("/home/19110207/code2readme_data//*.py"))
import csv
import pandas as pd
from tqdm import trange
import pickle

import matplotlib.pyplot as plt


l=''
k=''
n=0
code_len, readme_len = 0,0

xx = []
yy = []

df = pd.DataFrame(columns =["ENG","FR"])

with open('D:/Sem 5/Natural language processing/code2readme/code2readme_data/dump.tsv', 'wt') as out_file:
  tsv_writer = csv.writer(out_file, delimiter='\t')

  for i in trange(20000):
    # print("file no --> ", i)

    
    path = os.walk("D:/Sem 5/Natural language processing/code2readme/code2readme_data/data/{}".format(i+1))

    for root, directories, files in path:

      for file in files:
        # print(file)
        


         # print("python")
        if (".py" in file) or (".cpp" in file) or (".c" in file) or (".java" in file) or (".cs" in file) or (".js" in file) :
          try:
            # print("yes")
            flag=1
            # print(file)
            os.chdir("D:/Sem 5/Natural language processing/code2readme/code2readme_data/data/{}".format(i+1))
            f = open("all_py_{}.txt".format(i+1),"a")
            f1 = open(root+"/"+file, "r")
            l = f1.read()
            l = l+""
            f1.close()
            #print(l)

            f.write(l)
            f.close()
          except:
            pass


        if "README.md" in file and flag==1:
          try:
            flag=2
            # print("yes")
            os.chdir("D:/Sem 5/Natural language processing/code2readme/code2readme_data/data/{}".format(i+1))
            a = open("all_readme_{}.txt".format(i+1),"a")
            a1 = open(root+"/"+file, "r")
            k = a1.read()
            k = k+""
            a1.close()
            #print(l)

            a.write(k)
            a.close()
          except:
            # print("pass")
            pass

        else:
          continue
          

       


        if(flag==2):



          if(len(l)<= 7000 and len(k) >= 100 and len(l)!=0 and len(k)!=0):
            try:
              # print(l,k)
              l = str(l).replace('\n','AAA')
              k = str(k).replace('\n','AAA')
              # print(l)
              df = df.append({'ENG': str(l).replace('|',''), 'FR':str(k).replace('|','')},ignore_index=True)
              # print(df)
              # tsv_writer.writerow([r'{}'.format(l), r'{}'.format(k)])
              # tsv_writer.writerow(["XXXXXXXXX", "############"])
            except Exception as e:
              print(e)

          if(len(l)<300000 and len(k)<300000):
            xx.append(len(l))
            yy.append(len(k))
          else:
            xx.append(300000)
            yy.append(len(k))

          code_len += len(l)
          readme_len += len(k)
          n += 1
# print(len(df))
# with open(r'C:\Users\ANIL KURLE\Desktop\try.pickle', 'wb') as handle:
#     pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
# df.to_csv(r'C:\Users\ANIL KURLE\Desktop\dumksjdbp.csv',index=False,quoting=csv.QUOTE_NONE,escapechar='\\')


print("avg code len --> ",code_len/n, "avg readme len --> ", readme_len/n)

zz = []

for i in range(len(xx)):
  zz.append(i+1)

# for i in yy:
#   print(i)

plt.plot(xx, zz, label = "Code lengths")
plt.plot(yy, zz, label = "Readme lengths")

plt.show()







       
        
      
        
        
        
        
        