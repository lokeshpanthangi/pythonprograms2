total_emails = int(input("Total Emails :"))
emails_with_free = int(input("Emails with Free :"))
spam_emails = int(input("Spam Emails :"))
spam_and_free = int(input("Spam and Free :"))

Spam = spam_emails / total_emails
Free = emails_with_free / total_emails
Free_Spam = spam_and_free / spam_emails

print(Free_Spam)