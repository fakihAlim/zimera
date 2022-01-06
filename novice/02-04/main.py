from containers import Readers, Clients, Configs

if __name__ == "__main__":
    Configs.config.override(
        {
            "domain_name": "imap.gmail.com",
            "email_address": "email",
            "password": "password",
            "mailbox": "INBOX",
        }
    )
    email_reader = Readers.er()
    print(email_reader.read())
