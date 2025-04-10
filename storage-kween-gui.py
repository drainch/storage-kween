from dearpygui.dearpygui import *
import os
import subprocess
import time

# Check and install required system tools if needed (run manually or via setup script)
REQUIRED_COMMANDS = ["du", "find", "fdupes", "paccache", "pacman", "lsblk", "free", "uname"]

def check_dependencies():
    missing = []
    for cmd in REQUIRED_COMMANDS:
        if subprocess.call(f"command -v {cmd}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
            missing.append(cmd)
    if missing:
        print("Missing system tools:", ", ".join(missing))
        print("\nInstall them using your package manager:")
        print("sudo pacman -S " + " ".join(missing))
        exit(1)

check_dependencies()

create_context()
create_viewport(title="Storage Queen 👑", width=900, height=600)
setup_dearpygui()

results_cache = ""

def update_panel(label, content):
    delete_item("main_panel", children_only=True)
    add_text(label, parent="main_panel")
    add_separator(parent="main_panel")
    add_text(content, parent="main_panel", wrap=800)

def run_analyzer(sender, app_data, user_data):
    update_panel("📊 Disk Analyzer", "Scanning disk usage...")
    output = subprocess.getoutput("du -h --max-depth=1 ~ | sort -hr | head -n 15")
    update_panel("📊 Disk Analyzer", output)

def clean_junk(sender, app_data, user_data):
    update_panel("🧹 Junk Cleaner", "Cleaning pacman cache and logs...")
    subprocess.call(["paccache", "-r"])
    subprocess.call(["sudo", "rm", "-rf", "/var/log/*.log"])
    update_panel("🧹 Junk Cleaner", "Done cleaning. Your majesty's filesystem is fresh.")

def find_large_files(sender, app_data, user_data):
    update_panel("🔍 Large Files", "Locating large files...")
    output = subprocess.getoutput("find ~ -type f -exec du -h {} + | sort -hr | head -n 15")
    update_panel("🔍 Large Files", output)

def find_duplicates(sender, app_data, user_data):
    update_panel("🧂 Duplicates", "Looking for duplicate files via MD5 hash...")
    output = subprocess.getoutput("fdupes -r ~ | head -n 40")
    update_panel("🧂 Duplicates", output if output else "No duplicates found!")

def safe_delete_mode(sender, app_data, user_data):
    update_panel("💣 Safe Delete", "Not yet implemented, but soon you'll queue files for deletion with mercy.")

with window(label="Storage Queen 👑", width=900, height=600):
    with child_window(width=180, border=True):
        add_button(label="📊 Analyze", callback=run_analyzer)
        add_button(label="🧹 Clean Junk", callback=clean_junk)
        add_button(label="🔍 Large Files", callback=find_large_files)
        add_button(label="🧂 Duplicates", callback=find_duplicates)
        add_button(label="💣 Safe Delete", callback=safe_delete_mode)
    add_same_line()
    with child_window(tag="main_panel", width=700, height=550, border=True):
        add_text("👑 Welcome to Storage Queen\nClick a button to begin.", wrap=700)
    add_text("Built for the Arch community, with love.", bullet=True)

show_viewport()
start_dearpygui()
destroy_context()
