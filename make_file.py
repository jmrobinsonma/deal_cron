

url_list = []

user_search_name =  input("\nEnter a name for the search: ")
user_email = input("\nEnter an email address: ")
url = input("\nEnter a url: ")
url_list.append(url)
next_url = input("\nEnter another url or 'q' to quit: ")

while next_url != 'q':
	url_list.append(next_url)
	next_url = input("\nEnter another url or 'q' to quit: ")

args = {
	"search_name": user_search_name,
	"email": user_email,
	"urls": url_list
}

flagged_urls = ""

for i in url_list:
	flagged_urls = flagged_urls + f" -u '{i}'"

shell = "#!bin/bash"

python_path = "/home/jmr/scrapers/deal_cron/venv/bin/python3"
file_path = f"/home/jmr/scrapers/deal_cron/{args['search_name']}.sh"

script = f"{shell}\n{python_path} {file_path} {user_search_name} {user_email}{flagged_urls}"

with open(file_path, "w") as f:
	f.write(script)
