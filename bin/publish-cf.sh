#!/bin/sh

# We'll never read stdin
exec <&-

self_dir=`dirname $0`
self_name=`basename $0`

usage () {
	cat >&2 <<EOF
Usage: $self_name domain-name dist-dir [site-path]
DESCRIPTION
	Uploads distribution from dist-dir to Cloudfront distribution's origin
	S3 bucket and creates invalidation for cloudfront distribution.

	The Cloudfront distribution is selected based on domain-name: it must
	be listed among distribution's aliases.

	Furthermore, distribution's origin must be S3 bucket in form:
	bucket-name.s3.amazonaws.com

	If site-path is given, the distribution is uploaded to this directory
	in the bucket. Otherwise it is uploaded to the root.
EOF
}

echoe () {
	echo "$1" >&2
}
echov () {
	echo "$1" >&2
}

if [ $# -eq 0 ]; then
	usage
	echoe "domain-name must be given."
	exit 1
fi
domain_name="$1"
shift

if [ $# -eq 0 ]; then
	usage
	echoe "dist-dir must be given."
	exit 1
fi
dist_dir="$1"
shift

if [ ! -d "$dist_dir" ]; then
	echoe "$dist_dir does not exist or is not a directory."
	exit 1
fi
subdir="$1"
if [ -n "$subdir" ]; then
	subdir="$subdir/"
fi

if [ ! -f "$dist_dir/index.html" ]; then
	echoe "$dist_dir does not contain index.html."
	echoe "This is a wrong directory."
	exit 1
fi

which aws >/dev/null || exit 1
which jq >/dev/null || exit 1

distribution_id=`aws cloudfront list-distributions \
	--output text \
	--query '(DistributionList.Items[?Aliases.Items[0]=='\'"$domain_name"\''])[0].Id'` \
	|| exit 2

if [ -z "$distribution_id" -o "$distribution_id" = None ]; then
	echoe "Could not determine distribution id."
	exit 2
fi

echov "Distribution id: $distribution_id"

s3_url=`aws cloudfront get-distribution \
	--id "$distribution_id" \
	--output text \
	--query 'Distribution.DistributionConfig.Origins.Items[0].DomainName'` \
	|| exit 2

if [ -z "$s3_url" -o "$s3_url" = None ]; then
	echoe "Could not determine s3 bucket url."
	exit 2
fi

s3_bucket=`expr "$s3_url" : '\(.*\).s3\.amazonaws\.com$'`

if [ -z "$s3_bucket" ]; then
	s3_bucket=`expr "$s3_url" : '\(.*\).s3-website-.*\.amazonaws\.com$'`
fi

if [ -z "$s3_bucket" ]; then
	echoe "S3 bucket url $s3_url is not of form bucket.s3.amazonaws.com or bucket.s3-website-<region>.amazonaws.com"
	exit 2
fi

echov "Origin bucket: $s3_bucket"

echov "Uploading distribution..."

if ! aws s3 sync --delete $dist_dir "s3://$s3_bucket/${subdir}" >&2; then
	echoe "Upload failed! Distribution may be partially updated!"
	exit 3
fi

echov "Creating invalidation..."

if ! aws cloudfront create-invalidation >/dev/null \
	--paths '/*' \
	--distribution-id "$distribution_id"; then
	echoe "Failed to create Cloudfront invalidation."
	echoe "The bucket is already updated, however."
	exit 3
fi

echov "Done"
