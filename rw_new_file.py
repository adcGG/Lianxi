import os
newfile = os.getcwd()+'\\t1.txt'
b_new_file = open(newfile,'w')
t_n = b_new_file.write('I like Python!')
b_new_file.write('\nI want to earn money!')
print('往文件里写入%d字节内容'%(t_n))


b_new_file = open(newfile,'r')
tt = b_new_file.read()
print(tt)

b_new_file.close()

