#!/bin/bash

# Variables
SHARED_FOLDER="/media/sf_SharedFolder"  # VirtualBox shared folder path on Linux
LOG_DIR="/var/log"                      # Directory containing logs
APACHE_LOG_DIR="/var/log/apache2"       # Directory for Apache logs (default for Debian/Ubuntu)

# Ensure the shared folder is accessible
if [[ ! -d "$SHARED_FOLDER" ]]; then
    echo "Error: Shared folder $SHARED_FOLDER not found. Ensure it is mounted correctly."
    exit 1

# 1. Gather logs from Linux machine and copy directly to the shared folder
echo "Gathering logs from Linux machine and transferring to the shared folder..."
cp "$LOG_DIR/auth.log" "$SHARED_FOLDER/auth.log"
cp "$LOG_DIR/syslog" "$SHARED_FOLDER/syslog"

# Include Apache access and error logs if they exist
if [[ -d "$APACHE_LOG_DIR" ]]; then
    echo "Including Apache logs..."
    cp "$APACHE_LOG_DIR/access.log" "$SHARED_FOLDER/apache_access.log"
    cp "$APACHE_LOG_DIR/error.log" "$SHARED_FOLDER/apache_error.log"
else
    echo "Apache log directory not found. Skipping Apache logs."

# 2. Weekly task: Gather last week's logs and transfer them to the shared folder
if [[ $(date +%u) -eq 7 ]]; then  # Check if today is Sunday (end of the week)
    echo "Gathering weekly logs..."
    WEEKLY_LOG_FILE="$SHARED_FOLDER/weekly_logs.txt"
    find "$LOG_DIR/" -type f -mtime -7 -exec cat {} \; > "$WEEKLY_LOG_FILE"
    echo "Weekly logs transferred to the shared folder as $WEEKLY_LOG_FILE."

echo "Log gathering and transfer script completed."