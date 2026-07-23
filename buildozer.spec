[app]

title = CryptaGen

package.name = cryptagen
package.domain = org.cryptagen

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0
version.code = 1

requirements = python3,kivy==2.3.1,kivymd==1.2.0,pillow

orientation = portrait
fullscreen = 1

icon.filename = icon.png

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True

android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
