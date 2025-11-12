import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 {len(synced)} comandos sincronizados.")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

# Comando /painel
@bot.tree.command(name="painel", description="Abre o painel do AutoKief.")
async def painel(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Painel AutoKief ⚙️",
        description="Bem-vindo ao painel do AutoKief!\nUse os botões abaixo para gerar e gerenciar suas chaves.",
        color=discord.Color.green()
    )
    embed.set_footer(text="Kief System - AutoKief")

    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Gerar Key 🔑", style=discord.ButtonStyle.green))
    view.add_item(discord.ui.Button(label="Ver Keys 📜", style=discord.ButtonStyle.blurple))
    view.add_item(discord.ui.Button(label="Suporte 💬", style=discord.ButtonStyle.gray, url="https://discord.gg/seulink"))

    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

# Inicie o bot
bot.run("MTQzNzA5MDMzOTkxODgzOTk4MA.GmdLEQ.Gm0O_niDLNDIih1YqYr-kMoRGngA7-VdL-zbIo")
