# Create Your Own Twitter Bot
## Table of Contents
* [What You Will Need To Start](https://github.com/anish-jampana/Create-Your-Own-TwitterBot/blob/main/README.md#what-you-will-need-to-start)
* [Setting Up A Twitter Development Account](https://github.com/anish-jampana/Create-Your-Own-TwitterBot#setting-up-a-twitter-development-account)
* [Importing Tweepy](https://github.com/anish-jampana/Create-Your-Own-TwitterBot#importing-tweepy)
* [Twitter Bot Source Code](https://github.com/anish-jampana/Create-Your-Own-TwitterBot#twitter-bot-source-code)
* [A Fully Functional Twitter Bot!](https://github.com/anish-jampana/Create-Your-Own-TwitterBot/blob/main/README.md#a-fully-functional-twitter-bot)

## What you will need to start
### Install Python (If you haven't already)
For this project, we will be using python (This bot, specifically, is running on Python 3.7.9). You can download and install at https://www.python.org/downloads/ and check whether it is installed properly on your computer by typing ```python3 --version``` in your terminal. It should output the correct Python version that you've downloaded.

### Install an IDE for Python 
You don't necessarily need an IDE for this project, but it is highly recommended to get used to a specific Python IDE for both this project and future projects. For the Twitter Bot, I used Atom Text Editor which is decently popular among Python Developers. If necessary, download the latest version at https://atom.io/

## Setting up a Twitter Development Account
### Step 1: Fill Out A Twitter Developer Application
Assuming you have a twitter account to use for this project (recommend creating a totally separate account just for this project), go to https://developer.twitter.com/en and log in with your account credentials. Once you're in the Twitter Developer Portal/Dashboard, click "Create New App" and fill out the necessary fields. This can honestly be whatever you want, but make sure the App Permissions are set to "Read, Write, and Direct Messages". This is important because you will want your Twitter Bot to be able to not only read data on Twitter but also post tweets.

### Step 2: Get Keys and Access Tokens
Once your Developer App is completed and approved, all you need to do now is get your API keys and Access Tokens! To do this, go to your Developer Portal/Dashboard and find the app you just created under "Projects". Right next to the settings icon for your project, there should be a key icon on the far right. Click on that to access the necessary keys and tokens for this project. You will need to retrieve the following keys.

```
CONSUMER (API) KEY = 
CONSUMER (API) SECRET = 
ACCESS TOKEN = 
ACCESS SECRET = 
```
Once you have the api key and secret and access token and secret, make sure to save this as you will need them later when writing the code for the Twitter Bot. 
IMPORTANT: MAKE SURE TO NOT SHARE THIS INFO WITH OTHERS AS IT IS PRIVATE FOR YOUR INDIVIDUAL TWITTER ACCOUNT! However, you can always regenerate new keys of course.

## Importing Tweepy
### What is Tweepy?
Tweepy is essentially an open source package for Python that lets your interact with the Twitter API. Tweet + py (the file type for Python) = Tweepy, get it?! Without Tweepy, making a Twitter Bot would be loads complicated, so thank Tweepy for making Twitter Bots fun and easy to create. 

### Downloading Tweepy
To download tweepy, you need to do the following:
```
pip3 install tweepy
```
Specifically for Python 3.7 (in my case):
```
pip3 install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b
```
If ```pip3``` doesn't work, try just ```pip```.

## Twitter Bot Source Code
Go to **twitterbot.py** to find the exact source code for this project. 
Note: You will need to replace **tweets.txt** with another txt file to read through. I've included **sample.txt** in this repository that you can use just to test the bot, but later on, you may want to play around with your own txt file for the bot to tweet. Once, you replace **tweets.txt** with your own file of choice, you will need to copy and paste either **follow.py** or **tweetfile.py** depending on how you are going to use the twitter bot.

### follow.py
**follow.py** is a python file that will allow you to follow all accounts that have followed your twitter bot each time you run **twitterbot.py** once you have copied and pasted **follow.py**

### tweetfile.py
**tweetfile.py** is a python file that will allow to tweet line by line from a txt file. You can set it at whatever interval you like but for this project, it is set to 86400 seconds (24 hours). Once again, you need to copy and paste **tweetfile.py** to **twitterbot.py** to use it.

## A Fully Functional Twitter Bot!
Once you have completed the above steps, you should have a fully working twitter bot! Congrats! Remember, however, that you can only run this locally on your computer as it hasn't been implemented on a server. To run this locally on your terminal, type in your filepath using ```cd filepath/``` up until the python file and press Enter. Then type ```python3 [nameoffile].py``` to test and run the program. 

Note: If you want to run the file on a working server for free, go to https://www.pythonanywhere.com/ and create an account. Go to files on the site and upload **twitterbot[server].py** from this repository and create a task on the site that runs **twitterbot[server].py** automatically, free of charge, on a daily basis.
