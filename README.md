# Blind Auction Web App

This is a simple blind auction web application built using Python and Flask. Users can submit anonymous bids, and once bidding is closed, the app reveals the highest bidder as the winner.

## Features

- Submit a name and a secret bid.
- All bids are stored in memory during runtime.
- Displays the winner with the highest bid.
- Handles cases where no bids are submitted.
- Clean, minimal HTML template structure using Jinja2.

## Tech Stack

- **Backend:** Python 3.11+, Flask
- **Frontend:** HTML5, Jinja2 templating
- **Version Control:** Git

## Project Structure

bidProjects
app.py               # Main Flask app logic
Templates/
        index.html       # Bid submission page
        no_bids.html     # Message when no bids are found
        winner.html      # Winner display page

## Getting Started

### 1. Clone the Repository

### bash
git clone https://github.com/ayoubgeek/blind-auction-flask-app.git
cd blind-auction-flask-app

## 2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # For Unix/macOS
venv\Scripts\activate     # For Windows

## 3. Install Dependencies
pip install -r requirements.txt

If you don’t have requirements.txt yet, install Flask manually:
pip install Flask

## 4. Run the App
python app.py

### Visit http://127.0.0.1:5000 in your browser to access the app.

## How It Works
	•	Users are prompted to enter their name and bid on the homepage.
	•	Submitted bids are stored in a dictionary in memory.
	•	When the bidding session ends, the app checks who placed the highest bid and displays the winner.
	•	If no bids were made, a separate message is shown.

⸻

## Example Output
	•	Bid Submission Page: Input your name and your bid securely.
	•	No Bids Page: “No bids have been placed yet.”
	•	Winner Page: “Congratulations [Name], you won with a bid of $[Amount]!”

⸻

## Notes
	•	This app is intended for educational and demonstration purposes.
	•	Data is stored temporarily in memory and will reset on every server restart.

⸻

License

This project is open-source and available under the MIT License.