# apps/

Put `ApiDemos-debug.apk` here for the mobile tests (the `.apk` itself is git-ignored).

```bash
# with the GitHub CLI
gh release download -R appium/android-apidemos -p "*.apk" -D apps
```

Or download it from https://github.com/appium/android-apidemos/releases and save it as
`apps/ApiDemos-debug.apk`.
