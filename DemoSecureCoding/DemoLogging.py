import datetime

def write_log(log_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {log_message}"
    print(log_entry)

def transfer_fund(sender, recipient, amount):
    log_message = f"Transaction: {sender} transferred {amount}"
    write_log(log_message)

sender = "Hitesh"
recipient = "John"
amount = 2000

transfer_fund(sender,recipient,amount)

