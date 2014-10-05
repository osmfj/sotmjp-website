#!/bin/bash
################################################################################
# BACKUP script
################################################################################

# AMAZON S3 INFORMATION
export AWS_ACCESS_KEY_ID="foobar_aws_key_id"
export AWS_SECRET_ACCESS_KEY="foobar_aws_access_key"

export PASSPHRASE="foobar_gpg_passphrase"

# Specify which GPG key you would like to use (even if you have only one).
GPG_KEY="foobar_gpg_key"

DEST="s3+http://backup-bucket/"

PGSQL_DB=( 'sotmjp2014' )
PGSQL_USER="postgres"

# BACKUP /etc
duplicity 	--full-if-older-than 1M \
		 	--no-encryption \
		 	/etc/nginx/ ${DEST}/nginx
duplicity 	remove-older-than 3M \
		 	--no-encryption \
			--force \
			${DEST}/nginx

# BACKUP /srv/sites/sotmj-website/sotmjp/settings
duplicity 	--full-if-older-than 1M \
		 	--no-encryption \
		 	/srv/sites/sotmjp-website/sotmjp/settings \
		 	${DEST}/settings
duplicity 	remove-older-than 3M \
		 	--no-encryption \
			--force \
			${DEST}/settings

# BACKUP databases
OUTPUT_PATH="/opt/BACKUP/"

for ((i=0; i<${#PGSQL_DB[@]}; i++))
do
 DB=${PGSQL_DB[$i]} 
 FILE=$DB.$(date +"%Y-%m-%d").sql.gz
 sudo -u postgres pg_dump -U ${PGSQL_USER} -C -f ${OUTPUT_PATH}/${FILE} -F t $DB
done

duplicity 	--full-if-older-than 1M \
		 	--no-encryption \
		 	${OUTPUT_PATH} ${DEST}/databases
duplicity 	remove-older-than 3M \
		 	--no-encryption \
			--force \
			${DEST}/databases

# remove database dumps older than 7 days
find ${OUTPUT_PATH} -mtime +7 -type f -exec rm -f {} \;

unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset PASSPHRASE
