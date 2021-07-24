# IRC Network to connect to
#network = 'irc.devel.redhat.com'
#network = 'irc.freenode.net'
network = 'irc-2.devel.redhat.com'
# Port to connect on
port = 6667
# Channel to join (automatically)
chan = 'trinity-quiz'
# Nickname of bot
nickname = 'quizbot'
# Username to use when identifying with services (or not)
username = nickname
# Whether to use a password to identify with services or not
password = False
# IRC nick names that can control the bot
masters = [nickname, 'nkshirsa']
# High score database file (is automatically created)
hiscoresdb = 'hiscores.sql'
# Whether to print 'category - question - answer' to STDOUT
verbose = True
