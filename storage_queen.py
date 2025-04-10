from dearpygui.dearpygui import *
import os

create_context()
create_viewport(title="Storage Queen 👑", width=900, height=600)
setup_dearpygui()

def update_panel(label, content):
    delete_item("main_panel", children_only=True)
    add_text(label, parent="main_panel")
    add_separator(parent="main_panel")
    add_text(content, parent="main_panel", wrap=800)

def run_analyzer(sender, app_data, user_data):
    update_panel("📊 Disk Analyzer", "Coming soon: pie charts and file usage heatmaps.")

def clean_junk(sender, app_data, user_data):
    update_panel("🧹 Cleaning Junk...", "Simulating: /var/log, pacman cache, thumbnail junk...")

def find_large_files(sender, app_data, user_data):
    update_panel("🔍 Finding Big Files...", "Scanning ~/ for files >100MB...")

def find_duplicates(sender, app_data, user_data):
    update_panel("🧂 Duplicate Files", "Hashing all files... This will take a while.")

def safe_delete_mode(sender, app_data, user_data):
    update_panel("💣 Safe Delete Mode", "Queue files for review. Nothing is deleted yet.")

with window(label="Storage Queen 👑", width=900, height=600):
    with child_window(width=180, border=True):
        add_button(label="📊 Analyze", callback=run_analyzer)
        add_button(label="🧹 Clean Junk", callback=clean_junk)
        add_button(label="🔍 Large Files", callback=find_large_files)
        add_button(label="🧂 Duplicates", callback=find_duplicates)
        add_button(label="💣 Safe Delete", callback=safe_delete_mode)
    add_same_line()
    with child_window(tag="main_panel", width=700, height=550, border=True):
        add_text("👑 Welcome to Storage Queen", wrap=700)

    add_text("Ready.", bullet=True)

show_viewport()
start_dearpygui()
destroy_context()
