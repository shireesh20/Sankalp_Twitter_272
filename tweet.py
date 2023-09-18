"""
@Author: Bhargav
@Purpose: Based on the route provided from HTML, call the twitter apis and perform necessary actions
"""

import tweepy
import config

from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__, static_folder="static")

# Store tweets in a dictionary
tweets = {}


client = tweepy.Client(
    consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET,
)


@app.route("/")
def index():
    print(tweets)
    return render_template("home.html", tweets=tweets)


@app.route("/create_tweet", methods=["POST"])
def create_tweet():
    text = request.form.get("tweetText")

    response = client.create_tweet(text=text)
    tweets[response.data["id"]] = {
        "text": response.data["text"],
        "id": response.data["id"],
    }

    return jsonify(response.data)


@app.route("/delete_tweet/<tweet_id>", methods=["POST"])
def delete_tweet(tweet_id):
    print("in delete route with tweet id, ", tweet_id)
    response = client.delete_tweet(id=tweet_id)
    print(response)
    if tweet_id in tweets:
        del tweets[tweet_id]

    print("deleted tweet")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
