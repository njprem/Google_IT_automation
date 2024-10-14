import subprocess
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)