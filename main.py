import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
import random

API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.reply("🚀 வணக்கம் அஷ்ரஃப்! \n\n/ashraf - உங்க பெயர்ல மெசேஜ்\n/panna - கணிப்பு")

@dp.message(Command('ashraf'))
async def ashraf_command(message: types.Message):
    await message.reply("✨ **அஷ்ரஃப் ஸ்பெஷல்** ✨\n\n🔥 பண்ண பாரென்!\n🚀 100% கரெக்ட்")

@dp.message(Command('panna'))
async def panna_command(message: types.Message):
    predictions = [
        "✅ இன்று உங்கள் நாள் - பண்ண பாரென்! 🚀",
        "🎯 கிரீன் சிக்னல் - 100% வெற்றி! 💚",
        "💰 இன்று ஜாக்பாட் அடிக்கலாம்! ⚡",
        "🔮 பண்ணா பாரென் - சூப்பர் ரிசல்ட்! 💫"
    ]
    await message.reply(f"🔮 **அஷ்ரஃப் ப்ரெடிக்ஷன்** 🔮\n\n{random.choice(predictions)}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
