// Radial wavefunctions of the hydrogenlike atom: pick n, l and Z, see R_nl(r) and the radial distribution r^2 R^2.
//
// R_nl(r) = N_nl (2 rho / n)^l L_{n-l-1}^{2l+1}(2 rho / n) e^{-rho / n} with rho = Z r / a0 and the associated Laguerre
// polynomial built by its three-term recurrence, so every state is exact. Left: R_nl(r) in units of (1/a0)^{3/2},
// with its n - l - 1 radial nodes marked in red; the curve contracts and grows as Z rises. Right: the radial
// distribution P(r) = r^2 R^2 (probability per a0 of finding the electron between r and r + dr, at any angle), with
// the average <r> = (a0 n^2 / Z)[1 + (1 - l(l+1)/n^2)/2] dashed (the most probable distance was dropped: its label
// overlapped <r>). The r axis rescales with n^2 / Z. The verdict names the state, its nodes, its energy and <r>.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch05/01), in a reveal.js deck through a module-script loader, and in Jupyter or
// Colab through the anywidget package. No dependencies. The l buttons are plain numbers and the orbital's name (2s,
// 3p, ...) is a tag in the l colour at the top right of the P(r) panel (the user found "0 (s)" buttons confusing,
// 2026-11-11). Model keys, optional: fontSize (CSS size), n (1 to 5),
// l (0 to n - 1), Z (1 to 3), status (false hides the verdict line), probe (true adds a slider "inside r": the
// area of P(r) up to that r is shaded darker, the verdict reports the probability inside it and the radius that
// holds 90%; page ch05/02 and deck 02 use it, page ch05/01 and deck 01 do not).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00", PURPLE = "#6a3d9a", GRAY = "#6c757d";
const SVGNS = "http://www.w3.org/2000/svg";

const NMAX = 5, ZMAX = 3, M = 600;                                   // states offered, grid points per curve
const LETTER = "spdfg";
const LCOL = [TEAL, PURPLE, ORANGE, GRAY, GRAY];
const EH_EV = 13.6057;                                               // E_h / 2 in eV

// ------------------------------------------------------------------ the radial functions
const fact = (k) => { let f = 1; for (let i = 2; i <= k; i++) f *= i; return f; };

// associated Laguerre L_k^a(x) by the three-term recurrence
function laguerre(k, a, x) {
  let l0 = 1, l1 = 1 + a - x;
  if (k === 0) return l0;
  for (let i = 1; i < k; i++) { const l2 = ((2 * i + 1 + a - x) * l1 - (i + a) * l0) / (i + 1); l0 = l1; l1 = l2; }
  return l1;
}

// R_nl(r) in units of a0^{-3/2}, r in a0
function radial(n, l, Z, r) {
  const N = Math.sqrt(Math.pow(2 * Z / n, 3) * fact(n - l - 1) / (2 * n * fact(n + l)));
  const x = 2 * Z * r / n;
  return N * Math.pow(x, l) * laguerre(n - l - 1, 2 * l + 1, x) * Math.exp(-x / 2);
}

// ------------------------------------------------------------------ drawing
const W = 1000, H = 400;
const AL = 66, AR = 480, BL = 580, BR = 984, PT = 34, PB = 352;      // left panel (R) and right panel (P), shared heights

const CSS = `
.re-root { --re-fg: #212529; --re-muted: #6c757d; --re-border: #ced4da; --re-btn: #f8f9fa; --re-card: #ffffff;
  --re-teal: ${TEAL}; --re-purple: ${PURPLE}; --re-orange: ${ORANGE}; --re-red: ${CARDINAL}; --re-gray: ${GRAY};
  --re-zero: #ced4da; --re-on: #e7f1f4; --re-fill: rgba(16, 120, 149, 0.18); --re-fill2: rgba(16, 120, 149, 0.5);
  color: var(--re-fg); background: var(--re-card); border: 1px solid var(--re-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.re-root.re-dark { --re-fg: #e9ecef; --re-muted: #adb5bd; --re-border: #495057; --re-btn: #2b3035; --re-card: #1e2125;
  --re-teal: #45a9c6; --re-purple: #b08be0; --re-orange: #f59f3a; --re-red: #f05d6f; --re-gray: #adb5bd;
  --re-zero: #495057; --re-on: #1f3a44; --re-fill: rgba(69, 169, 198, 0.22); --re-fill2: rgba(69, 169, 198, 0.55); }
.re-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.3em; margin: 0 0 0.3em; }
.re-group { display: flex; align-items: center; gap: 0.35em; }
.re-lab { color: var(--re-muted); }
.re-btn { font: inherit; color: var(--re-fg); background: var(--re-btn); border: 1px solid var(--re-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.re-btn:hover { border-color: ${TEAL}; }
.re-btn:disabled { opacity: 0.35; cursor: default; }
.re-btn.re-active { border-color: var(--re-teal); background: var(--re-on); font-weight: 600; }
.re-plot { display: block; width: 100%; height: auto; }
.re-plot text { font-family: inherit; fill: var(--re-fg); }
.re-slider { width: 11em; margin: 0 0.2em; vertical-align: middle; accent-color: var(--re-teal); }
.re-val { font-weight: 600; min-width: 5.5em; }
.re-status { font-weight: 600; margin: 0.2em 0 0; min-height: 1.4em; }
.re-note { color: var(--re-muted); }
`;

function svg(tag, attrs, parent) {
  const e = document.createElementNS(SVGNS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (parent) parent.appendChild(e);
  return e;
}

function html(tag, cls, parent, text) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text !== undefined) e.textContent = text;
  if (parent) parent.appendChild(e);
  return e;
}

// SVG text with pieces: [["R", ""], ["nl", "sub"], ["(r)", ""]]
function rich(t, parts) {
  t.textContent = "";
  parts.forEach(([s, kind]) => {
    const ts = document.createElementNS(SVGNS, "tspan");
    ts.textContent = s;
    if (kind === "sub") { ts.setAttribute("dy", "0.3em"); ts.setAttribute("font-size", "75%"); }
    if (kind === "sup") { ts.setAttribute("dy", "-0.45em"); ts.setAttribute("font-size", "75%"); }
    if (kind === "back-sub") { ts.setAttribute("dy", "-0.3em"); }
    if (kind === "back-sup") { ts.setAttribute("dy", "0.45em"); }
    t.appendChild(ts);
  });
  return t;
}

const nice = (v) => { const p = Math.pow(10, Math.floor(Math.log10(v))); const m = v / p; return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p; };
const fmt = (v, d = 2) => v.toFixed(d);

let uid = 0;

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "re-root", el);
  root.setAttribute("data-prevent-swipe", "");
  root.style.fontSize = get("fontSize", "15px");

  const controls = html("div", "re-controls", root);
  const ngroup = html("div", "re-group", controls); html("span", "re-lab", ngroup, "n =");
  const nbtns = [];
  for (let n = 1; n <= NMAX; n++) {
    const b = html("button", "re-btn", ngroup, String(n)); b.type = "button";
    b.addEventListener("click", () => { b.blur(); setState(n, Math.min(curL, n - 1), curZ); });
    nbtns.push(b);
  }
  const lgroup = html("div", "re-group", controls); html("span", "re-lab", lgroup, "l =");
  const lbtns = [];
  for (let l = 0; l < NMAX; l++) {
    const b = html("button", "re-btn", lgroup, String(l)); b.type = "button";
    b.addEventListener("click", () => { b.blur(); setState(curN, l, curZ); });
    lbtns.push(b);
  }
  const zgroup = html("div", "re-group", controls); html("span", "re-lab", zgroup, "Z =");
  const zbtns = [];
  for (let Z = 1; Z <= ZMAX; Z++) {
    const b = html("button", "re-btn", zgroup, Z === 1 ? "1 (H)" : Z === 2 ? "2 (He⁺)" : "3 (Li²⁺)"); b.type = "button";
    b.addEventListener("click", () => { b.blur(); setState(curN, curL, Z); });
    zbtns.push(b);
  }

  const probe = get("probe", false) === true;
  let probeR = null, lastKey = "";
  let slider = null, probeVal = null;
  if (probe) {
    const pg = html("div", "re-group", controls); html("span", "re-lab", pg, "inside r \u2264");
    slider = html("input", "re-slider", pg); slider.type = "range"; slider.min = "0"; slider.max = "10"; slider.step = "0.01";
    slider.addEventListener("input", () => { probeR = +slider.value; draw(); });
    probeVal = html("span", "re-val", pg, "");
  }

  const plot = svg("svg", { viewBox: `0 0 ${W} ${H}`, class: "re-plot", role: "img",
    "aria-label": "the radial function of the chosen state, and its radial probability distribution" }, root);
  const clipA = `re-clipa-${uid}`, clipB = `re-clipb-${uid++}`;
  const defs = svg("defs", {}, plot);
  svg("rect", { x: AL, y: PT - 4, width: AR - AL, height: PB - PT + 8 }, svg("clipPath", { id: clipA }, defs));
  svg("rect", { x: BL, y: PT - 4, width: BR - BL, height: PB - PT + 8 }, svg("clipPath", { id: clipB }, defs));

  const axis = (x0, x1) => {
    svg("line", { x1: x0, x2: x0, y1: PT, y2: PB, stroke: "var(--re-muted)", "stroke-width": 1 }, plot);
    svg("line", { x1: x0, x2: x1, y1: PB, y2: PB, stroke: "var(--re-muted)", "stroke-width": 1 }, plot);
  };
  axis(AL, AR); axis(BL, BR);
  const headA = svg("text", { x: AL, y: PT - 14, "font-size": 15, "font-weight": 600 }, plot);
  const headB = svg("text", { x: BL, y: PT - 14, "font-size": 15, "font-weight": 600 }, plot);
  rich(headB, [["radial distribution P(r) = r", ""], ["2", "sup"], ["R", "back-sup"], ["2", "sup"], ["(r)", "back-sup"]]);
  const xlabA = svg("text", { x: (AL + AR) / 2, y: PB + 40, "text-anchor": "middle", "font-size": 14, style: "fill: var(--re-muted)" }, plot);
  const xlabB = svg("text", { x: (BL + BR) / 2, y: PB + 40, "text-anchor": "middle", "font-size": 14, style: "fill: var(--re-muted)" }, plot);
  [xlabA, xlabB].forEach((t) => rich(t, [["r (units of a", ""], ["0", "sub"], [")", "back-sub"]]));
  const ylabA = svg("text", { x: 18, y: (PT + PB) / 2, "text-anchor": "middle", "font-size": 14, transform: `rotate(-90 18 ${(PT + PB) / 2})`,
    style: "fill: var(--re-muted)" }, plot);
  rich(ylabA, [["R", ""], ["nl", "sub"], [" (units of a", "back-sub"], ["0", "sub"], ["-3/2", "sup"], [")", "back-sup"]]);
  const ylabB = svg("text", { x: BL - 48, y: (PT + PB) / 2, "text-anchor": "middle", "font-size": 14,
    transform: `rotate(-90 ${BL - 48} ${(PT + PB) / 2})`, style: "fill: var(--re-muted)" }, plot);
  rich(ylabB, [["P (per a", ""], ["0", "sub"], [")", "back-sub"]]);

  const ticksG = svg("g", {}, plot);
  const gA = svg("g", { "clip-path": `url(#${clipA})` }, plot);
  const gB = svg("g", { "clip-path": `url(#${clipB})` }, plot);
  const zeroA = svg("line", { x1: AL, x2: AR, stroke: "var(--re-zero)", "stroke-width": 1.2 }, gA);
  const curveA = svg("path", { fill: "none", "stroke-width": 2.6, "stroke-linejoin": "round" }, gA);
  const nodesG = svg("g", {}, gA);
  const fillB = svg("path", { fill: "var(--re-fill)", stroke: "none" }, gB);
  const fillP = svg("path", { fill: "var(--re-fill2)", stroke: "none" }, gB);
  const curveB = svg("path", { fill: "none", "stroke-width": 2.6, "stroke-linejoin": "round" }, gB);
  const probeLine = svg("line", { y1: PT, y2: PB, stroke: "var(--re-red)", "stroke-width": 1.6, visibility: "hidden" }, gB);
  const probeLab = svg("text", { y: PB - 8, "font-size": 13, "font-weight": 600, style: "fill: var(--re-red)", visibility: "hidden" }, plot);
  const avLine = svg("line", { y1: PT, y2: PB, stroke: "var(--re-fg)", "stroke-width": 1.2, "stroke-dasharray": "6 4" }, gB);
  const avLab = svg("text", { y: PT + 16, "font-size": 13 }, plot);
  const eTag = svg("text", { x: AR - 6, y: PT + 20, "text-anchor": "end", "font-size": 15, "font-weight": 600 }, plot);
  const nameTag = svg("text", { x: BR - 6, y: PT + 24, "text-anchor": "end", "font-size": 22, "font-weight": 700 }, plot);

  const status = html("div", "re-status", root);
  if (get("status", true) === false) status.style.display = "none";
  html("div", "re-note", root).innerHTML =
    "P(r)&thinsp;dr is the probability of finding the electron between r and r + dr, at any angle" +
    (probe ? ". Dashed: the average distance ⟨r⟩; the darker area is the probability inside the chosen r." :
      " (Lecture 5.2). Dashed: the average distance ⟨r⟩.");

  // ---------------------------------------------------------------- state
  let curN = Math.min(NMAX, Math.max(1, Math.round(get("n", 2))));
  let curL = Math.min(curN - 1, Math.max(0, Math.round(get("l", 0))));
  let curZ = Math.min(ZMAX, Math.max(1, Math.round(get("Z", 1))));

  function draw() {
    const n = curN, l = curL, Z = curZ;
    const rmax = (2.6 * n * n + 6) / Z;
    const r = new Float64Array(M + 1), R = new Float64Array(M + 1), P = new Float64Array(M + 1);
    let rmin = 0, rmaxv = 0, pmax = 0;
    for (let i = 0; i <= M; i++) {
      r[i] = rmax * i / M; R[i] = radial(n, l, Z, r[i]); P[i] = r[i] * r[i] * R[i] * R[i];
      rmin = Math.min(rmin, R[i]); rmaxv = Math.max(rmaxv, R[i]); pmax = Math.max(pmax, P[i]);
    }
    const span = Math.max(rmaxv, -rmin, 1e-9);
    const yA0 = rmin < -0.08 * span ? rmin * 1.15 : -0.12 * span, yA1 = rmaxv * 1.15;
    const XA = (x) => AL + (x / rmax) * (AR - AL), XB = (x) => BL + (x / rmax) * (BR - BL);
    const YA = (v) => PB - ((v - yA0) / (yA1 - yA0)) * (PB - PT);
    const YB = (v) => PB - (v / (pmax * 1.15)) * (PB - PT);
    const col = LCOL[l];

    let dA = "", dB = "", dF = `M${XB(0)},${YB(0)}`;
    for (let i = 0; i <= M; i++) {
      dA += (i ? "L" : "M") + XA(r[i]).toFixed(1) + "," + YA(R[i]).toFixed(1);
      dB += (i ? "L" : "M") + XB(r[i]).toFixed(1) + "," + YB(P[i]).toFixed(1);
      dF += "L" + XB(r[i]).toFixed(1) + "," + YB(P[i]).toFixed(1);
    }
    dF += `L${XB(rmax)},${YB(0)}Z`;
    curveA.setAttribute("d", dA); curveA.setAttribute("stroke", col);
    curveB.setAttribute("d", dB); curveB.setAttribute("stroke", col);
    fillB.setAttribute("d", dF);
    zeroA.setAttribute("y1", YA(0)); zeroA.setAttribute("y2", YA(0));

    // nodes: sign changes of R away from the origin
    nodesG.innerHTML = "";
    const nodes = [];
    for (let i = 1; i < M; i++) {
      if (R[i] === 0 || (R[i] > 0) !== (R[i + 1] > 0)) {
        if (R[i] !== 0 && R[i + 1] === 0) continue;
        const x = r[i] - R[i] * (r[i + 1] - r[i]) / (R[i + 1] - R[i]);
        if (x > 1e-6) nodes.push(x);
      }
    }
    nodes.forEach((x) => svg("circle", { cx: XA(x), cy: YA(0), r: 5.5, fill: "var(--re-red)" }, nodesG));

    // average distance
    const rav = (n * n / Z) * (1 + 0.5 * (1 - l * (l + 1) / (n * n)));
    avLine.setAttribute("x1", XB(rav)); avLine.setAttribute("x2", XB(rav));
    const rightAv = rav > 0.6 * rmax;
    avLab.setAttribute("x", XB(rav) + (rightAv ? -6 : 6)); avLab.setAttribute("text-anchor", rightAv ? "end" : "start");
    rich(avLab, [["⟨r⟩ = " + fmt(rav, 2) + " a", ""], ["0", "sub"]]);

    // the probe: probability inside r, and the radius that holds 90%
    let inside = 0, r90 = 0;
    if (probe) {
      const key = `${n}${l}${Z}`;
      if (key !== lastKey || probeR === null) { probeR = n * n / Z; lastKey = key; }
      probeR = Math.min(rmax, Math.max(0, probeR));
      slider.max = String(rmax); slider.step = String(rmax / 400); slider.value = String(probeR);
      const dr = rmax / M;
      let tot = 0, dP = `M${XB(0)},${YB(0)}`;
      for (let i = 1; i <= M; i++) {
        const seg = 0.5 * (P[i - 1] + P[i]) * dr;                  // trapezoid strip from r[i-1] to r[i]
        if (!r90 && tot + seg >= 0.9) r90 = r[i - 1] + dr * (0.9 - tot) / seg;
        if (r[i] <= probeR) { inside = tot + seg; dP += "L" + XB(r[i]).toFixed(1) + "," + YB(P[i]).toFixed(1); }
        else if (r[i - 1] < probeR) {                                // the strip that the probe cuts through
          const f = (probeR - r[i - 1]) / dr, Pp = P[i - 1] + f * (P[i] - P[i - 1]);
          inside = tot + 0.5 * (P[i - 1] + Pp) * f * dr;
          dP += "L" + XB(probeR).toFixed(1) + "," + YB(Pp).toFixed(1);
        }
        tot += seg;
      }
      dP += `L${XB(probeR)},${YB(0)}Z`;
      fillP.setAttribute("d", dP);
      probeLine.setAttribute("x1", XB(probeR)); probeLine.setAttribute("x2", XB(probeR)); probeLine.setAttribute("visibility", "visible");
      const rightP = probeR > 0.12 * rmax;
      probeLab.setAttribute("x", XB(probeR) + (rightP ? -6 : 6)); probeLab.setAttribute("text-anchor", rightP ? "end" : "start");
      probeLab.setAttribute("visibility", "visible");
      probeLab.textContent = `${(100 * inside).toFixed(1)}%`;
      probeVal.textContent = `${fmt(probeR, 2)} a\u2080`;
    }

    // ticks
    ticksG.innerHTML = "";
    const step = nice(rmax / 5);
    for (let x = 0; x <= rmax + 1e-9; x += step) {
      [[XA, "a"], [XB, "b"]].forEach(([X]) => {
        svg("line", { x1: X(x), x2: X(x), y1: PB, y2: PB + 6, stroke: "var(--re-muted)", "stroke-width": 1 }, ticksG);
        const t = svg("text", { x: X(x), y: PB + 22, "text-anchor": "middle", "font-size": 13, style: "fill: var(--re-muted)" }, ticksG);
        t.textContent = Number.isInteger(step) ? String(Math.round(x)) : x.toFixed(1);
      });
    }
    const yt = (v, X0, Y, label) => {
      svg("line", { x1: X0 - 6, x2: X0, y1: Y(v), y2: Y(v), stroke: "var(--re-muted)", "stroke-width": 1 }, ticksG);
      const t = svg("text", { x: X0 - 10, y: Y(v) + 4, "text-anchor": "end", "font-size": 12, style: "fill: var(--re-muted)" }, ticksG);
      t.textContent = label;
    };
    yt(0, AL, YA, "0"); yt(rmaxv, AL, YA, fmt(rmaxv, rmaxv < 0.2 ? 3 : 2));
    if (rmin < -0.08 * span) yt(rmin, AL, YA, fmt(rmin, -rmin < 0.2 ? 3 : 2));
    yt(0, BL, YB, "0"); yt(pmax, BL, YB, fmt(pmax, pmax < 0.2 ? 3 : 2));

    // labels and verdict
    const name = `${n}${LETTER[l]}`;
    rich(headA, [[`R`, ""], [`${n}${l}`, "sub"], [`(r): the radial function`, "back-sub"]]);
    nameTag.textContent = name; nameTag.setAttribute("style", `fill: ${col}`);
    const E = -EH_EV * Z * Z / (n * n);
    rich(eTag, [[`E`, ""], [`${n}`, "sub"], [` = −${fmt(Math.abs(E), 2)} eV`, "back-sub"]]);
    eTag.setAttribute("style", `fill: ${col}`);
    const nr = n - l - 1;
    const ion = Z === 1 ? "H" : Z === 2 ? "He⁺" : "Li²⁺";
    status.innerHTML = probe ?
      `<b style="color:${col}">${name}</b> of ${ion}: ${(100 * inside).toFixed(1)}% of the electron lies inside r = ${fmt(probeR, 2)} a<sub>0</sub>; ` +
      `90% lies inside ${fmt(r90, 2)} a<sub>0</sub>, and ⟨r⟩ = ${fmt(rav, 2)} a<sub>0</sub>.` :
      `<b style="color:${col}">${name}</b> of ${ion}: ${nr} radial node${nr === 1 ? "" : "s"} (and ${l} angular), ` +
      `E = −${fmt(Math.abs(E), 2)} eV, ⟨r⟩ = ${fmt(rav, 2)} a<sub>0</sub>` +
      (l === 0 ? ". An s function is nonzero at the nucleus." : `. Near the nucleus R grows as r<sup>${l}</sup>.`);
    nbtns.forEach((b, k) => b.classList.toggle("re-active", k + 1 === n));
    lbtns.forEach((b, k) => { b.disabled = k >= n; b.classList.toggle("re-active", k === l); });
    zbtns.forEach((b, k) => b.classList.toggle("re-active", k + 1 === Z));
  }

  function setState(n, l, Z) { curN = n; curL = l; curZ = Z; draw(); }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("re-dark")) root.classList.toggle("re-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  draw();
  syncDark();
  return () => { if (obs) obs.disconnect(); };
}

export default { render };
