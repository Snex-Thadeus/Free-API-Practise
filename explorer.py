from twilio.rest import Client 


client = Client(
    "ACa58cc88cde3cedb825651ae997d0c34b",
    "dbe29be7097e1cb4f0ff9a56c5625b23"
)

for msg in client.messages.list()
    print(msg.body)
    msg.delete()

msg = client.messages.create(
    to="+254368762",
    from_="+34657821689",
    body=" Hello snex ....",
)
print (f"Created a new message:" {msg.sid})