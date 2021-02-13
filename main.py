# # tic-tac toe
#
# # function to visualize the board for the user
# def board(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
#
# # define rows
# row1 = ["1", "2", "3"]
# row2 = ["4", "5", "6"]
# row3 = ["7", "8", "9"]
#
# # call board function
# board(row1, row2, row3)
#
# is_continued = True
#
# while is_continued:
#     board_number = input("Enter the board  :")
#     if board_number <= 3:
#         row1[board_number - 1] = raw_input("Select X or O : ")
#     elif board_number <= 6:
#         row2[board_number - 4] = raw_input("Select X or O :")
#     elif board_number <= 9:
#         row3[board_number - 7] = raw_input("Select X or O : ")
#     else:
#         print("Please enter the correct board number")
#
#     if row1[0] == "1" or row1[1] == "2" or row1[2] == "3" or row2[0] == "4" or row2[1] == "5" or row2[2] == "6" or row3[
#     0] == "7" or row3[1] == "8" or row3[2] == "9":
#         pass
#     else:
#         is_continued = False
#
#     if row1[0] == row1[1] == row1[2] or row2[0] == row2[1] == row2[2] or row3[0] == row3[1] == row3[2] or row1[0
#         ] == row2[0] == row3[0] or  row1[1] == row2[1] == row3[1] or  row1[2] == row2[2] == row3[2] or  row1[0
#         ] == row2[1] == row3[2] or  row1[2] == row2[1] == row3[0]:
#         print("You won the game")
#         is_continued = False
#
#     board(row1, row2, row3)
#
# if not is_continued:
#     print("Please start the new game")
#
#
#
