actions = {
    "apt_update": {
        "cascade_skip": False,
        "command": "apt-get update",
        "expected_return_code": 0,
    },
    "apt_upgrade": {
        "cascade_skip": False,
        "command": "apt-get upgrade -y",
        "expected_return_code": 0,
    },
}