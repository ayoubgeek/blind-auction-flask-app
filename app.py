from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Dictionary to store bidders and their bids
auction_list = {}

@app.route('/', methods=["GET", "POST"])
def index():
    """
    Route for the main bidding page.
    Handles both displaying the form (GET) and processing bids (POST).
    """
    if request.method == "POST":
        # Get user input from the submitted form
        name = request.form["name"]
        bid = request.form["bid"]

        # Save bid if it's a valid number
        if name and bid.isdigit():
            auction_list[name] = int(bid)

            # Redirect to same page with success message (as query parameters)
            return redirect(url_for('index', name=name, bid=bid))

    # Render the form, optionally showing a success message
    return render_template("index.html", name=request.args.get("name"), bid=request.args.get("bid"))

@app.route('/winner')
def winner():
    """
    Route to display the winner with the highest bid.
    Returns an error message if no bids were placed.
    """
    if not auction_list:
        return render_template("no_bids.html")

    # Determine the highest bidder
    winner_name = max(auction_list, key=auction_list.get)
    winner_bid = auction_list[winner_name]

    # Show the result page with winner details
    return render_template("winner.html", name=winner_name, bid=winner_bid)

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)