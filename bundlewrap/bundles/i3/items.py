actions = {
    "apt_update": {
        "cascade_skip": False,
        "command": "apt-get update",
    },
}
actions = {
    "apt_upgrade": {
        "cascade_skip": False,
        "command": "apt-get upgrade -y",
    },
}
pkg_apt = {
    "i3": {
        "installed": True,
    },
    "xorg": {
        "installed": True,
    },
    "tmux": {
        "installed": True,
    },
    "mplayer": {
        "installed": True,
    },
    "chromium-browser": {
        "installed": True,
    },
    "unclutter": {
        "installed": True,
    },
    "xdotool": {
        "installed": True,
    },
}
users = {
    "cccp": {
        "groups": [
            "adm",
            "audio",
            "cdrom",
            "dialout",
            "games",
            "gpio",
            "i2c",
            "input",
            "netdev",
            "plugdev",
            "render",
            "spi",
            "sudo",
            "users",
            "video",
            "tty",
        ],
    },
}
# files = {
#     "/dev/tty2": {
#         "mode": "0660",
#         "content_type": "binary",
#         "group": None,
#         "owner": None
#     },
# }

files = {
    "/home/cccp/.xinitrc": {
        "owner": None,
        "group": None,
        "content_type": "text",
        "source": "xinitrc",
    },
    "/home/cccp/.i3/config": {
        "owner": None,
        "group": None,
        "content_type": "text",
        "source": "i3.config",
    },
    "/home/cccp/start_video": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "start_video.sh",
    },
    "/home/cccp/show_video": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "show_video.sh",
    },
    "/home/cccp/start_stream": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "start_stream.sh",
    },
    "/home/cccp/show_stream": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "show_stream.sh",
    },
    "/home/cccp/start_chrome": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "start_chrome.sh",
    },
     "/home/cccp/mplayer_msg": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "mplayer_msg.sh",
    },
}
