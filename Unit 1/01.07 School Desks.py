class_a = input("Enter number of students in Classroom A: ")
class_b = input("Enter number of students in Classroom B: ")
class_c = input("Enter number of students in Classroom C: ")
class_a_desks = (int(class_a)) // 2
class_a_desks_remain = (int(class_a)) % 2
class_a_total = (int(class_a_desks)) + (int(class_a_desks_remain))
class_b_desks = (int(class_b)) // 2
class_b_desks_remain = (int(class_b)) % 2
class_b_total = (int(class_b_desks)) + (int(class_b_desks_remain))
class_c_desks = (int(class_c)) // 2
class_c_desks_remain = (int(class_c)) % 2
class_c_total = (int(class_c_desks)) + (int(class_c_desks_remain))
print ((int(class_a_total)) + (int(class_b_total)) + (int(class_c_total)))