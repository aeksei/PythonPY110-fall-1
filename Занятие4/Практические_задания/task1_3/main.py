import re


def task():
    emails = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz"

    email_pattern = re.compile(r"@(\w+)\.(\w+)")  # TODO используйте запоминающие группы
    print(email_pattern.findall(emails))


if __name__ == "__main__":
    task()
