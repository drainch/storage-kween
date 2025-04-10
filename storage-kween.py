from dearpygui.dearpygui import *
import os
import hashlib

results = []

def human_size(size):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def scan_folder_callback(sender, app_data, user_data):
    folder = get_value("folder_input")
    clear_table("results_table")
    results.clear()

    for root, _, files in os.walk(folder):
        for f in files:
            try:
                path = os.path.join(root, f)
                size = os.path.getsize(path)
                last_access = os.path.getatime(path)
                results.append((path, size, last_access))
            except:
                continue

    results.sort(key=lambda x: x[1], reverse=True)

    for path, size, access in results[:50]:
        add_table_row("results_table", [path, human_size(size), str(int(access))])

def hash_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return None

def find_duplicates_callback(sender, app_data, user_data):
    hashes = {}
    dupes = []
    for path, _, _ in results:
        h = hash_file(path)
        if not h:
            continue
        if h in hashes:
            dupes.append((path, hashes[h]))
        else:
            hashes[h] = path
    log_info(f"Found {len(dupes)} duplicate pairs")
    for p1, p2 in dupes:
        log_info(f"DUPE:\n → {p1}\n ↔ {p2}")

# Setup GUI
create_context()
create_viewport(title='Storage Kween 👑', width=900, height=600)
setup_dearpygui()

with window(label="Storage Kween", width=900, height=600):
    add_input_text(tag="folder_input", label="Folder to Scan", default_value=os.getcwd())
    add_button(label="Scan Folder", callback=scan_folder_callback)
    add_button(label="Find Duplicates", callback=find_duplicates_callback)
    add_table(tag="results_table", header_row=True, resizable=True, borders_innerV=True, borders_outerH=True)
    add_table_column(label="File")
    add_table_column(label="Size")
    add_table_column(label="Last Access")
    add_logger()

show_viewport()
start_dearpygui()
destroy_context()
