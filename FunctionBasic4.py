# default argument

def ssh_login(username, ip_add, platform='cisco'):
    print(f"ssh {username}@{ip_add}")
    print(f"{username}@{platform}#configure terminal")


ssh_login("johndoe","192.168.1.1")