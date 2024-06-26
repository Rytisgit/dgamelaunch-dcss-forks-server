#!/bin/bash
source "$DGL_CONF_HOME/dgl-manage.conf"

cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-testcrawl
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-dcssca
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-hellcrawl
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-gnollcrawl
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-bloatcrawl2
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-gooncrawl
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-xcrawl
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-stoatsoup
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-kimchicrawl
cp -a -n $DGL_CHROOT/crawl-master/crawl-git $DGL_CHROOT/crawl-master/crawl-bcadrencrawl
/home/crawl-dev/dgamelaunch-config/bin/dgl update-trunk
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc testcrawl crawl-forks/feat/free_up_the_inventory
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc6 dcssca crawl-forks/dcssca/bugfix
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc6 hellcrawl crawl-forks/hellcrawl/bugfix
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc6 gnollcrawl crawl-forks/gnollcrawl/bugfix
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc bloatcrawl2 bloatcrawl2/master
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc stoatsoup stoatsoup/master
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc gooncrawl gooncrawl/gooncrawl_stable
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc xcrawl crawl-forks/xcrawl/bugfix
sleep 5
/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc kimchicrawl crawl-forks/kimchicrawl/bugfix
sleep 5
#/home/crawl-dev/dgamelaunch-config/bin/dgl update-gcc bcadrencrawl bcadrencrawl/bCrawl #Currently bcadren crawl main branch `bCrawl` is simply not compiling due to a programming error. I've left a message to bcadren, no need to try compiling until it's fixed