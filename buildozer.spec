[app]
title = MuzikAsistani
package.name = muzikasistani
package.domain = org.muzik
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1

# Kivy yeterlidir, ekstra bir şeye gerek yok
requirements = python3,kivy

orientation = portrait
# İnternet iznini mutlaka ekle!
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
