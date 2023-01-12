pkg_apt = {
    "tmux": {
        "installed": True,
    },
    "mplayer": {
        "installed": True,
        "needs": ["action:apt_update"],
    },
    "chromium-browser": {
        "installed": True,
        "needs": ["action:apt_update"],
    },
    "unclutter": {
        "installed": True,
    },
    "xdotool": {
        "installed": True,
    },
}
