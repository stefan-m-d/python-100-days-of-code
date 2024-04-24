from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
img_path_true = "Day 34 - Quiz App with API/images/true.png"
img_path_false = "Day 34 - Quiz App with API/images/false.png"


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        right_img=PhotoImage(file=img_path_true)
        wrong_img=PhotoImage(file=img_path_false)
        
        self.score = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR, fg="white", font=("Ariel", 20, "bold"))
        self.score.grid(column=1, row=0, pady=10)
        
        self.right_btn = Button(image=right_img, highlightthickness=0, command=self.answer_true)
        self.right_btn.grid(column=0, row=3, pady=10)

        self.wrong_btn = Button(image=wrong_img, highlightthickness=0, command=self.answer_false)
        self.wrong_btn.grid(column=1, row=3, pady=10)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)
        
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some Question Text", 
            font=("Ariel", 20, "italic"))
        
        self.get_next_question()
        
        self.window.mainloop() 
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
        
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)