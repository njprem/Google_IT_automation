import subprocess

# Run the ping command to check connectivity to google.com
response = subprocess.run(["ping", "-c", "4", "google.com"], capture_output=True)
print(response.stdout.decode())