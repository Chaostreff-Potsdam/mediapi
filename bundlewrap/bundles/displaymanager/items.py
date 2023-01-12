pkg_apt = {
    "lightdm": {
        "installed": True,
    },
}
files = {
    "/etc/lightdm/lightdm.conf": {
        "owner": "root",
        "group": "root",
        "mode": "0644",
        "content_type": "text",
        "source": "lightdm.conf",
    },
}
actions = {
    "set graphical boot target": {
        "command": "systemctl set-default graphical.target",
        "expected_return_code": 0,
    },
}
