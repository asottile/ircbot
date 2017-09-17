"""Print RT ticket information."""
import re

from ocflib.infra.rt import rt_connection
from ocflib.infra.rt import RtTicket


REGEX = re.compile(r'(?:rt#|ocf.io/rt/)([0-9]+)')


def register(bot):
    bot.listen(REGEX.pattern, show_ticket)


def show_ticket(text, match, bot, respond):
    """Show RT ticket details."""
    rt = rt_connection(user='create', password=bot.rt_password)
    for ticket in REGEX.findall(text):
        try:
            t = RtTicket.from_number(rt, int(ticket))
            respond(str(t))
        except AssertionError:
            pass
