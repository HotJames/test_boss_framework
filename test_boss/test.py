import shelve

'''
龵
'''
f = shelve.open('/Users/james/PycharmProjects/test_boss_framework/tempdict/tempjson')

print(f['客户编码'])
print(f['客户名称'])

print(f.keys())