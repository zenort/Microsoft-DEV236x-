owner=input("enter name for contact person for training group: ")
num_people=input("enter the total number attending the course: ")
training_time=input("enter the training time selected: ")
min_early=15

print("Reminder: training is schedule at "+training_time+ " for the ",owner, "group of ",num_people, " attendees")
print("Please arrive", min_early, "minutes early for the first class")