/* Materia e comunità: SVG leggeri, geometrie deterministiche, nessun loop di rendering. */
(() => {
  "use strict";
  const reduced = matchMedia("(prefers-reduced-motion: reduce)");
  const ns = "http://www.w3.org/2000/svg";
  const number = new Intl.NumberFormat("it-IT");
  const svgNode = (tag, attrs) => {
    const node = document.createElementNS(ns, tag);
    Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value));
    return node;
  };

  const cork = document.getElementById("cork-study");
  if (cork) {
    cork.innerHTML = `<p class="material-label">Studio di materia <span>01 — Sughero</span></p>
      <svg class="cork-section" viewBox="0 0 600 600" role="img" aria-label="Interpretazione del sughero: dodici strati irregolari e una trama porosa"></svg>
      <div class="cork-controls"><label for="cork-growth">Fai crescere la trama <output for="cork-growth">12 / 12</output></label>
      <input id="cork-growth" type="range" min="1" max="12" value="12" step="1" aria-valuetext="12 strati su 12">
      <p>Dodici anelli, un richiamo al ciclo di decortica.</p></div>`;
    const svg = cork.querySelector("svg");
    const layers = [];
    // The same perturbations keep the contours nested, like a cut through bark.
    for (let ring = 12; ring >= 1; ring--) {
      const layer = svgNode("g", { class: "cork-layer", "data-layer": ring });
      let path = "";
      for (let j = 0; j <= 120; j++) {
        const angle = j / 120 * Math.PI * 2;
        const radius = (16 + ring * 19) * (1 + .058 * Math.sin(angle * 3 + .7) + .028 * Math.cos(angle * 7) + .012 * Math.sin(angle * 13));
        const x = 300 + Math.cos(angle) * radius;
        const y = 300 + Math.sin(angle) * radius * .94;
        path += `${j ? "L" : "M"}${x.toFixed(1)},${y.toFixed(1)} `;
      }
      layer.append(svgNode("path", { d: path + "Z", fill: ring % 3 === 0 ? "#E8C28E" : "#F1DEC0", "fill-opacity": ".13", stroke: ring % 3 === 0 ? "#A96A47" : "#C3976E", "stroke-width": ring % 3 === 0 ? "1.6" : ".8", pathLength: "1", class: "cork-contour" }));
      let pores = "";
      for (let p = 0; p < ring * 4; p++) {
        const a = p * 2.39996 + ring * .8;
        const r = (16 + ring * 19 - 7) * (1 + .058 * Math.sin(a * 3 + .7) + .028 * Math.cos(a * 7) + .012 * Math.sin(a * 13));
        const x = 300 + Math.cos(a) * r;
        const y = 300 + Math.sin(a) * r * .94;
        pores += `M${x.toFixed(1)},${y.toFixed(1)}l${(1.5 + p % 4).toFixed(1)},${(p % 3 - 1).toFixed(1)} `;
      }
      layer.append(svgNode("path", { d: pores, stroke: "#976443", "stroke-width": "1.3", "stroke-linecap": "round", opacity: ".42", fill: "none" }));
      svg.append(layer);
      layers.push(layer);
    }
    const input = cork.querySelector("input");
    const update = () => {
      layers.forEach(layer => layer.classList.toggle("dormant", +layer.dataset.layer > +input.value));
      cork.querySelector("output").textContent = `${input.value} / 12`;
      input.setAttribute("aria-valuetext", `${input.value} strati su 12`);
    };
    input.addEventListener("input", update);
    // One finite reveal. Native range works with pointer, touch and keyboard.
    if (!reduced.matches) layers.forEach(layer => {
      layer.querySelector(".cork-contour").animate(
        [{ strokeDasharray: "1", strokeDashoffset: "1", opacity: .1 }, { strokeDasharray: "1", strokeDashoffset: "0", opacity: 1 }],
        { duration: 1800, delay: +layer.dataset.layer * 80, easing: "ease-out" }
      );
    });
  }

  const centers = [[85,90],[210,65],[345,80],[465,72],[140,210],[310,200],[480,195],[95,340],[315,365],[490,335],[175,465]];
  function communityPoints(comuni) {
    return comuni.flatMap((c, group) => Array.from({ length: Math.round(c.abitanti_2025 / 100) }, (_, i) => {
      const angle = i * 2.39996;
      const radius = Math.sqrt(i) * 5.4;
      return { x: centers[group][0] + Math.cos(angle) * radius, y: centers[group][1] + Math.sin(angle) * radius,
        color: c.fascia === "costiera" ? "var(--blue)" : "var(--green)" };
    }));
  }
  window.initCommunityField = (root, comuni) => {
    const svg = svgNode("svg", { viewBox: "0 0 580 540" });
    communityPoints(comuni).forEach((p, i) => {
      const dot = svgNode("circle", { cx: p.x, cy: p.y, r: "2.7", fill: p.color });
      svg.append(dot);
      if (!reduced.matches) dot.animate(
        [{ opacity: 0, transform: `translate(${(i % 7 - 3) * 5}px, 14px)` }, { opacity: 1, transform: "translate(0, 0)" }],
        { duration: 1400, delay: i % 19 * 25, easing: "ease-out", fill: "backwards" }
      );
    });
    root.append(svg);
    root.insertAdjacentHTML("beforeend", `<span class="community-signature">11 comunità. Un territorio condiviso.</span>`);
  };

  window.initPopulationStory = (root, chapters, skipTo) => {
    root.classList.add("population-story");
    const labels = ["Le comunità", "Le due velocità", "Chi arriva", "Le generazioni"];
    root.innerHTML = `<div class="container">
      <div class="population-heading"><p class="section-eyebrow">Il territorio è fatto di persone</p><a href="#${skipTo}">Vai ai dati completi <span aria-hidden="true">↗</span></a></div>
      <div class="population-tabs" role="tablist" aria-label="Quattro letture della popolazione">${labels.map((label, i) => `<button type="button" id="population-tab-${i}" role="tab" aria-selected="${i === 0}" aria-controls="population-panel" tabindex="${i === 0 ? 0 : -1}" data-scene="${i}"><span>0${i + 1}</span>${label}</button>`).join("")}</div>
      <div class="population-panel" id="population-panel" role="tabpanel" aria-labelledby="population-tab-0" tabindex="0">
        <div class="population-copy"><p class="chapter-index"></p><h2 class="chapter-title"></h2><p class="chapter-context"></p><p class="population-value"></p><p class="population-value-label"></p><p class="chapter-source"></p></div>
        <figure class="population-figure"><svg viewBox="0 0 580 540" role="img" aria-labelledby="population-graphic-title"><title id="population-graphic-title"></title><g class="people-points"></g></svg><figcaption></figcaption></figure>
      </div></div>`;
    const svg = root.querySelector("svg");
    const pointGroup = root.querySelector(".people-points");
    const dots = Array.from({ length: 401 }, (_, i) => {
      const dot = svgNode("circle", { r: "3", cx: "0", cy: "0", class: "person-point", style: `--delay:${i % 13 * 12}ms` });
      pointGroup.append(dot);
      return dot;
    });
    const labelGroup = svgNode("g", { class: "population-chart-labels", "aria-hidden": "true" });
    svg.append(labelGroup);
    const grid = (count, x, y, color, columns = 15, spacing = 10) => Array.from({ length: count }, (_, i) => ({ x: x + i % columns * spacing, y: y + Math.floor(i / columns) * spacing, color }));
    const scenes = [
      { points: communityPoints(window.RISSTE_DATA.comuni), labels: [[30,520,"Costa", "var(--blue)"],[330,520,"Interno", "var(--green)"]], caption: "Ogni punto ≈ 100 residenti nel 2025. Un gruppo per comune; disposizione non geografica. Blu: costa. Verde: interno.", title: "Undici gruppi di residenti, uno per comune: 35.242 abitanti complessivi." },
      { points: [...grid(106,60,145,"var(--blue)"), ...grid(246,330,145,"var(--green)")], labels: [[60,95,"COSTA · 4 COMUNI"],[60,120,"10.616 · +14,0 %"],[330,95,"INTERNO · 7 COMUNI"],[330,120,"24.626 · −10,1 %"]], caption: "Ogni punto ≈ 100 residenti nel 2025. Variazioni rispetto al 2001. Fonte: Studio 1, Tab. 1c, p. 25.", title: "Costa: 10.616 residenti, più 14 per cento dal 2001. Interno: 24.626 residenti, meno 10,1 per cento." },
      { points: [...grid(34,60,180,"var(--cork)",7,20), ...grid(33,330,180,"var(--green)",7,20)], labels: [[60,120,"SALDO NATURALE"],[60,148,"−3.402"],[330,120,"SALDO MIGRATORIO"],[330,148,"+3.286"],[60,355,"96,6 % del deficit compensato"]], caption: "Ogni punto ≈ 100 persone di saldo, 2002–2023. Nati meno morti a sinistra; iscritti meno cancellati a destra.", title: "Saldo naturale meno 3.402; saldo migratorio più 3.286. Compensazione del 96,6 per cento." },
      { points: [...grid(100,60,160,"var(--blue)",10,11), ...grid(301,320,160,"var(--green)",16,11)], labels: [[60,100,"UNDER 15"],[60,130,"100 giovani"],[320,100,"OVER 65"],[320,130,"301 anziani"]], caption: "Ogni punto = 1 persona nel rapporto tra anziani e giovani. Indice di vecchiaia 2025, non popolazione totale.", title: "Per ogni 100 giovani sotto i 15 anni ci sono 301 persone con più di 65 anni." },
    ];
    const buttons = [...root.querySelectorAll("[role=tab]")];
    let active = -1;
    const show = (index) => {
      if (active === index) return;
      active = index;
      const c = chapters[index], scene = scenes[index];
      root.dataset.scene = index;
      root.querySelector("[role=tabpanel]").setAttribute("aria-labelledby", `population-tab-${index}`);
      buttons.forEach((b, i) => { b.setAttribute("aria-selected", i === index); b.tabIndex = i === index ? 0 : -1; });
      const values = { ".chapter-index": `0${index + 1} / 04 — ${labels[index]}`, ".chapter-title": c.title, ".chapter-context": c.context,
        ".population-value": `${c.prefix || ""}${number.format(c.value)}${c.unit ? " " + c.unit : ""}`, ".population-value-label": c.valueLabel, ".chapter-source": `Fonte: ${c.source}` };
      Object.entries(values).forEach(([selector, text]) => { root.querySelector(selector).textContent = text; });
      root.querySelector("figcaption").textContent = scene.caption;
      root.querySelector("title").textContent = scene.title;
      dots.forEach((dot, i) => {
        const p = scene.points[i];
        dot.style.opacity = p ? "1" : "0";
        if (p) { dot.style.transform = `translate(${p.x}px, ${p.y}px)`; dot.style.fill = p.color; }
      });
      labelGroup.replaceChildren();
      scene.labels.forEach(([x, y, text, color]) => { const label = svgNode("text", { x, y, fill: color || "var(--ink-muted)" }); label.textContent = text; labelGroup.append(label); });
    };
    buttons.forEach((button, i) => {
      button.addEventListener("click", () => show(i));
      button.addEventListener("keydown", e => {
        const keys = { ArrowRight: (i + 1) % 4, ArrowLeft: (i + 3) % 4, Home: 0, End: 3 };
        if (!(e.key in keys)) return;
        e.preventDefault();
        const next = keys[e.key];
        show(next); buttons[next].focus();
      });
    });
    show(0);
  };
})();
