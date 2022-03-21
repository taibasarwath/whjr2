from tkinter import *
root = Tk()
root.geometry("600x600")

percentage_grade_3_label = Label(root)
percentage_grade_5_label = Label(root)
percentage_grade_10_label = Label(root)

class grade_3():
    def __init__(self,  language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
    def percentage(self): 
        total_marks = self.language_arts +self.mathematics
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100/200
        percentage_grade_3_label["text"] = grade_3_percentage
        
class grade_5():
    def __init__(self,  language_arts, mathematics,social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
    def percentage(self):
        total_marks = self.language_arts +self.mathematics + self.social_studies 
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100/300
        percentage_grade_5_label["text"] = grade_5_percentage 
        
class grade_10():
    def __init__(self, language_arts, mathematics,social_studies,foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language
    def percentage(self):
        total_marks =self.language_arts +self.mathematics + self.social_studies +  self.foreign_language
        total_marks_with_100 = total_marks * 100
        grade_10_percentage = total_marks_with_100/400
        percentage_grade_10_label["text"] = grade_10_percentage
        
object_grade_3 = grade_3(40,50)
grade_3_btn=Button(root,text="Grade 3",command=object_grade_3.percentage)
grade_3_btn.pack(padx=20, pady =20)
percentage_grade_3_label.pack(padx=20, pady =20)

object_grade_5 = grade_5(40,50,90)
grade_5_btn=Button(root,text="Grade 5",command=object_grade_5.percentage)
grade_5_btn.pack(padx=20, pady =20)
percentage_grade_5_label.pack(padx=20, pady =20)

object_grade_10 = grade_10(40, 50,70,90)
grade_10_btn=Button(root,text="Grade 3",command=object_grade_10.percentage)
grade_10_btn.pack(padx=20, pady =20)
percentage_grade_10_label.pack(padx=20, pady =20)
root.mainloop()

