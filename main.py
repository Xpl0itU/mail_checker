import dotenv
import json
import os
from MailChecker import MailChecker


if __name__ == "__main__":
    dotenv.load_dotenv()
    config = dict()
    with open("config.json", "r") as f:
        config = json.load(f)
    mailchecker = MailChecker(
        os.environ["SERVER"], os.environ["EMAIL"], os.environ["PASSWORD"], os.environ["FOLDER"]
    )
    mailchecker.login()
    checked_mails = mailchecker.check_list_of_mails(
        config["to_check"],
    )
    if checked_mails == []:
        print("No mails checked")
        exit(1)
    ret = 0
    for i in range(len(checked_mails)):
        if not checked_mails[i]:
            print(f"Mail from {config['to_check'][i]['mail']} not found")
    exit(ret)
