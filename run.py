import re
import mmap

log_file = '/home/zhuk/communicator.log'
re_pattern = '.+<Message.+control_id="(\d+)".+mes_number="(\d+)".+'
data = {}
with open(log_file, 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
        for line in mmap_obj.read().decode('utf-8').split('\n'):
            match = re.search(re_pattern, line)
            if match:
                key = match.group(1)
                if key not in data:
                    data[key] = []
                data[key].append(match.group(2))
for key in data.keys():
    print('{} {}'.format(key, max(data[key])))