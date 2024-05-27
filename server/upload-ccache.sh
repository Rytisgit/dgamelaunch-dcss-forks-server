#!/bin/bash

tar -czf data/ccache.tar.gz -C data ccache

split -b 100M data/ccache.tar.gz data/ccache_part_

tag=$(date +v%y%m%d%H%M)

gh release create $tag -R refracta/dcss-webtiles-server -t build-ccache -B ccache -n ""

gh release upload $tag data/ccache_part_* -R refracta/dcss-webtiles-server

echo "Compression and upload completed!"