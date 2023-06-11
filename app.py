from functions import ThreadJob 
import tkinter as tk
import threading
import requests

class DDoSInterface:
    def __init__(self, root):
        self.root = root
        self.endpoint = tk.StringVar()
        self.response = tk.StringVar()
        self.delay = tk.IntVar()
        self.running = False
        self.event = threading.Event()
        self.k = None

        self.endpoint_label = tk.Label(root, text="Endpoint:")
        self.endpoint_entry = tk.Entry(root, textvariable=self.endpoint)
        self.delay_label = tk.Label(root, text="Delay (minutes):")
        self.delay_entry = tk.Entry(root, textvariable=self.delay)
        self.start_button = tk.Button(root, text="Start DDoS", command=self.start_ddos)
        self.stop_button = tk.Button(root, text="Stop DDoS", command=self.stop_ddos)
        self.save_button = tk.Button(root, text="Save Response", command=self.save_response)
        self.output_text = tk.Text(root, height=50, width=40)

        self.endpoint_label.pack()
        self.endpoint_entry.pack()
        self.delay_label.pack()
        self.delay_entry.pack()
        self.start_button.pack()
        self.stop_button.pack()
        self.save_button.pack()
        self.output_text.pack()

    def start_ddos(self):
        if self.running:
            return

        delay = self.delay.get()

        self.running = True
        self.ddos_request(delay)

    def save_response(self):
        # write the response to a file
        with open("response.txt", "w") as f:
            f.write(self.output_text.get("1.0", tk.END))

    def send_request(self):
        endpoint = self.endpoint.get()
        self.response = requests.get(endpoint).json()
        self.output_text.insert(tk.END, self.response)
        self.output_text.see(tk.END)

    def stop_ddos(self):
        self.output_text.insert(tk.END, "\nDDoS request ended\n")
        self.event.set()
        self.k.join()


    def ddos_request(self, delay):
        self.output_text.insert(tk.END, "DDoS request started\n")
        self.k = ThreadJob(self.send_request, self.event, delay)
        self.k.start()
        

# Create the Tkinter window
root = tk.Tk()
root.title("DDoS Program")

# Create the DDoS interface
ddos_interface = DDoSInterface(root)

# Run the Tkinter event loop
root.mainloop()

