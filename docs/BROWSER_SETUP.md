# Website Blocker - Browser Setup Guide

## Why Browsers Might Show the Real Site or Security Errors

Modern browsers use **DNS over HTTPS (DoH)** which bypasses your computer's hosts file. Here's how to fix it:

---

## Chrome/Edge (Chromium-based)

### Disable DNS over HTTPS:
1. Open Chrome/Edge
2. Go to: `chrome://settings/security` or `edge://settings/privacy`
3. Scroll down to **"Use secure DNS"**
4. Turn it **OFF** or select "With your current service provider"
5. Restart the browser

### Quick Link:
- Chrome: `chrome://flags/#dns-over-https` - Set to "Disabled"
- Edge: `edge://flags/#dns-over-https` - Set to "Disabled"

---

## Firefox

### Disable DNS over HTTPS:
1. Open Firefox
2. Go to: `about:preferences#general`
3. Scroll to **"Network Settings"**
4. Click **"Settings..."**
5. Uncheck **"Enable DNS over HTTPS"**
6. Click OK and restart Firefox

### Quick Method:
1. Type `about:config` in address bar
2. Accept the warning
3. Search for: `network.trr.mode`
4. Set value to: `5` (DoH disabled)
5. Restart Firefox

---

## After Disabling DoH:

1. **Close browser completely** (check Task Manager)
2. **Flush DNS**:
   ```cmd
   ipconfig /flushdns
   ```
3. **Restart browser**
4. **Test**: Visit a blocked site - you should see the block page!

---

## Alternative: Use Incognito/Private Mode

Sometimes private browsing mode respects hosts file better:
- Chrome: `Ctrl+Shift+N`
- Firefox: `Ctrl+Shift+P`
- Edge: `Ctrl+Shift+N`

---

## Still Not Working?

### Clear Browser Cache:
- Chrome/Edge: `Ctrl+Shift+Delete` → Select "All time" → Clear cached images and files
- Firefox: `Ctrl+Shift+Delete` → Select "Everything" → Clear cache

### Check Certificate is Installed:
Run in CMD as Admin:
```cmd
certutil -store "Root" | findstr "localhost"
```

You should see: `Subject: CN=localhost`

If not, reinstall:
```cmd
cd "C:\Users\satwi\Projects\Website Blocker"
certutil -addstore "Root" server.crt
```

---

## Quick Test

Visit: `http://127.0.0.1` in your browser

**Expected:** You see the purple gradient "Site Blocked" page
**If not:** Server isn't running - restart `website_blocker.py` as Admin
