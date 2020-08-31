

from hashlib import md5


pwd = "musen001"

# md5加密
new_md5 = md5()
new_md5.update(pwd.encode("utf-8"))
res = new_md5.hexdigest()

print(res)
