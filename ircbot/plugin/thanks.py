"""Show your appreciation."""
import random


def register(bot):
    bot.listen(r'^thanks', thanks, require_mention=True)
    bot.listen(r'^thank (.*)$', thank_someone, require_mention=True)


def thanks(text, match, bot, respond):
    """Thank create for being a helpful robot."""
    respond(random.choice((
        "you're welcome",
        'you are most welcome',
        'any time',
        'sure thing boss',
    )))


def thank_someone(text, match, bot, respond):
    """Have create thank somebody on your behalf."""
    respond('thanks, {}!'.format(match.group(1)), ping=False)
