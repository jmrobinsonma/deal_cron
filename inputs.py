def get_user_inputs():

	url_list = []

	user_search_name =  input("\nEnter a name for the search: ")
	user_email = input("\nEnter an email address: ")
	url = input("\nEnter a url: ")
	url_list.append(url)
	next_url = input("\nEnter another url or 'q' to quit: ")

	while next_url != 'q':
		url_list.append(next_url)
		next_url = input("\nEnter another url or 'q' to quit: ")

	ARGS = {
		"search_name": user_search_name,
		"email": user_email,
		"urls": url_list
	}
	return ARGS

