from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text= "Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column =1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Some text ",width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))

        img_wrong = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=img_wrong, highlightthickness=0, command=self.false_pressed)
        self.button_wrong.grid(row=2, column=1)

        img_right = PhotoImage(file="images/true.png")
        self.button_right = Button(image=img_right, highlightthickness=0, command=self.true_pressed)
        self.button_right.grid(row=2, column=0)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)