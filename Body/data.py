import random
import os


def random_large_text():
    with open("large_text", "r") as file:
        return random.choice(file.readlines())


def delete_html():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.html')
    check_file = os.path.exists(path)
    if check_file:
        os.remove(path)


def company_ogrn():
    with open("companyOGRN", "r") as file1:
        ogrn_list = [i.strip() for i in file1.readlines()]
        return ogrn_list


def ogrnip():
    with open("OGRNIP", "r") as file2:
        ogrnip_list = [i.strip() for i in file2.readlines()]
        return ogrnip_list


REQUEST_TEXT = ('ООО ЛОГИСТИКА ДЛЯ БИЗНЕСА', 'ООО КГАЗС-ИНВЕСТ', 'ООО СПЕЦПРОМТОРГНН', 'НАТС', 'ООО СТАП')
HEADERS = {
    'Content-Type': 'application/json'
}
PAYLOAD_SEARCH = {
    "text": f"{random.choice(REQUEST_TEXT)}",
    "pagination": {
        "page": 1,
        "limit": 20
    },
    "autocomplete": False,
    "filter": {
        "status": [],
        "region": [],
        "activity_main_code_class": [],
        "taxation_system": [],
        "business_size": [],
        "is_ip": [
            "false"
        ]
    },
    "sort": {
        "register_date": "asc"
    }
}
PAYLOAD_EGRIP = {
    "pagination": {
        "page": 1,
        "limit": 10
    },
    "sorting": [
        {
            "column_name": "register_date",
            "sort_type": "desc",
            "priority": 1
        }
    ]
}
PAGINATION = {
    "pagination": {
        "limit": 20,
        "page": 1
    }
}
PAYLOAD_ACTIVITY = {
    "sorting": [
        {
            "column_name": "fullname",
            "priority": 1,
            "sort_type": "asc"
        },
        {
            "column_name": "register_date",
            "priority": 2,
            "sort_type": "asc"
        }
    ]
}
PAYLOAD_INSTANCES = {
    "pagination": {
        "page": 1,
        "limit": 10
    },
    "sorting": [
        {
            "column_name": "register_date",
            "sort_type": "desc",
            "priority": 1
        }
    ]
}
PAYLOAD_LICENSES = {
    "pagination": {
        "page": 1,
        "limit": 20
    },
    "sorting": [
        {
            "column_name": "begin_date",
            "sort_type": "desc",
            "priority": 1
        }
    ],
    "status": ""
}
PAYLOAD_EGRUL = {
    "pagination": {
        "page": 1,
        "limit": 20
    },
    "sorting": [
        {
            "column_name": "register_date",
            "sort_type": "DESC",
            "priority": 1
        }
    ]
}
PAYLOAD_PARTICIPANTS = {
    "pagination": {
        "page": 1,
        "limit": 20
    },
    "sorting": [
        {
            "column_name": "register_date",
            "sort_type": "desc",
            "priority": 1
        }
    ]
}
PAYLOAD_MSP = {
    "pagination": {
        "page": 1,
        "limit": 20
    },
    "form_code": []
}
