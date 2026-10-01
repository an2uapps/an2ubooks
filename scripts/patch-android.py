# Adds release signing (keys come from Codemagic) and an auto-increasing version number to the Android project.
import os, re
p = 'android/app/build.gradle'
s = open(p).read()
if 'signingConfigs' not in s:
    s = s.replace("    buildTypes {", """    signingConfigs {
        release {
            storeFile file(System.getenv("CM_KEYSTORE_PATH") ?: "release.keystore")
            storePassword System.getenv("CM_KEYSTORE_PASSWORD")
            keyAlias System.getenv("CM_KEY_ALIAS")
            keyPassword System.getenv("CM_KEY_PASSWORD")
        }
    }
    buildTypes {""", 1)
    s = s.replace("        release {\n            minifyEnabled false", "        release {\n            signingConfig signingConfigs.release\n            minifyEnabled false", 1)
build = os.environ.get('BUILD_NUMBER', '1')
s = re.sub(r'versionCode \d+', 'versionCode ' + build, s, count=1)
open(p, 'w').write(s)
print('patched', p, 'versionCode', build)
