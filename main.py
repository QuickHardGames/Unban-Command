@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):

            await ctx.guild.unban(user)
            embed = discord.Embed(title="Unbanned!",
                                  description=member +
                                  " was given another life by god",
                                  colour=discord.Colour.green())
            embed.add_field(name="reason:",
                            value="Ask the Moderator",
                            inline=False)
            await ctx.send(embed=embed)
            return

    await ctx.send(member + " was not found")
