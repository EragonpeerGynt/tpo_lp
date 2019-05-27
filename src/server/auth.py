# Copy to auth.py
# This sample data should be enough to test the parts of the site
# which do not require a database connection

dbase = 'heroku_bcbf8278618ec11'
dbuser = 'DATABASE_USERNAME'
dbpass = 'DATABASE_PASSWORD'
dbhost = 'eu-cdbr-west-02.cleardb.net'

timestamp_public = "cert.pem"
timestamp_private = "key.pem"

# For Python 3, gitkey must be bytes
gitkey = b'github-secret'
sesskey = 'session-secret'
debug = True