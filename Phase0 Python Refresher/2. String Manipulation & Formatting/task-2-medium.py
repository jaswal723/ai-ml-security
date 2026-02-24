# Task - Take a messy syslog string: syslog = " Oct 14 10:11:02 firewall sshd[1234]: Failed password for root from 10.10.10.10 \n". Use .strip() and .split() to extract just the attacker's IP address.

raw_log = " Oct 14 10:11:02 firewall sshd[1234]: Failed password for root from 10.10.10.10 \n"
split_log = raw_log.split()
print(f'Attacker IP address - {split_log[-1]}')