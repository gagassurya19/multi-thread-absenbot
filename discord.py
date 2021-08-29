import requests

urlwebhook = str(input('Masukkan urlwebhook: '))
print(urlwebhook)
class sendMessage:
    def info(message, userLength, room):
        content = "```🔔 [INFO] " + str(message) + " | Jumlah akun: " + str(userLength) + " | Server: " + str(room) + "```"
        send(content)
    
    def warning(user, message, time):
        content = "``` ⚠️ [WARNING] " + user + " | " + str(message) + " | " + str(time) + "```"
        send(content)
    
    def done(message):
        content = "```🥳 [DONE] " + message + " | Check please 👉 https://bit.ly/siakad-absen```"
        send(content)

    def success(user, time):
        content = "> :white_check_mark: [SUCCESS] " + user + " | " + str(time)
        send(content)

    def failed(user, time):
        content = "> :name_badge: [FAILED] " + user + " | " + str(time)
        send(content)
        
def send(message):
    
    # DEMO
    # urlwebhook = "https://discord.com/api/webhooks/880392824091189248/TZ_g1OA38OJaOce7BxL8FBEaugXXzdU9eegnCYgWkwrXJ6bTK2Hxe4rXblGnHeiUYO6r"
            
    # ROOM1
    # urlwebhook = "https://discord.com/api/webhooks/880445221840777237/emXvfNQCscaZFeglslJ26pQ6CJUs7urbl1l1NMOG5K-g_MD6UWbaYLPVTXHUp7yKVGx-"
    
    # ROOM2
    # urlwebhook = "https://discord.com/api/webhooks/880445567161991168/FtQSGXreL3FG3IdMEpElKpl6hB2jlRMcX3WF3BI2COP3Tpmu5GjtSbkh1Pj2PXdFR1Rg"

    data = {"content": message}
    response = requests.post(urlwebhook, json=data)