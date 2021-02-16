import os
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
formatted_urls = ""

for i in url_list:
	formatted_urls = formatted_urls + f" -u '{i}'"

# Format the shell script
shell = "#!bin/bash"
python_path = "/home/jmr/scrapers/deal_cron/venv/bin/python3"
dot_py_path = "/home/jmr/scrapers/deal_cron/dealcron.py"
project_path = f"/home/jmr/scrapers/deal_cron/{user_search_name}"
shell_script_path = f"{project_path}/{user_search_name}.sh"

os.system(f"mkdir {project_path}")

shell_script = f"{shell}\n{python_path} {dot_py_path} {user_search_name} {user_email}{formatted_urls}"
with open(shell_script_path, "w") as f:
	f.write(shell_script)

os.system(f". {shell_script_path}")

# Format a docker run command and shell script
#docker_run_command = f"docker run --name {user_search_name} -idt jmr/dealtest /bin/bash -c 'python3 dealcron.py {user_search_name} {user_email}{formatted_urls}'"
#os.system(docker_run_command)

#docker_start_script = f"{shell}\ndocker start {user_search_name}"
#with open(shell_script_path, "w") as f:
#	f.write(docker_start_script)
