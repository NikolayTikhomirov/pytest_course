import random


class AllData:
    names = ["data", "meta"]
    company_status = ["ACTIVE", "CLOSED", "BANKRUPT"]
    invalid_status = random.choice(["invalid", "INVALID", "invalid_status", "INVALID_STATUS"])