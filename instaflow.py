import requests

g = '\x1b[1;32m'
r = '\x1b[1;31m'
b = '\x1b[1;34m'
c = '\x1b[1;36m'
w = '\x1b[1;37m'

logo = (f"""\033[1;37m
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m╭╮╭╮╭┳━━━┳━━━┳━━━┳━>
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭>
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰>
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭>
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰>
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32m╱╰╯╰╯╰━━━┻━━━┻━━━┻━>
\033[1;34m═══════════════════════════════════════════════
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mGITHUB  \033[1;37m:> Woode-Ahmed
\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mFACEBOOK \033[1;37m:> a.woode.249
\033[1;34m═══════════════════════════════════════════════""")

print(logo)

Username = input(b + "INSTAGRAM USER: ")
print('\033[1;34m𝑺𝑶𝑴𝑬 𝑯𝑨𝑪𝑲𝑬𝑹𝑺 𖠔 | ᏔᏫᏫᎠᎬ ✓')


response = requests.post("https://leofame.com/free-instagram-followers", data={"username": Username})


print(len(response.text))


if "Please Wait 48 hours or submit different instagram account" in response.text:
    print("Please Wait 48 hours or submit different instagram account")
else:
    print(logo)
    print("DONE")