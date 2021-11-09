from twilio.rest import Client 


client = Client(
    "ID",
    "oken"
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
