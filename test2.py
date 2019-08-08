import re
s = '\n                主演：寺田农,鹫尾真知子,龟山助清\n        '
p = re.compile('\s+(.*)\s+')
r_list = p.findall(s)
print(r_list)