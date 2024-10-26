from discord import app_commands
from discord.ext import commands
import discord
from ayarlar import ayarlar, DEVELOPERS_IDS
import random
import time
import os



description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

#Komutların sınıfı
class CommandTree(app_commands.CommandTree):
    async def on_error(self, interaction: discord.Interaction[discord.Client], error: app_commands.AppCommandError) -> None:
        #Hata işeleme: Slash komutlarında hata oluşursa
        await interaction.response.send_message(f"Komutta bir hata oluştu: {error}")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
help_command = "help"
tree_cls = CommandTree

bot = commands.Bot(command_prefix='-', description=description, intents=intents, tree_cls=tree_cls)
GUILD_ID = discord.Object(id=829299088046424074)

#Bot çalışınca olacaklar.
@bot.event
async def on_ready():
    #Slash komutları senkronize edilip edilmediğini doğruluyoruz.
    """
    try:
        bot.tree.sync()
        print(f"{bot.user} giriş yaptı ve slash komutları senkronize edildi.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    """
    await bot.tree.sync(guild=GUILD_ID) #Salsh komutlarını Discord'a kaydetme veya güncelleme.
    activity = discord.Game("Bir şey")
    await bot.change_presence(activity=activity) #Bota 'oynuyor' etkinliği veriyoruz
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_disconnect(self):
    print(f"{bot.user} çıkış yaptı. (ID: {bot.user.id})")

@bot.command()
async def on_command_error(ctx, error):
    await ctx.send(f"Bir hata oluştu: {error}")

@bot.command()
async def hybrid_command(ctx):
    await ctx.send("Bu komutu kullanamazsınız.")


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def onDestroy(ctx):
    """Botu kapatma komutu"""
    await ctx.send("Bot kapatılıyor o7")
    time.sleep(1)
    await bot.close()

# Dosya gönderme komudu. Örnek olarak 'images' klasöründeki resimlerden rastgele seçer.
@bot.command()
async def mem(ctx):
    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

#Burada slash komutları yer alır.

@bot.tree.command(name="hi", description="Botu selamla")
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message(f"As, {interaction.user.mention}")

@bot.tree.command(name="ondestroy", description="Yalnızca geliiştiricler için.")
async def ondestroy(interaction: discord.Interaction):
    if interaction.user.id in DEVELOPERS_IDS:
        #Geliştirici ise
        await interaction.response.send_message(f"Bot kapatılıyor o7 \n Kapatan: {interaction.user.mention}")
        time.sleep(1)
        await bot.close()
    else:
        await interaction.response.send_message("Bu komutu kullanamazsın :x: ")

@bot.tree.command(name="test", description="Test command")
async def test(interaction: discord.Interaction, deger: str):
    await interaction.response.send_message(f"Değer: {deger}")

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")




bot.run(ayarlar["TOKEN"])