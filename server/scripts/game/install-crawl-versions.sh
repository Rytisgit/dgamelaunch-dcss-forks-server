#!/bin/bash
source "$DGL_CONF_HOME/dgl-manage.conf"
source "$DGL_CONF_HOME/versions.conf"

for v in $VERSIONS; do
    if [ "$v" == "git" ]; then
        continue
    fi
    cp -a --update=none "$DGL_CHROOT/crawl-master/crawl-init" "$DGL_CHROOT/crawl-master/crawl-$v"
done

dgl update-trunk 2>&1 | ts '[%Y-%m-%d %H:%M:%S]' | tee -a /home/crawl-dev/logs/trunk.log
dgl update-gcc dcst dcst/test 2>&1 | ts '[%Y-%m-%d %H:%M:%S]' | tee -a /home/crawl-dev/logs/dcst.log 
dgl update-gcc nostalgia crawl-forks/nostalgia/bugfix 6 2>&1 | ts '[%Y-%m-%d %H:%M:%S]' | tee -a /home/crawl-dev/logs/nostalgia.log 
dgl update-gcc yiufcrawl crawl-forks/yiufcrawl/bugfix 6 2>&1 | ts '[%Y-%m-%d %H:%M:%S]' | tee -a /home/crawl-dev/logs/yiufcrawl.log 
dgl update-gcc oofcrawl crawl-forks/oofcrawl/bugfix 6 2>&1 | ts '[%Y-%m-%d %H:%M:%S]' | tee -a /home/crawl-dev/logs/oofcrawl.log 
dgl update-gcc boggartcrawl crawl-forks/boggartcrawl/bugfix 6 2>&1 | ts '[%Y-%m-%d %H:%M:%S]' | tee -a /home/crawl-dev/logs/boggartcrawl.log