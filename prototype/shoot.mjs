// Screenshot di verifica del prototipo con Chrome di sistema.
// Uso: node shoot.mjs
import { chromium } from "playwright-core";
import { mkdirSync } from "node:fs";

mkdirSync("shots", { recursive: true });
const browser = await chromium.launch({ channel: "chrome" });
const errors = [];

async function shoot(page, url, name, { width = 1440, height = 900, actions = [] } = {}) {
  await page.setViewportSize({ width, height });
  await page.goto(url, { waitUntil: "networkidle" });
  await page.waitForTimeout(900);
  for (const a of actions) {
    if (a.scrollTo != null) { await page.evaluate((y) => scrollTo({ top: y, behavior: "instant" }), a.scrollTo); await page.waitForTimeout(a.wait ?? 1100); }
    if (a.click) { await page.click(a.click); await page.waitForTimeout(a.wait ?? 900); }
    if (a.eval) { await page.evaluate(a.eval); await page.waitForTimeout(a.wait ?? 600); }
    await page.screenshot({ path: `shots/${name}-${a.tag}.png` });
  }
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
  console.log(`${name}: overflow-x = ${overflow}px`);
}

for (const [file, base] of [["index.html", "landing"], ["alta-gallura.html", "gallura"]]) {
  const page = await browser.newPage();
  page.on("console", (m) => m.type() === "error" && errors.push(`${base}: ${m.text()}`));
  page.on("pageerror", (e) => errors.push(`${base}: PAGEERROR ${e.message}`));
  const url = `file://${process.cwd()}/${file}`;

  if (base === "landing") {
    await shoot(page, url, `${base}-d`, { actions: [
      { tag: "01-hero" },
      { scrollTo: 1200, tag: "02-cap1" },
      { scrollTo: 3000, tag: "03-cap3" },
      { scrollTo: 5200, tag: "04-cap5" },
      { eval: () => document.getElementById("progetto").scrollIntoView({ behavior: "instant" }), tag: "05-progetto" },
      { eval: () => document.getElementById("sezioni").scrollIntoView({ behavior: "instant" }), tag: "06-porte" },
      { eval: () => scrollTo(0, document.body.scrollHeight), tag: "07-footer" },
    ]});
  } else {
    await shoot(page, url, `${base}-d`, { actions: [
      { tag: "01-hero" },
      { scrollTo: 2000, tag: "02-cap3" },
      { eval: () => document.getElementById("popolazione").scrollIntoView({ behavior: "instant" }), tag: "03-pop" },
      { eval: () => document.getElementById("saldi").scrollIntoView({ behavior: "instant" }), tag: "04-saldi" },
      { eval: () => document.getElementById("economia").scrollIntoView({ behavior: "instant" }), tag: "05-economia" },
      { eval: () => document.getElementById("ambiente").scrollIntoView({ behavior: "instant" }), tag: "06-ambiente" },
      { eval: () => document.getElementById("comuni").scrollIntoView({ behavior: "instant" }), tag: "07-comuni" },
      { click: "[data-comune='calangianus']", tag: "08-drawer", wait: 1100 },
      { eval: () => document.getElementById("approfondimenti").scrollIntoView({ behavior: "instant" }), tag: "09-approf", wait: 400 },
    ]});
    // mobile
    await shoot(page, url, `${base}-m`, { width: 390, height: 844, actions: [
      { tag: "01-hero" },
      { eval: () => document.getElementById("popolazione").scrollIntoView({ behavior: "instant" }), tag: "02-pop" },
      { eval: () => document.getElementById("comuni").scrollIntoView({ behavior: "instant" }), tag: "03-comuni" },
      { click: "[data-comune='calangianus']", tag: "04-drawer" },
    ]});
  }
  await page.close();
}
const lm = await browser.newPage();
lm.on("pageerror", (e) => errors.push(`landing-m: PAGEERROR ${e.message}`));
await shoot(lm, `file://${process.cwd()}/index.html`, "landing-m", { width: 390, height: 844, actions: [
  { tag: "01-hero" },
  { scrollTo: 1000, tag: "02-cards" },
]});
await lm.close();

/* ---- pagine nuove ---- */
async function shootPage(file, base, actions, mobile) {
  const page = await browser.newPage();
  page.on("console", (m) => m.type() === "error" && errors.push(`${base}: ${m.text()}`));
  page.on("pageerror", (e) => errors.push(`${base}: PAGEERROR ${e.message}`));
  await shoot(page, `file://${process.cwd()}/${file}`, `${base}-d`, { actions });
  if (mobile) await shoot(page, `file://${process.cwd()}/${file}`, `${base}-m`, { width: 390, height: 844, actions: mobile });
  await page.close();
}

await shootPage("progetto.html", "progetto", [
  { tag: "01-hero" },
  { eval: () => document.getElementById("metodo").scrollIntoView({ behavior: "instant" }), tag: "02-metodo" },
  { eval: () => document.getElementById("gruppo").scrollIntoView({ behavior: "instant" }), tag: "03-gruppo" },
  { eval: () => document.getElementById("documenti").scrollIntoView({ behavior: "instant" }), tag: "04-doc" },
], [
  { tag: "01-hero" },
  { eval: () => document.getElementById("documenti").scrollIntoView({ behavior: "instant" }), tag: "02-doc" },
]);

await shootPage("strategia.html", "strategia", [
  { tag: "01-hero" },
  { eval: () => document.getElementById("filiere").scrollIntoView({ behavior: "instant" }), tag: "02-filiere" },
  { eval: () => document.getElementById("roadmap").scrollIntoView({ behavior: "instant" }), tag: "03-roadmap" },
  { eval: () => document.querySelector(".tl-pill").click(), tag: "04-pill", wait: 1000 },
  { eval: () => document.getElementById("approfondimenti")?.scrollIntoView({ behavior: "instant" }), tag: "05-approf", wait: 400 },
], [
  { tag: "01-hero" },
  { eval: () => document.getElementById("roadmap").scrollIntoView({ behavior: "instant" }), tag: "02-roadmap" },
]);

await shootPage("sughero-sardegna.html", "sughero", [
  { tag: "01-hero" },
  { scrollTo: 1800, tag: "02-cap" },
  { eval: () => document.getElementById("risorsa").scrollIntoView({ behavior: "instant" }), tag: "03-risorsa" },
  { eval: () => document.getElementById("esploratore").scrollIntoView({ behavior: "instant" }), tag: "04-esploratore" },
  { eval: () => document.querySelector("[data-open30]").click(), tag: "05-drawer", wait: 1100 },
  { eval: () => { document.querySelector(".drawer-overlay")?.click(); }, tag: "06-drawer-chiuso", wait: 500 },
  { eval: () => document.getElementById("approfondimenti").scrollIntoView({ behavior: "instant" }), tag: "07-approf", wait: 400 },
], [
  { tag: "01-hero" },
  { eval: () => document.getElementById("esploratore").scrollIntoView({ behavior: "instant" }), tag: "02-esploratore" },
  { eval: () => document.querySelector("[data-open30]").click(), tag: "03-drawer", wait: 1100 },
]);

await shootPage("innovazione.html", "innovazione", [
  { tag: "01-hero" },
  { eval: () => document.getElementById("ricerca").scrollIntoView({ behavior: "instant" }), tag: "02-ricerca" },
  { eval: () => document.getElementById("direttrici").scrollIntoView({ behavior: "instant" }), tag: "03-direz" },
  { eval: () => document.getElementById("framework").scrollIntoView({ behavior: "instant" }), tag: "04-framework" },
  { eval: () => document.getElementById("sintesi").scrollIntoView({ behavior: "instant" }), tag: "05-sintesi" },
  { eval: () => document.getElementById("biblioteca").scrollIntoView({ behavior: "instant" }), tag: "06-biblio" },
  { eval: () => { const i = document.getElementById("b-q"); i.value = "compositi"; i.dispatchEvent(new Event("input")); }, tag: "07-ricerca-compositi", wait: 800 },
], [
  { tag: "01-hero" },
  { eval: () => document.getElementById("biblioteca").scrollIntoView({ behavior: "instant" }), tag: "02-biblio" },
]);

console.log(errors.length ? `\nERRORI:\n${errors.join("\n")}` : "\nNessun errore console.");
await browser.close();
