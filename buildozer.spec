[app]
title = BCC Control
package.name = bcccontrol
package.domain = org.ceet.bcc

# Configuration des sources
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db
source.include_patterns = Pages/*,*.db,CEET.png,My_Image.png
source.exclude_dirs = tests, bin, venv

# Version et métadonnées
version = 1.5
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py

# Dépendances Python
requirements = python3,kivy==2.2.0,kivymd==1.1.1,pillow

# Configuration des icônes
icon.filename = CEET.png
icon.adaptive_icon = True
presplash.filename = CEET.png

# Configuration de l'orientation (CORRECTION)
orientation = portrait

[buildozer]
log_level = 2
# Amélioration pour GitHub Actions
warn_on_root = 1

[android]
# Versions Android
api = 34
minapi = 21
ndk = 25b
sdk = 34

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,VIBRATE

# Architectures supportées
android.archs = arm64-v8a, armeabi-v7a

# Configuration d'orientation Android (DOUBLEMENT IMPORTANT)
android.orientation = portrait

# Configuration des icônes Android
android.icon = CEET.png
android.adaptive_icon_foreground = CEET.png
android.adaptive_icon_background = #FFFF00

# Métadonnées
android.meta_data = com.google.android.gms.version=12451000

# Optimisations pour la compilation
android.gradle_dependencies = 
android.add_compile_options = sourceCompatibility JavaVersion.VERSION_1_8, targetCompatibility JavaVersion.VERSION_1_8

# Configuration du manifeste
android.manifest.intent_filters = 

# Optimisation de la taille
android.release_artifact = aab
android.debug_artifact = apk

[ios]
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
