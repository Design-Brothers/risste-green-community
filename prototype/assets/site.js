/* Green community Alta Gallura — prototipo v1: interazioni condivise */
(() => {
  "use strict";

  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const NARROW = () => matchMedia("(max-width: 767px)").matches;

  /* ---------- formato italiano ---------- */
  const nfInt = new Intl.NumberFormat("it-IT");
  const fmtInt = (n) => (n == null ? "—" : nfInt.format(Math.round(n)));
  const fmtDec = (n, d = 1) =>
    n == null ? "—" : new Intl.NumberFormat("it-IT", { minimumFractionDigits: d, maximumFractionDigits: d }).format(n);
  const fmtPct = (n, sign = false, d = 1) =>
    n == null ? "—" : `${sign && n > 0 ? "+" : ""}${fmtDec(n, d)} %`;
  window.fmt = { int: fmtInt, dec: fmtDec, pct: fmtPct };

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- nav ---------- */
  const nav = $(".nav");
  if (nav) {
    const onScroll = () => nav.classList.toggle("scrolled", scrollY > 30);
    addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- orbi fluttuanti ---------- */
  window.initOrbs = (container, orbs, { pointer = true, parallax = true } = {}) => {
    const layer = document.createElement("div");
    layer.className = "orbs";
    layer.setAttribute("aria-hidden", "true");
    const els = orbs.map((o, i) => {
      const el = document.createElement("div");
      el.className = "orb";
      el.style.cssText = `left:${o.x}%;top:${o.y}%;width:${o.size}px;height:${o.size}px;margin-left:${-o.size / 2}px;margin-top:${-o.size / 2}px;background:radial-gradient(circle at 40% 40%, ${o.colors[0]} 0%, ${o.colors[1]} 45%, transparent 72%);opacity:${o.opacity ?? 0.85};filter:blur(${o.blur ?? 48}px)`;
      layer.appendChild(el);
      if (!REDUCED) {
        el.animate(
          [
            { transform: "translate(0px, 0px)" },
            { transform: `translate(${o.drift}px, ${-o.drift * 0.8}px)` },
            { transform: `translate(${-o.drift * 0.6}px, ${o.drift * 0.5}px)` },
            { transform: "translate(0px, 0px)" },
          ],
          { duration: (o.duration ?? 18 + i * 3) * 1000, iterations: Infinity, easing: "ease-in-out", delay: -(o.delay ?? 0) * 1000 }
        );
      }
      return el;
    });
    container.prepend(layer);

    if (REDUCED) return;
    let px = 0, py = 0, sy = 0, raf = null;
    const paint = () => {
      raf = null;
      const ty = parallax ? -Math.min(scrollY, 900) * 0.14 : 0;
      layer.style.transform = `translate3d(${px * 10}px, ${py * 8 + ty}px, 0)`;
      els.forEach((el, i) => {
        const f = (i % 2 ? -1 : 1) * (1 + (i % 3) * 0.5);
        el.style.translate = `${px * 12 * f}px ${py * 10 * f}px`;
      });
      void sy;
    };
    const schedule = () => { if (!raf) raf = requestAnimationFrame(paint); };
    if (pointer) addEventListener("pointermove", (e) => {
      px = (e.clientX / innerWidth - 0.5) * 2;
      py = (e.clientY / innerHeight - 0.5) * 2;
      schedule();
    }, { passive: true });
    if (parallax) addEventListener("scroll", schedule, { passive: true });
  };

  /* palette dal brief (COMPONENTI.md §1) */
  window.ORB_PALETTES = {
    landing: [
      { x: 62, y: 18, size: 520, colors: ["#7CFF3F", "#3FE9FF"], drift: 26, delay: 0 },
      { x: 18, y: 48, size: 460, colors: ["#4E9A3F", "#7CFF3F"], drift: 22, delay: 4 },
      { x: 74, y: 60, size: 420, colors: ["#3FE9FF", "#2F6FB0"], drift: 30, delay: 8 },
      { x: 40, y: 82, size: 380, colors: ["#7CFF3F", "#4E9A3F"], drift: 18, delay: 2 },
      { x: 50, y: 42, size: 220, colors: ["#FFFFFF", "#DFFCF6"], drift: 12, delay: 6 },
    ],
    "alta-gallura-hero": [
      { x: 30, y: 42, size: 480, colors: ["#7CFF3F", "#4E9A3F"], drift: 24, delay: 0 },
      { x: 72, y: 40, size: 480, colors: ["#3FE9FF", "#2F6FB0"], drift: 24, delay: 6 },
    ],
    sughero: [{ x: 70, y: 40, size: 520, colors: ["#E8C28E", "#C2603A"], drift: 20, delay: 0 }],
  };

  /* ---------- reveal on scroll ---------- */
  const io = new IntersectionObserver(
    (entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add("in")),
    { threshold: 0.12 }
  );
  $$(".reveal").forEach((el) => io.observe(el));

  /* ---------- count-up ---------- */
  const countUp = (el, to, { dur = 900, dec = 0, prefix = "", suffix = "" } = {}) => {
    if (REDUCED) { el.textContent = prefix + (dec ? fmtDec(to, dec) : fmtInt(to)) + suffix; return; }
    const t0 = performance.now();
    const step = (t) => {
      const k = Math.min(1, (t - t0) / dur);
      const e = 1 - Math.pow(1 - k, 3);
      const v = to * e;
      el.textContent = prefix + (dec ? fmtDec(v, dec) : fmtInt(v)) + suffix;
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const ioCount = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target;
      ioCount.unobserve(el);
      countUp(el, parseFloat(el.dataset.count), {
        dec: +(el.dataset.dec || 0), prefix: el.dataset.prefix || "", suffix: el.dataset.suffix || "",
      });
    });
  }, { threshold: 0.5 });
  $$("[data-count]").forEach((el) => ioCount.observe(el));

  /* ---------- anelli di decortica ---------- */
  window.decorticaRings = ({ size = 480, tone = "green", spin = false, id = "g" } = {}) => {
    const [a, b] = tone === "green" ? ["#4E9A3F", "#3FE9FF"] : ["#C2603A", "#E8C28E"];
    let circles = "";
    for (let i = 0; i < 12; i++) {
      circles += `<circle cx="50" cy="50" r="${4 + i * 3.8}" fill="none" stroke="url(#rings-${id})" stroke-width="${i % 3 === 0 ? 2.2 : 1.1}" opacity="${0.25 + (i / 12) * 0.6}"/>`;
    }
    return `<svg class="rings${spin ? " spin" : ""}" width="${size}" height="${size}" viewBox="0 0 100 100" aria-hidden="true">
      <defs><radialGradient id="rings-${id}"><stop offset="0%" stop-color="${b}"/><stop offset="100%" stop-color="${a}"/></radialGradient></defs>${circles}</svg>`;
  };
  $$("[data-rings]").forEach((el) => {
    el.innerHTML = decorticaRings({
      size: +(el.dataset.size || 480), tone: el.dataset.rings, spin: el.dataset.spin === "1", id: el.dataset.rings + (el.dataset.size || ""),
    });
  });

  /* ---------- intro a capitoli ---------- */
  const ORB_TONES = {
    green: ["#7CFF3F", "#4E9A3F"], cyan: ["#3FE9FF", "#4E9A3F"],
    blue: ["#3FE9FF", "#2F6FB0"], cork: ["#E8C28E", "#C2603A"],
  };

  window.initChapters = (root, chapters, skipTo) => {
    if (REDUCED || NARROW()) { renderChapterCards(root, chapters); return; }

    root.classList.add("chapters");
    const track = document.createElement("div");
    track.className = "chapters-track";
    track.style.height = `${chapters.length * 100 + 60}vh`;
    const stage = document.createElement("div");
    stage.className = "chapters-stage";
    stage.innerHTML = `
      <div class="chapter-orb" aria-hidden="true"></div>
      <div class="chapter-ghost" aria-hidden="true"></div>
      <div class="chapter-grid">
        ${chapters.map((c, i) => `
          <div class="chapter-slide${i === 0 ? " active" : ""}" data-i="${i}">
            <div class="chapter-text">
              <span class="chapter-index">0${i + 1} / 0${chapters.length} — Capitolo</span>
              <h2 class="chapter-title">${c.title}</h2>
              <p class="chapter-context">${c.context}</p>
              <p class="chapter-source">Fonte: ${c.source}</p>
            </div>
            <div>
              <p class="chapter-value"><span data-val>${c.prefix ?? ""}0</span><span class="unit">${c.unit ?? ""}</span></p>
              <p class="chapter-value-label">${c.valueLabel ?? ""}</p>
            </div>
          </div>`).join("")}
      </div>
      <ol class="chapters-dots" aria-label="Avanzamento introduzione">
        ${chapters.map((_, i) => `<li${i === 0 ? ' class="active"' : ""} data-goto="${i}"></li>`).join("")}
      </ol>
      <div class="chapters-progress" aria-hidden="true">01 / 0${chapters.length}</div>
      <p class="scroll-hint" style="bottom:26px">Scorri<span aria-hidden="true">↓</span></p>
      <a class="skip-intro" href="#${skipTo}">Salta l'introduzione</a>`;
    track.appendChild(stage);
    root.appendChild(track);

    const orb = $(".chapter-orb", stage);
    const ghost = $(".chapter-ghost", stage);
    const slides = $$(".chapter-slide", stage);
    const dots = $$(".chapters-dots li", stage);
    const progress = $(".chapters-progress", stage);
    const hint = $(".scroll-hint", stage);
    let active = -1;

    const setChapter = (i) => {
      if (i === active) return;
      active = i;
      const c = chapters[i];
      slides.forEach((s, k) => {
        const on = k === i;
        s.classList.toggle("active", on);
        if (on) {
          [".chapter-text", ".chapter-value", ".chapter-value-label"].forEach((sel, j) => {
            const n = $(sel, s);
            if (!n) return;
            n.style.animation = "none"; void n.offsetWidth;
            n.style.animation = `chapterIn .7s ${j * 0.08}s cubic-bezier(.2,.8,.2,1) both`;
          });
          const vEl = $("[data-val]", s);
          countUp(vEl, c.value, { dec: c.dec || 0, prefix: c.prefix || "", dur: 900 });
        }
      });
      dots.forEach((d, k) => d.classList.toggle("active", k === i));
      progress.textContent = `0${i + 1} / 0${chapters.length}`;
      ghost.style.opacity = 0;
      setTimeout(() => { ghost.textContent = c.ghost; ghost.style.opacity = 1; }, 220);
      const [c1, c2] = ORB_TONES[c.tone];
      const pos = c.orbPos ?? { x: 68, y: 50, s: 62 };
      orb.style.background = `radial-gradient(circle at 40% 40%, ${c1} 0%, ${c2} 52%, transparent 72%)`;
      orb.style.left = pos.x + "%";
      orb.style.top = pos.y + "%";
      orb.style.width = orb.style.height = pos.s + "vmin";
      orb.style.marginLeft = orb.style.marginTop = -pos.s / 2 + "vmin";
      if (hint) hint.style.opacity = i === 0 ? 1 : 0;
    };

    const onScroll = () => {
      const r = track.getBoundingClientRect();
      const total = r.height - innerHeight;
      const p = Math.min(1, Math.max(0, -r.top / total));
      setChapter(Math.min(chapters.length - 1, Math.floor(p * chapters.length)));
      const sc = 0.9 + p * 0.35;
      orb.style.transform = `scale(${sc})`;
    };
    addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    dots.forEach((d) => d.addEventListener("click", () => {
      const i = +d.dataset.goto;
      const top = track.offsetTop + ((track.offsetHeight - innerHeight) / chapters.length) * i + 2;
      scrollTo({ top, behavior: "smooth" });
    }));
  };

  function renderChapterCards(root, chapters) {
    root.classList.add("chapters", "as-cards");
    const track = document.createElement("div");
    track.className = "chapters-track";
    track.innerHTML = `<div class="chapters-stage"><div class="chapter-grid container" style="display:block">
      ${chapters.map((c, i) => `
        <div class="chapter-slide active"><div class="chapter-card">
          <span class="chapter-index">0${i + 1} / 0${chapters.length}</span>
          <h2 class="chapter-title" style="font-size:30px">${c.title}</h2>
          <p class="chapter-value" style="justify-self:start;font-size:52px;margin-top:14px">${c.prefix ?? ""}${c.dec ? fmtDec(c.value, c.dec) : fmtInt(c.value)}<span class="unit">${c.unit ?? ""}</span></p>
          <p class="chapter-context" style="margin-top:10px">${c.context}</p>
          <p class="chapter-source">Fonte: ${c.source}</p>
        </div></div>`).join("")}
    </div></div>`;
    root.appendChild(track);
  }

  /* ---------- sottomenu sticky ---------- */
  window.initSubnav = (navEl, afterEl) => {
    if (!navEl) return;
    const links = $$("a[href^='#']", navEl);
    const sections = links.map((a) => $(a.getAttribute("href"))).filter(Boolean);
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        links.forEach((a) => a.classList.toggle("active", a.getAttribute("href") === "#" + e.target.id));
      });
    }, { rootMargin: "-30% 0px -55% 0px" });
    sections.forEach((s) => spy.observe(s));
    if (afterEl) {
      const vis = new IntersectionObserver(([e]) => navEl.classList.toggle("visible", !e.isIntersecting), { threshold: 0 });
      vis.observe(afterEl);
    } else navEl.classList.add("visible");
  };

  /* ---------- slope rows (popolazione 2001 → 2025) ---------- */
  window.slopeRows = (container, rows) => {
    const maxAbs = Math.max(...rows.map((r) => Math.abs(r.var)));
    container.innerHTML = rows.map((r) => {
      const pct = r.var;
      const angle = (pct / maxAbs) * -9; // inclinazione visiva controllata
      const color = r.fascia === "costiera" ? "var(--blue)" : "var(--green)";
      return `<div class="slope-row">
        <span class="slope-name">${r.nome}</span>
        <span class="slope-val">${fmtInt(r.da)}</span>
        <div class="slope-track" aria-hidden="true">
          <span class="slope-line" style="background:${color};transform:rotate(${angle.toFixed(2)}deg)"></span>
        </div>
        <span class="slope-val right">${fmtInt(r.a)}</span>
        <span class="slope-delta ${pct < 0 ? "neg" : "pos"}">${fmtPct(pct, true)}</span>
      </div>`;
    }).join("");
  };

  /* ---------- barre divergenti (saldi) ---------- */
  window.divergeRows = (container, rows) => {
    const max = Math.max(...rows.flatMap((r) => [Math.abs(r.neg), Math.abs(r.pos)]));
    container.innerHTML = rows.map((r) => {
      const w = (v) => (Math.abs(v) / max) * 40;
      return `<div class="diverge-row">
        <span class="diverge-name">${r.nome}</span>
        <div class="diverge-track">
          <span class="diverge-axis"></span>
          <div class="diverge-bar neg" style="width:${w(r.neg)}%"><span>${fmtInt(r.neg)}</span></div>
          <div class="diverge-bar pos" style="width:${w(r.pos)}%"><span>+${fmtInt(r.pos)}</span></div>
        </div>
      </div>`;
    }).join("");
  };

  /* ---------- sparkline SVG ---------- */
  window.sparkline = (points, { w = 440, h = 90, color = "var(--green)" } = {}) => {
    const vals = points.map((p) => p[1]);
    const min = Math.min(...vals), max = Math.max(...vals);
    const pad = 8;
    const X = (i) => pad + (i / (points.length - 1)) * (w - pad * 2 - 44);
    const Y = (v) => h - pad - ((v - min) / (max - min || 1)) * (h - pad * 2 - 16);
    const d = points.map((p, i) => `${i ? "L" : "M"}${X(i).toFixed(1)},${Y(p[1]).toFixed(1)}`).join(" ");
    const labels = points.map((p, i) =>
      `<text x="${X(i)}" y="${h - 1}" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">${p[0]}</text>` +
      `<text x="${X(i)}" y="${Y(p[1]) - 6}" font-size="10" font-weight="600" fill="var(--ink)" text-anchor="middle">${fmtInt(p[1])}</text>`
    ).join("");
    return `<svg class="spark" viewBox="0 0 ${w} ${h}" role="img" aria-label="Popolazione ${points[0][0]}–${points.at(-1)[0]}">
      <path d="${d}" fill="none" stroke="${color}" stroke-width="2.2" stroke-linecap="round"/>
      ${points.map((p, i) => `<circle cx="${X(i)}" cy="${Y(p[1])}" r="3" fill="#fff" stroke="${color}" stroke-width="2"/>`).join("")}
      ${labels}</svg>`;
  };

  /* ---------- barra impilata uso suolo ---------- */
  const LAND_COLORS = ["#4E9A3F", "#8BC34A", "#207868", "#D9A441", "#C2603A", "#7A6685", "#2F6FB0", "#B9CFC4"];
  window.landStack = (container, classi) => {
    const top = classi.filter((c) => c.pct != null).slice(0, 6);
    const rest = Math.max(0, 100 - top.reduce((s, c) => s + c.pct, 0));
    const segs = [...top.map((c, i) => ({ ...c, color: LAND_COLORS[i] }))];
    if (rest > 0.4) segs.push({ classe: "Altre classi (non dettagliate)", pct: rest, color: "#E3ECE8" });
    container.innerHTML = `
      <div class="stack" role="img" aria-label="Uso del suolo: ${top.map((c) => `${c.classe} ${fmtPct(c.pct)}`).join(", ")}">
        ${segs.map((s) => `<div style="width:${s.pct}%;background:${s.color}" title="${s.classe} — ${fmtPct(s.pct)}"></div>`).join("")}
      </div>
      <div class="stack-legend">
        ${segs.map((s) => `<span><i style="background:${s.color}"></i>${s.classe} · ${fmtPct(s.pct)}</span>`).join("")}
      </div>`;
  };

  /* ---------- lightbox figure ---------- */
  $$("dialog.lightbox").forEach((dlg) => {
    dlg.addEventListener("click", (e) => { if (e.target === dlg) dlg.close(); });
  });
  window.openLightbox = (id) => document.getElementById(id)?.showModal();

  /* ---------- drawer scheda comune ---------- */
  window.initComuneDrawer = (data, { crossLink = true } = {}) => {
    const overlay = $(".drawer-overlay");
    const drawer = $(".drawer");
    const body = $(".drawer-body", drawer);
    const titleEl = $(".drawer-title", drawer);
    const bySlug = Object.fromEntries(data.map((c) => [c.slug, c]));
    const order = data.map((c) => c.slug);
    let lastTrigger = null;

    const render = (c) => {
      const fasciaLabel = c.fascia === "costiera" ? "Costa" : "Interno";
      const fasciaColor = c.fascia === "costiera" ? "var(--blue)" : "var(--green)";
      const spark = sparkline(
        [[2001, c.abitanti_2001], [2011, c.abitanti_2011], [2023, c.abitanti_2023], [2025, c.abitanti_2025]],
        { color: fasciaColor }
      );
      $(".drawer-funzione", drawer).textContent = c.funzione;
      $(".drawer-funzione", drawer).className = "drawer-funzione" + (c.fascia === "costiera" ? " costa" : "");
      $(".drawer-eyebrow.fascia-tag", drawer).innerHTML =
        `<i style="width:8px;height:8px;border-radius:50%;background:${fasciaColor};display:inline-block"></i> ${fasciaLabel} — Alta Gallura`;

      body.innerHTML = `
        <div class="drawer-kpis">
          <div class="drawer-kpi"><div class="v">${fmtInt(c.abitanti_2025)}</div><div class="l">Residenti (1° gen 2025)</div></div>
          <div class="drawer-kpi"><div class="v ${c.var_pct_2001_2023 < 0 ? "neg" : "pos"}">${fmtPct(c.var_pct_2001_2023, true)}</div><div class="l">Variazione popolazione 2001-2023</div></div>
          <div class="drawer-kpi"><div class="v">${fmtPct(c.over65_pct)}</div><div class="l">Over 65 sul totale (2025)</div></div>
          <div class="drawer-kpi"><div class="v">${fmtInt(c.imprese_2025)}</div><div class="l">Imprese attive (2025)</div></div>
        </div>

        <h4>Popolazione 2001 → 2025</h4>
        ${spark}

        <h4>Com'è fatto il territorio</h4>
        <p class="muted" style="margin-bottom:10px">Sugherete: <strong>${fmtInt(c.sugherete_ha)} ha</strong>${c.sugherete_ha > 0 ? "" : " (assenti nelle tabelle dello studio)"}. Sei classi principali di uso del suolo, in % del territorio comunale.</p>
        <div data-landstack></div>

        <h4>Cosa dice lo studio</h4>
        ${c.inquadramento.map((p) => `<p>${p}</p>`).join("")}
        <p class="muted" style="margin-top:10px"><strong>Filiera bosco-sughero.</strong> ${c.implicazioni_sughero}</p>
        <p class="muted" style="margin-top:8px"><strong>Filiera suinicola agroforestale.</strong> ${c.implicazioni_suinicola}</p>

        <h4>Punti di attenzione</h4>
        <ul class="crit">${c.criticita.map((x) => `<li>${x}</li>`).join("")}</ul>
        <h4>Opportunità</h4>
        <ul class="opp">${c.opportunita.map((x) => `<li>${x}</li>`).join("")}</ul>

        <h4>Elementi identitari</h4>
        <div class="identita-tags">${c.identita.map((x) => `<span>${x}</span>`).join("")}</div>

        ${crossLink && (c.slug === "calangianus" || c.slug === "tempio-pausania") ? `
        <a class="cross-link" href="#" onclick="return false" title="Pagina in arrivo nel prototipo finale">
          <span aria-hidden="true">◍</span> Vedi questo comune nella Sughereta Sardegna →
        </a>` : ""}

        <div class="drawer-nav">
          <button data-prev>← Comune precedente</button>
          <button data-next>Comune successivo →</button>
        </div>
        <p class="muted" style="margin-top:26px;font-size:12px">Fonte: Studio Green community UCAG 193 — Allegato II, scheda comunale; Tab. 1a-1c, 2a.</p>`;

      landStack($("[data-landstack]", body), c.uso_suolo);
      const i = order.indexOf(c.slug);
      const prev = $("[data-prev]", body), next = $("[data-next]", body);
      prev.disabled = i <= 0; next.disabled = i >= order.length - 1;
      prev.onclick = () => open(order[i - 1]);
      next.onclick = () => open(order[i + 1]);
      $(".drawer-title", drawer);
      titleEl.textContent = c.comune;
      titleEl.tabIndex = -1;
    };

    const open = (slug, push = true) => {
      const c = bySlug[slug];
      if (!c) return;
      render(c);
      overlay.classList.add("open");
      drawer.classList.add("open");
      document.body.style.overflow = "hidden";
      if (push) history.replaceState(null, "", `?comune=${slug}`);
      setTimeout(() => titleEl.focus({ preventScroll: true }), 350);
    };
    const close = () => {
      overlay.classList.remove("open");
      drawer.classList.remove("open");
      document.body.style.overflow = "";
      history.replaceState(null, "", location.pathname);
      lastTrigger?.focus();
    };

    document.addEventListener("click", (e) => {
      const t = e.target.closest("[data-comune]");
      if (t) { lastTrigger = t; open(t.dataset.comune); }
    });
    overlay.addEventListener("click", close);
    $("[data-close]", drawer).addEventListener("click", close);
    $("[data-copy]", drawer).addEventListener("click", async (e) => {
      const btn = e.currentTarget;
      try {
        await navigator.clipboard.writeText(location.href);
        btn.textContent = "Copiato ✓";
      } catch { btn.textContent = location.href; }
      setTimeout(() => (btn.textContent = "Copia link"), 1600);
    });
    addEventListener("keydown", (e) => e.key === "Escape" && close());

    // apertura da URL
    const slug = new URLSearchParams(location.search).get("comune");
    if (slug && bySlug[slug]) open(slug, false);

    return { open, close };
  };

  /* ---------- griglia comuni + filtro ---------- */
  window.initComuniGrid = (gridEl, data) => {
    const card = (c) => {
      const fasciaColor = c.fascia === "costiera" ? "var(--blue)" : "var(--green)";
      return `<button class="comune-card" data-comune="${c.slug}" data-fascia="${c.fascia}">
        <span class="fascia-tag"><i style="background:${fasciaColor}"></i>${c.fascia === "costiera" ? "Costa" : "Interno"}</span>
        <span class="open-hint" aria-hidden="true">↗</span>
        <h3>${c.comune}</h3>
        <p class="funzione">${c.funzione}</p>
        <div class="nums">
          <div><div class="v">${fmtInt(c.abitanti_2025)}</div><div class="l">residenti 2025</div></div>
          <div><div class="v ${c.var_pct_2001_2023 < 0 ? "neg" : "pos"}">${fmtPct(c.var_pct_2001_2023, true, 0)}</div><div class="l">dal 2001</div></div>
          <div><div class="v">${fmtInt(c.sugherete_ha)}</div><div class="l">ha sugherete</div></div>
        </div>
        <span class="card-orb" style="background:radial-gradient(circle at 40% 40%, ${c.fascia === "costiera" ? "#3FE9FF, #2F6FB0" : "#7CFF3F, #4E9A3F"} 0%, transparent 70%)"></span>
      </button>`;
    };
    const renderGrid = (fascia) => {
      const rows = data.filter((c) => !fascia || c.fascia === fascia);
      gridEl.innerHTML = rows.map(card).join("");
      const count = $(".filter-count");
      if (count) count.textContent = `${rows.length} comuni`;
    };
    renderGrid("");
    $$(".filter-bar .chip").forEach((chip) =>
      chip.addEventListener("click", () => {
        $$(".filter-bar .chip").forEach((c) => c.classList.remove("active"));
        chip.classList.add("active");
        renderGrid(chip.dataset.fascia || "");
      })
    );
  };
})();
