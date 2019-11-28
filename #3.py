from itertools import groupby

n=int(input('Enter number of pupils '))
primary_dict={}

list_of_subj=[]
for i in range(n):
    students = input('Enter name of student: ')
    subjects=input('Enter his subjects: ').split()
    primary_dict[students]=subjects
#    list_of_subj+=subjects                                                       #uncomment to convenient debugging
#    list_of_subj.sort()
#    new_list_of_subj = [el for el, _ in groupby(list_of_subj)]                   #sort to check iterations before debugging

def student_for_sub(student):
    return primary_dict[student]

def sub_for_student(subject):
    s=[]
    for key in primary_dict.keys():
        if subject in primary_dict[key]:
            s.append(key)
        else:
            print(key,'dont studying this')
    return s
            
def show_all():
    for k in sorted(primary_dict.keys()):
        print(k, ':',primary_dict[k])
    return     
    


