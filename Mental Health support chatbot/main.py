import tkinter as tk
from emotion_detector import detect_emotion
from resources import resources

def respond():
    user_input = user_entry.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")

    if any(word in user_input.lower() for word in ["suicide", "kill myself", "die"]):
        bot_response = resources["emergency"]
    else:
        emotion = detect_emotion(user_input)
        bot_response = resources[emotion]

    chat_log.insert(tk.END, "Bot: " + bot_response + "\n")
    user_entry.delete(0, tk.END)

# GUI
window = tk.Tk()
window.title("Mental Health Chatbot")

chat_log = tk.Text(window, height=20, width=60)
chat_log.pack()

user_entry = tk.Entry(window, width=50)
user_entry.pack()

send_button = tk.Button(window, text="Send", command=respond)
send_button.pack()

window.mainloop()
