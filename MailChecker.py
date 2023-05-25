import datetime
from imap_tools import MailBox, AND


class MailChecker:
    def __init__(self, server: str, user: str, password: str) -> None:
        self.server = server
        self.user = user
        self.password = password

    def login(self):
        self.mailbox = MailBox(self.server).login(self.user, self.password)

    def check_mail(self, mail: str, subject: str) -> bool:
        for _ in self.mailbox.fetch(
            AND(subject=subject, from_=mail, date=datetime.date.today()), limit=1
        ):
            return True
        return False

    def check_list_of_mails(self, to_check: list) -> list:
        results = list()
        for _ in to_check:
            results.append(
                self.check_mail(self.mailbox, to_check["mail"], to_check["subject"])
            )
        return results
