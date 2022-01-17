import random, textwrap

# This script generates test cards from blocks of questions as follows:
# 
# Test card header, card number 1
# 1. Question 1...
# 2. Question 2...
# 3. ...
# ...
# ----- whitespace -----
# Test card header, card number 2
# 1. Question 1...
# 2. Question 2...
# 3. ...
# ...

################################### EDIT HERE ##################################

number_of_cards = 20 # Any number is valid.
# This is a test card header, printed before questions.
header = "\n                           Test card № "
file_name = "test_cards.txt"
separator = " " # Line under the test card.
text_width = 80 # Number of characters to wrap in.

question_blocks_init = [ # This bracket must be here.

# BLOCK 1
# ==============================================================================
[
"Question 1",
"Question 2",
"Question 3",
"Question 4",
"Question 5",

],
# ==============================================================================
# BLOCK 2
# ==============================================================================
[
"Question 1",
"Question 2",
"Question 3",
"Question 4",
"Question 5",
"Question 6",
"Question 7",

],
# ==============================================================================
# BLOCK 3
# ==============================================================================
[
"Question 1",
"Question 2",
"Question 3",
"Question 4",
"Question 5",
"Question 6",
"Question 7",
"Question 8",
"Question 9",
"Question 10",

],
# ==============================================================================
# BLOCK N... (Insert python lists with questions further on, if you need more).
# ==============================================================================








] # This bracket must be here.

################################## DO NOT EDIT #################################
number_of_questions = len(question_blocks_init)

# Set up textwrap formatter.
tw = textwrap.TextWrapper(text_width, initial_indent="", subsequent_indent="   ")


# Complement the lists of questions if there are not enough questions.
question_blocks = []
for q in range(number_of_questions):
	block = question_blocks_init[q]
	while len(block) < number_of_cards:
		block += block
	question_blocks.append(block)

# Sfuffle the question blocks in place to randomize order.
for q in range(number_of_questions):
	random.shuffle(question_blocks[q])

# Start an empty string and append to it.
# EDITED: due to shuffle beforehand, use .pop() to take all the questions
# without excessive duplication. This ensures uniform distribution.
file_body = ""
for i in range(number_of_cards):
	file_body += header + str(i+1) + "\n"
	for q in range(number_of_questions):
		file_body += str(q+1) + ". " + tw.fill(question_blocks[q].pop()) + "\n"
	file_body += separator + "\n"

# Print the output to the command line and to the file.
print(file_body)
print(file_body, file=open(file_name, "w"))
