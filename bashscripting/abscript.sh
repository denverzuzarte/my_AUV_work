#!/bin/bash

# Define variables
Source="/home/denver/bashscripting/datab"
backup="//home/denver/bashscripting/backup"
num=7

#timestamp
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

# make a backup
backupfile="$backup/backup_$timestamp.tar.gz"
tar -czf "$backupfile" -C "$Source" .

# Delete old backups
cd "$backup" || exit
ls -t backup_*.tar.gz | sed -e "1,${num}d" | xargs -I {} rm -f {}

echo "Backup completed: $backupfile"
