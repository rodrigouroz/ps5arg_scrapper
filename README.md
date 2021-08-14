# PS5 scrapper

Based on the idea of the [Housing scrapper](https://github.com/rodrigouroz/housing_scrapper) I developed a script to check availability of a PS5 in stores in Argentina (it's sold out everywhere)

## Instalation
This was tested with Python 3.8.

To install dependencies:

`pip3 install -r requirements.txt`

## Configuration

There's a `configuration.sample.yml` that you can use as a template for your configuration. Copy that file to a new one in the root folder and name it `configuration.yml`

You need to configure two aspects of the script: the listing providers and the notifier.

For the notifier you need to create a Telegram bot first: [Create a Telegram bot](https://core.telegram.org/bots)

Creating the bot will give you an authorization token. Save it for later, you'll need it.

A bot can't talk with you directly, you have two options: you talk to it first, thus allowing it to reply to you, or you can add it to a group. Whatever option you choose, you need to get the `chat_id` of either your account or the group.

After you've done either of the above, run this little script to find the `chat_id` (replace with your authorization token):

```python
import telegram
bot = telegram.Bot(token=MY_TOKEN)
print([u.message.chat.id for u in bot.get_updates()])
```
You'll see a list with an element, that's the `chat_id` you need to save for later. Write it down :-)

With the authorization token and the chat id you can now configure the notifier. Here's an example:

```yaml
notifier:
    enabled: true
    chat_id: <CHAT_ID>
    token: <TOKEN>
```

If you have issues with SSL certificates you can disable SSL validation with the attribute `disable_ssl`, by default it is enabled.

You're all set. Now run `python3 main.py` and sit tight!

## Running

That's up to you. What I've found more useful is to run it once an hour. For that I put it in the crontab:

`0 * * * * cd /<PATH_TO_PROJECT>/ps5arg_scrapper && python3 main.py >> run.log 2>&1`
