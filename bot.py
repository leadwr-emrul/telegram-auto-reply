from telethon import TelegramClient, events

api_id = 35558481
api_hash = "1d844047bd1d2069069b528637c90c00"

client = TelegramClient("session", api_id, api_hash)

AUTO_REPLY = """
✨ DKWin ✨
🎨 Color Trading Platform 🎨

━━━━━━━━━━━━━━━━━━━
💼 আমাদের সাথে কাজ করলে ইনশাল্লাহ ভালো প্রফিট করার সুযোগ পাবেন
━━━━━━━━━━━━━━━━━━━

🔗 Registration Link 👇
https://dkwin9.com/#/register?invitationCode=186731981267

━━━━━━━━━━━━━━━━━━━
📩 এটি একটি অটো রিপ্লাই সেট করা
🙏 অনুগ্রহ করে কেউ বিরক্ত হবেন না
━━━━━━━━━━━━━━━━━━━
"""

replied_users = set()

@client.on(events.NewMessage(incoming=True))
async def handler(event):

    if not event.is_private:
        return

    sender = await event.get_sender()

    if sender.is_self:
        return

    if sender.bot:
        return

    if sender.id in replied_users:
        return

    replied_users.add(sender.id)

    await event.reply(AUTO_REPLY)

print("Bot Running...")

client.start()
client.run_until_disconnected()
