#!/bin/bash

source "$DGL_CONF_HOME/dgl-manage.conf"
sed -i 's|games = OrderedDict(trunk + stable_versions + forks)|games = OrderedDict(trunk + forks)' "$DGL_CONF_HOME/config.py"
dgl publish --confirm > /dev/null 2>&1
echo
