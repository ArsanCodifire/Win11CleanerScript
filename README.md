# 🧹 Win11CleanerScript 

A lightweight Windows cleanup utility built with **Python** and **CustomTkinter**.

It removes temporary files, frees disk space, and displays detailed cleanup statistics through a modern graphical interface.

## ✨ Features

- 🗑️ Cleans Windows temporary files
- 📂 Cleans:
  - User Temp
  - Windows Temp
  - DirectX Shader Cache
  - Windows Error Reports
  - Thumbnail Cache
- 📊 Displays:
  - Files deleted
  - Files skipped
  - Space freed
  - Cleanup duration
  - Per-folder statistics
- 📄 Detailed cleanup report for deleted and skipped files
- ⚡ Runs cleanup in a background thread to keep the interface responsive
- 🔒 Automatically requests Administrator privileges when required

---

## 📸 Interface

The application displays:

- Current cleanup status
- Deleted file count
- Skipped file count
- Space freed (MB)
- Cleanup duration
- Folder-by-folder statistics

---

## 📦 Requirements

- Windows 10 or Windows 11
- Python 3.10 or later

Install the required dependency:

```bash
pip install customtkinter
```

---

## 🚀 Running

Launch the application with:

```bash
python app.pyw
```

or simply run:

```text
Start Cleanup.vbs
```

The application automatically requests Administrator privileges before starting.

### Start Automatically with Windows (Optional)

`Start Cleanup.vbs` can also be used as a Windows startup launcher.

To launch the cleaner automatically when you sign in:

1. Press **Win + R**.
2. Type:

   ```text
   shell:startup
   ```

3. Press **Enter**.
4. Place a **shortcut** to `Start Cleanup.vbs` (recommended) or the `.vbs` file itself into the Startup folder.

The cleaner will now launch automatically whenever Windows starts.

### Custom Shortcut Icon (Optional)

The `Icons` folder contains the application icon (`cleaner.ico`).

To assign it to your shortcut:

1. Right-click the shortcut and select **Properties**.
2. Open the **Shortcut** tab.
3. Click **Change Icon...**
4. Browse to the `Icons` folder and select `cleaner.ico`.

This only changes the appearance of the shortcut. The application works normally without a custom icon.

---

## 📁 Project Structure

```text
Cleaner Script/
│
├── app.pyw             # Main application
├── cleaner.py          # Cleanup engine
├── Start Cleanup.vbs   # Launcher / Windows Startup script
├── Icons/
│   └── cleaner.ico
├── LICENSE
└── README.md
```

---

## ⚠️ Notes

- Some files may be skipped because they are currently being used by Windows or another application.
- Administrator privileges are required to clean certain system folders.
- Only temporary files and cache directories are cleaned. Personal files are never modified.

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

Copyright © 2026 ArsanCodifire.
