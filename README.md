<!-- Profile README visual pass v0.5; artwork and theme-aware stats -->
<h1 align="center">KONAN931 <code>// DWP™</code></h1>

<p align="center">
  <img
    src="https://i.ibb.co/Xkp97BYT/D8662870-5-DD7-4145-9-E4-F-ED9-A0-E18-F372.png"
    width="100%"
    alt="Artwork selected for the Konan931 GitHub profile"
  >
</p>

<p align="center">
  <samp>I'm learning through projects, experiments, and failures both small and large — especially around programming languages, systems programming, and developer tools.</samp>
  <br>
  <samp>Also interested in security, scientific computing, filmmaking, and music, both analog and digital. No language dogma.</samp>
</p>

---

## Binary greeting

<details>
<summary><strong>Reveal the original C source</strong> · <code>./github_greeting</code></summary>

```c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void githubGreeting() {
    const char *binaryGreeting[] = {
        "01001010","01110101","01110011","01110100","00100000",
        "00101000","01100100","01100101","00101001","01100011",
        "01101111","01100100","01101001","01101110","01100111",
        "00101110"
    };

    for (int i = 0; i < 16; ++i) {
        long v = strtol(binaryGreeting[i], NULL, 2);
        putchar((char)v);
    }
    putchar('\n');
}

void githubGreetingTok() {
    char buffer[235];
    strcpy(buffer,
      "00111100 01001010 01110101 01110011 01110100 00100000 "
      "00101000 01100100 01100101 00101001 01100011 "
      "01101111 01100100 01101001 01101110 01100111 "
      "00100000 01110100 01101111 01101011 01100101 "
      "01101110 01110011 00101110 00101010 00111110 "
    );

    const char *delim = " ";
    char *token = strtok(buffer, delim);
    while (token) {
        long v = strtol(token, NULL, 2);
        putchar((char)v);
        token = strtok(NULL, delim);
    }
    putchar('\n');
}

int main() {
    printf("Executing this little github greeting -> please wait (and stay calm)...\n");
    githubGreeting();
    githubGreetingTok();
    return 0;
}
```

</details>
<p align="center">
  <img
    src="https://komarev.com/ghpvc/?username=Konan931&amp;label=EYES%20ON%20SYSTEM&amp;color=7e302c&amp;style=flat-square"
    alt="Approximate GitHub profile view counter"
  >
</p>

> **Just (de)coding.** Some projects are useful; others are simply worth exploring.

## Featured work

### Templates

**[compact-dev](https://github.com/Konan931/compact-dev)** — A project generator and repository auditor with composable presets.

Contributions are welcome, especially for planned `go-cli` and `c-cli` presets with real build/test flows. TypeScript/Node overlays and audit improvements are also on the [roadmap](https://github.com/Konan931/compact-dev/blob/main/docs/roadmap.md). See [CONTRIBUTING.md](https://github.com/Konan931/compact-dev/blob/main/CONTRIBUTING.md).

### Projects & tools

- **[coding-platform-quality-watch](https://github.com/Konan931/coding-platform-quality-watch)** — Reproducible reports and a small web interface for examining problems in coding-learning platforms (v0.2 foundation).
- **[FreiFahren](https://github.com/Konan931/FreiFahren)** — My fork of the [original project](https://github.com/MaxL/FreiFahren). Exploring multi-city support and internationalization; these are [planned improvements](https://github.com/Konan931/FreiFahren/blob/main/docs/PHASE_2_MULTI_CITY.md), not finished features. Feedback and contributions welcome.
- **[netcontrol](https://github.com/Konan931/netcontrol)** — A small Python CLI for Linux network diagnostics, with JSON output and unit tests.

### Berlin & Brandenburg · Pilzatlas (DE)

**[Pilzatlas-Lab](https://github.com/Konan931/Pilzatlas-Lab)** — Ein experimenteller Pilzatlas mit Karten, Datenquellen und Exkursionsplanung für Berlin und Brandenburg. Hinweise, Tests und Beiträge zur Weiterentwicklung sind willkommen.

### Learning & experiments

**[C-Repo](https://github.com/Konan931/C-Repo)** — An older collection of C utilities and exercises. Kept as a learning repository, with room for fixes, tests and documentation improvements.

### Beyond the public repositories

I also work on film and music projects; not all of that work is public here. For related projects and collaborations, see [Digital Welfare Productions](https://github.com/Digital-Welfare-Productions).

## GitHub activity

<p align="center">
  <a href="https://github.com/Konan931?tab=repositories">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api?username=Konan931&amp;show_icons=true&amp;hide_rank=true&amp;hide_border=true&amp;theme=dark_github">
      <img width="390" src="https://github-stats-extended.vercel.app/api?username=Konan931&amp;show_icons=true&amp;hide_rank=true&amp;hide_border=true&amp;theme=light_github" alt="Konan931 public GitHub activity statistics">
    </picture>
  </a>
  <a href="https://github.com/Konan931?tab=repositories">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/top-langs/?username=Konan931&amp;layout=compact&amp;langs_count=8&amp;hide_border=true&amp;theme=dark_github">
      <img width="390" src="https://github-stats-extended.vercel.app/api/top-langs/?username=Konan931&amp;layout=compact&amp;langs_count=8&amp;hide_border=true&amp;theme=light_github" alt="Languages by code in public GitHub repositories">
    </picture>
  </a>
</p>

<sub>Statistics are indicative, not measures of skill. External image providers may cache results or be temporarily unavailable.</sub>

## Learning & profiles

**Boot.dev**

<p align="left">
  <img src="https://api.boot.dev/v1/users/public/73318f51-ed24-4329-b58e-80ef445a3f4f/thumbnail" alt="Konan931's Boot.dev profile card">
</p>

**W3Schools**

<a href="https://www.w3profile.com/KonanKompile/">
  <img
    src="https://img.shields.io/badge/W3Schools-KonanKompile-04AA6D?style=flat-square&amp;logo=w3schools&amp;logoColor=white"
    alt="W3Schools profile: KonanKompile"
  >
</a>

---

<sub>Digital Welfare Productions™ Unltd. International · 2026</sub>

---
![](https://hit.yhype.me/github/profile?account_id=168050918)
