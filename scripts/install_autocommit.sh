#!/bin/bash
# Install/uninstall the launchd job that auto-commits + pushes this repo.
# Usage: scripts/install_autocommit.sh [install|uninstall] [interval_seconds]
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LABEL="com.pranav.ml-autocommit"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
ACTION="${1:-install}"
INTERVAL="${2:-600}"

if [ "$ACTION" = "uninstall" ]; then
  launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
  rm -f "$PLIST"; echo "Uninstalled."; exit 0
fi

cat > "$PLIST" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string>
    <string>$REPO/scripts/auto_commit.py</string>
  </array>
  <key>EnvironmentVariables</key><dict>
    <key>PATH</key><string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
  </dict>
  <key>StartInterval</key><integer>$INTERVAL</integer>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>$REPO/auto_commit.log</string>
  <key>StandardErrorPath</key><string>$REPO/auto_commit.log</string>
</dict></plist>
PL
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "Installed: runs every ${INTERVAL}s. Log: $REPO/auto_commit.log"
