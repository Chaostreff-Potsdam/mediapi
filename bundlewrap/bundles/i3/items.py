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
    "set graphical boot target": {
        "command": "systemctl set-default graphical.target",
        "expected_return_code": 0,
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
    "lightdm": {
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
           # "autologin",
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
    # "/home/cccp/.bash_profile": {
    #     "owner": None,
    #     "group": None,
    #     "mode": "0770",
    #     "content_type": "text",
    #     "source": "bash_profile",
    # },
       "/home/cccp/.xsession": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "xsession",
    },
    "/etc/X11/xorg.conf.d/52-resolution-fix.conf":{
        "owner": "root",
        "group": "root",
        "mode": "0644",
        "content_type": "text",
        "source": "resolution-fix.conf",
    },
    # "/etc/systemd/system/getty@tty1.service.d/autologin.conf":{
    #     "owner": "root",
    #     "group": "root",
    #     "mode": "0644",
    #     "content_type": "text",
    #     "source": "autologin.conf"
    # }
    "/etc/lightdm/lightdm.conf":{
        "owner": "root",
        "group": "root",
        "mode": "0644",
        "content_type": "text",
        "source": "lightdm.conf"
    },
}
#
# #systemctl --quiet set-default graphical.target
# cat > /etc/systemd/system/getty@tty1.service.d/autologin.conf << EOF
# [Service]
# ExecStart=
# ExecStart=-/sbin/agetty --autologin $USER --noclear %I \$TERM
# EOF
#           sed /etc/lightdm/lightdm.conf -i -e "s/^\(#\|\)autologin-user=.*/autologin-user=$USER/"
#           disable_raspi_config_at_boot
#