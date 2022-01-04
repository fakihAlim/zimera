from containers import Readers, Clients, Configs

if __name__ == "__main__":
    Configs.config.override({
        "domain_name": "imap.gmail.com",
        "email_address": "email@email.com",
        "password": "coba",
        "mailbox": "INBOX"
    })
    email_reader = Readers.email_reader()

    print (email_reader.read(('SUBJECT TestSubject')))