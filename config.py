import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("BQBqm6Gmadzmm-xQfHRllXUYY_CtYAv_CnQDdAa_NGZuvxvkcq_d6iiDTYUPbnekZdGzuxE1hAoihMP2vtG_VSOJj8bwEnY_Elu2dZRZH9AkZ_zbDFF2nhdlSjz4AfO4q2UZ2STMnjCBPQqGJ7Kyb_aXiErlZJNlIIsn8XFIMg3iUgQ1BSaCHc3ovi96m3izAhPSkyPQgxmhfkwFnWUy6PZjlnteehtZxtildbRJ215xOx1cZ49H_-bytr35KN-qCpjVTp1zq2LxKToTmhdXNvst4oX59b2jwNCLnEbA7W_u-dZM5m6Z4gijHxOIx_c-WJNr1cOsRC9pmJ-5GcJJPF-taIEtjQA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
