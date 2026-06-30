[app]
title = MuzikAsistani
package.name = muzik
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
# Versiyonları boş bırak, Buildozer en uygun olanı kendi bulsun
android.api = 33
android.minapi = 21
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
