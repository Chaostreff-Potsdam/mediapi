pkg_apt = {
    "pulseaudio": {
        "installed": True,
    },
}
files = {
    "/home/cccp/.config/pulse/client.conf": {
        "owner": None,
        "group": None,
        "content_type": "text",
        "source": "pulse.conf",
    },
    "/home/cccp/mute.sh": {
        "owner": None,
        "group": None,
        "mode": "0770",
        "content_type": "text",
        "source": "mute.sh",
    },
}
