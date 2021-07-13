#Import necessary packages
import discord
from discord.ext import commands
import yfinance as yf
from regFunctions import * #Rounding and colour functions are in this file
import plotly.graph_objs as plotter

#Create discord client
client = commands.Bot(command_prefix="$",help_command=None)

#Create a price command
@client.command(name="price")
async def price(context, arg):
    arg = toUpper(arg)

    #Verify the symbol exists
    exists = exist(arg)
    if not exists:
        await context.message.channel.send("Sorry! That symbol does not exist. Only Canadian and American listings are supported.")
        return

    #Obtain the price
    data = yf.download(tickers=arg, period='1d', interval='1m')
    price = roundTwo(data["Close"][-1])

    #Obtain visuals for embed
    ticker = yf.Ticker(arg)
    all_info = ticker.info
    name = all_info['longName']
    logo = all_info['logo_url']

    #Obtain values for embed
    open = roundTwo(all_info['open'])
    high = roundTwo(all_info['dayHigh'])
    low = roundTwo(all_info['dayLow'])

    #Determine right colour for embed, green means increase from open red means decrease
    percent = percentCalc(open,data["Close"][-1])
    colour = higherLower(open,data["Close"][-1])

    #Create the embed
    myEmbed = discord.Embed(title=name,color = colour)
    myEmbed.set_thumbnail(url=logo)
    myEmbed.add_field(name="Price",value=f"{price} ({percent})",inline=False)
    myEmbed.add_field(name="Open",value=open,inline=False)
    myEmbed.add_field(name="High",value=high,inline=False)
    myEmbed.add_field(name="Low",value=low,inline=False)

    #Send the embed
    await context.message.channel.send(embed=myEmbed)

#Command to get information on a certain stock
@client.command(name="info")
async def info(context,arg):
    arg = toUpper(arg)

    #Verify stock exists
    exists = exist(arg)
    if not exists:
        await context.message.channel.send("Sorry! That symbol does not exist. Only Canadian and American listings are supported.")
        return

    #Gather info on stock
    ticker = yf.Ticker(arg)
    all_info = ticker.info
    name = all_info['longName']
    logo = all_info['logo_url']
    website = all_info['website']
    country = all_info['country']
    industry = all_info['industry']
    open = roundTwo(all_info['open'])

    #Download data to determine right colour of embed and price
    data = yf.download(tickers=arg, period='1d', interval='1m')
    price = roundTwo(data["Close"][-1])
    percent = percentCalc(open,data["Close"][-1])
    colour = higherLower(open,data["Close"][-1])

    #Create the embed and send it
    myEmbed = discord.Embed(title=name,color = colour, url = website)
    myEmbed.add_field(name="Price",value=f"{price} ({percent})",inline=False)
    myEmbed.add_field(name="Symbol",value=arg,inline=False)
    myEmbed.add_field(name="Country",value=country,inline=False)
    myEmbed.add_field(name="Industry",value=industry,inline=False)
    myEmbed.set_thumbnail(url=logo)
    await context.message.channel.send(embed=myEmbed)

#Create a command to graph the intra-day values of a stock given a time interval
@client.command(name="graph")
async def graph(context, arg, arg_two):
    arg = toUpper(arg)

    #Verify the stock exists
    exists = exist(arg)
    if not exists:
        await context.message.channel.send("Sorry! That symbol does not exist. Only Canadian and American listings are supported.")
        return

    #Verify a valid interval is given
    valid_interval = interval(arg_two)
    if not valid_interval:
        await context.message.channel.send("Invalid time interval, 15m showed by default")
        arg_two = '15m'

    #Gather the name of the stock
    ticker = yf.Ticker(arg)
    all_info = ticker.info
    name = all_info['longName']
    open = roundTwo(all_info['open'])

    #Download stock price data using given interval
    data = yf.download(tickers= arg, period='1d', interval=arg_two)

    #Create the graph
    fig = plotter.Figure()
    fig.add_trace(plotter.Candlestick(x=data.index,open=data["Open"],high=data["High"],low=data["Low"],close=data["Close"],name = f"{arg} Graph"))

    #Modify graph layouts to be more visually appealing
    fig.update_layout(
        title=f"{name} 1 Day Stock Chart",
        xaxis=dict(
            title = "Time",
            rangeslider_visible = False,
            gridcolor = 'rgb(80,80,80,0)'
        ),
        yaxis = dict(
            title = "Price",
            gridcolor = 'rgb(80,80,80,0)'
        ),
        font=dict(
            size=18,
            color="White",
            family = "Raleway"
        ),
        margin=dict(t=50,b=0,l=0,r=10),
        paper_bgcolor='rgb(47,49,54,0)',
        plot_bgcolor='rgb(47,49,54,20)',
    )

    #Determine side colour of the embed
    minData = yf.download(tickers= arg, period='1d', interval='1m')
    colour = higherLower(open,minData["Close"][-1])

    #Write the graph as an image and save it to the images directory as fig1
    fig.write_image("images/fig1.png")
    file = discord.File("images/fig1.png")

    #Create the embed, attaching the graph and send it to the channel
    myEmbed = discord.Embed(color=colour)
    myEmbed.set_image(url="attachment://fig1.png")
    await context.send(file = file, embed=myEmbed)

#Create a ping command to send latency of bot
@client.command(name="ping")
async def ping(context):
    myEmbed = discord.Embed(title="Ping Reply",color = 0x738ADB)
    myEmbed.add_field(name="Pong 🏓",value=str(int(client.latency * 1000)) + " ms",inline=False)
    await context.send(embed=myEmbed)

#Create a github command to show github link
@client.command(name="github")
async def github(context):
    myEmbed = discord.Embed(title="Github Reply",description = "This stock bot was made as a side project to help develop some of my coding skills. Glad to see you like it! Check out the [Github link](https://github.com/Momin-C) to see some of my other projects and view this bot's source code", color = 0x738ADB)
    await context.send(embed=myEmbed)

#Create a help command to guide users on how to use the bot
@client.command(name="help")
async def help(context):
    myEmbed = discord.Embed(title="Commands",description = "This stock bot shows information from prices listed on US and Canadian Stock exchanges! All monetary values are in USD",color = 0x738ADB)
    myEmbed.add_field(name="$help",value="Shows all available commands",inline=False)
    myEmbed.add_field(name="$ping",value="Returns pong and bot stats",inline=False)
    myEmbed.add_field(name="$github",value="Shows the github repository link",inline=False)
    myEmbed.add_field(name="$price Symbol",value="Shows the current price (USD) and the day's values for the given stock symbol as well as percent change from open",inline=False)
    myEmbed.add_field(name="$info Symbol",value="Gives information about the given stock symbol",inline=False)
    myEmbed.add_field(name="$graph Symbol Interval",value="Graphs the stock chart for intra-day using the given interval, valid intervals are 1m, 2m, 5m, 15m, 30m, 1h, 90m",inline=False)
    await context.send(embed=myEmbed)

#When the bot is active, send a message to the general channel instructing users to use the $help command
@client.event
async def on_ready():
    q = open("ServerID.txt","r")
    server_ID = int(q.read())
    
    general_channel = client.get_channel(server_ID)
    await general_channel.send("Bot is up and ready! Use $help to view commands")

#Run client on server by reading the bot token from another file
f = open("ClientID.txt","r")
TOKEN = f.read()
client.run(TOKEN)