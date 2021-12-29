#1 exec time olcme timeit 
import timeit
code = """[4, 2, 3, 1, 5].sort()"""

execution_time = timeit.timeit(code, number=1)

print(execution_time)

#%% for execetion using datetime
import datetime

begin_time = datetime.datetime.now()

[4, 2, 3, 1, 5].sort()



print(datetime.datetime.now() - begin_time)


#%% #only datetime now using
import datetime

x = datetime.datetime.now()
print(x)