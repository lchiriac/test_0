user_count_mapper.py
import  sys

for  line in sys.stdin:
(user, item, rating) = line.strip().split()
print  "LongValueSum:%s\t1" % user
