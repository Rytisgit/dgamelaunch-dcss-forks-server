#!/bin/bash

source "$DGL_CONF_HOME/dgl-manage.conf"
sed -i 's|games = OrderedDict(trunk + stable_versions + forks)|games = OrderedDict(trunk + forks)|g' "$DGL_CONF_HOME/config.py"
sed -i 's|CONFIG_MORGUE_URL|http://164.92.176.162:8081/morgue/%n/|g' "$DGL_CONF_HOME/config.py"
sed -i 's|CONFIG_SERVER_ID|discount.forks.server|g' "$DGL_CONF_HOME/config.py"
sed -i 's|CONFIG_DGL_SERVER|discount.forks.server|g' "$DGL_CONF_HOME/dgl-manage.conf"
sed -i 's|CONFIG_WEB_SAVEDUMP_URL|http://164.92.176.162:8081/saves|g' "$DGL_CONF_HOME/dgl-manage.conf"
sed -i 's|Welcome to WebTiles!|Welcome to WebTiles! Accounts were reset on 2025-05-31, Create new accounts.|g' "$/crawl-master/webserver/templates/banner.html"
sed -i 's|Welcome to WebTiles!|Welcome to WebTiles! Accounts were reset on 2025-05-31, Create new accounts.|g' "$DGL_CONF_HOME/crawl-build/crawl-git-repository/crawl-ref/source/webserver/templates/banner.html"
cp -r $DGL_CONF_HOME/server/etc/webserver/* $WEBDIR
dgl publish --confirm > /dev/null 2>&1
echo
