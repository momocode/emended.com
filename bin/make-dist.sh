#!/bin/sh

set -e

cd `dirname $0`/..

prog=`basename $0`

usage () {
	echo "Usage: $prog site-url" >&2
}

if [ $# -lt 1 ]; then
	usage
	exit 1
fi

SITEURL="$1"

if expr "$SITEURL" : '.*/$' >/dev/null; then
	echo "$prog: site-url should not include trailing slash: $SITEURL" >&2
	echo "" >&2
	usage
	exit 2
fi

SITEURL="$SITEURL" pelican -d -s publishconf.py

case "$SITEURL" in
	https://emended.com)
		cp specific/emended.com/* output >&2
		;;
	https://draft.emended.com)
		cp specific/draft.emended.com/* output >&2
		;;
	*)
		echo "Development build for $SITEURL" >&2
		;;
esac
