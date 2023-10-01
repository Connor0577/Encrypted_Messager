import random
import math
from textwrap import wrap
from email.message import EmailMessage
import ssl
import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication
import os

jumbo = {"A": "juq3w", "a": "dji2n", "B": "wp1dn", "b": "s0lzu", "C": "ms5yb", "c": "oskq6", "D": "WP8fE", "d": "Gmp9U", "E": "ph4zf", "e": "y2qDc", "F": "JGV6A", "f": "vGS7a", "G": "bgh8U", "g": "v9fCS", "H": "XY3vZ", "h": "ddx2u", "I": "XS5xs", "i": "yC1Dx", "J": "bf2vK", "j": "cFA8a",
"K": "DqI2u", "k": "kL5yN", "L": "fE2QN", "l": "of7YU", "M": "S4xYL", "m": "WT7XB", "N": "U8lLU", "n": "iSy9W", "O": "dZ0aI", "o": "Exv4x", "R": "YMD3v", "r": "Mu2Px", "S": "cz7UE", "s": "uv4rQ", "T": "yln2i", "t": "tmq5y", "U": "NvH6Y", "u": "RGh8w", "V": "XIQ3g", "v": "lvJ4M", "W": "bRB8n",
"w": "ln3GM", "X": "sc2uT", "x": "DoT5f", "Y": "SR2uG", "y": "gcw6q", "Z": "ue5Sb", "z": "dt9Fn", "0": "IaI4f", "1": "dkZ7K", "2": "ro6KW", "3": "ko4Id", "4": "Zo3hn", "5": "IqI5J", "6": "Wf6Sx", "7": "La2RT", "8": "Jj4lq", "9": "In5Ym", ".": "rF8WT", "?": "bd9tf", ",": "JqG0A", "!": "Yhl1D",
"@": "yKS7m", "#": "l3zrU", "$": "mt7Jm", " ": " "}


key_list = list(jumbo.keys())
val_list = list(jumbo.values())

print("\nTop secret communication\n\n")

choice = input("Would you like to Encrypt or Decrypt something? Enter e/d ")

if choice == "e":
    start = input("\nWhat to encrypt: ")

    encrypted =  ""

    for element in start:
        if element in jumbo:
            encrypted += jumbo[element]
    
    from_addr = "example@gmail.com"
    email_password = '''Your gmail or other SMTP service password'''
    to_addr = "example@gmail.com"
    subject = 'Encypted Communication' 
    content = encrypted

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_addr, email_password)
        smtp.sendmail(from_addr, to_addr, msg.as_string())
    
    print("\nEncrypted Message Sent to your email!\n")


else:
    finish = input("\nWhat message would you like to decrypt? ")

    sasha = finish.split(" ")

    lengthy = len(sasha)
    decrypted = ""

    for i in range(int(lengthy)):
        if sasha[i] != "":
            separated = wrap(sasha[i], 5)
            for x in separated:
                if x in jumbo.values():
                    position = val_list.index(x)
                    decrypted += (key_list[position])
            decrypted += " "

    print("\n" + decrypted + "\n")


