import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


# ======== POST PADRÃO =========
class PostModal(discord.ui.Modal, title="Criar Novo Post"):
                titulo = discord.ui.TextInput(
                    label="📖 Título", placeholder="Digite o título do arquivo")
                por = discord.ui.TextInput(
                    label="🛠 Por", placeholder="Digite o nome do autor")
                idioma = discord.ui.TextInput(label="🌐 Idioma",
                                              placeholder="Ex: Português")
                tamanho = discord.ui.TextInput(label="📦 Tamanho",
                                               placeholder="Ex: 1,55 GB")
                link = discord.ui.TextInput(label="🔗 Link de Download",
                                            placeholder="Cole o link aqui")

                async def on_submit(self, interaction: discord.Interaction):
                                embed = discord.Embed(
                                    title="Bibliotecario -  Acervo Do Nerd",
                                    color=discord.Color.from_rgb(88, 101, 242))
                                embed.add_field(name="📖 Título",
                                                value=f"`{self.titulo.value}`",
                                                inline=False)
                                embed.add_field(name="🛠 Por",
                                                value=f"`{self.por.value}`",
                                                inline=False)
                                embed.add_field(name="🌐 Idioma",
                                                value=f"`{self.idioma.value}`",
                                                inline=False)
                                embed.add_field(
                                    name="📦 Tamanho",
                                    value=f"`{self.tamanho.value}`",
                                    inline=False)
                                embed.add_field(name="🔗 Download",
                                                value=f"`{self.link.value}`",
                                                inline=False)

                                view = discord.ui.View()
                                button = discord.ui.Button(
                                    label="📥 Download",
                                    style=discord.ButtonStyle.link,
                                    url=self.link.value)
                                view.add_item(button)

                                await interaction.response.send_message(
                                    embed=embed, view=view)


# ======== MODS =========
class ModsModal(discord.ui.Modal, title="Postar Mod de Jogo"):
                nome_mod = discord.ui.TextInput(
                    label="🎮 Nome do Mod", placeholder="Digite o nome do mod")
                descricao = discord.ui.TextInput(label="❓ O que é?",
                                                 placeholder="Descreva o mod")
                jogo = discord.ui.TextInput(
                    label="🕹 Qual Jogo",
                    placeholder="Para qual jogo é este mod?")
                link = discord.ui.TextInput(label="🔗 Link para Download",
                                            placeholder="Cole o link aqui")

                async def on_submit(self, interaction: discord.Interaction):
                                embed = discord.Embed(
                                    title="🛠 Mod de Jogo",
                                    color=discord.Color.from_rgb(0, 170, 255))
                                embed.add_field(
                                    name="🎮 Nome do Mod",
                                    value=f"`{self.nome_mod.value}`",
                                    inline=False)
                                embed.add_field(
                                    name="❓ O que é?",
                                    value=f"`{self.descricao.value}`",
                                    inline=False)
                                embed.add_field(name="🕹 Qual Jogo",
                                                value=f"`{self.jogo.value}`",
                                                inline=False)
                                embed.add_field(name="🔗 Download",
                                                value=f"`{self.link.value}`",
                                                inline=False)

                                view = discord.ui.View()
                                button = discord.ui.Button(
                                    label="📥 Download",
                                    style=discord.ButtonStyle.link,
                                    url=self.link.value)
                                view.add_item(button)

                                await interaction.response.send_message(
                                    embed=embed, view=view)


# ======== PROGRAMAS =========
class ProgramaModal(discord.ui.Modal, title="Postar Programa"):
                nome = discord.ui.TextInput(
                    label="💻 Nome do Programa",
                    placeholder="Digite o nome do programa")
                tamanho = discord.ui.TextInput(label="📦 Tamanho",
                                               placeholder="Ex: 500 MB")
                idioma = discord.ui.TextInput(label="🌐 Idioma",
                                              placeholder="Ex: Português")
                link = discord.ui.TextInput(label="🔗 Link para Download",
                                            placeholder="Cole o link aqui")

                async def on_submit(self, interaction: discord.Interaction):
                                embed = discord.Embed(
                                    title="💻 Programa",
                                    color=discord.Color.from_rgb(0, 255, 150))
                                embed.add_field(name="💻 Nome do Programa",
                                                value=f"`{self.nome.value}`",
                                                inline=False)
                                embed.add_field(
                                    name="📦 Tamanho",
                                    value=f"`{self.tamanho.value}`",
                                    inline=False)
                                embed.add_field(name="🌐 Idioma",
                                                value=f"`{self.idioma.value}`",
                                                inline=False)
                                embed.add_field(name="🔗 Download",
                                                value=f"`{self.link.value}`",
                                                inline=False)

                                view = discord.ui.View()
                                button = discord.ui.Button(
                                    label="📥 Download",
                                    style=discord.ButtonStyle.link,
                                    url=self.link.value)
                                view.add_item(button)

                                await interaction.response.send_message(
                                    embed=embed, view=view)


class BotaoModal(discord.ui.Modal, title="Criar até 2 botões personalizados"):
                label1 = discord.ui.TextInput(
                    label="🔘 Texto do botão 1",
                    placeholder="Ex: Canal do Discord")
                link1 = discord.ui.TextInput(label="🔗 Link do botão 1",
                                             placeholder="https://...",
                                             style=discord.TextStyle.short)

                label2 = discord.ui.TextInput(
                    label="🔘 Texto do botão 2 (opcional)", required=False)
                link2 = discord.ui.TextInput(
                    label="🔗 Link do botão 2 (opcional)", required=False)

                async def on_submit(self, interaction: discord.Interaction):
                                view = discord.ui.View()

                                # Botão 1 (obrigatório)
                                view.add_item(
                                    discord.ui.Button(
                                        label=self.label1.value.strip(),
                                        style=discord.ButtonStyle.link,
                                        url=self.link1.value.strip()))

                                # Botão 2 (opcional)
                                if self.label2.value and self.link2.value:
                                                view.add_item(
                                                    discord.ui.Button(
                                                        label=self.label2.
                                                        value.strip(),
                                                        style=discord.
                                                        ButtonStyle.link,
                                                        url=self.link2.value.
                                                        strip()))

                                # Envia apenas os botões (sem embed)
                                await interaction.response.send_message(
                                    view=view)


# ======== BOT =========
@bot.event
async def on_ready():
                await bot.tree.sync()
                print(
                    f"✅ Bot conectado como {bot.user} e comandos sincronizados!"
                )


@bot.tree.command(name="post",
                  description="Cria post de repositorios de arquivos ")
async def post(interaction: discord.Interaction):
                await interaction.response.send_modal(PostModal())


@bot.tree.command(name="mods", description="Postar mod de jogo")
async def mods(interaction: discord.Interaction):
                await interaction.response.send_modal(ModsModal())


@bot.tree.command(name="programa", description="Postar programa")
async def programa(interaction: discord.Interaction):
                await interaction.response.send_modal(ProgramaModal())


@bot.tree.command(name="botao", description="Cria até 2 botões com seus links")
async def botao(interaction: discord.Interaction):
                await interaction.response.send_modal(BotaoModal())


bot.run(os.getenv("DISCORD_TOKEN"))
