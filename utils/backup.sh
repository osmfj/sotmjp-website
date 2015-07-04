#!/bin/bash
################################################################################
# BACKUP script
################################################################################

source credentials.inc

# Specify which GPG key you would like to use (even if you have only one).
GPG_KEY="CCFABB9B"

DEST="s3+http://osmfj-backup/stateofthemap.jp/"

PGSQL_DB=( 'sotmjp2014' )
PGSQL_USER="postgres"

# BACKUP /srv/sites/sotmj-website/sotmjp/settings
duplicity 	--full-if-older-than 1M \
			--encrypt-key ${GPG_KEY} \
			--s3-use-new-style \
		 	/srv/sites/sotmjp-website/sotmjp/settings \
		 	${DEST}/settings
duplicity 	remove-older-than 3M \
			--encrypt-key ${GPG_KEY} \
			--s3-use-new-style \
			--force \
			${DEST}/settings

# BACKUP /srv/sites/sotmj-website/site_media
duplicity 	--full-if-older-than 1M \
			--encrypt-key ${GPG_KEY} \
			--s3-use-new-style \
		 	/srv/sites/sotmjp-website/site_media \
		 	${DEST}/site_media
duplicity 	remove-older-than 3M \
			--encrypt-key ${GPG_KEY} \
			--s3-use-new-style \
			--force \
			${DEST}/site_media


# BACKUP databases
OUTPUT_PATH="/opt/BACKUP/"

for ((i=0; i<${#PGSQL_DB[@]}; i++))
do
 DB=${PGSQL_DB[$i]} 
 FILE=$DB.$(date +"%Y-%m-%d").sql.gz
 sudo -u postgres pg_dump -U ${PGSQL_USER} -C -f ${OUTPUT_PATH}/${FILE} -F t $DB
done

duplicity 	--full-if-older-than 1M \
			--encrypt-key ${GPG_KEY} \
			--s3-use-new-style \
		 	${OUTPUT_PATH} ${DEST}/databases
duplicity 	remove-older-than 3M \
			--encrypt-key ${GPG_KEY} \
			--s3-use-new-style \
			--force \
			${DEST}/databases

# remove database dumps older than 7 days
find ${OUTPUT_PATH} -mtime +7 -type f -exec rm -f {} \;

unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset PASSPHRASE
