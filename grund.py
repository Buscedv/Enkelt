# Enkelt: Programming Language
# Enkelt: Programeringsspråk
# A simple programming language with Swedish syntax.
# Ett simpelt programeringspråk med Svensk syntax.
# Developed by: Edvard Busck-Nielsen 11.12.2018
# Utvecklat av: Edvard Busck-Nielsen 11.12.2018
# 1.5
# GNU GPL v. 3.0

import sys
import os



def interpreter(code):

	global global_if
	global global_is_if
	global global_if_history
	global global_is_an
	global global_an_history
	can_continue = True

	for i, line in enumerate(code):
		cmd = ""
		i = i+1
		if cmd == "}" or "}" in line:
			if global_is_if:
				global_is_if = False
				global_if_history = True
				cmd = ""
			elif global_is_an:
				global_is_an = False
				global_an_history == True
				global_if_history = True
				cmd = ""
			continue
		if (
				global_is_if == False and global_is_an == False or
				global_is_if and global_if or
				global_is_an and global_if == False and global_if_history or
				global_if == False and "annars" in line or
				global_is_if and global_if and global_is_an

			):
				for chr in line:
					if cmd == "#":
						cmd = ""
						break
					elif cmd == "töm":
						os.system('clear')
						cmd = ""
						break
					elif cmd == "skriv" and line[-1] == ")" and "(" in line:
						print(print_func(line, i))
						cmd = ""
						break
					elif cmd == "var" and "=" in line:
						var_func(line, i)
						cmd = ""
						break
					elif cmd == "matte" and "(" in line and ")" in line:
						print (math_func(line, i))
						cmd = ""
						break
					elif cmd == "om" and "(" in line and ")" in line:
						if_func(line, i)
						cmd = ""
						break
					elif cmd == "annars" and global_if_history:
						annars_func(line, i)
						cmd = ""
						break
					else:
						if chr != " ":
							cmd += chr
							if cmd == "#":
								cmd = ""
								break
							elif cmd == "töm":
								os.system('clear')
								cmd = ""
								break
							elif cmd == "skriv" and line[-1] == ")" and "(" in line:
								print(print_func(line, i))
								cmd = ""
								break
							elif cmd == "var" and "=" in line:
								var_func(line, i)
								cmd = ""
								break
							elif cmd == "matte" and "(" in line and ")" in line:
								print (math_func(line, i))
								cmd = ""
								break
							elif cmd == "om" and "(" in line and ")" in line:
								if_func(line, i)
								cmd = ""
								break
							elif cmd == "annars" and global_if_history:
								annars_func(line, i)
								cmd = ""
								break
				continue

		else:
			continue

def annars_func(code, line):
	global global_is_an
	global global_an_history
	global_is_an = True
	global_an_history = True

def parse_expr(expr, line):
	first = ""
	first1 = ""
	second = ""
	second1 = ""
	evaluation = ""
	lex_second = False
	found_string = False
	result = False

	first_var_stat = False
	second_var_stat = False

	for chr in expr:
		if lex_second:
			if found_string and chr == '"':
				continue
			elif found_string == False and chr == '"':
				found_string = True
			elif found_string:
				second += chr
			elif chr != " ":
				second += chr
		elif chr == "=" or chr == "!" or chr == "<" or chr == ">":
			evaluation += chr
			lex_second = True
		else:
			first += chr
	if first[0] == "$":
		for chr in first:
			if chr != " ":
				first1 += chr
		first = ""
		for chr in first1:
			first += chr
		first_var_stat = True
		first = Global_Variables[first[1:]]
	if second[0] == "$":
		for chr in second:
			if chr != " ":
				second1 += chr
		second = ""
		for chr in second1:
			second += chr
		second_var_stat = True
		second = Global_Variables[second[1:]]

	if evaluation == "=":
		if str(first) == str(second):
			result = True
		else:
			result = False
	elif evaluation == "!":
		if str(first) != str(second):
			result = True
		else:
			result = False
	elif evaluation == "<":
		if int(first) < int(second):
			result = True
		else:
			result = False
	elif evaluation == ">":
		if int(first) > int(second):
			result = True
		else:
			result = False
	return result



def if_func(code, line):
	cmd = ""
	lex_expr = False
	get_exp = False
	expression = ""
	boolean = False


	global global_if
	global global_is_if
	global global_if_history
	global global_an_history

	for chr in code:
		if lex_expr:
			if get_exp:
				if chr == ")":
					break
				else:
					expression += chr
			elif chr == "(":
				get_exp = True
		elif cmd == "om":
			lex_expr = True
		elif chr != " ":
			cmd += chr
			if cmd == "om":
				lex_expr = True
	boolean = parse_expr(expression, line)

	if boolean:
		global_if = True
	else:
		global_if = False
	global_is_if = True
	global_if_history = True
	global_an_history = False


def math_parse(num1, expr, num2, line):
	num1_var = False
	num2_var = False
	result = 0

	if num1[0] == "$":
		num1_var = True
	if num2[0] == "$":
		num2_var = True
	if expr == "+":
		if num1_var == False and num2_var == False:
			result = int(num1)+int(num2)
			return result
		elif num1_var == True and num2_var == True:
			num1 = Global_Variables[num1[1:]]
			num2 = Global_Variables[num2[1:]]
			result = int(num1)+int(num2)
			return result
		elif num1_var == True and num2_var == False:
			num1 = Global_Variables[num1[1:]]
			result = int(num1)+int(num2)
			return result
		elif num1_var == False and num2_var == True:
			num2 = Global_Variables[num2[1:]]
			result = int(num1)+int(num2)
			return result
	elif expr == "-":
		if num1_var == False and num2_var == False:
			result = int(num1)-int(num2)
			return result
		elif num1_var == True and num2_var == True:
			num1 = Global_Variables[num1[1:]]
			num2 = Global_Variables[num2[1:]]
			result = int(num1)-int(num2)
			return result
		elif num1_var == True and num2_var == False:
			num1 = Global_Variables[num1[1:]]
			result = int(num1)-int(num2)
			return result
		elif num1_var == False and num2_var == True:
			num2 = Global_Variables[num2[1:]]
			result = int(num1)-int(num2)
			return result
	elif expr == "*":
		if num1_var == False and num2_var == False:
			result = int(num1)*int(num2)
			return result
		elif num1_var == True and num2_var == True:
			num1 = Global_Variables[num1[1:]]
			num2 = Global_Variables[num2[1:]]
			result = int(num1)*int(num2)
			return result
		elif num1_var == True and num2_var == False:
			num1 = Global_Variables[num1[1:]]
			result = int(num1)*int(num2)
			return result
		elif num1_var == False and num2_var == True:
			num2 = Global_Variables[num2[1:]]
			result = int(num1)*int(num2)
			return result
	elif expr == "/":
		if num1_var == False and num2_var == False:
			result = int(num1)/int(num2)
			return result
		elif num1_var == True and num2_var == True:
			num1 = Global_Variables[num1[1:]]
			num2 = Global_Variables[num2[1:]]
			result = int(num1)/int(num2)
			return result
		elif num1_var == True and num2_var == False:
			num1 = Global_Variables[num1[1:]]
			result = int(num1)/int(num2)
			return result
		elif num1_var == False and num2_var == True:
			num2 = Global_Variables[num2[1:]]
			result = int(num1)/int(num2)
			return result
	elif expr == "%":
		if num1_var == False and num2_var == False:
			result = int(num1)%int(num2)
			return result
		elif num1_var == True and num2_var == True:
			num1 = Global_Variables[num1[1:]]
			num2 = Global_Variables[num2[1:]]
			result = int(num1)%int(num2)
			return result
		elif num1_var == True and num2_var == False:
			num1 = Global_Variables[num1[1:]]
			result = int(num1)%int(num2)
			return result
		elif num1_var == False and num2_var == True:
			num2 = Global_Variables[num2[1:]]
			result = int(num1)%int(num2)
			return result
	else:
		print ("Error linje nr. "+line+" matte()")			

def math_func(code, line):
	cmd = ""
	expression = ""
	first_num = ""
	second_num = ""
	cmd_found = False
	lex_math = False
	get_first_num = False
	get_second_num = False
	for chr in code:
		if lex_math and chr != " ":
			if get_first_num and chr != ")" and chr != "(" and chr != "+" and chr != "-" and chr != "*" and chr != "%" and chr != "/":
				first_num += chr
			elif get_second_num and first_num != "" and chr != ")" and chr != "(" and chr != "+" and chr != "-" and chr != "*" and chr != "%" and chr != "/":
				second_num += chr
			elif chr == ")":
				break
			elif chr == "(":
				get_first_num = True
			elif chr == "+" or chr == "-" or chr == "*" or chr == "%" or chr == "/":
				get_second_num = True
				get_first_num = False
				expression = chr
		elif cmd == "matte" and lex_math == False:
			cmd_found = True
			lex_math = True
		elif cmd_found == False:
			if chr != " ":				
				cmd += chr
				if cmd == "matte" and lex_math == False:
					cmd_found = True
					lex_math = True
	return math_parse(first_num, expression, second_num, line)

def var_func(code, line):
	cmd = ""
	inp_stat = False
	inp_stat_chr = False
	inp_stat_first = False
	inp_stat_end = False
	inp_lex = False
	inp_lex_name = False
	got_inp_name = False
	inp_title = False
	string = ""
	inp_name = ""
	result = ""
	result1 = ""
	title = ""
	inp_name_res = ""
	inp_stat_space = False
	if "in(" in code or "in (" in code:
		for chr in code:
			if inp_lex_name:
				if chr == "=":
					inp_lex_name = False
					got_inp_name = True
					for chr in inp_name:
						if chr != " ":
							inp_name_res += chr
					inp_name = ""
					for chr in inp_name_res:
						inp_name += chr
					inp_stat = True
				else:
					inp_name += chr
			elif inp_stat:
				if inp_title:
					if chr ==')':
						title = title[:-1]
						result = input(title)
						break
					else:
						title += chr
				elif string == "in(" and code[-1] == ")":
					if '("' in code and '")' in code:
						inp_title = True
					else:
						result = input()
						break
				elif chr != " ":
					string += chr
			elif cmd == "var" and got_inp_name == False:
				inp_lex_name = True
			else:
				if inp_lex == False and got_inp_name == False and chr != " ":
					cmd += chr
		var_name = inp_name
	elif "+" in code and "matte" not in code:
		cmd = ""
		var_stat = False
		var_stat_chr = False
		var_stat_first = False
		var_stat_end = False
		var_lex = False
		var_lex_name = False
		got_var_name = False
		first_val = False
		second_val = False
		get_first = False
		get_second = False
		string = ""
		var_name = ""
		result = ""
		var_name_res = ""
		first = ""
		second = ""
		first1 = ""
		second1 = ""
		var_stat_space = False
		for chr in code:
			if var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					for chr in var_name:
						if chr != " ":
							var_name_res += chr
					var_name = ""
					for chr in var_name_res:
						var_name += chr
					var_stat = True
					first_val = True
				else:
					if chr != " ":
						var_name += chr	
			
			elif var_stat:
				if chr == '+' and first != "":
					second_val = True
					first_val = False
				elif first_val:
					first += chr
				elif second_val:
					second += chr
			elif cmd == "var" and got_var_name == False:
				var_lex_name = True
			else:
				if var_lex == False and got_var_name == False and chr != " ":
					cmd += chr
					if cmd == "var" and got_var_name == False:
						var_lex_name = True
		if '$' in first:
			for chr in first:
				if chr != " ":
					first1 += chr
			first = ""
			for chr in first1:
				first += chr
		elif '"' in first:
			for chr in first:
				if chr == '"' and get_first:
					get_first = False
					break
				elif get_first:
					first1 += chr
				elif chr == '"' and get_first == False:
					get_first = True
			first = ""
			first = first1

		if '$' in second:
			for chr in second:
				if chr != " ":
					second1 += chr
			second = ""
			for chr in second1:
				second += chr
		elif '"' in second:
			for chr in second:
				if chr == '"' and get_second:
					get_second = False
					break
				elif get_second:
					second1 += chr
				elif chr == '"' and get_second == False:
					get_second = True
			second = ""
			second = second1
		if first[0] == "$":
			first = Global_Variables[first[1:]]
		if second[0] == "$":
			second = Global_Variables[second[1:]]
		result = str(first)+str(second)



	elif '"' in code:
		cmd = ""
		var_stat = False
		var_stat_chr = False
		var_stat_first = False
		var_stat_end = False
		var_lex = False
		var_lex_name = False
		got_var_name = False
		string = ""
		var_name = ""
		result = ""
		var_name_res = ""
		var_stat_space = False
		for chr in code:
			if var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					for chr in var_name:
						if chr != " ":
							var_name_res += chr
					var_name = ""
					for chr in var_name_res:
						var_name += chr
					var_stat = True
				else:
					if chr != " ":
						var_name += chr
				
			
			elif var_stat:
				if chr == '"' and var_stat_first:
					string += chr
					break
				elif var_stat_chr:
					string += chr
				elif chr == '"' and var_stat_first == False:
					var_stat_first = True
					var_stat_chr = True
			elif cmd == "var" and got_var_name == False:
				var_lex_name = True
			else:
				if var_lex == False and got_var_name == False:
					cmd += chr
		result = string[:-1]
	elif "matte" in code:
		cmd = ""
		var_stat = False
		var_stat_chr = False
		var_stat_first = False
		var_stat_end = False
		var_lex = False
		var_lex_name = False
		got_var_name = False
		string = ""
		var_name = ""
		result = ""
		to_claculate = ""
		var_name_res = ""
		var_stat_space = False
		for chr in code:
			if var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					for chr in var_name:
						if chr != " ":
							var_name_res += chr
					var_name = ""
					for chr in var_name_res:
						var_name += chr
					var_stat = True
				else:
					if chr != " ":
						var_name += chr
			
			elif var_stat:
				if chr != ")":
					to_claculate += chr
				elif chr == ")" and to_claculate != "":
					to_claculate += chr
					result = math_func(to_claculate, line)
					result = str(result)
			elif cmd == "var" and got_var_name == False:
				var_lex_name = True
			else:
				if var_lex == False and got_var_name == False and chr != " ":
					cmd += chr
					if cmd == "var" and got_var_name == False:
						var_lex_name = True
	elif "$" in code and "matte" not in code:
		cmd = ""
		int_stat = False
		int_stat_chr = False
		int_stat_first = False
		int_stat_end = False
		int_lex = False
		int_lex_name = False
		got_int_name = False
		string = ""
		int_name = ""
		result = ""
		result1 = ""
		int_name_res = ""
		int_stat_space = False
		for chr in code:
			if int_lex_name:
				if chr == "=":
					int_lex_name = False
					got_int_name = True
					for chr in int_name:
						if chr != " ":
							int_name_res += chr
					int_name = ""
					for chr in int_name_res:
						int_name += chr
					int_stat = True
				else:
					if chr != " ":
						int_name += chr
			elif int_stat:
				string += chr
			elif cmd == "var" and got_int_name == False:
				int_lex_name = True
			else:
				if int_lex == False and got_int_name == False and chr != " ":
					cmd += chr
					if cmd == "var" and got_int_name == False:
						int_lex_name = True
		for chr in string:
			if chr != " ":
				result1 += chr
		for chr in result1:
			result += chr
		var_name = int_name
		result = Global_Variables[result[1:]]
	else:
		cmd = ""
		int_stat = False
		int_stat_chr = False
		int_stat_first = False
		int_stat_end = False
		int_lex = False
		int_lex_name = False
		got_int_name = False
		string = ""
		int_name = ""
		result = ""
		result1 = ""
		int_name_res = ""
		int_stat_space = False
		for chr in code:
			if int_lex_name:
				if chr == "=":
					int_lex_name = False
					got_int_name = True
					for chr in int_name:
						if chr != " ":
							int_name_res += chr
					int_name = ""
					for chr in int_name_res:
						int_name += chr
					int_stat = True
				else:
					if chr != " ":
						int_name += chr
			elif int_stat:
					string += chr
			elif cmd == "var" and got_int_name == False:
				int_lex_name = True
			else:
				if int_lex == False and got_int_name == False:
					cmd += chr
		for chr in string:
			if chr != " ":
				result1 += chr
		for chr in result1:
			result += chr
		var_name = int_name
	Global_Variables.update({var_name:result})

def print_func(code, line):
	cmd = ""
	print_stat = False
	print_stat_chr = False
	print_stat_first = False
	print_stat_end = False
	print_lex = False
	was_variable = False
	string = ""
	if '$' in code and '"' not in code:
		for chr in code:
			if print_lex and chr == ")":
				was_variable = True
				break
			elif print_lex and chr == "(":
				print_stat_first = True
				print_stat = True
			elif print_stat:
				if print_stat_chr:
					string += chr
				elif chr == '$' and print_stat_first:
					print_stat_chr = True
			elif cmd == "skriv":
				print_lex = True
			elif print_lex == False and chr != " ":
				cmd += chr
	else:
		for chr in code:
			if print_lex and chr == ")":
				print_stat_end = True
			elif print_lex and chr == "(":
				print_stat_first = True
				print_stat = True
			elif print_stat:
				if chr == '"' and print_stat_end:
					string += chr
				elif print_stat_chr:
					string += chr
				elif chr == '"' and print_stat_first:
					print_stat_chr = True
			elif cmd == "skriv":
				print_lex = True
			else:
				if print_lex == False and chr != " ":
					cmd += chr
	if was_variable:
		string = Global_Variables[string]
		return string
	else:
		return string[:-1]

Global_Variables = {}
global_if = False
global_is_if = False
global_if_history = False
global_is_an = False
global_an_history = False
code = []
with open(sys.argv[1], "r") as file:
	code1 = file.readlines()
	code = (line.rstrip('\n') for line in code1)
	code = '***'.join(code)
	code = code.replace("\t", "    ")
	code = code.split('***')

interpreter(code)