import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client



        #nqn==========


        @self.client.event
        async def on_message(msg):
            if ":" == msg.content[0] and ":" == msg.content[-1]:
                emoji_name = msg.content[1:-1]
                for emoji in msg.guild.emojis:
                    if emoji_name == emoji.name:
                        await msg.channel.send(str(emoji))
                        await msg.delete()
                        break

            await client.process_commands(msg)

        #error handling

        @self.client.event
        async def on_command_error(ctx,error):
            if isinstance(error,commands.MissingPermissions):
                await ctx.send("You don't have the required permissions")
                await ctx.message.delete()
            elif isinstance(error,commands.MissingRequiredArgument):
                await ctx.send("Please enter all the required arguments")
                await ctx.message.delete()
            else:
                raise error


def setup(client):
    client.add_cog(Events(client))
    