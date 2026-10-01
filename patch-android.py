# Adds release signing (keys come from secure build variables) and an auto-increasing version number.
import os, re
p = 'android/app/build.gradle'
s = open(p).read()
if 'signingConfigs' not in s:
    s = s.replace("    buildTypes {", """    signingConfigs {
        release {
            storeFile file("release.keystore")
            storePassword System.getenv("AN2U_KEYSTORE_PASSWORD")
            keyAlias System.getenv("AN2U_KEY_ALIAS")
            keyPassword System.getenv("AN2U_KEY_PASSWORD")
        }
    }
    buildTypes {""", 1)
    s = s.replace("        release {\n            minifyEnabled false", "        release {\n            signingConfig signingConfigs.release\n            minifyEnabled false", 1)
build = os.environ.get('BUILD_NUMBER', '1')
s = re.sub(r'versionCode \d+', 'versionCode ' + build, s, count=1)
open(p, 'w').write(s)
print('patched', p, 'versionCode', build)
