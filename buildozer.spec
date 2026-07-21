[app]
title = CryptaGen
package.name = cryptagen
package.domain = org.cryptagen
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

requirements = python3,kivy

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True

orientation = portrait

fullscreen = 0

icon.filename = icon.png

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
