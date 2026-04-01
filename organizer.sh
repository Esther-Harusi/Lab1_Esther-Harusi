#!/bin/bash

Original_file="grades.csv"
archive_dir="archive"
Log_file="organizer.log"

if [ ! -f "$Original_file" ]; then
    echo "Error: '$Original_file' not found in the current directory."
    exit 1
fi

if [ ! -d "$archive_dir" ]; then
    mkdir "$archive_dir"
    echo "Created directory: $archive_dir"
fi

Timestamp=$(date +"%Y%m%d-%H%M%S")

Archived_filename="grades_${Timestamp}.csv"
Archived_path="${Archive_dir}/${Archived_filename}"

mv "$Original_file" "$Archived_path"
echo "Archived: '$Original_file'  '$Archived_path'"

touch "$Original_file"
echo "Reset: New empty '$Original_file' created."


echo "[${Timestamp}] Original: ${Original_file} | Archived as: ${Archived_path}" >> "$Log_file"
echo "Logged operation to '$Log_file'."

echo ""
echo "Done! Archiving complete."

