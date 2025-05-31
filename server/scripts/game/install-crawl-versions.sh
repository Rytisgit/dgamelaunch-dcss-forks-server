#!/bin/bash
source "$DGL_CONF_HOME/dgl-manage.conf"
source "$DGL_CONF_HOME/versions.conf"

for v in $VERSIONS; do
    if [ "$v" == "git" ]; then
        continue
    fi
    cp -a --update=none "$DGL_CHROOT/crawl-master/crawl-init" "$DGL_CHROOT/crawl-master/crawl-$v"
done

dgl update-trunk
dgl update-gcc dcst dcst/test
dgl update-gcc addedcrawl crawl-forks/nostalgia/bugfix 6
dgl update-gcc addedcrawl crawl-forks/yiufcrawl/bugfix 6
dgl update-gcc addedcrawl crawl-forks/oofcrawl/bugfix 6
dgl update-gcc addedcrawl crawl-forks/boggartcrawl/bugfix 6