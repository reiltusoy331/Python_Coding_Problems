# The Return Statement

def generate_email(username, domain="gmail.com"):
	email_generated = f"{username}@{domain}"
	return email_generated 

my_name = ["Knox","Trevor","Vince"]
my_email_list =[]


for name in my_name:
	new_emails = generate_email(name)
	my_email_list.append(new_emails) 
	

for new_email in my_email_list:
	print(f"Newly generated email: \"{new_email}\"")
	

