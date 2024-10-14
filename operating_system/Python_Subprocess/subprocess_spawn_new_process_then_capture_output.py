import subprocess




process_popen = subprocess.Popen(['echo', 'Hello from popen!'], stdout=subprocess.PIPE, text=True)

output_popen, _ = process_popen.communicate()

output_popen.strip()  # Extracting the stdout and stripping any extra whitespace

