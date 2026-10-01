# AN2U Books – mobile app (Android + iPhone)

This is your website packaged as a real app with Capacitor. The book pages are bundled inside the app, so it opens fast and the reader works offline. The view counter and natural voice use your live site (https://an2ubooks.netlify.app).

You do not install anything on your computer. A cloud service called Codemagic builds the app files for you.

## Before you start (one time)
1. Deploy the latest website zip to Netlify first. It now includes `privacy.html` and the small change that lets the app reach your view counter and voice.
2. The privacy page already has your contact email (annamalai1431986@gmail.com). Change it in `privacy.html` if you want a different public address.
3. If your custom domain becomes final, replace `https://an2ubooks.netlify.app` in `www/index.html` (search for LIVE_URL) before building.

## Accounts you need
| Account | Cost | For |
|---|---|---|
| GitHub (github.com) | Free | holds this project so Codemagic can read it |
| Codemagic (codemagic.io) | Free tier is enough for occasional builds | builds the app in the cloud |
| Google Play Console | $25 once | publishing on Android |
| Apple Developer Program | $99 a year | publishing on iPhone (also needed for TestFlight) |

## Step 1 – Put the project on GitHub
1. Create a new empty private repository on github.com, for example `an2u-books-app`.
2. On the repository page choose "uploading an existing file" and drag in everything from this folder (unzipped): `www`, `resources`, `scripts`, `package.json`, `capacitor.config.json`, `codemagic.yaml`, `.gitignore`. Commit.

## Step 2 – Android
1. In Codemagic, sign in with GitHub and add the repository. Choose the `codemagic.yaml` configuration.
2. Codemagic → Teams → Code signing identities → Android → create a new keystore. Name the reference `an2u_keystore`. Codemagic keeps it safe. **Never lose this; Google Play needs the same key for every update.**
3. Start the workflow "AN2U Books – Android". After about 10 minutes you can download an `.aab` (for Google Play) and an `.apk` (install directly on any Android phone to test).
4. In Google Play Console: create the app, fill the listing from `STORE_LISTING.md`, upload the `.aab` to an internal test track first, test on your phone, then promote to production. New personal developer accounts must run a closed test with 12 testers for 14 days before production access; Google shows the current rule in the Console.

## Step 3 – iPhone
1. Join the Apple Developer Program. In App Store Connect create the app with bundle ID `com.an2u.books`.
2. In App Store Connect → Users and Access → Integrations, create an API key. In Codemagic → Teams → Integrations add it as `AN2U Codemagic key`.
3. Start the workflow "AN2U Books – iPhone". It signs the app and sends it to TestFlight.
4. Install TestFlight on your iPhone and test. When happy, choose the build in App Store Connect, fill the listing from `STORE_LISTING.md`, and submit for review.

## Updating the app later
When the website changes, copy the new `index.html` (and any new covers) into `www`, upload to GitHub, and run the workflows again. Each Android build gets a new version number automatically. For iPhone, Codemagic raises the build number.

## Notes
* The app icon and launch screen are made from your logo automatically (`resources` folder). Send me a higher-resolution logo if you want them sharper.
* Apple reviews apps that are only a website in a frame. This one is bundled with the reader, offline reading, bookmarks and audio, which is what they look for. In the review notes say: "A reading app for the author's own books, works offline, with bookmarks, highlights and read-aloud."
* Nothing was built or run on a phone here. Test the first builds on real phones, especially reading, full screen, Listen, and the contact form.
