import subprocess
import time

# This is the "Active Defense" function
def block_ip(ip):
    print(f"BLOCKING ATTACKER IP: {ip}")
    # This command adds a specific rule to the Windows Firewall
    cmd = f'netsh advfirewall firewall add rule name="AutoBlock_BruteForce" dir=in action=block remoteip={ip}'
    subprocess.run(cmd, shell=True)

print("Monitoring Windows Event Logs for failed login attempts...")

while True:
    try:
        raw_output = subprocess.check_output('wevtutil qe Security /q:"*[System[(EventID=4625)]]" /f:text /c:1', shell=True)
        log_text = raw_output.decode()

        lines = log_text.splitlines()

        for line in lines:
            if "Source Network Address" in line:
                # Split the line and take the last part (the actual IP)
                attacker_ip = line.split()[-1]
                
                # Check if it's a real IP (not a dash)
                if attacker_ip != "-":
                    block_ip(attacker_ip)
                    print("Attack mitigated. System secure.")
                    # Exit the script after blocking to prevent duplicate rules
                    exit()
    except subprocess.CalledProcessError:
        pass
    time.sleep(2)
