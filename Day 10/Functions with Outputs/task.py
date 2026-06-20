#Function that prints data
def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    output_string = first_name + " " + last_name

    print(output_string)

#Function that returns data
def format_name2 (f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    output_string = first_name + " " + last_name

    return output_string

#print the name with the first letter of each capitalized
format_name("flynn","dog")
print(format_name2("dash", "dog"))
