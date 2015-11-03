import logging
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

dgl_mode = True

bind_nonsecure = True # Set to false to only use SSL
bind_address = ""
bind_port = 8080

logging_config = {
    "filename": "%%CHROOT_WEBDIR%%/run/webtiles.log",
    "level": logging.INFO,
    "format": "%(asctime)s %(levelname)s: %(message)s"
}

password_db = "%%CHROOT_LOGIN_DB%%"

static_path = "%%CHROOT_WEBDIR%%/static"
template_path = "%%CHROOT_WEBDIR%%/templates/"

# Path for server-side unix sockets (to be used to communicate with crawl)
server_socket_path = None # Uses global temp dir

# Server name, so far only used in the ttyrec metadata
server_id = "cao"

# Disable caching of game data files
game_data_no_cache = False

# Watch socket dirs for games not started by the server
watch_socket_dirs = True

# Game configs
# %n in paths is replaced by the current username
games = OrderedDict([
    ("dcss-0.17", dict(
        name = "DCSS 0.17",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.17" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.17/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.17/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl17/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.17", dict(
        name = "Sprint 0.17",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.17" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.17/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.17/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl17-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    

    ("dcss-git", dict(
        name = "DCSS trunk",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        send_json_options = True,
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl-git/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-git", dict(
        name = "Sprint trunk",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        send_json_options = True,
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl-git-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    
    ("dcss-0.16", dict(
        name = "DCSS 0.16",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.16" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.16/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.16/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl16/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.16", dict(
        name = "Sprint 0.16",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.16" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.16/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.16/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl16-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),

    ("dcss-0.15", dict(
        name = "DCSS 0.15",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.15" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.15/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.15/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl15/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.15", dict(
        name = "Sprint 0.15",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.15" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.15/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.15/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl15-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("zd-0.15", dict(
        name = "Zot Defence 0.15",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.15" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.15/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.15/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl15-zotdef/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-zotdef"])),

    ("dcss-0.14", dict(
        name = "DCSS 0.14",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.14" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.14/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.14/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl14/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.14", dict(
        name = "Sprint 0.14",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.14" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.14/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.14/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl14-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("zd-0.14", dict(
        name = "Zot Defence 0.14",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        send_json_options = True,
        pre_options = [ "0.14" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.14/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.14/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl14-zotdef/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-zotdef"])),
    
    ("dcss-0.13", dict(
        name = "DCSS 0.13",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.13" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.13/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.13/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl13/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.13", dict(
        name = "Sprint 0.13",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.13" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.13/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.13/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl13-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("zd-0.13", dict(
        name = "Zot Defence 0.13",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.13" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.13/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.13/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl13-zotdef/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-zotdef"])),

    ("dcss-0.12", dict(
        name = "DCSS 0.12",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.12" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.12/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.12/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl12/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.12", dict(
        name = "Sprint 0.12",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.12" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.12/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.12/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl12-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("zd-0.12", dict(
        name = "Zot Defence 0.12",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.12" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.12/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.12/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl12-zotdef/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-zotdef"])),

    ("dcss-0.11", dict(
        name = "DCSS 0.11",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.11" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.11/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.11/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl11/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.11", dict(
        name = "Sprint 0.11",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.11" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.11/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.11/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl11-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("zd-0.11", dict(
        name = "Zot Defence 0.11",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.11" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.11/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.11/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl11-zotdef/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-zotdef"])),

    ("dcss-0.10", dict(
        name = "DCSS 0.10",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.10" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.10/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.10/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl10/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.10", dict(
        name = "Sprint 0.10",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.10" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.10/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.10/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl10-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("zd-0.10", dict(
        name = "Zot Defence 0.10",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options = [ "0.10" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.10/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.10/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "http://crawl.akrasiac.org/rawdata/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%-crawl10-zotdef/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-zotdef"])),
])

dgl_status_file = "%%CHROOT_WEBDIR%%/run/status"

# Set to None not to read milestones
milestone_file = [
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.10/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.10/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.10/saves/milestones-zotdef",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.11/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.11/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.11/saves/milestones-zotdef",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.12/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.12/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.12/saves/milestones-zotdef",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.13/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.13/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.13/saves/milestones-zotdef",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.14/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.14/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.14/saves/milestones-zotdef",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.15/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.15/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.15/saves/milestones-zotdef",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.16/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.16/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.17/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.17/saves/milestones-sprint",
    "%%CHROOT_CRAWL_GAMEDIR%%/saves/milestones",
    "%%CHROOT_CRAWL_GAMEDIR%%/saves/milestones-sprint"
]

status_file_update_rate = 5

recording_term_size = (80, 24)

max_connections = 200

# Script to initialize a user, e.g. make sure the paths
# and the rc file exist. This is not done by the server
# at the moment.
init_player_program = "/bin/init-webtiles.sh"

ssl_options = None # No SSL
# ssl_options = {
#     "certfile": "/etc/ssl/private/s-z.org.crt",
#     "keyfile": "/etc/ssl/private/s-z.org.key",
#     "ca_certs": "/etc/ssl/private/sub.class1.server.ca.pem"
# }
# ssl_address = ""
# ssl_port = 8443

connection_timeout = 600
max_idle_time = 5 * 60 * 60

# Seconds until stale HTTP connections are closed
# This needs a patch currently not in mainline tornado.
http_connection_timeout = 600

kill_timeout = 10 # Seconds until crawl is killed after HUP is sent

nick_regex = r"^[a-zA-Z0-9]{3,20}$"
max_passwd_length = 20

# crypt() algorithm, e.g. "1" for MD5 or "6" for SHA-512; see crypt(3).
# If false, use traditional DES (but then only the first eight characters
# are significant).
crypt_algorithm = "6"
# If crypt_algorithm is true, the length of the salt string to use.  If
# crypt_algorithm is false, a two-character salt is used.
crypt_salt_length = 16

login_token_lifetime = 7 # Days

uid = 5  # If this is not None, the server will setuid to that (numeric) id
gid = 60  # after binding its sockets.

umask = None # e.g. 0077

chroot = "%%DGL_CHROOT%%"

pidfile = "%%CHROOT_WEBDIR%%/run/webtiles.pid"
daemon = True # If true, the server will detach from the session after startup

player_url = "http://crawl.akrasiac.org/scoring/players/%s.html"
