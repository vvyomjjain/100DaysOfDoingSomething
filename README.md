<h1 align="center">#100DaysOfDoingSomething</h1>

<p align="center"> 
    <img width="200" src="./logo.png" alt="logo">
</p>

<p align="center">
A twitter bot which likes and retweets any tweet containing #100DaysOfDoingSomething
</p>

## Description

This is a twitter bot which is made for motivating people to learn and do development. By tweeting their daily progress, they can let the world know about their efforts. This bot will also provide motivational replies to the users. This will not be just plain reply but dynamically selected from a pool of replies.

## Installation

For this project we need the tweepy library. The version to be installed depends on the version of python. 

1. Check version
   ```bash
   python --version
   ```
2. If you have **Python 3.6**
   ```bash
   pip install tweepy
   ```
3. If you have **Python 3.7**
   ```bash
   pip3 install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b
   ```
 
## Roadmap

- [x] Finding tweets with #100DaysOfDoingSomething
- [x] Liking tweets
- [x] Retweeting those tweets
- [ ] Replying a constant message
- [ ] Replying randomly from a pool of messages

## Usage

The usage of the app needs a developer account for twitter. After signing up for that, follow these steps.

1. Fork and Clone the repo.
2. Make a file **credentials.py**
   ```python
    consumer_key = '<your_consumer_key>'
    consumer_secret = '<your_consumer_secret>'
    access_token = '<your_access_token>'
    access_token_secret = '<your_access_token_secret>'
3. Run **tweetbot.py**
    ```bash
    python tweetbot.py
    ```
## Resources

- [![Video](http://img.youtube.com/vi/W0wWwglE1Vc/0.jpg)](http://www.youtube.com/watch?v=W0wWwglE1Vc)  This video by @ykdojo
- [This guide](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library) by DigitalOcean
