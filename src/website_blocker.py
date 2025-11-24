import tkinter as tk
from tkinter import messagebox
import json
import os
import platform
import ctypes
from datetime import datetime, timedelta
from pathlib import Path
from proxy_server import ProxyServer


class WebsiteBlocker:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Blocker")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        # Setup paths
        self.base_dir = Path(__file__).parent.parent
        self.config_dir = self.base_dir / "config"
        self.assets_dir = self.base_dir / "assets"

        # Configuration
        self.config_file = self.config_dir / "blocked_sites.json"
        self.blocked_websites = self.load_blocked_sites()

        # Hosts file path
        if platform.system() == "Windows":
            self.hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        else:
            self.hosts_path = "/etc/hosts"

        # Blocking configuration
        self.redirect_ip = "127.0.0.1"
        self.timer_id = None

        # Start HTTP server
        block_page_path = str(self.assets_dir / "block_page.html")
        self.proxy_server = ProxyServer(block_page_path)
        self.proxy_server.start()

        # Preset sites
        self.presets = [
            "facebook.com",
            "twitter.com",
            "instagram.com",
            "reddit.com",
            "youtube.com",
            "tiktok.com",
            "netflix.com",
            "twitch.tv",
        ]

        # Check admin privileges
        if not self.is_admin():
            messagebox.showwarning(
                "Admin Required",
                "Please run as Administrator to modify the hosts file.",
            )

        self.setup_ui()

    def is_admin(self):
        """Check if running with admin privileges"""
        try:
            if platform.system() == "Windows":
                return ctypes.windll.shell32.IsUserAnAdmin()
            else:
                return os.geteuid() == 0  # type: ignore
        except Exception:
            return False

    def setup_ui(self):
        """Setup the user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        title = tk.Label(
            header_frame,
            text="🚫 Website Blocker",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white",
        )
        title.pack(pady=20)

        # Input frame
        input_frame = tk.Frame(self.root, bg="#ecf0f1", padx=20, pady=15)
        input_frame.pack(fill=tk.X)

        tk.Label(
            input_frame, text="Enter Website:", font=("Arial", 11), bg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=(0, 10))

        self.website_entry = tk.Entry(
            input_frame, font=("Arial", 11), width=30, relief=tk.FLAT, bg="white"
        )
        self.website_entry.pack(side=tk.LEFT, padx=5, ipady=5)
        self.website_entry.bind("<Return>", lambda e: self.add_website())

        add_btn = tk.Button(
            input_frame,
            text="Add & Block",
            command=self.add_website,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2",
        )
        add_btn.pack(side=tk.LEFT, padx=5)

        # Preset buttons
        preset_frame = tk.Frame(self.root, bg="#ecf0f1", padx=20, pady=10)
        preset_frame.pack(fill=tk.X)

        tk.Label(preset_frame, text="Quick Add:", font=("Arial", 9), bg="#ecf0f1").pack(
            side=tk.LEFT, padx=(0, 10)
        )

        for preset in self.presets[:4]:
            btn = tk.Button(
                preset_frame,
                text=preset.replace(".com", "").replace(".tv", "").capitalize(),
                command=lambda p=preset: self.quick_add(p),  # type: ignore
                bg="#3498db",
                fg="white",
                font=("Arial", 8),
                relief=tk.FLAT,
                padx=8,
                pady=3,
                cursor="hand2",
            )
            btn.pack(side=tk.LEFT, padx=2)

        # List frame
        list_frame = tk.Frame(self.root, bg="#ecf0f1", padx=20, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            list_frame,
            text="Blocked Websites",
            font=("Arial", 12, "bold"),
            bg="#ecf0f1",
        ).pack(anchor=tk.W, pady=(0, 10))

        # Scrollable listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            list_frame,
            font=("Courier", 10),
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE,
            relief=tk.FLAT,
            bg="white",
            selectbackground="#3498db",
            activestyle="none",
        )
        self.listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        # Bind events
        self.listbox.bind("<Delete>", lambda e: self.remove_website())
        self.listbox.bind("<Double-Button-1>", lambda e: self.toggle_individual())

        # Control buttons
        btn_frame = tk.Frame(self.root, bg="#ecf0f1", padx=20, pady=15)
        btn_frame.pack(fill=tk.X)

        tk.Button(
            btn_frame,
            text="🔓 Toggle Selected",
            command=self.toggle_individual,
            bg="#f39c12",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=8,
            cursor="hand2",
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame,
            text="❌ Remove Selected",
            command=self.remove_website,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=8,
            cursor="hand2",
        ).pack(side=tk.LEFT, padx=5)

        # Timer buttons
        tk.Label(btn_frame, text="Block for:", font=("Arial", 9), bg="#ecf0f1").pack(
            side=tk.LEFT, padx=(20, 5)
        )

        for duration, label in [(30, "30m"), (60, "1h"), (120, "2h"), (240, "4h")]:
            tk.Button(
                btn_frame,
                text=label,
                command=lambda d=duration: self.block_with_timer(d),  # type: ignore
                bg="#9b59b6",
                fg="white",
                font=("Arial", 8),
                relief=tk.FLAT,
                padx=10,
                pady=5,
                cursor="hand2",
            ).pack(side=tk.LEFT, padx=2)

        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 9),
            bg="#34495e",
            fg="white",
            anchor=tk.W,
            padx=10,
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        self.update_listbox()

    def load_blocked_sites(self):
        """Load blocked sites from JSON"""
        try:
            if self.config_file.exists():
                with open(self.config_file, "r") as f:
                    return json.load(f)
        except Exception:
            pass
        return []

    def save_blocked_sites(self):
        """Save blocked sites to JSON"""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.blocked_websites, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")

    def add_website(self):
        """Add website to block list"""
        website = self.website_entry.get().strip().lower()

        if not website:
            messagebox.showwarning("Input Error", "Please enter a website")
            return

        website = (
            website.replace("http://", "").replace("https://", "").replace("www.", "")
        )
        if "/" in website:
            website = website.split("/")[0]

        if website in self.blocked_websites:
            messagebox.showinfo("Already Exists", f"{website} is already in the list")
            return

        self.blocked_websites.append(website)
        self.save_blocked_sites()
        self.block_single_website(website)
        self.update_listbox()
        self.website_entry.delete(0, tk.END)
        self.status_label.config(text=f"🔒 Blocked: {website}", fg="#27ae60")

    def quick_add(self, website):
        """Quick add preset website"""
        self.website_entry.delete(0, tk.END)
        self.website_entry.insert(0, website)
        self.add_website()

    def remove_website(self):
        """Remove selected website"""
        try:
            selection = self.listbox.curselection()
            if not selection:
                messagebox.showwarning("Selection Error", "Please select a website")
                return

            index = selection[0]
            website = self.blocked_websites[index]

            if messagebox.askyesno("Confirm", f"Remove {website}?"):
                self.unblock_single_website(website)
                self.blocked_websites.pop(index)
                self.save_blocked_sites()
                self.update_listbox()
                self.status_label.config(text=f"Removed: {website}", fg="#e74c3c")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def toggle_individual(self):
        """Toggle block status for selected website"""
        try:
            selection = self.listbox.curselection()
            if not selection:
                messagebox.showwarning("Selection Error", "Please select a website")
                return

            index = selection[0]
            website = self.blocked_websites[index]

            if self.is_website_blocked(website):
                self.unblock_single_website(website)
                self.status_label.config(
                    text=f"🔓 Unblocked: {website} - Press Ctrl+Shift+R to refresh",
                    fg="#f39c12",
                )
            else:
                self.block_single_website(website)
                self.status_label.config(
                    text=f"🔒 Blocked: {website} - Press Ctrl+Shift+R to refresh",
                    fg="#27ae60",
                )

            self.update_listbox()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def block_single_website(self, website):
        """Block a single website by adding to hosts file"""
        try:
            with open(self.hosts_path, "r") as f:
                hosts_content = f.read()

            variations = [
                website,
                f"www.{website}",
                f"m.{website}",
                f"mobile.{website}",
                f"app.{website}",
                f"api.{website}",
            ]

            new_entries = []
            for var in variations:
                entry = f"{self.redirect_ip} {var}"
                if entry not in hosts_content:
                    new_entries.append(entry)

            if new_entries:
                with open(self.hosts_path, "a") as f:
                    f.write("\n" + "\n".join(new_entries) + "\n")

            # Aggressive DNS flushing
            if platform.system() == "Windows":
                os.system("ipconfig /flushdns > nul 2>&1")
                os.system("nbtstat -R > nul 2>&1")
                os.system("nbtstat -RR > nul 2>&1")
                os.system("arp -d * > nul 2>&1")
            else:
                os.system("sudo killall -HUP mDNSResponder > /dev/null 2>&1")

        except PermissionError:
            messagebox.showerror("Permission Error", "Run as Administrator")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to block: {str(e)}")

    def unblock_single_website(self, website):
        """Unblock a single website by removing from hosts file"""
        try:
            with open(self.hosts_path, "r") as f:
                lines = f.readlines()

            variations = [
                website,
                f"www.{website}",
                f"m.{website}",
                f"mobile.{website}",
                f"app.{website}",
                f"api.{website}",
            ]

            with open(self.hosts_path, "w") as f:
                for line in lines:
                    if not any(
                        var in line and (self.redirect_ip in line or "0.0.0.0" in line)
                        for var in variations
                    ):
                        f.write(line)

            # Flush DNS
            if platform.system() == "Windows":
                os.system("ipconfig /flushdns > nul 2>&1")
                os.system("nbtstat -R > nul 2>&1")
                os.system("nbtstat -RR > nul 2>&1")
                os.system("arp -d * > nul 2>&1")
            else:
                os.system("sudo killall -HUP mDNSResponder > /dev/null 2>&1")

        except PermissionError:
            messagebox.showerror("Permission Error", "Run as Administrator")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to unblock: {str(e)}")

    def is_website_blocked(self, website):
        """Check if website is currently blocked in hosts file"""
        try:
            with open(self.hosts_path, "r") as f:
                content = f.read()

            return (
                f"{self.redirect_ip} {website}" in content
                or f"{self.redirect_ip} www.{website}" in content
                or f"0.0.0.0 {website}" in content
                or f"0.0.0.0 www.{website}" in content
            )
        except Exception:
            return False

    def block_with_timer(self, minutes):
        """Block all sites for specified time"""
        if not self.blocked_websites:
            messagebox.showwarning("No Sites", "Add websites first")
            return

        for website in self.blocked_websites:
            if not self.is_website_blocked(website):
                self.block_single_website(website)

        self.update_listbox()

        end_time = datetime.now() + timedelta(minutes=minutes)
        self.status_label.config(
            text=f"⏰ Blocked until {end_time.strftime('%H:%M')}", fg="#9b59b6"
        )

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.timer_id = self.root.after(minutes * 60 * 1000, self.timer_expired)

    def timer_expired(self):
        """Handle timer expiration"""
        for website in self.blocked_websites:
            self.unblock_single_website(website)

        self.update_listbox()
        self.status_label.config(
            text="⏰ Timer expired - Sites unblocked", fg="#f39c12"
        )
        messagebox.showinfo("Timer", "Blocking period ended")

    def update_listbox(self):
        """Update the listbox display"""
        self.listbox.delete(0, tk.END)
        for website in self.blocked_websites:
            status = "🔒" if self.is_website_blocked(website) else "🔓"
            self.listbox.insert(tk.END, f"{status} {website}")


def main():
    root = tk.Tk()
    WebsiteBlocker(root)  # noqa: F841
    root.mainloop()


if __name__ == "__main__":
    main()
