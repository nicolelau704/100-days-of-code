#Uses website reeborg.ca to jump over hurdles
#
#There is no way to turn the robot right, so create a function
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#When hurdles are the same height, use this function to jump over them
# def hurdle_jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#When hurdles are different heights, use this function to jump over them
# def varying_jump():
#     turn_left()
#     while wall_on_right() and not wall_in_front():
#         move()
#         if right_is_clear():
#             turn_right()
#             move()
#             turn_right()
#             move()
#         turn_left()
#
#teacher's version of varying_jump()
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#Use a for loop when you know the exact number of hurdles to jump
# for hurdles in range(0, 6):
#    hurdle_jump()
#
#You can use a while loop when you know the exact number of hurdles to jump
# num_of_hurdles = 6
# while num_of_hurdles > 0:
#    hurdle_jump()
#    num_of_hurdles -= 1
#
#When you don't know how many hurdles to jump, keep jumping until you reach the goal
# while not at_goal():
#    hurdle_jump()
#
#Only jump when there is a hurdle, otherwise move forward until you reach the goal
# while not at_goal():
#    if wall_in_front():
#        hurdle_jump()
#    elif front_is_clear():
#        move()
#
#Jump hurdles at different heights when they appear, otherwise move forward unti you reach the goal
#while not at_goal():
#    if wall_in_front():
#        varying_jump()
#    else:
#        move()