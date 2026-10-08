<!-- DWP GitHub Profile Dashboard v0.4 | First restrained enhancement -->
<h1 align="center">KONAN931 <code>// DWP™</code></h1>

<p align="center">
  <samp>Digital Welfare Productions™ · Systems · Security · Science · Creative Code</samp>
  <br>
  <samp>Low-level curiosity. High-level experiments. Inspectable results.</samp>
</p>

<p align="center">
  <img
    src="https://komarev.com/ghpvc/?username=Konan931&amp;label=EYES%20ON%20SYSTEM&amp;color=7e302c&amp;style=flat-square"
    alt="Approximate GitHub profile view counter"
  >
</p>

> **Just (de)coding.** Beyond syntax: systems, science, security, and strange but useful experiments.

## Featured work

- **[Pilzatlas-Lab](https://github.com/Konan931/Pilzatlas-Lab)** — Field-research tooling for fungi, habitats, and exploratory mapping.
- **[coding-platform-quality-watch](https://github.com/Konan931/coding-platform-quality-watch)** — Reproducibility-focused tooling for investigating coding-platform behavior.
- **[polyglot_topics_lab](https://github.com/Konan931/polyglot_topics_lab)** — Cross-language programming experiments and comparisons.

## GitHub telemetry

<p align="center">
  <a href="https://github.com/Konan931?tab=repositories">
    <img
      height="170"
      src="https://github-stats-extended.vercel.app/api?username=Konan931&amp;show_icons=true&amp;hide_border=true&amp;theme=transparent"
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

---

<sub>Digital Welfare Productions™ · Think, test, trace, repeat.</sub>
