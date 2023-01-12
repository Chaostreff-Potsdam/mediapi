pkg_apt = {
    "xorg": {
        "installed": True,
    },
    "autorandr": {
        "installed": True,
    },
}
files = {
    "/home/cccp/.xinitrc": {
        "owner": None,
        "group": None,
        "content_type": "text",
        "source": "xinitrc",
    },
    "/home/cccp/.xsession": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "xsession",
    },
    "/etc/X11/xorg.conf.d/52-resolution-fix.conf": {
        "owner": "root",
        "group": "root",
        "mode": "0644",
        "content_type": "text",
        "source": "resolution-fix.conf",
    },
}
