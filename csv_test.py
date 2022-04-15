# import module

import csv
import platform
import os
import math

# convert


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1000)))
    p = math.pow(1000, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def collect_data(path):
    # generic system info

    network_name = platform.node()
    machine_type = platform.machine()
    processor_type = platform.processor()
    platform_type = platform.platform()
    operating_system = platform.system()
    operating_system_release = platform.release()
    operating_system_version = platform.version()

    # csv file

    with open(os.path.join(path, "System_Information.csv"), "w", newline="") as csvfile:

        fieldnames = [
            "Network Name",
            "Machine Type",
            "Processor Type",
            "Platform Type",
            "Operating System",
            "Operating System Version",
            "Operating System Release",
        ]

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()
        thewriter.writerow(
            {
                "Network Name": network_name,
                "Machine Type": machine_type,
                "Processor Type": processor_type,
                "Platform Type": platform_type,
                "Operating System": operating_system,
                "Operating System Version": operating_system_version,
                "Operating System Release": operating_system_release,
            }
        )
