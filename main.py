import asyncio, discord, requests, pyttsx3
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
engine = pyttsx3.init()

def hablar(text: str):
    engine.say(text)
    engine.runAndWait() 

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.event
async def respuesta_ante_comando_inexistente(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("¡Comando no encontrado! Usa `$ayuda` para ver la lista de comandos disponibles.")

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
    
@bot.command()
async def ayuda(ctx):
    ayuda_texto = """Comandos disponibles:
    $hola - Saluda al bot
    $clima [ciudad] - Muestra el clima de una ciudad
    $masinfo - Enlaces sobre cambio climático
    $calentamiento_global - Información sobre el calentamiento global
    $emisiones_co2 - Información sobre emisiones de CO2
    $extincion_especies - Información sobre extinción de especies
    $crisis_climatica - Información sobre la crisis climática"""
    await ctx.send(ayuda_texto)

@bot.command()
async def masinfo(ctx):
    info = """Más información sobre cambio climático:
    - Climate Crisis: https://www.un.org/es/un75/climate-crisis-race-we-can-win
    - Causas y Efectos: https://www.un.org/es/climatechange/science/causes-effects-climate-change"""
    await ctx.send(info)
    hablar(info)

def consultar_API_de_clima(city: str) -> str:
    base_url = f"https://wttr.in/{city}?format=%C\n\nTemperatura: %t\nViento: %w\nHumedad: %h\nAmanecer: %S\nAtardecer: %s&lang=es"
    response = requests.get(base_url) 
    return response.text.strip() if response.status_code == 200 else "No se pudo obtener la información del clima."

@bot.command()
async def clima(ctx, *, city: str):
    info_del_clima = consultar_API_de_clima(city)
    await ctx.send(f"Clima en {city}:\n{info_del_clima}")
    hablar(info_del_clima)

@bot.command()
async def calentamiento_global(ctx):
    info = """El calentamiento global es el aumento a largo plazo de la temperatura media del sistema climático de la Tierra.
    • La temperatura global ha aumentado aproximadamente 1.1°C desde 1880
    • Los últimos 7 años han sido los más calientes registrados
    • El nivel del mar sube 3.3mm por año debido al derretimiento de los glaciares"""
    await ctx.send(info)
    hablar(info)

@bot.command()
async def emisiones_co2(ctx):
    info = """Las emisiones de CO2 son la principal causa del cambio climático:
    • Producimos 36.3 mil millones de toneladas de CO2 al año
    • La quema de combustibles fósiles representa el 87% de las emisiones
    • La deforestación contribuye con un 10% adicional de emisiones"""
    await ctx.send(info)
    hablar(info)

@bot.command()
async def extincion_especies(ctx):
    info = """El cambio climático está causando una extinción masiva de especies:
    • 1 millón de especies están en riesgo de extinción
    • Los arrecifes de coral podrían desaparecer para 2050
    • La pérdida de biodiversidad amenaza la seguridad alimentaria global"""
    await ctx.send(info)
    hablar(info)

@bot.command()
async def crisis_climatica(ctx):
    info = """La crisis climática requiere acción inmediata:
    • Necesitamos reducir emisiones un 45% para 2030
    • 100 empresas son responsables del 71% de emisiones globales
    • La transición a energías renovables es crucial para nuestra supervivencia"""
    await ctx.send(info)
    hablar(info)

bot.run("TOKEN")
