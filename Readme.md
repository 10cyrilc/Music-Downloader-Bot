# Spotify Downloader BOT

## Table of Contents
* [What is This BOT?](#What-is-This-BOT?)
* [Setup](#setup)
* [Bugs](#Bugs)
* [My BOT Channel](#My-BOTs-Channel)


## What is This BOT?

### Ever Wondered how to download songs from Spotify?
### This BOT Can help you to download songs from spotify using <a href = "https://github.com/spotDL/spotify-downloader">spotdl</a>

## Setup

### On Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/10cyrilc/spotify-bot)

### On VPS or Locally

#### Without Docker
```
git clone https://github.com/10cyrilc/spotify-bot.git
cd spotify-bot

Edit edit_me.py with Details as Follows,

Get you BOT_TOKEN from @BotFather, Required
Get API_ID and API_HASH from my.telegram.org, Required
Edit BOT_TEXT if Required
Get LOG_CHANNEL from Your Channel Settings for Logging, Required
Your MONGODB_URI from your MongoDB Account, Required
SESSION_NAME for Your Collection Name in MongoDB
BOT_OWNER is The User ID of The Developer, Required

sudo pip3 install virtualenv 
virtualenv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python bot.py
```

#### With Docker
```
Edit the config.py with required Details
Build Dockerfile in the Repo
Run The Docker Image
````

## Bugs

#### This is Currently in Development Stages, So it has Bugs that I am unaware of 
#### If You Find any Bugs Feel Free to contact <a href="https://t.me/c_text_bot">Cyril C Thomas</a>

## My BOTs Channel
<a href="https://t.me/c_bots_support">C BOTs</a>