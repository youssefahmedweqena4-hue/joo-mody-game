import random
import tkinter as tk


class JooModyGame:

  def __init__(self, root):
    self.root = root
    self.root.title("Joo & Mody - Guess The Number 🎮")
    self.root.geometry("400x520")
    self.root.configure(bg="#050505")  # أسود فاحم
    self.root.resizable(False, False)

    self.secret_number = random.randint(1, 100)
    self.attempts = 0
    self.best_score = None

    self.create_widgets()

  def create_widgets(self):
    # العنوان الرئيسي بلون الأخضر النيون
    title_label = tk.Label(
        self.root,
        text="🔥 Joo & Mody 🔥",
        font=("Segoe UI", 22, "bold"),
        fg="#00ff66",  # أخضر نيون ساطع
        bg="#050505",
    )
    title_label.pack(pady=(20, 5))

    sub_label = tk.Label(
        self.root,
        text="Guess a number between 1 and 100",
        font=("Segoe UI", 11, "bold"),
        fg="#00ffff",  # سماوي نيون
        bg="#050505",
    )
    sub_label.pack(pady=(0, 15))

    # صندوق إدخال الرقم
    self.entry = tk.Entry(
        self.root,
        font=("Segoe UI", 22, "bold"),
        justify="center",
        width=8,
        bg="#121212",
        fg="#00ff66",
        insertbackground="#00ff66",
        relief="solid",
        bd=2,
    )
    self.entry.pack(pady=10)
    self.entry.focus()
    self.entry.bind("<Return>", lambda event: self.check_guess())

    # زر التخمين بلون الأخضر النيون
    guess_btn = tk.Button(
        self.root,
        text="Submit Guess 🚀",
        font=("Segoe UI", 12, "bold"),
        bg="#050505",
        fg="#00ff66",
        activebackground="#00ff66",
        activeforeground="#050505",
        relief="solid",
        bd=2,
        cursor="hand2",
        padx=15,
        pady=5,
        command=self.check_guess,
    )
    guess_btn.pack(pady=10)

    # شاشة النتيجة والتوجيهات (Hint Box)
    self.result_label = tk.Label(
        self.root,
        text="Good Luck! Enter your first guess.",
        font=("Segoe UI", 11, "bold"),
        fg="#00ff66",
        bg="#121212",
        width=35,
        height=2,
        relief="groove",
        bd=2,
    )
    self.result_label.pack(pady=15)

    # عداد المحاولات وأفضل نتيجة
    self.stats_label = tk.Label(
        self.root,
        text="Attempts: 0  |  Best Score: --",
        font=("Segoe UI", 10, "bold"),
        fg="#00ffff",
        bg="#050505",
    )
    self.stats_label.pack(pady=5)

    # زر إعادة اللعب
    reset_btn = tk.Button(
        self.root,
        text="🔄 New Game",
        font=("Segoe UI", 10, "bold"),
        bg="#050505",
        fg="#00ffff",
        activebackground="#00ffff",
        activeforeground="#050505",
        relief="solid",
        bd=2,
        cursor="hand2",
        command=self.reset_game,
    )
    reset_btn.pack(pady=(15, 0))

  # نافذة منبثقة مخصصة
  def show_custom_popup(self, title, message, title_color="#00ff66"):
    popup = tk.Toplevel(self.root)
    popup.title(title)
    popup.geometry("340x200")
    popup.configure(bg="#050505")
    popup.resizable(False, False)
    popup.grab_set()
    popup.transient(self.root)

    lbl_title = tk.Label(
        popup,
        text=title,
        font=("Segoe UI", 16, "bold"),
        bg="#050505",
        fg=title_color,
    )
    lbl_title.pack(pady=(20, 10))

    lbl_msg = tk.Label(
        popup,
        text=message,
        font=("Segoe UI", 10, "bold"),
        bg="#050505",
        fg="#00ffff",
        justify="center",
    )
    lbl_msg.pack(pady=10)

    btn_ok = tk.Button(
        popup,
        text="OK",
        font=("Segoe UI", 10, "bold"),
        bg="#050505",
        fg="#00ff66",
        activebackground="#00ff66",
        activeforeground="#050505",
        relief="solid",
        bd=2,
        width=10,
        cursor="hand2",
        command=popup.destroy,
    )
    btn_ok.pack(pady=10)

  def check_guess(self):
    user_input = self.entry.get().strip()

    if not user_input.isdigit() and not (
        user_input.startswith("-") and user_input[1:].isdigit()
    ):
      self.show_custom_popup(
          "Error",
          "❌ Invalid input!\nPlease enter a valid number.",
          title_color="#ff3333",
      )
      self.entry.delete(0, tk.END)
      return

    guess = int(user_input)

    if guess < 1 or guess > 100:
      self.show_custom_popup(
          "Out of Range",
          "⚠️ Number out of range!\nPlease enter a number between 1 and 100.",
          title_color="#facc15",
      )
      self.entry.delete(0, tk.END)
      return

    self.attempts += 1

    if guess < self.secret_number:
      self.result_label.config(
          text=f"📈 Higher! ({guess} is too low)", fg="#facc15"
      )
    elif guess > self.secret_number:
      self.result_label.config(
          text=f"📉 Lower! ({guess} is too high)", fg="#facc15"
      )
    else:
      self.result_label.config(
          text=f"🎉 Correct! The number was {self.secret_number}", fg="#00ff66"
      )

      if self.best_score is None or self.attempts < self.best_score:
        self.best_score = self.attempts

      self.show_custom_popup(
          "🏆 Winner! 🏆",
          f"🎉 Congratulations Joo & Mody!\nYou guessed it in {self.attempts} attempts!",
          title_color="#00ff66",
      )

    self.update_stats()
    self.entry.delete(0, tk.END)

  def update_stats(self):
    best_text = str(self.best_score) if self.best_score is not None else "--"
    self.stats_label.config(
        text=f"Attempts: {self.attempts}  |  Best Score: {best_text}"
    )

  def reset_game(self):
    self.secret_number = random.randint(1, 100)
    self.attempts = 0
    self.result_label.config(
        text="Game reset! Enter a new guess.", fg="#00ff66"
    )
    self.update_stats()
    self.entry.delete(0, tk.END)


if __name__ == "__main__":
  root = tk.Tk()
  app = JooModyGame(root)
  root.mainloop()