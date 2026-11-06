import json

def lade_emails(pfad):
    with open(pfad, encoding="utf-8") as datei:
        emails = json.load(datei)
    return emails

def finde_email(emails, email_id):
    for email in emails:
        if email["id"] == email_id:
            return email
    return None

emails = lade_emails("emails.json")

for email in emails:
    print(f"#{email['id']} - {email['betreff']} - {email['absender']}")


print(finde_email(emails, 2))    # the email from Max (Umzug)
print(finde_email(emails, 99))   # None