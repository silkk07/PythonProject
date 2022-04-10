
import psutil

print(f"Physical CPU cores: {psutil.cpu_count(logical=False)}")
print(f"Logical CPU cores: {psutil.cpu_count(logical=True)}")
