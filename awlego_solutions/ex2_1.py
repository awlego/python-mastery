import tracemalloc

# storing data as single string
f = open('../Data/ctabus.csv')
tracemalloc.start()
data = f.read()
print(len(data))
current, peak = tracemalloc.get_traced_memory()
print(current, peak)
# 12361088 24722188

# storing data as list of strings
f = open('../Data/ctabus.csv')
tracemalloc.start()
lines = f.readlines()
print(lines[:20])
print(len(lines))
current, peak = tracemalloc.get_traced_memory()
print(current, peak)
# 45350019 45358584
# wow this is so much more -- this is like 45MB compared to 12/24MB

