import os
import time

subjects = ["Math", "Physics", "Business Studies"]
years = ["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]
question_papers = []
answer_papers = []


for subject in subjects:
	if os.path.isdir(subject) == False:
		subjects.remove(subject)

num = 1
print("\nThese are the subjects which are available on your computer: ")
print()
for subject in subjects:
	print("%d: %s" % (num, subject))
	num += 1
subject_num_selected = input("\nEnter the corresponding number for the subject you want: ")
print()
while subject_num_selected.isdigit() == False or int(subject_num_selected) > len(subjects):
	print("Make sure to enter the relevant number...")
	subject_num_selected = input("Try again: ")
subject_selected = subjects[int(subject_num_selected) - 1]

num = 1
papers = next(os.walk(subject_selected))[1]
for paper in papers:
	print("%d: %s" % (num, paper))
	num += 1
paper_num_selected = input("\nEnter the corresponding number for the paper you want: ")
print()
while paper_num_selected.isdigit() == False or int(paper_num_selected) > len(papers):
	print("Make sure to enter the relevant number...")
	paper_num_selected = input("Try again: ")
paper_selected = papers[int(paper_num_selected) - 1]

directory = subject_selected + "/" + paper_selected
papers_list = os.listdir(directory)

sum_or_win = input("Do you want a summer paper or a winter paper [s/w] ?: ")
while sum_or_win != "s" and sum_or_win != "w":
	sum_or_win = input("Make sure you type either 's' or 'w': ")

num = 1
print("\nHere are the years available...\n")
for year in years:
	print("%d: %s" % (num, year))
	num += 1
year_num_selected = input("\nEnter the corresponding number for the year you want: ")
print()
problem = True
while problem == True:
	while year_num_selected.isdigit() == False or int(year_num_selected) > len(years):
		print("Make sure to enter the relevant number...")
		year_num_selected = input("Try again: ")
	if year_num_selected == "13" and sum_or_win == "w":
		ask1 = input("The only papers available for 2015 are summer ones, so do you want those instead [y/n]?: ")
		while ask1 != "y" and ask1 != "n":
			ask1 = input("Make sure to type either 'y' or 'n': ")
		if ask1 == "y":
			sum_or_win = "s"
			problem = False
		else:
			problem = True
			year_num_selected = input("Enter the corresponding number for the year you want: ")
			continue
	problem = False
year_selected = years[int(year_num_selected) - 1]

identifier = sum_or_win + year_selected[-2:]

for paper in papers_list:
	if identifier in paper:
		if "qp" in paper:
			question_papers.append(paper)
		elif "ms" in paper:
			answer_papers.append(paper)

if len(question_papers) == 0:
	print("Uh oh! You don't seem to have this particular paper!")
	quit()

if len(question_papers) > 1:
	print("This paper has multiple variants...")
	print()
	num = 1
	for item in question_papers:
		print(num, ": code", item[-6:-4])
		num += 1
	code_num_selected = input("\nWhich code do you wish to access?: ")
	while code_num_selected.isdigit() == False or int(code_num_selected) > len(question_papers):
		print("Make sure to enter the relevant number...")
		code_num_selected = input("Try again: ")
	question_paper_selected = question_papers[int(code_num_selected) - 1]
	answer_paper_selected = answer_papers[int(code_num_selected) - 1]
else:
	question_paper_selected = question_papers[0]
	if len(answer_papers) > 0:
		answer_paper_selected = answer_papers[0]
	else:
		answer_paper_selected = []

cwd = os.getcwd()

if answer_paper_selected != []:
	print("\nDo you also want to open the mark scheme?: ")
	print()
	print("1: Open just the question paper")
	print("2: Open just the mark scheme")
	print("3: Open both the question paper and the mark scheme")
	open_ask = input("\nWhich code do you wish to access?: ")
	while open_ask.isdigit() == False or int(open_ask) > 3:
		print("Make sure to enter the relevant number...")
		open_ask = input("Try again: ")
	if open_ask == "1":
		os.startfile(cwd + "/" + directory + "/" + str(question_paper_selected))
	elif open_ask == "2":
		os.startfile(cwd + "/" + directory + "/" + str(answer_paper_selected))
	elif open_ask == "3":
		os.startfile(cwd + "/" + directory + "/" + str(question_paper_selected))
		os.startfile(cwd + "/" + directory + "/" + str(answer_paper_selected))







		





