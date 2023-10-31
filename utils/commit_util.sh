#!/bin/env bash

git add -A
git reset HEAD *.md
git status

# Checking if "yolo" argument is provided
if [ "$1" == "yolo" ]; then
  COMMIT_MSG=$(fortune 2>/dev/null) || COMMIT_MSG="okaayyy-lets-go"
  CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

  echo "\r\nCOMMIT_MSG=$COMMIT_MSG\r\n"
  git commit -m "$COMMIT_MSG"
  git push origin "$CURRENT_BRANCH" --force
fi
