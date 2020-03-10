import discord
import random
import threading
from discord import Embed
#時間
import asyncio
import time
from datetime import datetime
from discord.ext import tasks

#ネット
import requests
import sys
import webbrowser
import re
import bs4
import urllib.request, urllib.error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options




client = discord.Client()

options = Options()
options.binary_location = '/app/.apt/usr/bin/google-chrome'
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)




@tasks.loop()
async def loop2():
    await asyncio.sleep(600)
    
    # chromedriverの設定
    global options
    options = Options()
    options.binary_location = '/app/.apt/usr/bin/google-chrome'
    options.add_argument('--headless')
    #ローカル
    """
    options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    driver = webdriver.Chrome(options=options,executable_path="C:/for_python/chromedriver.exe")
    """
    #グローバル
    global driver
    driver = webdriver.Chrome(options=options)
    

loop2.start()  





"""
# ブラウザのオプションを格納する変数をもらってきます。
options = Options()

# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
options.set_headless(True)

# ブラウザを起動する
driver = webdriver.Chrome(chrome_options=options)
"""


@client.event
async def on_ready():
  
    jikken_channel = client.get_channel(678225467756511235)
    await jikken_channel.send(client.user.name+"がログインしました")

@client.event  
async def on_member_join(member):
    #新規メンバー歓迎

    welcome_channel = client.get_channel(659375054185955341)
    welcome_channel1 = client.get_channel(551670688277069831)
    
    if member.guild.id == 659375053707673600:#BOT数センチ鯖なら
        await welcome_channel.send(member.name + "さんがBOT数センチ(略)サーバーに参加しました:tada:\nいらっしゃいませ～^^")
        
    if member.guild.id == 587909823665012757:#無法地帯鯖なら
        await welcome_channel.send(member.name + "さんがbotが占領していた！(略)サーバーに参加しました:tada:\nいらっしゃいませ～^^")

    if member.guild.id == 551401799194640421:#あんず鯖なら
        await welcome_channel.send(member.name + "さんがあんずのお部屋サーバーに参加しました:tada:\nいらっしゃいませ～^^")
        await welcome_channel1.send(member.name + "さんがあんずのお部屋サーバーに参加しました:tada:\nいらっしゃいませ～^^")


    
@client.event
async def on_message(message):
    mcs = message.channel.send

    #掘った芋いじったな？
    if message.content == ("n!time"):
        await mcs(datetime.now().strftime('%H:%M'))

    #メモ帳の中身を読みます
    
    if message.content.startswith("!test read"):
        path_r = 'C:/for_python/pyTEST.txt'
        with open(path_r) as f:
            
            for s_line in f:
                await mcs(s_line)

    if message.content.startswith("!test write"):

        def memocheck(m):
            return m.author == message.author
        await message.channel.send("追加内容を教えて下さい")
        reply = await client.wait_for( "message" , check = memocheck )
        
            
            
        path_w = 'C:/for_python/pyTEST.txt'

        await mcs("ファイルに上書き保存しました")
        s = reply.content

        with open(path_w, mode='a') as f:
            f.write(s+"\n")

    #挨拶コード

    if message.content == "起きてますか？":
        await message.channel.send("起きてます3")

    if message.content.startswith("おはよう"):
        if message.author.bot:
            return
     
        m = "おはよう！" + message.author.name + "さん！"
        await message.channel.send(m)

    if message.content.startswith("こんにちは"):
        if message.author.bot:
            return

        m = "こんにちは！" + message.author.name + "さん！"
        await message.channel.send(m)
            
    if message.content.startswith("こんばんは"):
        if message.author.bot:
            return
        
        m = "こんばんは！" + message.author.name + "さん！"
        await message.channel.send(m)

    #ここら辺ぐちゃぐちゃ

    if message.content.startswith("help"):
        await message.channel.send("1ページ目")

    if message.content.startswith("1ページ目"):
        if message.author.bot:
            emoji = ("\U000025B6")
            await message.add_reaction(emoji)

    if message.content.startswith("2ページ目"):
        if message.author.bot:
            emoji = ("\U000025B6")
            await message.add_reaction(emoji)

    if message.content == ("リアクション"):
        emoji = ("\U000025B6")
        await message.add_reaction(emoji)
        


    if message.content == '/test2':
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
          message_zokusei = dir(message)
          await message.channel.send("```"+str(message_zokusei)+"```")

    
    #数当て
    number_emoji = [":zero:",":one:",":two:",
                    ":three:",":four:",":five:",
                    ":six:",":eight:",":nine:"]
    num_channel = client.get_channel(684626706543542283)
    number = [0,1,2,3,4,5,6,7,8,9]
  
    if message.channel == num_channel:
      
      if message.author.bot:
        return
      
      else:      
        randomnumber_B = str(random.uniform(0, 10))[:1]

        if message.content in str(number):
      
          if message.content == randomnumber_B:#乱数と解答が一致していたら
            await mcs(number_emoji[int(randomnumber_B)])
            await mcs("大正解！")

            
          if message.content != randomnumber_B:#一致していなかったら
            await mcs(number_emoji[int(randomnumber_B)])
            await mcs("不正解！残念でした！またチャレンジしてね")

    #フォーマット練習
            
    if message.content == "フォーマット":

        s = '迫真'
        await mcs(f'右:{s:☆>8}')
        await mcs(f'左:{s:☆<8}')
        await mcs(f'中央:{s:☆^8}')

    if message.content =="テスト":
        await mcs("**テスト1\tテスト2**(t)")
        
    mcs = message.channel.send
    
    #https:で始まる文章ならば
    """
    if message.content.startswith("https:"):
        get_url_info = requests.get(message.content)
        status_code = get_url_info.status_code
            
        if status_code == 200:
            await mcs("存在する(接続可能な)サイトです。")

            with open("test-text.html", "wb") as f:
                f.write(get_url_info.content)

            with open("test-text.html", "wb") as f:
                await mcs(f.read(get_url_info.content))
    """

    #yahoo限定
    if message.content=="よろしく2":
        response = requests.get("https://www.yahoo.co.jp/")
        print(response.text)

        html_doc = requests.get("https://www.yahoo.co.jp/").text
        soup = bs4.BeautifulSoup(html_doc, "html.parser")
        print(soup.prettify())

        elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
        await mcs(elems[0].contents[0])

    if message.content=="よろしく3":
        response = requests.get("https://w4.minecraftserver.jp/#page=1&type=break&duration=daily")
        print(response.text)

        html_doc = requests.get("https://w4.minecraftserver.jp/#page=1&type=break&duration=daily").text
        soup = bs4.BeautifulSoup(html_doc, "html.parser")
        print(soup.prettify())

        elems = soup.find_all("span")
        print(elems)

    if message.content=="よろしく4":
        
        driver.get("https://w4.minecraftserver.jp/#page=1&type=break&duration=daily")
        html = driver.page_source.encode('utf-8')
        soup = bs4.BeautifulSoup(html, "html.parser")
        
    
        #情報を選別
        #全体を取得
        number_one = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3)")
        number_two = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3)")
        number_three = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3)")
  
         
        #整地量系を取得
        number_one_mine = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span.ranked-data")
        number_two_mine = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span.ranked-data")
        number_three_mine = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > span.ranked-data")

        #アイコン
        number_one_img = str(soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > img"))
        icon_url_one = number_one_img[24:-16]
        number_two_img = str(soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > img"))
        icon_url_two = number_two_img[24:-16]
        number_three_img = str(soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > img"))
        icon_url_three = number_three_img[24:-16]
   
        
        #一位の情報！
        if len(number_one_mine.text[4:]) == 9:
            
            MCID = number_one.text[:-42]
            em_bot = discord.Embed(title=MCID,color=0xffd700)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_one)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_one_mine.text[4:])#整地量表示
            await mcs(embed = em_bot)

        if len(number_one_mine.text[4:]) == 10:

            MCID = number_one.text[:-43]
            em_bot = discord.Embed(title=MCID,color=0xffd700)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_one)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_one_mine.text[4:])#整地量表示
            await mcs(embed = em_bot)
            
        #二位の情報！
        if len(number_two_mine.text[4:]) == 9:

            MCID = number_two.text[:-42]
            em_bot = discord.Embed(title=MCID,color=0xc0c0c0)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_two)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_two_mine.text[4:])#整地量表示
            await mcs(embed = em_bot)

        if len(number_two_mine.text[4:]) == 10:

            MCID = number_two.text[:-43]
            em_bot = discord.Embed(title=MCID,color=0xc0c0c0)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_two)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_two_mine.text[4:])#整地量表示
            await mcs(embed = em_bot)
            
        #三位の情報！
        if len(number_three_mine.text[4:]) == 9:

            MCID = number_three.text[:-42]
            em_bot = discord.Embed(title=MCID,color=0xd2691e)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_three)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_three_mine.text[4:])#整地量表示
            await mcs(embed = em_bot)

        if len(number_three_mine.text[4:]) == 10:

            MCID = number_three.text[:-43]
            em_bot = discord.Embed(title=MCID,color=0xd2691e)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_three)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_three_mine.text[4:])#整地量表示
            await mcs(embed = em_bot)
         

    
@tasks.loop()
async def loop():
    await asyncio.sleep(60)
    now = datetime.now().strftime('%H:%M')
    if now == '23:55':
        
        driver.get("https://w4.minecraftserver.jp/#page=1&type=break&duration=daily")
        html = driver.page_source.encode('utf-8')
        soup = bs4.BeautifulSoup(html, "html.parser")

        build_ranking = client.get_channel(686479881843900416)
        bcs = build_ranking.send

        
        #情報を選別
        #全体を取得
        number_one = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3)")
        number_two = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3)")
        number_three = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3)")
  
         
        #整地量系を取得
        number_one_mine = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span.ranked-data")
        number_two_mine = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span.ranked-data")
        number_three_mine = soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > span.ranked-data")

        #アイコン
        number_one_img = str(soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > img"))
        icon_url_one = number_one_img[24:-16]
        number_two_img = str(soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > img"))
        icon_url_two = number_two_img[24:-16]
        number_three_img = str(soup.select_one("#ranking-container > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > img"))
        icon_url_three = number_three_img[24:-16]
   
    
        #一位の情報！
        if len(number_one_mine.text[4:]) == 9:
            
            MCID = number_one.text[:-42]
            em_bot = discord.Embed(title=MCID,color=0xffd700)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_one)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_one_mine.text[4:])#整地量表示
            await bcs(embed = em_bot)

        if len(number_one_mine.text[4:]) == 10:

            MCID = number_one.text[:-43]
            em_bot = discord.Embed(title=MCID,color=0xffd700)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_one)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_one_mine.text[4:])#整地量表示
            await bcs(embed = em_bot)
            
        #二位の情報！
        if len(number_two_mine.text[4:]) == 9:

            MCID = number_two.text[:-42]
            em_bot = discord.Embed(title=MCID,color=0xc0c0c0)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_two)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_two_mine.text[4:])#整地量表示
            await bcs(embed = em_bot)

        if len(number_two_mine.text[4:]) == 10:

            MCID = number_two.text[:-43]
            em_bot = discord.Embed(title=MCID,color=c0c0c0)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_two)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_two_mine.text[4:])#整地量表示
            await bcs(embed = em_bot)
            
        #三位の情報！
        if len(number_three_mine.text[4:]) == 9:

            MCID = number_three.text[:-42]
            em_bot = discord.Embed(title=MCID,color=d2691e)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_three)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_three_mine.text[4:])#整地量表示
            await bcs(embed = em_bot)

        if len(number_three_mine.text[4:]) == 10:

            MCID = number_three.text[:-43]
            em_bot = discord.Embed(title=MCID,color=d2691e)#MCIDをタイトルに
            em_bot.set_thumbnail(url=icon_url_three)#アイコンをサムネイルに
            em_bot.add_field(name = "整地量",value = number_three_mine.text[4:])#整地量表示
            await bcs(embed = em_bot)
        
loop.start()  
    


 
            
                
                 

    

"""
    #ネット取得
    if message.content == "ネット情報":
        get_url_info = requests.get('https://w.atwiki.jp/tohomusicdb/pages/176.html')
        # BeautifulSoup オブジェクトを作成
        bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'html.parser')
        await mcs(type(bs4Obj))

    
        



@client.event
async def on_raw_reaction_add(reaction):

    jikken_channel = client.get_channel(678225467756511235)

    reaction_m = reaction.message_id

    msg = await jikken_channel.fetch_message(reaction_m)
    

    if reaction.channel_id == (678225467756511235):
        if reaction.user_id != (677424892597108747):
            await jikken_channel.send("2ページ目")
            await msg.delete()
"""


@client.event
async def on_raw_reaction_add(reaction):
    
    jikken_channel = client.get_channel(678225467756511235)
    
    await jikken_channel.send("リアクションが押されました(うるさい)")


        

        



    

  
                    
            


client.run("Njc3NDI0ODkyNTk3MTA4NzQ3.XkUDlw.wLqznaUXe9CF6H0nIbLZfReihx0")
