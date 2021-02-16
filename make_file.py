# Get the user input

url_list = []

user_search_name =  input("\nEnter a name for the search: ")
user_email = input("\nEnter an email address: ")
url = input("\nEnter a url: ")
url_list.append(url)
next_url = input("\nEnter another url or 'a' to advance: ")

while next_url != 'a':
	url_list.append(next_url)
	next_url = input("\nEnter another url or 'a' to advance: ")

# Format the urls

flagged_urls = ""

for i in url_list:
	flagged_urls = flagged_urls + f" -u '{i}'"

# Format the shell script

shell = "#!bin/bash"

python_path = "/home/jmr/scrapers/deal_cron/venv/bin/python3"
dot_py_path = "/home/jmr/scrapers/deal_cron/dealcron.py"
shell_script_path = f"/home/jmr/scrapers/deal_cron/{user_search_name}.sh"

shell_script = f"{shell}\n{python_path} {dot_py_path} {user_search_name} {user_email}{flagged_urls}"

with open(shell_script_path, "w") as f:
	f.write(shell_script)

# Format a docker run command and shell script

#docker_run = f"docker run --name {user_search_name} -idt jmr/jobcron /bin/bash -c 'python3 dealcron.py {user_search_name} {user_email}{flagged_urls}'"
#docker_script = f"{shell}\n{docker_run}"


