#!/bin/sh

function alive () {
  kill -0 $1 >/dev/null 2>&1
}

port=${1-8000}
(
cd `dirname $0`/../output || exit 1
exec python -m http.server -b 127.0.0.1 "$port"
) &
pid=$!
sleep 1
if ! alive $pid; then
	echo "Failed to start http server" >&2
	exit 2
fi
SITEURL="http://127.0.0.1:$port" pelican -dr -s publishconf.py
