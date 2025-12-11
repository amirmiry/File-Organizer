## 📁 File Organizer Script

A simple yet powerful Python script that automatically scans a directory, detects files by type, and organizes them into categorized subfolders.
This tool helps keep your workspace clean by sorting images, documents, videos, audio files, and archives into separate directories.

---

### 🚀 Features

- Automatically scans a base directory (including subdirectories)

- Categorizes files by extension:

  - Images

  - Documents

  - Videos

  - Audio

  - Archives

- Creates folders for each category if they don't already exist

- Safely copies files into their respective category folders

- Prevents errors due to duplicate file copying

---

### 📂 Project Structure
├── file_organizer.py <br>
└── README.md

### 🛠️ Technologies Used
- Python 3.x

- Built-in libraries:

  - pathlib

  - shutil

No external modules are required.

---

### ⚙️ How It Works

The script:

1. Defines a `base_dir` where files are searched

2. Defines a `target_dir` where sorted folders will be created

3. Scans the base directory recursively

4. Matches file extensions to predefined categories

5. Copies each file into the appropriate folder under `target_dir`

---

### 📌 Configuration

Inside the script, you can modify:
```python
base_dir = Path("/home/amirmiri/Desktop")
target_dir = base_dir / "sorted"
```
Change these paths to define where the script should search and where sorted files should be placed.

#### You can also customize file types in `FILE_CATEGORIES`:

```python
FILE_CATEGORIES = {
    "images": [...],
    "documents": [...],
    "videos": [...],
    "audio": [...],
    "archives": [...]
}
```
---

### ▶️ Usage

1. Clone or download the script.

2. Ensure you have Python installed.

3. Run the script:
```python
python3 file_organizer.py
```
---
### 📁 Output Example

```css
Desktop/
└── sorted/
    ├── images/
    ├── documents/
    ├── videos/
    ├── audio/
    └── archives/
```
---

### ⚠️ Notes & Improvements

- The script uses shutil.copy() — duplicate files are ignored if the same file already exists.

- The extension .jpj in the images list appears to be a typo — consider replacing with .jpg.

- You may extend the script to:

  - Move files instead of copying

  - Add logging

  - Handle duplicate filenames

  - Create a GUI
---

### 📜 License

This project is open-source and available under the MIT License.
Feel free to modify and use it in your own projects.
