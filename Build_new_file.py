import os
newfile = os.getcwd()+'\\t1.txt'
b_new_file = open(newfile,'w')
# t_n = b_new_file.write('I like Python!')
b_new_file.close()
print('%s成功建立'%(newfile))