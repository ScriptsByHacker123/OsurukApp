[app]
# (str) Title of your application
title = AlverApp

# (str) Package name
package.name = alverapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.alver

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's include everything needed)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements
# python3 ve kivy standarttır, ek kütüphanelerin varsa buraya virgülle ekle
requirements = python3,kivy

# (str) Application orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (str) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir (False)
android.private_storage = True

[buildozer]
# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display build progress in a readable way
show_log = 1
