# DDoS Interface Program

# Disclaimer: This project is for educational purposes only. Unauthorized use of this code to disrupt services is illegal and unethical. Always ensure compliance with laws and obtain proper authorization before using tools like this.

This Python-based graphical user interface (GUI) simulates a DDoS (Distributed Denial of Service) tool. Built with Tkinter, the application allows users to send repeated HTTP GET requests to a specified endpoint at a configurable interval.

## Features

- Endpoint Input: Specify the target URL for requests.
- Configurable Delay: Set the delay between requests in minutes.
- Start and Stop DDoS: Begin or halt the HTTP request process at any time.
- Response Viewer: Display server responses in a scrollable text area.
- Save Responses: Save received server responses to a text file (response.txt) for analysis.

## Components

- GUI Interface: Built using Tkinter for user-friendly interaction.
- Threaded Requests: Uses multithreading to send HTTP requests without freezing the UI.
- Response Management: Captures and displays server responses in real time.

## How It Works
1. Enter the target endpoint URL in the "Endpoint" field.
2. Set the delay interval (in minutes) between requests in the "Delay" field.
3. Click "Start DDoS" to begin sending requests.
4. Monitor responses in the output text area.
5. Click "Stop DDoS" to end the requests.
6. Use the "Save Response" button to save responses to response.txt.

## Usage

1. Clone the repository:
2. Install dependencies:
```bash
pip install requests
```

3. Run the script:
```bash
python app.py
```

## Notes
Legal Compliance: This tool is intended for controlled and ethical testing purposes only. Using it for malicious activities is strictly prohibited.
Future Improvements

### Future Work
- Add error handling for invalid URLs or connection failures.
- Provide logging options for enhanced response tracking.
- Implement rate limiting or burst modes for different testing scenarios.
