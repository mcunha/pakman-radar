# scoop-radar
A data-driven, automated discovery and ranking engine for the Scoop package manager ecosystem on Windows

# Build Status
![Tests & Linting](https://github.com/mcunha/scoop-radar/actions/workflows/test.yml/badge.svg)
![Update Scoop Radar README](https://github.com/mcunha/scoop-radar/actions/workflows/update.yml/badge.svg)

# Acknowledgements
This project was heavily inspired by the original `awesome-scoop` directories maintained by [algomaniac](https://github.com/algomaniac) and [tapannallan](https://github.com/tapannallan).

# 📊 Ecosystem Health
* **Total Unique Recipes**: 25350
* **Ecosystem Auto-Update Health**: 85.86%
* **Ecosystem Reliability**: 92.1% (Sampled URL Health)
* **Official vs. Community**: 31133 Official / 49155 Community
* **Bucket Ecosystem**: 52 Scoop / 2 Shovel
* **Bucket Graveyard (Stale > 1 Year)**: 🪦 3

### Ecosystem Growth (All Recipes)
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="growth_all_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="growth_all_light.svg">
  <img alt="All Recipes Growth" src="growth_all_light.svg">
</picture>

### Scoop vs Shovel Growth
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="growth_scoop_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="growth_scoop_light.svg">
    <img alt="Scoop Recipes Growth" src="growth_scoop_light.svg" width="49%">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="growth_shovel_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="growth_shovel_light.svg">
    <img alt="Shovel Recipes Growth" src="growth_shovel_light.svg" width="49%">
  </picture>
</p>

# 🚀 Getting Started
To add and use any of the buckets listed below, simply run the following command in your terminal:
```powershell
scoop bucket add <bucket-name> <bucket-url>
```
For example, to add a specific bucket, find its URL from the list below and run:
```powershell
scoop bucket add my-awesome-bucket https://github.com/user/my-awesome-bucket
```
After adding the bucket, you can install any of its applications like this:
```powershell
scoop install my-awesome-bucket/<app-name>
```

# Third party buckets by popularity


## 💎 Hidden Gems
These buckets are actively maintained and feature a high percentage of **unique** applications not found in official repositories. Great for discovering niche tools!

| Repository | Unique Recipes | Total Recipes | Score | Auto-Update |
| :--- | :---: | :---: | :---: | :---: |
| **[littleli/scoop-clojure](directory/littleli+scoop-clojure.md)** | 💎 27 (100.0%) | 📦 27 | ⭐ 1.0 | 🔄 100% |
| **[TheRandomLabs/Scoop-Python](directory/TheRandomLabs+Scoop-Python.md)** | 💎 25 (100.0%) | 📦 25 | ⭐ 1.0 | 🔄 100% |
| **[borger/scoop-galaxy-integrations](directory/borger+scoop-galaxy-integrations.md)** | 💎 21 (100.0%) | 📦 21 | ⭐ 1.0 | 🔄 100% |
| **[ACooper81/scoop-apps](directory/ACooper81+scoop-apps.md)** | 💎 151 (99.3%) | 📦 152 | ⭐ 1.0 | 🔄 94% |
| **[Scoopforge/Extras-CN](directory/Scoopforge+Extras-CN.md)** | 💎 89 (98.9%) | 📦 90 | ⭐ 1.0 | 🔄 97% |
| **[kengwang/scoop-ctftools-bucket](directory/kengwang+scoop-ctftools-bucket.md)** | 💎 74 (96.1%) | 📦 77 | ⭐ 1.0 | 🔄 99% |
| **[arch3rPro/PST-Bucket](directory/arch3rPro+PST-Bucket.md)** | 💎 246 (94.6%) | 📦 260 | ⭐ 1.0 | 🔄 93% |
| **[tldrw/scoop-security](directory/tldrw+scoop-security.md)** | 💎 109 (91.6%) | 📦 119 | ⭐ 1.0 | 🔄 97% |
| **[amorphobia/siku](directory/amorphobia+siku.md)** | 💎 91 (91.0%) | 📦 100 | ⭐ 1.0 | 🔄 95% |
| **[hoilc/scoop-lemon](directory/hoilc+scoop-lemon.md)** | 💎 2292 (91.0%) | 📦 2520 | ⭐ 1.0 | 🔄 95% |







## 🥄 Scoop Compatible Buckets
These buckets are fully compatible with Scoop (and Shovel). They contain standard JSON manifests.

<details>
<summary><b>Click to expand 52 Scoop buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |
| **[anderlli0053/DEV-tools](directory/anderlli0053+DEV-tools.md)** | 📦 23621 | ⭐ 1.0 | 🔄 83% |  |
| **[cmontage/scoopbucket-third](directory/cmontage+scoopbucket-third.md)** | 📦 13738 | ⭐ 1.0 | 🔄 87% |  |
| **[kkzzhizhou/scoop-apps](directory/kkzzhizhou+scoop-apps.md)** | 📦 13531 | ⭐ 1.0 | 🔄 87% |  |
| **[lzwme/scoop-proxy-cn](directory/lzwme+scoop-proxy-cn.md)** | 📦 10673 | ⭐ 1.0 | 🔄 86% |  |
| **[duzyn/scoop-cn](directory/duzyn+scoop-cn.md)** | 📦 6337 | ⭐ 1.0 | 🔄 85% |  |
| **[hoilc/scoop-lemon](directory/hoilc+scoop-lemon.md)** | 📦 2520 | ⭐ 1.0 | 🔄 95% |  |
| **[ScoopInstaller/Extras](directory/ScoopInstaller+Extras.md)** | 📦 2300 | ⭐ 1.0 | 🔄 92% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[ScoopInstaller/Main](directory/ScoopInstaller+Main.md)** | 📦 1506 | ⭐ 1.0 | 🔄 94% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[DoveBoy/Apps](directory/DoveBoy+Apps.md)** | 📦 811 | ⭐ 1.0 | 🔄 100% |  |
| **[ScoopInstaller/Versions](directory/ScoopInstaller+Versions.md)** | 📦 571 | ⭐ 1.0 | 🔄 74% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[Calinou/scoop-games](directory/Calinou+scoop-games.md)** | 📦 398 | ⭐ 1.0 | 🔄 92% | ⭐ Known Scoop<br>⭐ Known Shovel |
| **[ScoopInstaller/PHP](directory/ScoopInstaller+PHP.md)** | 📦 391 | ⭐ 1.0 | 🔄 4% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[matthewjberger/scoop-nerd-fonts](directory/matthewjberger+scoop-nerd-fonts.md)** | 📦 366 | ⭐ 1.0 | 🔄 92% | ⭐ Known Scoop<br>⭐ Known Shovel |
| **[xrgzs/sdoog](directory/xrgzs+sdoog.md)** | 📦 342 | ⭐ 1.0 | 🔄 93% |  |
| **[ScoopInstaller/Java](directory/ScoopInstaller+Java.md)** | 📦 329 | ⭐ 1.0 | 🔄 86% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[akirco/aki-apps](directory/akirco+aki-apps.md)** | 📦 302 | ⭐ 1.0 | 🔄 86% |  |
| **[ScoopInstaller/Nirsoft](directory/ScoopInstaller+Nirsoft.md)** | 📦 290 | ⭐ 1.0 | 🔄 100% | 👑 Official Scoop |
| **[chawyehsu/dorado](directory/chawyehsu+dorado.md)** | 📦 271 | ⭐ 1.0 | 🔄 94% |  |
| **[arch3rPro/PST-Bucket](directory/arch3rPro+PST-Bucket.md)** | 📦 260 | ⭐ 1.0 | 🔄 93% |  |
| **[hu3rror/scoop-muggle](directory/hu3rror+scoop-muggle.md)** | 📦 164 | ⭐ 1.0 | 🔄 82% |  |
| **[ACooper81/scoop-apps](directory/ACooper81+scoop-apps.md)** | 📦 152 | ⭐ 1.0 | 🔄 94% |  |
| **[ViCrack/scoop-bucket](directory/ViCrack+scoop-bucket.md)** | 📦 148 | ⭐ 1.0 | 🔄 99% |  |
| **[ScoopInstaller/Nonportable](directory/ScoopInstaller+Nonportable.md)** | 📦 131 | ⭐ 1.0 | 🔄 88% | 👑 Official Scoop |
| **[tldrw/scoop-security](directory/tldrw+scoop-security.md)** | 📦 119 | ⭐ 1.0 | 🔄 97% |  |
| **[amorphobia/siku](directory/amorphobia+siku.md)** | 📦 100 | ⭐ 1.0 | 🔄 95% |  |
| **[Scoopforge/Extras-CN](directory/Scoopforge+Extras-CN.md)** | 📦 90 | ⭐ 1.0 | 🔄 97% |  |
| **[rasa/scoops](directory/rasa+scoops.md)** | 📦 78 | ⭐ 1.0 | 🔄 71% |  |
| **[kengwang/scoop-ctftools-bucket](directory/kengwang+scoop-ctftools-bucket.md)** | 📦 77 | ⭐ 1.0 | 🔄 99% |  |
| **[niheaven/scoop-sysinternals](directory/niheaven+scoop-sysinternals.md)** | 📦 75 | ⭐ 1.0 | 🔄 100% | ⭐ Known Scoop |
| **[TheRandomLabs/scoop-nonportable](directory/TheRandomLabs+scoop-nonportable.md)** | 📦 73 | ⭐ 1.0 | 🔄 86% | <br>⭐ Known Shovel |
| **[cderv/r-bucket](directory/cderv+r-bucket.md)** | 📦 54 | ⭐ 1.0 | 🔄 94% |  |
| **[zhoujin7/tomato](directory/zhoujin7+tomato.md)** | 📦 52 | ⭐ 1.0 | 🔄 85% |  |
| **[jonz94/scoop-sarasa-nerd-fonts](directory/jonz94+scoop-sarasa-nerd-fonts.md)** | 📦 49 | ⭐ 1.0 | 🔄 100% |  |
| **[Paxxs/Cluttered-bucket](directory/Paxxs+Cluttered-bucket.md)** | 📦 46 | ⭐ 1.0 | 🔄 91% |  |
| **[kkzzhizhou/scoop-zapps](directory/kkzzhizhou+scoop-zapps.md)** | 📦 34 | ⭐ 1.0 | 🔄 94% |  |
| **[wzv5/ScoopBucket](directory/wzv5+ScoopBucket.md)** | 📦 34 | ⭐ 1.0 | 🔄 97% |  |
| **[noql-net/scoop](directory/noql-net+scoop.md)** | 📦 28 | ⭐ 1.0 | 🔄 100% |  |
| **[TheRandomLabs/Scoop-Python](directory/TheRandomLabs+Scoop-Python.md)** | 📦 25 | ⭐ 1.0 | 🔄 100% |  |
| **[borger/scoop-galaxy-integrations](directory/borger+scoop-galaxy-integrations.md)** | 📦 21 | ⭐ 1.0 | 🔄 100% |  |
| **[TheCjw/scoop-retools](directory/TheCjw+scoop-retools.md)** | 📦 19 | ⭐ 1.0 | 🔄 79% |  |
| **[TheRandomLabs/Scoop-Spotify](directory/TheRandomLabs+Scoop-Spotify.md)** | 📦 10 | ⭐ 1.0 | 🔄 90% |  |
| **[EFLKumo/jam](directory/EFLKumo+jam.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |
| **[tetradice/scoop-iyokan-jp](directory/tetradice+scoop-iyokan-jp.md)** | 📦 13 | ⭐ 1.0 | 🔄 100% |  |
| **[tod-org/tod](directory/tod-org+tod.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |
| **[LSchallot/JellyRoller](directory/LSchallot+JellyRoller.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |
| **[exoscale/cli](directory/exoscale+cli.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |
| **[meshery/scoop-bucket](directory/meshery+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |
| **[Qv2ray/mochi](directory/Qv2ray+mochi.md)** | 📦 15 | ⭐ 1.0 | 🔄 53% |  |
| **[lumen-oss/rocks-scoop](directory/lumen-oss+rocks-scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |
| **[KNOXDEV/wsl](directory/KNOXDEV+wsl.md)** | 📦 12 | ⭐ 1.0 | 🔄 25% |  |
| **[TheRandomLabs/Scoop-Bucket](directory/TheRandomLabs+Scoop-Bucket.md)** | 📦 13 | ⭐ 1.0 | 🔄 85% |  |
| **[rkbk60/scoop-for-jp](directory/rkbk60+scoop-for-jp.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

</details>

## ⛏️ Shovel Specific Buckets
These buckets utilize Shovel-specific features (like native YAML manifests) or are explicitly tagged for Shovel. They may not work with standard Scoop.

<details>
<summary><b>Click to expand 2 Shovel buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |
| **[Small-Ku/turbo-bucket](directory/Small-Ku+turbo-bucket.md)** | 📦 49 | ⭐ 1.0 | 🔄 96% |  |
| **[littleli/scoop-clojure](directory/littleli+scoop-clojure.md)** | 📦 27 | ⭐ 1.0 | 🔄 100% |  |

</details>

## 📦 All Known Buckets
A combined list of every bucket discovered in the ecosystem.

<details>
<summary><b>Click to expand all 54 discovered buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |
| **[anderlli0053/DEV-tools](directory/anderlli0053+DEV-tools.md)** | 📦 23621 | ⭐ 1.0 | 🔄 83% |  |
| **[cmontage/scoopbucket-third](directory/cmontage+scoopbucket-third.md)** | 📦 13738 | ⭐ 1.0 | 🔄 87% |  |
| **[kkzzhizhou/scoop-apps](directory/kkzzhizhou+scoop-apps.md)** | 📦 13531 | ⭐ 1.0 | 🔄 87% |  |
| **[lzwme/scoop-proxy-cn](directory/lzwme+scoop-proxy-cn.md)** | 📦 10673 | ⭐ 1.0 | 🔄 86% |  |
| **[duzyn/scoop-cn](directory/duzyn+scoop-cn.md)** | 📦 6337 | ⭐ 1.0 | 🔄 85% |  |
| **[hoilc/scoop-lemon](directory/hoilc+scoop-lemon.md)** | 📦 2520 | ⭐ 1.0 | 🔄 95% |  |
| **[ScoopInstaller/Extras](directory/ScoopInstaller+Extras.md)** | 📦 2300 | ⭐ 1.0 | 🔄 92% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[ScoopInstaller/Main](directory/ScoopInstaller+Main.md)** | 📦 1506 | ⭐ 1.0 | 🔄 94% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[DoveBoy/Apps](directory/DoveBoy+Apps.md)** | 📦 811 | ⭐ 1.0 | 🔄 100% |  |
| **[ScoopInstaller/Versions](directory/ScoopInstaller+Versions.md)** | 📦 571 | ⭐ 1.0 | 🔄 74% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[Calinou/scoop-games](directory/Calinou+scoop-games.md)** | 📦 398 | ⭐ 1.0 | 🔄 92% | ⭐ Known Scoop<br>⭐ Known Shovel |
| **[ScoopInstaller/PHP](directory/ScoopInstaller+PHP.md)** | 📦 391 | ⭐ 1.0 | 🔄 4% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[matthewjberger/scoop-nerd-fonts](directory/matthewjberger+scoop-nerd-fonts.md)** | 📦 366 | ⭐ 1.0 | 🔄 92% | ⭐ Known Scoop<br>⭐ Known Shovel |
| **[xrgzs/sdoog](directory/xrgzs+sdoog.md)** | 📦 342 | ⭐ 1.0 | 🔄 93% |  |
| **[ScoopInstaller/Java](directory/ScoopInstaller+Java.md)** | 📦 329 | ⭐ 1.0 | 🔄 86% | 👑 Official Scoop<br>⭐ Known Shovel |
| **[akirco/aki-apps](directory/akirco+aki-apps.md)** | 📦 302 | ⭐ 1.0 | 🔄 86% |  |
| **[ScoopInstaller/Nirsoft](directory/ScoopInstaller+Nirsoft.md)** | 📦 290 | ⭐ 1.0 | 🔄 100% | 👑 Official Scoop |
| **[chawyehsu/dorado](directory/chawyehsu+dorado.md)** | 📦 271 | ⭐ 1.0 | 🔄 94% |  |
| **[arch3rPro/PST-Bucket](directory/arch3rPro+PST-Bucket.md)** | 📦 260 | ⭐ 1.0 | 🔄 93% |  |
| **[hu3rror/scoop-muggle](directory/hu3rror+scoop-muggle.md)** | 📦 164 | ⭐ 1.0 | 🔄 82% |  |
| **[ACooper81/scoop-apps](directory/ACooper81+scoop-apps.md)** | 📦 152 | ⭐ 1.0 | 🔄 94% |  |
| **[ViCrack/scoop-bucket](directory/ViCrack+scoop-bucket.md)** | 📦 148 | ⭐ 1.0 | 🔄 99% |  |
| **[ScoopInstaller/Nonportable](directory/ScoopInstaller+Nonportable.md)** | 📦 131 | ⭐ 1.0 | 🔄 88% | 👑 Official Scoop |
| **[tldrw/scoop-security](directory/tldrw+scoop-security.md)** | 📦 119 | ⭐ 1.0 | 🔄 97% |  |
| **[amorphobia/siku](directory/amorphobia+siku.md)** | 📦 100 | ⭐ 1.0 | 🔄 95% |  |
| **[Scoopforge/Extras-CN](directory/Scoopforge+Extras-CN.md)** | 📦 90 | ⭐ 1.0 | 🔄 97% |  |
| **[rasa/scoops](directory/rasa+scoops.md)** | 📦 78 | ⭐ 1.0 | 🔄 71% |  |
| **[kengwang/scoop-ctftools-bucket](directory/kengwang+scoop-ctftools-bucket.md)** | 📦 77 | ⭐ 1.0 | 🔄 99% |  |
| **[niheaven/scoop-sysinternals](directory/niheaven+scoop-sysinternals.md)** | 📦 75 | ⭐ 1.0 | 🔄 100% | ⭐ Known Scoop |
| **[TheRandomLabs/scoop-nonportable](directory/TheRandomLabs+scoop-nonportable.md)** | 📦 73 | ⭐ 1.0 | 🔄 86% | <br>⭐ Known Shovel |
| **[cderv/r-bucket](directory/cderv+r-bucket.md)** | 📦 54 | ⭐ 1.0 | 🔄 94% |  |
| **[zhoujin7/tomato](directory/zhoujin7+tomato.md)** | 📦 52 | ⭐ 1.0 | 🔄 85% |  |
| **[Small-Ku/turbo-bucket](directory/Small-Ku+turbo-bucket.md)** | 📦 49 | ⭐ 1.0 | 🔄 96% |  |
| **[jonz94/scoop-sarasa-nerd-fonts](directory/jonz94+scoop-sarasa-nerd-fonts.md)** | 📦 49 | ⭐ 1.0 | 🔄 100% |  |
| **[Paxxs/Cluttered-bucket](directory/Paxxs+Cluttered-bucket.md)** | 📦 46 | ⭐ 1.0 | 🔄 91% |  |
| **[kkzzhizhou/scoop-zapps](directory/kkzzhizhou+scoop-zapps.md)** | 📦 34 | ⭐ 1.0 | 🔄 94% |  |
| **[wzv5/ScoopBucket](directory/wzv5+ScoopBucket.md)** | 📦 34 | ⭐ 1.0 | 🔄 97% |  |
| **[noql-net/scoop](directory/noql-net+scoop.md)** | 📦 28 | ⭐ 1.0 | 🔄 100% |  |
| **[littleli/scoop-clojure](directory/littleli+scoop-clojure.md)** | 📦 27 | ⭐ 1.0 | 🔄 100% |  |
| **[TheRandomLabs/Scoop-Python](directory/TheRandomLabs+Scoop-Python.md)** | 📦 25 | ⭐ 1.0 | 🔄 100% |  |
| **[borger/scoop-galaxy-integrations](directory/borger+scoop-galaxy-integrations.md)** | 📦 21 | ⭐ 1.0 | 🔄 100% |  |
| **[TheCjw/scoop-retools](directory/TheCjw+scoop-retools.md)** | 📦 19 | ⭐ 1.0 | 🔄 79% |  |
| **[TheRandomLabs/Scoop-Spotify](directory/TheRandomLabs+Scoop-Spotify.md)** | 📦 10 | ⭐ 1.0 | 🔄 90% |  |
| **[EFLKumo/jam](directory/EFLKumo+jam.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |
| **[tetradice/scoop-iyokan-jp](directory/tetradice+scoop-iyokan-jp.md)** | 📦 13 | ⭐ 1.0 | 🔄 100% |  |
| **[tod-org/tod](directory/tod-org+tod.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |
| **[LSchallot/JellyRoller](directory/LSchallot+JellyRoller.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |
| **[exoscale/cli](directory/exoscale+cli.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |
| **[meshery/scoop-bucket](directory/meshery+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |
| **[Qv2ray/mochi](directory/Qv2ray+mochi.md)** | 📦 15 | ⭐ 1.0 | 🔄 53% |  |
| **[lumen-oss/rocks-scoop](directory/lumen-oss+rocks-scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |
| **[KNOXDEV/wsl](directory/KNOXDEV+wsl.md)** | 📦 12 | ⭐ 1.0 | 🔄 25% |  |
| **[TheRandomLabs/Scoop-Bucket](directory/TheRandomLabs+Scoop-Bucket.md)** | 📦 13 | ⭐ 1.0 | 🔄 85% |  |
| **[rkbk60/scoop-for-jp](directory/rkbk60+scoop-for-jp.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

</details>

# 🛠️ Operational Health (Crawler Metrics)
* **Total Crawler Runs**: 1
* **Total Repo Updates**: 60
* **Ecosystem Growth (Since Last Run)**:
  * 🪣 +0 Buckets
  * 📦 +0 Recipes
* **Eviction Count**: 🗑️ 0
* **API Rate Limit Retries**: ⏳ 0
* **Cache Size**: 💾 2.13 MB
* **Pipeline Times (Last Run)**:
  * 🔍 Discovery: 2.19s
  * 📥 Update: 510.99s
* **Cumulative Compute Time**: 8.6 minutes
