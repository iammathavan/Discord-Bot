
# Discord Bot built using python

This is a discord bot project I worked on as one of my side projects. The bot is built using the Python programming language. I have worked on this bot for a few months and added features as time went on. To invoke the bot, the user must either use '$' or '.' every time before a command. For example, $meme will return a meme from Reddit in the channel. The bot has three sub-divisions of commands. They are Economic, Fun, and Administrator. First, the user can play with the bot's own currency system in the Economic portion. They can check their balance, steal coins from other players, work in a job, etc. The ultimate goal of this economic game is to make the users compete with each other and be the wealthiest user on the server. Administrator commands are only invoked if the command user has specific administrative power in the server. They are used to delete messages in channels, kick a member from the server, etc. Last but not least, the Fun commands are just some commands the users can use. They include getting gifs, memes, quotes, profile pictures, etc.

## Installation

Installing Requirements

```bash
  pip install -r requirements.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`BOT_TOKEN` = The bot token

`GIPHY_API_KEY` = Get the API key from [GIPHY](https://developers.giphy.com/dashboard/)

`PRAW_ID` = Get Praw ID from [REDDIT](https://www.reddit.com/dev/api/)

`PRAW_SECRET` = Get it from [REDDIT](https://www.reddit.com/dev/api/)

`REDDIT_USER` = Your Reddit username

`REDDIT_PASS` = Your Reddit password



## Few more changes

Also, change a variable in the constant.py file

`BOT_ID` = Change it to your own bot's ID

Then feel free to edit the bank.json file, and change the ID to your own bot.
## Screenshot

![Screenshot 2022-05-03 145320](https://user-images.githubusercontent.com/78320266/166525503-bc146ab0-844e-4432-ba13-7288f922b79b.png)

## Running the Bot

To run the bot

```bash
  python3 main.py
```


## Documentation

[discord.py](https://discordpy.readthedocs.io/en/stable/)

[python](https://docs.python.org/3/)

[json](https://docs.python.org/3/library/json.html)

[requests](https://docs.python-requests.org/en/latest/)

[giphy_client](https://developers.giphy.com/docs/sdk)

[praw](https://praw.readthedocs.io/en/stable/)


# Invite the Bot

Feel free to invite my bot to your own server and test it. If you have any suggestions, by all means reach out to me.

[INVITE the bot](https://discord.com/api/oauth2/authorize?client_id=930296939675811852&permissions=8&scope=bot)
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/AurthurMorgan)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mathavanp/)
[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/iammathavan/)
## License

[MIT](https://github.com/iammathavan/Discord-Bot/blob/main/LICENCE)

