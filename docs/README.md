# Website Blocker

A powerful and user-friendly website blocker application built with Python and Tkinter. Block distracting websites to boost your productivity by modifying your system's hosts file.

## Features

- 🚫 **Block Websites**: Add websites to your block list and activate blocking
- ✅ **Unblock Websites**: Easily remove all blocks when needed
- ⏱️ **Timer-Based Blocking**: Block websites for specific durations (30min, 1hr, 2hr, 4hr)
- ⚡ **Quick Presets**: One-click blocking for popular distracting sites
- 💾 **Persistent Storage**: Your blocked websites list is saved between sessions
- 🎨 **Clean GUI**: Simple and intuitive graphical interface with modern styling
- 📊 **Live Status Indicator**: See at a glance if blocking is active
- ⌨️ **Keyboard Shortcuts**: Press Enter to add, Delete to remove, double-click for quick actions
- 🔒 **System-Level Blocking**: Works by modifying the hosts file for effective blocking

## Requirements

- Python 3.6 or higher
- Administrator/Root privileges (required to modify hosts file)
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional packages required - uses Python standard library!

## Usage

### Windows

**Run as Administrator** (Right-click → Run as Administrator):

```powershell
python website_blocker.py
```

Or create a shortcut and set it to always run as administrator.

### Linux/Mac

Run with sudo:

```bash
sudo python3 website_blocker.py
```

## How to Use

1. **Add Websites**:
   - Enter a website URL (e.g., `facebook.com`, `youtube.com`)
   - Click "Add Website" or press Enter
   - The website will be added to your blocked list
   - Or click "⚡ Presets" to quickly add popular distracting sites

2. **Remove Websites**:
   - Select a website from the list
   - Click "Remove Selected", press Delete, or double-click
   - The website will be removed from your list

3. **Block All Websites**:
   - Click "Block All" to activate blocking
   - All websites in your list will be blocked immediately
   - **Note**: Requires administrator privileges
   - Status indicator will turn red when active

4. **Unblock All Websites**:
   - Click "Unblock All" to remove all blocks
   - **Note**: Requires administrator privileges
   - Status indicator will return to gray

5. **Use Timer-Based Blocking**:
   - Click any timer button (30min, 1hr, 2hr, 4hr)
   - Blocking will automatically activate and deactivate after the time expires
   - Perfect for focused work sessions

## How It Works

The application modifies your system's `hosts` file to redirect blocked websites to `127.0.0.1` (localhost), effectively blocking access to them. 

- **Windows**: `C:\Windows\System32\drivers\etc\hosts`
- **Linux/Mac**: `/etc/hosts`

When you block websites, entries like these are added:
```
127.0.0.1 facebook.com
127.0.0.1 www.facebook.com
```

## Important Notes

⚠️ **Administrator Privileges Required**: Modifying the hosts file requires admin/root access. Make sure to run the application with elevated privileges.

⚠️ **Browser Cache**: After blocking/unblocking, you may need to:
- Clear your browser cache
- Restart your browser
- Run `ipconfig /flushdns` (Windows) or `sudo dscacheutil -flushcache` (Mac)

⚠️ **Backup**: The app modifies your hosts file. While it's designed to be safe, consider backing up your hosts file before use.

## Configuration

Blocked websites are saved in `blocked_sites.json` in the same directory as the application. You can manually edit this file if needed.

## Troubleshooting

**"Permission denied" error**:
- Make sure you're running the application as Administrator (Windows) or with sudo (Linux/Mac)

**Websites not blocking**:
- Clear your DNS cache
- Restart your browser
- Check that the hosts file has been modified correctly

**Application won't start**:
- Ensure Python is installed correctly
- Check that tkinter is available: `python -m tkinter`

## License

Free to use and modify as needed.

## Disclaimer

This tool is for educational and productivity purposes. Use responsibly and in accordance with your organization's policies.
