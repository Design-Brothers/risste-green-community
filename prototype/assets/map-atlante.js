/* Mappa geografica dei 30 comuni della Sughereta Sardegna */
(() => {
  "use strict";

  const GEO = {
    bitti: [40.479, 9.308],
    berchidda: [40.786, 9.165],
    oschiri: [40.719, 9.101],
    budduso: [40.582, 9.258],
    nuoro: [40.321, 9.328],
    orune: [40.409, 9.370],
    "ala-dei-sardi": [40.650, 9.328],
    "villanova-monteleone": [40.504, 8.471],
    ozieri: [40.586, 9.001],
    orani: [40.250, 9.182],
    "tempio-pausania": [40.897, 9.104],
    telti: [40.876, 9.353],
    calangianus: [40.921, 9.194],
    mores: [40.548, 8.832],
    chiaramonti: [40.749, 8.818],
    padru: [40.765, 9.160],
    illorai: [40.357, 9.002],
    olbia: [40.923, 9.499],
    oliena: [40.271, 9.403],
    pozzomaggiore: [40.398, 8.659],
    benetutti: [40.456, 9.168],
    abbasanta: [40.126, 8.819],
    pattada: [40.582, 9.111],
    monti: [40.807, 9.325],
    ploaghe: [40.664, 8.747],
    bono: [40.415, 9.030],
    aidomaggiore: [40.171, 8.857],
    ardara: [40.621, 8.813],
    iglesias: [39.311, 8.537],
    bultei: [40.437, 9.064],
  };

  const SARDEGNA = {
    type: "Feature",
    properties: { name: "Sardegna" },
    geometry: {
      type: "Polygon",
      coordinates: [[
        [8.13, 40.74], [8.22, 41.26], [8.63, 41.26], [9.13, 41.26],
        [9.63, 41.14], [9.83, 40.92], [9.72, 40.58], [9.83, 40.32],
        [9.64, 39.98], [9.69, 39.52], [9.64, 39.14], [8.85, 38.86],
        [8.37, 39.14], [8.22, 39.52], [8.37, 40.05], [8.13, 40.36], [8.13, 40.74],
      ]],
    },
  };

  const CLASS_COLOR = {
    Alta: "#2E7D32", Media: "#F0B800", Bassa: "#F08800", "Molto bassa": "#D84315",
    Basso: "#2E7D32", Mediobasso: "#8BC34A", Medio: "#F0B800", Medioalto: "#F08800", Alto: "#D84315",
  };

  window.initAtlanteMap = (el, comuni, { onOpen } = {}) => {
    if (!el || !window.L || !comuni?.length) return null;
    const map = L.map(el, { scrollWheelZoom: false, zoomControl: true }).setView([40.15, 9.0], 7);
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      maxZoom: 19,
    }).addTo(map);
    L.geoJSON(SARDEGNA, {
      style: { color: "#4E9A3F", weight: 1.4, fillColor: "#4E9A3F", fillOpacity: 0.06 },
    }).addTo(map);

    const maxHa = Math.max(...comuni.map((c) => c.sugherete_ha || 1));
    let mode = "ivp";
    const layer = L.layerGroup().addTo(map);

    const classOf = (c) => {
      if (mode === "incendio") return c.classe_incendio;
      if (mode === "icr") return c.classe_icr;
      return c.classe_ivp;
    };

    const paint = () => {
      layer.clearLayers();
      comuni.forEach((c) => {
        const ll = GEO[c.slug];
        if (!ll) return;
        const cls = classOf(c);
        const r = 5 + Math.sqrt((c.sugherete_ha || 0) / maxHa) * 16;
        const marker = L.circleMarker(ll, {
          radius: r,
          color: "#132019",
          weight: 1,
          fillColor: CLASS_COLOR[cls] || "#999",
          fillOpacity: 0.82,
        });
        marker.bindTooltip(c.comune, {
          direction: "top",
          offset: [0, -Math.round(r)],
          opacity: 0.96,
          className: "map-name-tip",
        });
        marker.on("click", () => onOpen?.(c.slug));
        marker.addTo(layer);
      });
    };

    paint();

    return {
      map,
      setMode(next) {
        mode = next;
        paint();
      },
    };
  };

  window.renderAtlanteCards = (el, comuni, { hrefFor } = {}) => {
    if (!el || !comuni?.length) return;
    const sorted = [...comuni].sort((a, b) => a.comune.localeCompare(b.comune, "it"));
    el.innerHTML = sorted.map((c) => {
      const ha = window.fmt ? fmt.dec(c.sugherete_ha, 0) : Math.round(c.sugherete_ha);
      const color = CLASS_COLOR[c.classe_ivp] || "#999";
      const inner = `
        <span class="fascia-tag"><i style="background:${color}"></i>IVP ${c.classe_ivp}</span>
        <span class="open-hint" aria-hidden="true">↗</span>
        <h3>${c.comune}</h3>
        <p class="funzione">Rank ${c.rank} su 30 · ${ha} ha di sughereta</p>
        <div class="nums">
          <div><div class="v">${ha}</div><div class="l">ha sugherete</div></div>
          <div><div class="v">${c.classe_incendio}</div><div class="l">incendio</div></div>
          <div><div class="v">${c.classe_icr}</div><div class="l">ICR</div></div>
        </div>
        <span class="card-orb" style="background:radial-gradient(circle at 40% 40%, ${color}, transparent 70%)"></span>`;
      if (hrefFor) {
        return `<a class="comune-card" href="${hrefFor(c)}" title="${c.comune}" aria-label="Apri la scheda di ${c.comune}">${inner}</a>`;
      }
      return `<button class="comune-card" type="button" data-open30="${c.slug}" title="${c.comune}" aria-label="Apri la scheda di ${c.comune}">${inner}</button>`;
    }).join("");
  };
})();
