import discord
import random
import json
import datetime
import time
import requests

from discord.ext import commands, tasks
from discord import Embed
from discord.utils import get

version = "Public Beta"
dates = "Public Beta Release Date: 14 June, 2020"

client = commands.Bot(command_prefix='%')
# token = 'Enter your token!'


# ALL DEFINED FUNCTIONS ARE WRITTEN IN THIS SECTION

# DATE FORMATTER
def date_formatter(user_timestamp):

    formatted_month = ""
    year = user_timestamp[0:4]
    month = user_timestamp[5:7]
    day = user_timestamp[8:10]

    if (month == "01"):
        formatted_month = "January"
    elif (month == "02"):
        formatted_month = "February"
    elif (month == "03"):
        formatted_month = "March"
    elif (month == "04"):
        formatted_month = "April"
    elif (month == "05"):
        formatted_month = "May"
    elif (month == "06"):
        formatted_month = "June"
    elif (month == "07"):
        formatted_month = "July"
    elif (month == "08"):
        formatted_month = "August"
    elif (month == "09"):
        formatted_month = "September"
    elif (month == "10"):
        formatted_month = "October"
    elif (month == "11"):
        formatted_month = "November"
    elif (month == "12"):
        formatted_month = "December"

    formatted_datetime = day + " " + formatted_month + ", " + year

    return formatted_datetime


# TIME FORMATTER
def time_formatter(user_timestamp):

    formatted_time = ""
    hour_system = ""

    hour = user_timestamp[11:13]
    minute = user_timestamp[14:16]
    second = user_timestamp[17:19]

    formatted_hour = int(hour) + 6

    if (formatted_hour > 11 and formatted_hour < 24):
        hour_system = "PM"
        if(formatted_hour > 12):
            formatted_hour -= 12
    elif (formatted_hour < 12 and formatted_hour > -1):
        hour_system = "AM"
        if(formatted_hour == 00):
            formatted_hour += 12

    formatted_time = str(formatted_hour) + ":" + minute + \
        ":" + second + " " + hour_system

    return formatted_time


# ALL THE BOT EVENTS ARE WRITTEN IN THIS SECTION

# BOT INITIALIZES HERE
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with DarkRafe's life (¬‿¬)"))
    current_time = str(datetime.datetime.utcnow())
    formatted_date = date_formatter(current_time)
    formatted_time = time_formatter(current_time)

    print('Bot is logged in at: ' + formatted_time +
          "; " + formatted_date + ".\n")


# MEMBER JOINING COMMANDLINE NOTIFICATION
@client.event
async def on_member_join(member: discord.Member):

    # MODIFIED TIMESTAMP
    joined = str(member.joined_at)
    formatted_joined = date_formatter(joined)
    formatted_time = time_formatter(joined)

    # MODIFIED ROLE
    member_role = ""

    try:
        member_role = member.roles[1]
    except:
        member_role = "Not Assigned"

    # EMBEDDED WELCOME MESSAGE
    try:
        if (member.guild.id == '''Guild ID'''):
            embed = Embed(title="🎊 Welcome Message From Dark's Bot 🎉",
                          description="On Behalf Of " + member.guild.name,
                          color=0x069740,
                          timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=member.guild.icon_url)
            embed.add_field(name="🔴 Important Message 🔴",
                            value="Please enter your Riot_ID in the #riot_id text channel.", inline=False)
            embed.add_field(name="Joined Date", value=formatted_joined)
            embed.add_field(name="Joined Time",
                            value=formatted_time, inline=True)
            embed.add_field(name="Role", value=member_role, inline=True)
            embed.add_field(
                name=" (❁´◡`❁) ", value="Thank you for joining us. Enjoy your stay!", inline=False)
            embed.set_footer(text="By DarkRafe - Version: " + version)

            await member.send(embed=embed)
        else:
            embed = Embed(title="🎊 Welcome Message From Dark's Bot 🎉",
                          description="On Behalf Of " + member.guild.name,
                          color=0x069740,
                          timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=member.guild.icon_url)
            embed.add_field(name="🔴 Important Message 🔴",
                            value="We don't bite! So, don't feel shy to join voice channel or send texts.", inline=False)
            embed.add_field(name="Joined Date", value=formatted_joined)
            embed.add_field(name="Joined Time",
                            value=formatted_time, inline=True)
            embed.add_field(name="Role", value=member_role, inline=True)
            embed.add_field(
                name=" (❁´◡`❁) ", value="Thank you for joining us. Enjoy your stay!", inline=False)
            embed.set_footer(text="By DarkRafe - Version: " + version)

            await member.send(embed=embed)
        print(f"{member.display_name} has joined {member.guild.name}!!! 😗")
    except:
        print(
            f"Joining Message Error Occured For {member.display_name} at {member.guild.name} 😶")


# HANDLES ERRORS
@client.event
async def on_command_error(ctx, error):
    print(str(error) + " <----> occurred by: " +
          ctx.author.display_name + " in the " + ctx.author.guild.name + " 😞")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Invalid command, check %help to see all the commands. ❌")
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send("Leave it. It's out of your league! 😏")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Unfortunately, you don't have permission to perform this command. Please, ask the Admins or Moderators for permission. 🙃")


# ALL THE BOT COMMANDS ARE WRITTEN IN THIS SECTION

# PURGES MESSAGES FOR SPECIFIC ROLES
@client.command()
@commands.has_any_role('Dev', 'Mod', 'Admin', 'Moderator')
async def clear(ctx, amount: int):
    if(amount > 0 and amount < 101):
        await ctx.channel.purge(limit=amount+1)
    elif(amount > 100 and amount < 500):
        await ctx.send("Hold your horses! Don't get carried away bruh. Limit is (1-100). 🤨")
    else:
        await ctx.send("WTF is wrong with you? Enter a positive integer within (1-100) ffs. 🤬")


# KICKS MEMBER
@client.command()
@commands.has_any_role('Dev', 'Mod', 'Admin', 'Moderator')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send("Kicked: " + member.display_name)


# BANS MEMBER
@client.command()
@commands.has_any_role('Dev', 'Mod', 'Admin', 'Moderator')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send("Banned " + member.mention)


# UNBANS MEMBER
@client.command()
@commands.has_any_role('Dev', 'Mod', 'Admin', 'Moderator')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name and user.discriminator) == (member_name and member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("Unbanned " + user.mention)
            return


# SHOWS CLIENT SERVER LATENCY
@client.command()
async def ping(ctx):
    member = ctx.author
    await ctx.send(f'{round(client.latency*1000)-270-random.randint(0,5)}ms')

# SENDS BATTLE MESSAGE MENTIONING EVERYONE


@client.command()
@commands.has_permissions(read_message_history=True)
async def battle(ctx):
    await ctx.send("@everyone, anyone up for a scrim?")


# RANDOM ANSWER GENERATOR
@client.command()
@commands.has_permissions(read_message_history=True)
async def ask(ctx, *, question):
    responses = [
        'It is certain!',
        'Without a doubt!',
        'You may rely on it!',
        'Yes, definitely!',
        'It is decidedly so!',
        'As I see it, yes!',
        'Most likely!',
        'Yes!',
        'So far, it looks good!',
        'Signs point to yes!',
        'Reply hazy try again.',
        'Better not tell you now.',
        'Ask again later.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it :(',
        'Outlook not so good :(',
        'My sources say no :(',
        'Very doubtful :(',
        'My reply is no :('
    ]
    await ctx.send(f'Question: {question}\nWise Bot: {random.choice(responses)}')


# SHOWS PLAYERLIST WITH THEIR RIOT ID
@client.command()
@commands.has_permissions(read_message_history=True)
async def playerlist(ctx):
    with open('infos/riot_id.json', 'r') as riot:
        details = json.load(riot)
    with open('infos/riot_id.txt', 'w') as riotf:
        for i in range(len(details['riot_id'])):
            riotf.write(details['riot_id'][i]["Name"] +
                        " : " + details['riot_id'][i]["Riot_ID"] + "\n")
    riotf.close()

    with open('infos/riot_id.txt', 'r') as riotf:
        embed = Embed(description="Requested By: " + ctx.author.display_name,
                      color=ctx.author.color,
                      timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="NAME : RIOT_ID", value=riotf.read())
        embed.add_field(name="Version", value=version, inline=True)
        embed.set_footer(text="By DarkRafe")
        await ctx.send("Player List Of " + ctx.guild.name, embed=embed)
    riotf.close()


# SHOWS PLAYER INFORMATION (NAME, THUMBNAIL, STATUS, ON_PHONE, ROLE, JOIN DATE, CURRENTLY DOING)
@client.command()
@commands.has_permissions(read_message_history=True)
async def userinfo(ctx, *, member: discord.Member):

    # MODIFIED TIMESTAMP
    arrived = str(member.joined_at)
    joined = str(member.created_at)

    formatted_arrived = date_formatter(arrived)
    formatted_joined = date_formatter(joined)

    # MODIFIED STATUS OF MOBILE USER
    mobile = ""
    mobile_user = member.is_on_mobile()
    if (not mobile_user):
        mobile = "❎"
    else:
        mobile = "✅"

    # MODIFIED STATUS OF USER STATUS
    status = ""
    member_status = str(member.status)
    if(member_status == "dnd" or member_status == "DND"):
        status = "Do Not Disturb"
    else:
        status = member_status.upper()

    # MODIFIED ACTIVITY OF USER ACTIVITY
    activity_type = ""
    member_activity = ""

    try:
        activity_type = str(member.activity.type)
    except:
        activity_type = ""

    if (activity_type.lower() == "activitytype.playing"):
        member_activity = "Playing " + str(member.activity.name)
    elif (activity_type.lower() == "activitytype.custom"):
        member_activity = str(member.activity)
    elif (member_activity == ""):
        member_activity = "Sleepin' 😪 ⊙.☉"

    # THE EMBEDDED PLAYER INFORMATION
    embed = Embed(title="User Information",
                  description="Server Name: " + member.guild.name,
                  color=member.color,
                  timestamp=datetime.datetime.utcnow()
                  )
    embed.set_author(name=member.display_name)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="Currently On Phone", value=mobile, inline=True)
    embed.add_field(name="Role", value=member.top_role, inline=True)
    embed.add_field(name="Server Join Date", value=formatted_arrived)
    embed.add_field(name="Discord Join Date",
                    value=formatted_joined, inline=True)
    embed.add_field(name="Activity Status", value=member_activity, inline=True)
    embed.set_footer(text="By DarkRafe - Version: " + version)
    await ctx.send(embed=embed)


# SHOWS SERVER INFORMATION
@client.command()
@commands.has_permissions(read_message_history=True)
async def serverinfo(ctx):

    guild = ctx.guild

    # FORMATTED NAME OF GUILD OWNER
    owner = guild.owner.display_name
    owner_name = "👑 " + str(owner)

    # TEXT CHANNEL COUNT
    count = 0
    text_channel = guild.text_channels
    for channel in text_channel:
        count += 1
    text_channel_count = count

    # VOICE CHANNEL COUNT EXCEPT AFK
    count = 0
    voice_channel = guild.voice_channels
    for channel in voice_channel:
        count += 1
    voice_channel_count = count-1

    # FORMATTED AFK CHANNEL
    if(guild.afk_channel):
        afk_channel = guild.afk_channel.name
    else:
        afk_channel = "No AFK Channel"

    # FORMATTED REGION
    region = str(guild.region)
    formatted_region = region[0].upper()+region[1:]

    # FORMATTED GUILD ROLE EXCEPT @EVERYONE
    guild_role = ""
    for role in guild.roles:
        role_str = str(role)
        if (role_str[-3:].lower() != "bot"):
            guild_role += role_str+"\n"
    guild_role = guild_role[10:]

    # COUNTS ACTIVE MEMBER IN THE SERVER
    active_member_count = 0

    member_list = guild.members
    for member in member_list:
        if ((str(member.status) == "online" or str(member.status) == "idle") and not member.bot):
            #print(str(member.activity.name) + " : " + member.display_name)
            active_member_count += 1
    if (active_member_count == 0):
        active_member_count = "😞"

    # COUNTS OFFLINE MEMBER
    offline_member_count = 0

    for member in member_list:
        if ((str(member.status) == "offline" or str(member.status) == "dnd") and not member.bot):
            offline_member_count += 1
    if (offline_member_count == 0):
        offline_member_count = "🙃"

    # COUNTS BOT
    bot_count = 0

    for member in member_list:
        if(member.bot):
            bot_count += 1

    if (bot_count == 0):
        bot_count = "😞"

    # COUNTS PLAYER
    player_count = 0

    for member in member_list:
        if ((str(member.status) == "online" or str(member.status) == "idle") and not member.bot):
            member_activities = member.activities
            try:
                for i in range(len(member_activities)):
                    if(member_activities[i].name == "VALORANT"):
                        player_count += 1
            except:
                player_count += 0

    if (player_count == 0):
        player_count = "😞"

    # COUNTS OVERWATCH PLAYER
    ow_player_count = 0

    for member in member_list:
        if ((str(member.status) == "online" or str(member.status) == "idle") and not member.bot):
            member_activities = member.activities
            try:
                for i in range(len(member_activities)):
                    if(member_activities[i].name == "Overwatch"):
                        ow_player_count += 1
            except:
                ow_player_count += 0

    if (ow_player_count == 0):
        ow_player_count = "😞"

    # COUNTS OTHER PLAYER
    total_player_count = 0
    other_player_count = 0
    other_player_count_mso = 0
    total_game_name = ""
    game_name = ""
    game_name_mso = ""

    for member in member_list:
        if ((str(member.status) == "online" or str(member.status) == "idle") and not member.bot):
            member_activities = member.activities
            activity_type = ""

            for i in range(len(member_activities)):
                try:
                    activity_type = str(member.activities[i].type)
                except:
                    activity_type = ""

                if (activity_type.lower() == "activitytype.playing" and member_activities[i].name != "Overwatch"):
                    other_player_count_mso += 1
                    game_name_mso += str(member_activities[i].name) + \
                        " - " + member.mention + "\n"
                else:
                    other_player_count_mso += 0

    for member in member_list:
        if ((str(member.status) == "online" or str(member.status) == "idle") and not member.bot):
            member_activities = member.activities
            activity_type = ""

            for i in range(len(member_activities)):
                try:
                    activity_type = str(member.activities[i].type)
                except:
                    activity_type = ""

                if (activity_type.lower() == "activitytype.playing" and member_activities[i].name != "VALORANT"):
                    other_player_count += 1
                    game_name += str(member_activities[i].name) + \
                        " - " + member.mention + "\n"
                else:
                    other_player_count += 0

    for member in member_list:
        if ((str(member.status) == "online" or str(member.status) == "idle") and not member.bot):
            member_activities = member.activities
            activity_type = ""

            for i in range(len(member_activities)):
                try:
                    activity_type = str(member.activities[i].type)
                except:
                    activity_type = ""

                if (activity_type.lower() == "activitytype.playing"):
                    total_player_count += 1
                    total_game_name += str(
                        member_activities[i].name) + " - " + member.mention + "\n"
                else:
                    total_player_count += 0

    if (game_name == ""):
        game_name = "😁"

    if (other_player_count == 0):
        other_player_count = "😁"

    if (game_name_mso == ""):
        game_name_mso = "😁"

    if (other_player_count_mso == 0):
        other_player_count_mso = "😁"

    if (total_game_name == ""):
        total_game_name = "😁"

    if (total_player_count == 0):
        total_player_count = "😞"

    # COUNTS VOICE CONNECTION
    voice_count = 0

    for channel in voice_channel:
        channel_members = channel.members
        for mem in channel_members:
            voice_count += 1

    if (voice_count == 0):
        voice_count = "😞"

    # SERVER CREATION TIME
    server_created_at = guild.created_at
    year = int(datetime.datetime.utcnow().year - server_created_at.year)
    month = (datetime.datetime.utcnow().month - server_created_at.month) - 1

    if month < 0:
        month *= -1

    date = (datetime.datetime.utcnow().day - server_created_at.day)
    if date < 0:
        date += 30

    server_creation = "Year: " + \
        str(year) + " Month: " + str(month) + " Days: " + str(date)

    # THE EMBEDDED SERVER INFORMATION
    if (guild.id == '''Guild ID''' or guild.id == '''Guild ID'''):
        embed = Embed(title="Server Information",
                      description="Server Name: " + guild.name,
                      color=ctx.author.color,
                      timestamp=datetime.datetime.utcnow())
        embed.set_author(name=ctx.author.name)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Owner", value=owner_name)
        embed.add_field(name="Server Age", value=str(
            server_creation), inline=False)
        embed.add_field(name="Region", value=formatted_region)
        embed.add_field(name="AFK Channel", value=afk_channel)
        embed.add_field(name="Roles", value=guild_role, inline=True)
        embed.add_field(name="Member Count", value=guild.member_count)
        embed.add_field(name="Voice Channels", value=voice_channel_count)
        embed.add_field(name="Text Channels",
                        value=text_channel_count, inline=True)
        embed.add_field(name="Active Member", value=str(active_member_count))
        embed.add_field(name="Offline Member", value=str(offline_member_count))
        embed.add_field(name="Playing Valorant",
                        value=str(player_count), inline=True)
        embed.add_field(name="Bot Count", value=str(bot_count))
        embed.add_field(name="Voice Connected", value=str(voice_count))
        embed.add_field(name="Playing Other Games",
                        value=str(other_player_count), inline=True)
        embed.add_field(name="Other Games - Player",
                        value=game_name, inline=True)
        embed.set_footer(text="By DarkRafe - Version: " + version)

        await ctx.send(embed=embed)

    elif (guild.id == '''Guild ID'''):
        embed = Embed(title="Server Information",
                      description="Server Name: " + guild.name,
                      color=ctx.author.color,
                      timestamp=datetime.datetime.utcnow())
        embed.set_author(name=ctx.author.name)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Owner", value=owner_name)
        embed.add_field(name="Server Age", value=str(
            server_creation), inline=False)
        embed.add_field(name="Region", value=formatted_region)
        embed.add_field(name="AFK Channel", value=afk_channel)
        embed.add_field(name="Roles", value=guild_role, inline=True)
        embed.add_field(name="Member Count", value=guild.member_count)
        embed.add_field(name="Voice Channels", value=voice_channel_count)
        embed.add_field(name="Text Channels",
                        value=text_channel_count, inline=True)
        embed.add_field(name="Active Member", value=str(active_member_count))
        embed.add_field(name="Offline Member", value=str(offline_member_count))
        embed.add_field(name="Playing Overwatch",
                        value=str(ow_player_count), inline=True)
        embed.add_field(name="Bot Count", value=str(bot_count))
        embed.add_field(name="Voice Connected", value=str(voice_count))
        embed.add_field(name="Playing Other Games", value=str(
            other_player_count_mso), inline=True)
        embed.add_field(name="Other Games - Player",
                        value=game_name_mso, inline=True)
        embed.set_footer(text="By DarkRafe - Version: " + version)

        await ctx.send(embed=embed)

    else:
        embed = Embed(title="Server Information",
                      description="Server Name: " + guild.name,
                      color=ctx.author.color,
                      timestamp=datetime.datetime.utcnow())
        embed.set_author(name=ctx.author.name)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Owner", value=owner_name, inline=True)
        embed.add_field(name="Server Age", value=str(
            server_creation), inline=False)
        embed.add_field(name="Region", value=formatted_region)
        embed.add_field(name="AFK Channel", value=afk_channel)
        embed.add_field(name="Roles", value=guild_role, inline=True)
        embed.add_field(name="Member Count", value=guild.member_count)
        embed.add_field(name="Voice Channels", value=voice_channel_count)
        embed.add_field(name="Text Channels",
                        value=text_channel_count, inline=True)
        embed.add_field(name="Active Member", value=str(active_member_count))
        embed.add_field(name="Offline Member", value=str(offline_member_count))
        embed.add_field(name="Playing Games", value=str(
            total_player_count), inline=True)
        embed.add_field(name="Bot Count", value=str(bot_count))
        embed.add_field(name="Voice Connected", value=str(voice_count))
        embed.add_field(name="Games - Player",
                        value=str(total_game_name), inline=True)
        embed.set_footer(text="By DarkRafe - Version: " + version)

        await ctx.send(embed=embed)


# MEMBER LIST OF THE SERVER
@client.command()
@commands.has_any_role('Dev', 'Mod', 'Admin', 'Moderator', 'Noobs')
async def memberlist(ctx):
    guild = ctx.guild
    char_count = 0
    line_count = 0

    if (ctx.author.id == '''User ID'''):
        with open('infos/memberlist_' + guild.name + '.txt', "w", encoding="UTF-8") as memberlist_file:
            for member in guild.members:
                memberlist_file.write(
                    member.display_name + "    -    " + str(member.top_role) + "\n")
        memberlist_file.close()

        with open('infos/memberlist_' + guild.name + '.txt', 'r', encoding="UTF-8") as memberlist_file:

            for line in memberlist_file:
                line_count += 1
                for ch in line:
                    char_count += 1

            memberlist_file.close()

        embed = Embed(description="Requested By: " + ctx.author.display_name,
                      color=ctx.author.color,
                      timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(
            name="Message", value="Member List Has Been Created Successfully!", inline=False)
        embed.add_field(name="Character Count", value=char_count, inline=True)
        embed.add_field(name="Line Count", value=line_count, inline=True)
        embed.add_field(name="Version", value=version, inline=True)
        embed.set_footer(text="By DarkRafe")

        await ctx.send(embed=embed)
    else:
        await ctx.send("Leave it. It's out of your league! 😏")


@client.command()
@commands.has_permissions(read_message_history=True)
async def tmp(ctx, number):
    result = requests.get(f'https://api.truckersmp.com/v2/player/{number}')
    result_json = result.json()
    res = result_json['response']

    name = res['name']
    avatar = res['avatar']
    join_date = res['joinDate']
    banned = res['banned']
    is_staff = res['permissions']['isStaff']
    group_color = res['groupColor']

    embed = Embed(description="Requested By: " + ctx.author.display_name,
                  color=ctx.author.color,
                  timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=avatar)
    embed.add_field(name="IGN", value=name, inline=True)
    embed.add_field(name="Staff Member", value=is_staff)
    embed.add_field(name="Current Ban", value=banned, inline=True)
    embed.add_field(name="Joined Date Time", value=join_date, inline=False)

    await ctx.send(embed=embed)
        
        
# JOINS VOICE CHANNEL
@client.command()
@commands.has_permissions(read_message_history=True)
async def bb(ctx):

    channel = ctx.author.voice.channel
    voicechannel = await channel.connect()
    voicechannel.play(discord.FFmpegPCMAudio('audios/yo.mp3'))
    await ctx.send("Playing Yo Yo Yo! 😍")
    time.sleep(13)
    await voicechannel.disconnect()


@client.command()
@commands.has_permissions(read_message_history=True)
async def nolod(ctx):

    channel = ctx.author.voice.channel
    voicechannel = await channel.connect()
    voicechannel.play(discord.FFmpegPCMAudio('audios/nana.m4a'))
    await ctx.send("Playing Nolod! 😍")
    time.sleep(6)
    await voicechannel.disconnect()


@client.command()
@commands.has_permissions(read_message_history=True)
async def oggy(ctx):

    channel = ctx.author.voice.channel
    voicechannel = await channel.connect()
    voicechannel.play(discord.FFmpegPCMAudio('audios/oggy.mp3'))
    await ctx.send("Playing Oggy! 😍")
    time.sleep(6)
    await voicechannel.disconnect()


# SHOWS INFOS OF ACTIVE NON ACTIVITY MEMBER
#
@client.command()
@commands.has_permissions(read_message_history=True)
async def free(ctx):

    guild = ctx.guild
    guild_members = guild.members

    for member in guild_members:
        if((str(member.status) == "online" or str(member.status) == "idle") and not member.bot):
            member_activities = member.activities
            activity_type = ""

            if(len(member_activities) > 0):
                for i in range(len(member_activities)):
                    try:
                        activity_type = str(member_activities[i].type)
                    except:
                        activity_type = "none"

                    if (activity_type.lower() == "activitytype.playing"):
                        result = False
                        break
                    else:
                        result = True
                if (result):
                    await ctx.send(member.mention)
            elif (len(member_activities) == 0):
                await ctx.send(member.mention)

    await ctx.send("Anyone up for a scrim?")


# SECRET MESSAGE
@client.command()
@commands.has_permissions(read_message_history=True)
async def secret(ctx, *, message):
    await ctx.send(message[:1].upper() + message[1:], delete_after=5)
    await ctx.message.delete(delay=5.1)


# ALL THE CUSTOM DEFINED ERROR ARE WRITTEN IN THIS SECTION

# MISSINGREQUIREDARGUMENT EXCEPTION
@ask.error
async def ask_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add a Yes-No question after %ask. 😟")


@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a person after %userinfo. 😟")


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add an integer(whole number) after %clear. 😟")


@bb.error
async def bb_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add a url of your desired song after %bb. 😟")
    elif (str(error) == "Command raised an exception: ClientException: Already connected to a voice channel."):
        await ctx.send("I am busy right now! 🙄")
    elif (str(error) == "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'channel'"):
        await ctx.send("Join a voice channel first! 😑")


@nolod.error
async def nolod_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add a url of your desired song after %nolod. 😟")
    elif (str(error) == "Command raised an exception: ClientException: Already connected to a voice channel."):
        await ctx.send("I am busy right now! 🙄")
    elif (str(error) == "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'channel'"):
        await ctx.send("Join a voice channel first! 😑")


@oggy.error
async def oggy_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add a url of your desired song after %oggy. 😟")
    elif (str(error) == "Command raised an exception: ClientException: Already connected to a voice channel."):
        await ctx.send("I am busy right now! 🙄")
    elif (str(error) == "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'channel'"):
        await ctx.send("Join a voice channel first! 😑")


@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add a secret message after %secret. 😟")
        
        
@tmp.error
async def tmp_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add your truckersmp ID after %tmp. 😟")


client.run(token)
