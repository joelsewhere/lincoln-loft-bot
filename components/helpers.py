from collections.abc import Sequence
import discord

class Helpers:

    async def get_members(self, ctx,role_name):
        role = discord.utils.find(
            lambda r: r.name == role_name, ctx.guild.roles)

        users = []   
        for user in ctx.guild.members:
            if role in user.roles:
                users.append(user)
        return users

    def _message_check(self, channel=None, author=None, content=None, ignore_bot=True, lower=True):
        channel = self._make_sequence(channel)
        author = self._make_sequence(author)
        content = self._make_sequence(content)
        if lower:
            content = tuple(c.lower() for c in content)
        def check(message):
            if ignore_bot and message.author.bot:
                return False
            if channel and message.channel not in channel:
                return False
            if author and message.author not in author:
                return False
            actual_content = message.content.lower() if lower else message.content
            if content and actual_content not in content:
                return False
            return True
        return check

    def _make_sequence(self, seq):
        if seq is None:
            return ()
        if isinstance(seq, Sequence) and not isinstance(seq, str):
            return seq
        else:
            return (seq,)