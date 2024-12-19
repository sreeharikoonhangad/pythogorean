import tkinter as tk
from tkinter import ttk, messagebox
from owlready2 import get_ontology

# Load ontology
ontology = get_ontology("PythagoreanOntology.rdf").load()

# Function to display ontology concepts
def show_ontology_concepts():
    concepts = [cls.name for cls in ontology.classes()]
    messagebox.showinfo("Ontology Concepts", ", ".join(concepts))

# Interactive tutorial navigation
current_step = 0
steps = [
    "Step 1: Identify the sides (opposite, adjacent, hypotenuse).",
    "Step 2: Apply the formula: a² + b² = c².",
    "Step 3: Solve for the missing side."
]

def next_step():
    global current_step
    if current_step < len(steps) - 1:
        current_step += 1
        step_label.config(text=steps[current_step])
    else:
        messagebox.showinfo("Tutorial", "You have completed the tutorial!")

# Quiz functionality
def check_answer():
    try:
        user_answer = float(answer_entry.get())
        correct_answer = (3**2 + 4**2) ** 0.5
        if abs(user_answer - correct_answer) < 0.01:
            messagebox.showinfo("Quiz", "Correct!")
        else:
            messagebox.showerror("Quiz", f"Incorrect! The correct answer is {correct_answer:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a numeric value.")

# Hint functionality
hints = {
    "Find the hypotenuse": "Hint: Use the formula a² + b² = c².",
    "Verify a Right triangle": "Hint: Check if the given sides satisfy a² + b² = c²."
}

def show_hint():
    selected_hint = hint_menu.get()
    hint_label.config(text=hints.get(selected_hint, "Select a problem to see the hint."))

# Initialize the main window
root = tk.Tk()
root.title("Pythagorean Theorem Tutor")
root.geometry("800x600")

# Tabs
notebook = ttk.Notebook(root)
tutorial_tab = ttk.Frame(notebook)
quiz_tab = ttk.Frame(notebook)
feedback_tab = ttk.Frame(notebook)
notebook.add(tutorial_tab, text="Interactive Tutorials")
notebook.add(quiz_tab, text="Quizzes")
notebook.add(feedback_tab, text="Feedback")
notebook.pack(expand=1, fill="both")

# Interactive Tutorials Tab
tutorial_label = tk.Label(tutorial_tab, text="Welcome to the Pythagorean Theorem Tutorial!", wraplength=700)
tutorial_label.pack(pady=10)

step_label = tk.Label(tutorial_tab, text=steps[current_step], wraplength=700)
step_label.pack(pady=10)

next_button = tk.Button(tutorial_tab, text="Next Step", command=next_step)
next_button.pack(pady=10)

# Quizzes Tab
quiz_label = tk.Label(quiz_tab, text="Question: If a=3 and b=4, find c (hypotenuse).")
quiz_label.pack(pady=10)

answer_entry = tk.Entry(quiz_tab)
answer_entry.pack(pady=10)

submit_button = tk.Button(quiz_tab, text="Submit Answer", command=check_answer)
submit_button.pack(pady=10)

# Feedback Tab
hint_menu = ttk.Combobox(feedback_tab, values=list(hints.keys()))
hint_menu.pack(pady=10)

hint_label = tk.Label(feedback_tab, text="Select a problem to see a hint.")
hint_label.pack(pady=10)

hint_button = tk.Button(feedback_tab, text="Show Hint", command=show_hint)
hint_button.pack(pady=10)

# Ontology Button
ontology_button = tk.Button(root, text="Show Ontology Concepts", command=show_ontology_concepts)
ontology_button.pack(pady=10)

# Run the application
root.mainloop()
