import asyncio

from pytgcalls import idle

from config import call_py
from Userbot.quote import arq


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @TeamOctave |
    ------------------
"""
    )
    await call_py.join_chat(GROUP_ID, "1001654093157")
    await call_py.send_message(GROUP_ID, "I Used Your Code For Music")
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
