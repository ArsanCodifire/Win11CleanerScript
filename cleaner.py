import os
import shutil
import tempfile
import time


def clean():
    start = time.perf_counter()

    temp_path = tempfile.gettempdir()
    windows_temp = os.path.join(os.environ["SystemRoot"], "Temp")
    shader_cache = os.path.join(os.environ["LOCALAPPDATA"],"D3DSCache")
    error_reports = os.path.join(os.environ["PROGRAMDATA"],"Microsoft","Windows","WER")
    thumbnail_cache = os.path.join(os.environ["LOCALAPPDATA"],"Microsoft","Windows","Explorer")

    deleted = 0
    skipped = 0
    freed = 0
    skipped_items = []

    locations = {
    "Temp": temp_path,
    "Windows Temp": windows_temp,
    "DirectX Shader Cache": shader_cache,
    "Windows Error Reports": error_reports,
    "Thumbnail Cache": thumbnail_cache,
    }

    folder_stats = {}

    for folder_name, folder_path in locations.items():
        if not os.path.exists(folder_path):
            folder_stats[folder_name] = 0
            continue

        folder_deleted = 0

        try:
            items = os.listdir(folder_path)
        except Exception as e:
            skipped += 1
            skipped_items.append({
                "name": folder_name,
                "path": folder_path,
                "reason": str(e)
            })
            folder_stats[folder_name] = 0
            continue

        for item in items:
            path = os.path.join(folder_path, item)

            try:
                if os.path.isfile(path) or os.path.islink(path):
                    try:
                        freed += os.path.getsize(path)
                    except OSError:
                        pass

                    os.remove(path)
                    deleted += 1
                    folder_deleted += 1

                elif os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            try:
                                freed += os.path.getsize(
                                    os.path.join(root, file)
                                )
                            except OSError:
                                pass

                    shutil.rmtree(path)
                    deleted += 1
                    folder_deleted += 1

            except Exception as e:
                skipped += 1
                skipped_items.append({
                    "name": item,
                    "path": path,
                    "reason": str(e)
                })

        folder_stats[folder_name] = folder_deleted

    elapsed = round(time.perf_counter() - start, 2)

    if deleted == 0:
        status = "Nothing to Clean"
    elif skipped:
        status = "Partial Success"
    else:
        status = "Success"

    return {
        "status": status,
        "deleted": deleted,
        "skipped": skipped,
        "freed_mb": round(freed / 1024 / 1024, 2),
        "time": elapsed,
        "folders": folder_stats,
        "skipped_items": skipped_items
    }
