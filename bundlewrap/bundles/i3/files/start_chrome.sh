#! /bin/bash
chromium-browser \
	--disable-infobars \
	--kiosk \
	--start-fullscreen \
	--window-size=1920,1080 \
	--incognito \
	--noerrdialogs \
	--disable-translate \
	--no-first-run \
	--fast \
	--fast-start \
	--autoplay-policy=no-user-gesture-required \
    $1