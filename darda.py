import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
import asyncio
import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


webhook_url = 'WEBHOOK'


guvenli_kullanicilar = [404198294898868225, 9876543210]

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yaptı: {bot.user.name}')

@bot.event
async def on_member_join(member):
    try:
        
        if member.id in guvenli_kullanicilar:
            print(f"{member.name}#{member.discriminator} güvenli kullanıcıdır ve sunucudan atılmayacak.")
            return

       
        invite_link = await member.guild.text_channels[0].create_invite(max_age=0, max_uses=1)
        
        
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        
        await member.send(f"Sunucu Davet Bağlantısı: {invite_link}\nGiriş Zamanı: {current_time} Sunucuya girebilmek için hesabını doğrulat \n\n\n[SUNUCUYA GİRMEK İÇİN TIKLA](https://www.erenzy.dev)")

       
        await asyncio.sleep(0.1)  
        await member.kick(reason="Sunucudan atıldı")
        print(f"{member.name}#{member.discriminator} sunucudan atıldı.")

       
        webhook = DiscordWebhook(url=webhook_url, content=f'{member.name}#{member.discriminator} sunucudan atıldı (ID: {member.id})')
        webhook.execute()

    except discord.Forbidden:
        print(f"{member.name}#{member.discriminator} sunucudan atılamadı (yetki eksik).")
    except Exception as e:
        print(f"{member.name}#{member.discriminator} sunucudan atılırken hata oluştu: {e}")


bot.run('TOKEN')