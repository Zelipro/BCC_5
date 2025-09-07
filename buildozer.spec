[app]
title = BCC Control
package.name = bcccontrol
package.domain = org.ceet.bcc
source.dir = .

source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db
source.include_patterns = Pages/*,*.db,CEET.png,My_Image.png

version = 1.5
requirements = python3,kivy,kivymd,pillow

# Configuration correcte de l'icône
icon.filename = CEET.png
icon.adaptive_icon = True

# Ajout du presplash pour l'écran de démarrage
presplash.filename = CEET.png

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
ndk = 25b
sdk = 34
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a

# CORRECTION IMPORTANTE : Forcer l'orientation portrait
orientation = portrait
android.orientation = portrait

# Configuration de l'icône Android
android.icon = CEET.png
android.adaptive_icon_foreground = CEET.png
android.adaptive_icon_background = #FFFFFF

# Métadonnées de l'application
android.meta_data = com.google.android.gms.version=12451000
