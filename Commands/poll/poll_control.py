def split_cmd(content):
	cmd_list = content.split(' ')
	for cmd in cmd_list:
		if(cmd[0] == '"'):
			if(cmd[-1] == '"'):
				return None


def build_msg_str(title, options, numbers, comment=None):
	if(len(options) !=len(numbers)):
		print("data err")

	message = "__**" + "title" + "**__"
	if(comment != None):
		message = message + '\n' + comment

	message = message + "\n```"

	#get the widthto put options's string
	options_width = 0
	for option in options:
		if(len(option) > options_width):
			options_width = len(option)

	for option_index in range(len(numbers)):
		string_line = options[option_index].center(options_width) + " | "
		string_line = string_line + numbers[option_index]*"█" + ' ' + str(numbers[option_index])
		message = message + '\n' + string_line

	message = message + "\n```"
	return message



if __name__=="__main__":#for test function
	print( build_msg_str("test_title", ['aaaaa', 'bbbbbbbbbb', 'cc', 'd'], [5, 0, 9, 1]) )