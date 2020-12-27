import discord



class Messages:

    async def welcome_message(self, member):

        await member.create_dm()                                        
        resources = discord.Embed(title="Here are some roommate resources!", color=0xa25d54)
        resources.set_thumbnail(url="https://chicagoagentmagazine.com/wp-content/uploads/2012/04/PIN.jpg")
        resources.add_field(name="========================\nThe Loft Calendar", value="Click **[here](https://calendar.google.com/calendar/u/3?cid=bG9mdDMwMzZAZ21haWwuY29t)**\
                                                            to view the loft calendar\n> We use google calendar to schedule time in the theatre!\
                                                            The calendar can be viewed by everyone. If you'd like to *schedule* events on the calendar,\
                                                            reach out to one of your roommates to be given edit access!", inline=False)
        resources.add_field(name="========================\nRoommate Google Drive Folder", 
                            value="""Click\
                                    **[here](https://drive.google.com/drive/folders/1T4VFb__2OJMa7D3ORVkdVKJ16D_ChvDs?usp=sharing)**\
                                        to open the roommate folder.\n> If you can't find a light switch, or have questions about\
                                        how things work, this google drive folder is a good place to check.\
                                """, inline=False)

        resources.add_field(
            name='========================\nThe House Channel',
            value = f"""> Be sure to check out the **[welcome message](https://discord.com/channels/745756477855367268/745756477855367271/745806031447261214)** \
                in the The House Channel\
                and if it feels right, drop a message introducing yourself! _We're happy you're here!_ <:emoji_name:792429574565789717>\n\n***Welcome to The Lincoln Loft!***"""
        )

        posted_message = await member.dm_channel.send(
            f"""**Hi {member.name}!** 👋  I'm the `Lincoln Loft Bot`! 🤖\n\n""", embed=resources)

        await posted_message.add_reaction('🥳')
        await posted_message.add_reaction('🙌')
        await posted_message.add_reaction('✨')
        await posted_message.add_reaction('🎊')
        await posted_message.add_reaction('🎉')
        await posted_message.add_reaction('🎭')
        await posted_message.add_reaction('🧁')