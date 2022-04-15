import psutil
import math


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1000)))
    p = math.pow(1000, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


# CPU

physical_core = psutil.cpu_count(logical=False)
logical_core = psutil.cpu_count(logical=True)
freq_min = psutil.cpu_freq().min
freq_max = psutil.cpu_freq().max
cpu_util = psutil.cpu_percent(interval=1)
cpu_per_util = psutil.cpu_percent(interval=1, percpu=True)

# RAM

total_ram = convert_size(psutil.virtual_memory().total)
avail_ram = convert_size(psutil.virtual_memory().available)
used_ram = convert_size(psutil.virtual_memory().used)
perc_ram = psutil.virtual_memory().percent


print(f"Physical CPU cores: {physical_core}")
print(f"Logical CPU cores: {logical_core}")
print(f"Total Ram: {total_ram}")
