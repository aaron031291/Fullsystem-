#!/bin/bash
echo "🚀 Syncing with GitHub..."

# Add only new/modified files
git add .

# Get a summary of changes
git status

# Ask for a commit message
read -p "Enter commit message: " commit_message

# Commit & push
git commit -m "$commit_message"
git push origin main

echo "✅ Repository synced successfully!"
