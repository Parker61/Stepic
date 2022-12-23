import string

symbols = string.ascii_lowercase + string.digits + '_' + '@.'
s = input().lower()
ad = filter(lambda x: x.find('@') < x.find('.') and all(i in symbols for i in x), s.split())
print(*ad)
