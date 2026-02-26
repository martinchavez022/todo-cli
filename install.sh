#!/usr/bin/env bash

set -e

APP_NAME="todo"
SOURCE_FILE="todo.py"
INSTALL_DIR="/usr/local/bin"
PROJECT_DIR="$(pwd)"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}Installing ${APP_NAME}...${NC}"

# Check source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo -e "${RED}Error: ${SOURCE_FILE} not found in current directory.${NC}"
    exit 1
fi

# Check shebang, add if missing
if ! head -1 "$SOURCE_FILE" | grep -q "#!/usr/bin/env -S uv run --script"; then
    echo -e "${YELLOW}Adding shebang line to ${SOURCE_FILE}...${NC}"
    TMP=$(mktemp)
    echo "#!/usr/bin/env -S uv run --script" | cat - "$SOURCE_FILE" > "$TMP"
    mv "$TMP" "$SOURCE_FILE"
fi

sudo tee "${INSTALL_DIR}/${APP_NAME}" > /dev/null << EOF
#!/usr/bin/env bash
cd "${PROJECT_DIR}"
exec uv run --script "${PROJECT_DIR}/${SOURCE_FILE}" "\$@"
EOF

sudo chmod +x "${INSTALL_DIR}/${APP_NAME}"

# --- PATH setup for Bash ---
BASH_RC="$HOME/.bashrc"
BASH_LINE="export PATH=\"\$PATH:${INSTALL_DIR}\""

if [ -f "$BASH_RC" ]; then
    if ! grep -q "$INSTALL_DIR" "$BASH_RC"; then
        echo "$BASH_LINE" >> "$BASH_RC"
        echo -e "Added to ${BASH_RC}"
    else
        echo -e "${YELLOW}${INSTALL_DIR} already in ${BASH_RC}, skipping.${NC}"
    fi
fi

# --- PATH setup for Zsh ---
ZSH_RC="$HOME/.zshrc"
ZSH_LINE="export PATH=\"\$PATH:${INSTALL_DIR}\""

if [ -f "$ZSH_RC" ]; then
    if ! grep -q "$INSTALL_DIR" "$ZSH_RC"; then
        echo "$ZSH_LINE" >> "$ZSH_RC"
        echo -e "Added to ${ZSH_RC}"
    else
        echo -e "${YELLOW}${INSTALL_DIR} already in ${ZSH_RC}, skipping.${NC}"
    fi
fi

echo ""
echo -e "${GREEN}✓ Done! '${APP_NAME}' installed successfully.${NC}"
echo -e "${YELLOW}Reload your shell or run: source ~/.bashrc / source ~/.zshrc${NC}"
echo -e "Then use it as: ${GREEN}${APP_NAME} --help${NC}"
