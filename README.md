<!-- DWP GitHub Profile Dashboard v0.4 | First restrained enhancement -->
<h1 align="center">KONAN931 <code>// DWP™</code></h1>

<p align="center">
  <samp>I'm learning through various projects, small and big failures, front-, and backend experiments — particularly programming languages, systems programming and developer workflows.</samp>
  <br>
  <samp>Also an eye on security, scientific computing, film-making and music, analog and digital. No lang-religions.</samp>
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
---

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

**[compact-dev](https://github.com/Konan931/compact-dev)** — A compact, inspectable project generator and repository auditor with composable presets.

Contributions are welcome, especially for planned `go-cli` and `c-cli` presets with real build/test flows. TypeScript/Node overlays and audit improvements are also on the [roadmap](https://github.com/Konan931/compact-dev/blob/main/docs/roadmap.md). See [CONTRIBUTING.md](https://github.com/Konan931/compact-dev/blob/main/CONTRIBUTING.md).

### Public technical projects

- **[polyglot_topics_lab](https://github.com/Konan931/polyglot_topics_lab)** — Programming and tooling experiments across languages.
- **[coding-platform-quality-watch](https://github.com/Konan931/coding-platform-quality-watch)** — Reproducing and documenting issues in coding-learning platforms.
- **[C-Repo](https://github.com/Konan931/C-Repo)** — A collection of C utilities and experiments with strings, files, memory and more.

### Berlin & Brandenburg · Pilzatlas (DE)

**[Pilzatlas-Lab](https://github.com/Konan931/Pilzatlas-Lab)** — Ein experimenteller Pilzatlas mit Karten, Datenquellen und Exkursionsplanung für Berlin und Brandenburg. Hinweise, Tests und Beiträge zur Weiterentwicklung sind willkommen.

### Beyond the public repositories

I also work on film and music projects; not all of that work is public here. For related projects and collaborations, see [Digital Welfare Productions](https://github.com/Digital-Welfare-Productions).

## GitHub activity

<p align="center">
  <a href="https://github.com/Konan931?tab=repositories">
    <img
      height="170"
      src="https://github-stats-extended.vercel.app/api?username=Konan931&amp;show_icons=true&amp;hide_rank=true&amp;hide_border=true&amp;theme=transparent"
      alt="Konan931 public GitHub activity statistics"
    >
  </a>
  <a href="https://github.com/Konan931?tab=repositories">
    <img
      height="170"
      src="https://github-stats-extended.vercel.app/api/top-langs/?username=Konan931&amp;layout=compact&amp;langs_count=8&amp;hide_border=true&amp;theme=transparent"
      alt="Languages by repository code on GitHub"
    >
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
