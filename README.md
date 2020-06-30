# Crypto Report Generator
This project creates a report based on your chosen cryptocurrency. The report contains 3 key pieces of data:

* Historical Data - This is a plot that shows the past performance of your chosen cryptocurrency in a given time period.
* Trading Signals Plots - These plots shows key signals that may be useful for traders.
* Latest News - This is a compliation of the latest crypto news

## Project Installation
Once you have downloaded the repository, perform these commands:

1. pip install -r requirement.txt
2. python app.py

## Additional information
### Redis
This project uses Redis to perform a background task so you will need to install Redis and set the local redis url as an environment variable. 

Please set the local redis url as an environment variable in this format:

REDIS_URL: redis://localhost:6379

Please note: For windows users, you will need to install redis using the Windows Subsystem for Linux (WSL) platform. You can learn more here: 
https://medium.com/@RedisLabs/windows-subsystem-for-linux-wsl-10e3ca4d434e

Redis can be downloaded here: https://redis.io/download

### Environment Variables
You will need an api key from https://www.cryptocompare.com/. Please set the api key as an environment variable in this format:
API_KEY: yourapikeyhere

You will also need to set up a test gmail account. Once you've created this account, please enable the feature in gmail settings: 
Allowing less secure apps to access your account

You will then need to set up your gmail email and password as environment variables in this format:
SEND_MAIL_USERNAME: yourgmailusername
SEND_MAIL_PASSWORD: yourgmailpassword



