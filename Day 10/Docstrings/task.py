def format_name(f_name, l_name):
    """Takes a first and last name as inputs and returns the name back with
    the first letters of each capitalized"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



