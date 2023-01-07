#! /bin/bash

mplayer_pipe=".mplayer.fifo"
export $mplayer_pipe

if [[ ! -p $mplayer_pipe ]]; then
    mkfifo $mplayer_pipe
fi

i3-msg workspace video
i3-msg exec "mplayer -input file=$mplayer_pipe $1"
i3-msg fullscreen enable
