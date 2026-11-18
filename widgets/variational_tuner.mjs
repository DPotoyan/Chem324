// The variational recipe, by hand: tune a Gaussian trial function in a well and watch its average energy.
//
// Units hbar = m = 1. Three wells: the spring x^2/2 (the Gaussian family contains the exact ground state), the
// V-shaped well |x| (no Gaussian is exact; the best one is 0.5% high) and a Morse well D(1 - e^{-ax})^2 with D = 2.5
// (lopsided, so a second parameter, the center of the Gaussian, lowers the bound further). The trial function is
// exp(-(x - x0)^2 / 4 sigma^2), whose density is a normal curve of width sigma: kinetic energy 1 / 8 sigma^2, potential
// energy the average of V over the density (numerical). The exact ground state is solved once per well on a grid
// (Sturm bisection and inverse iteration) and drawn dashed for comparison.
// Left: the well, the exact level and state (dashed), the trial function on its own level (teal). Right: kinetic,
// potential and total energy against the width, with the present setting marked.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get. No dependencies.
// Model keys, optional: fontSize (CSS size), well ("spring", "vee" or "morse"), status and note (false hides the verdict or the description).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00";
const SVGNS = "http://www.w3.org/2000/svg";
const DM = 2.5, AM = 1 / Math.sqrt(2 * DM);                          // Morse depth and range: unit curvature at the bottom

const WELLS = {
  spring: { name: "spring", V: (x) => 0.5 * x * x, grid: [-9, 9], view: [-4.6, 4.6], center: false, formula: "V = ½x²" },
  vee: { name: "V-shaped", V: (x) => Math.abs(x), grid: [-14, 14], view: [-4.6, 4.6], center: false, formula: "V = |x|" },
  morse: { name: "Morse", V: (x) => { const e = 1 - Math.exp(-AM * x); return DM * e * e; }, grid: [-4, 40],
    view: [-2.6, 6.6], center: true, formula: "V = D(1 − e^(−ax))²" },
};
const ORDER = ["spring", "vee", "morse"];
const SMIN = 0.3, SMAX = 2.2, EMAX = 3.1;

// exact ground state of -1/2 d^2/dx^2 + V on a grid: energy by Sturm bisection, state by inverse iteration
function ground(w) {
  const N = 1200, [lo, hi] = w.grid, dx = (hi - lo) / (N + 1);
  const x = new Float64Array(N), d = new Float64Array(N);
  for (let i = 0; i < N; i++) { x[i] = lo + (i + 1) * dx; d[i] = 1 / (dx * dx) + w.V(x[i]); }
  const off = -0.5 / (dx * dx), e2 = off * off;
  const count = (lam) => {
    let c = 0, q = d[0] - lam;
    if (q < 0) c++;
    for (let i = 1; i < N; i++) { q = d[i] - lam - e2 / (q === 0 ? 1e-300 : q); if (q < 0) c++; }
    return c;
  };
  let a = 0, b = EMAX;
  for (let it = 0; it < 60; it++) { const m = 0.5 * (a + b); if (count(m) > 0) b = m; else a = m; }
  const E = 0.5 * (a + b), sig = E - 1e-10;
  let y = new Float64Array(N).fill(1);
  const cp = new Float64Array(N), dp = new Float64Array(N);
  for (let it = 0; it < 3; it++) {
    let m = d[0] - sig;
    cp[0] = off / m; dp[0] = y[0] / m;
    for (let i = 1; i < N; i++) { m = d[i] - sig - off * cp[i - 1]; cp[i] = off / m; dp[i] = (y[i] - off * dp[i - 1]) / m; }
    const z = new Float64Array(N);
    z[N - 1] = dp[N - 1];
    for (let i = N - 2; i >= 0; i--) z[i] = dp[i] - cp[i] * z[i + 1];
    let s = 0;
    for (let i = 0; i < N; i++) s += z[i] * z[i] * dx;
    s = Math.sqrt(s);
    for (let i = 0; i < N; i++) y[i] = Math.abs(z[i]) / s;
  }
  return { E, x, psi: y };
}

// average energy of the Gaussian trial function of width s centered at c
function energy(w, s, c) {
  const K = 1 / (8 * s * s), M = 240, h = 12 * s / M;
  let V = 0;
  for (let i = 0; i <= M; i++) {
    const u = -6 * s + i * h, p = Math.exp(-0.5 * u * u / (s * s)) / (s * Math.sqrt(2 * Math.PI));
    V += (i === 0 || i === M ? 0.5 : 1) * w.V(c + u) * p * h;
  }
  return { K, V, E: K + V };
}

function bestWidth(w, c) {                                           // golden-section search in sigma
  let a = SMIN, b = SMAX;
  const g = 0.6180339887;
  for (let it = 0; it < 60; it++) {
    const p = b - g * (b - a), q = a + g * (b - a);
    if (energy(w, p, c).E < energy(w, q, c).E) b = q; else a = p;
  }
  return 0.5 * (a + b);
}

const W = 1000, H = 400, PL = 58, PR = 600, PT = 26, PB = 368, QL = 690, QR = 980;

const CSS = `
.vt-root { --vt-fg: #212529; --vt-muted: #6c757d; --vt-border: #ced4da; --vt-btn: #f8f9fa; --vt-card: #ffffff;
  --vt-teal: ${TEAL}; --vt-orange: ${ORANGE}; --vt-red: ${CARDINAL}; --vt-wall: #e9ecef; --vt-on: #e7f1f4;
  color: var(--vt-fg); background: var(--vt-card); border: 1px solid var(--vt-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.vt-root.vt-dark { --vt-fg: #e9ecef; --vt-muted: #adb5bd; --vt-border: #495057; --vt-btn: #2b3035; --vt-card: #1e2125;
  --vt-teal: #45a9c6; --vt-orange: #f59f3a; --vt-red: #f05d6f; --vt-wall: #2b3035; --vt-on: #1f3a44; }
.vt-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.2em; margin: 0 0 0.3em; }
.vt-btns { display: flex; flex-wrap: wrap; gap: 0.35em; }
.vt-btn { font: inherit; color: var(--vt-fg); background: var(--vt-btn); border: 1px solid var(--vt-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.vt-btn:hover { border-color: ${TEAL}; }
.vt-btn.vt-active { border-color: var(--vt-teal); background: var(--vt-on); font-weight: 600; }
.vt-slider { display: flex; align-items: center; gap: 0.5em; }
.vt-slider input { width: 10em; accent-color: ${TEAL}; }
.vt-val { font-variant-numeric: tabular-nums; min-width: 2.6em; color: var(--vt-muted); }
.vt-plot { display: block; width: 100%; height: auto; }
.vt-plot text { font-family: inherit; fill: var(--vt-fg); }
.vt-status { font-weight: 600; margin: 0.2em 0 0; min-height: 2.8em; }
.vt-note { color: var(--vt-muted); }
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

// text with subscripts written as _{...}: SVG has no <sub>, and Unicode subscript glyphs render badly in some fonts
function rich(t, str) {
  t.textContent = "";
  str.split(/(_\{[^}]*\})/).forEach((part) => {
    if (!part) return;
    const ts = document.createElementNS(SVGNS, "tspan"), isSub = part.startsWith("_{");
    ts.textContent = isSub ? part.slice(2, -1) : part;
    if (isSub) { ts.setAttribute("dy", "0.3em"); ts.setAttribute("font-size", "75%"); }
    else if (t.lastChild && t.lastChild.getAttribute("dy") === "0.3em") ts.setAttribute("dy", "-0.225em");
    t.appendChild(ts);
  });
}

let uid = 0;

function render({ model, el }) {
  const get = (k, d) => { try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; } };

  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "vt-root", el);
  root.setAttribute("data-prevent-swipe", "");
  root.style.fontSize = get("fontSize", "15px");

  const controls = html("div", "vt-controls", root);
  const btns = html("div", "vt-btns", controls);
  const buttons = {};
  ORDER.forEach((key) => {
    const b = html("button", "vt-btn", btns, WELLS[key].name); b.type = "button";
    b.addEventListener("click", () => { b.blur(); choose(key); });
    buttons[key] = b;
  });
  const slider = (label, min, max, step) => {
    const box = html("label", "vt-slider", controls);
    html("span", null, box).innerHTML = label;
    const input = html("input", null, box); input.type = "range"; input.min = min; input.max = max; input.step = step;
    const val = html("span", "vt-val", box);
    input.addEventListener("change", () => input.blur());
    return { box, input, val };
  };
  const sW = slider("width σ", SMIN, SMAX, 0.01), sC = slider("center x<sub>0</sub>", -1, 2, 0.02);
  const best = html("button", "vt-btn", controls, "best"); best.type = "button";

  const plot = svg("svg", { viewBox: `0 0 ${W} ${H}`, class: "vt-plot", role: "img",
    "aria-label": "a potential well with a trial function and the exact ground state, beside the energy against the width" }, root);
  const clipId = `vt-clip-${uid++}`;
  const clip = svg("clipPath", { id: clipId }, svg("defs", {}, plot));
  svg("rect", { x: PL, y: PT, width: PR - PL, height: PB - PT }, clip);
  const Y = (e) => PB - (e / EMAX) * (PB - PT);
  const lab = (x, y, s, o = {}) => { const t = svg("text", Object.assign({ x, y, "font-size": 17 }, o), plot); t.textContent = s; return t; };
  const muted = "fill: var(--vt-muted)";
  for (let e = 0; e <= 3; e++) {
    svg("line", { x1: PL - 6, x2: PL, y1: Y(e), y2: Y(e), stroke: "var(--vt-muted)" }, plot);
    lab(PL - 10, Y(e) + 5, e, { "text-anchor": "end", style: muted });
    svg("line", { x1: QL - 6, x2: QL, y1: Y(e), y2: Y(e), stroke: "var(--vt-muted)" }, plot);
  }
  svg("line", { x1: PL, x2: PL, y1: PT, y2: PB, stroke: "var(--vt-muted)" }, plot);
  svg("line", { x1: QL, x2: QL, y1: PT, y2: PB, stroke: "var(--vt-muted)" }, plot);
  svg("line", { x1: QL, x2: QR, y1: PB, y2: PB, stroke: "var(--vt-muted)" }, plot);
  lab(16, (PT + PB) / 2, "energy", { "text-anchor": "middle", transform: `rotate(-90 16 ${(PT + PB) / 2})`, style: muted });
  lab(PR - 4, PB + 24, "x →", { "text-anchor": "end", style: muted });
  lab((QL + QR) / 2, PB + 24, "width σ of the trial function", { "text-anchor": "middle", style: muted });

  const g = svg("g", { "clip-path": `url(#${clipId})` }, plot);
  const wall = svg("path", { fill: "var(--vt-wall)", stroke: "none" }, g);
  const exactLine = svg("line", { stroke: "var(--vt-muted)", "stroke-width": 1.6, "stroke-dasharray": "6 5" }, g);
  const exactPsi = svg("path", { fill: "none", stroke: "var(--vt-muted)", "stroke-width": 2, "stroke-dasharray": "6 5" }, g);
  const trialFill = svg("path", { fill: "var(--vt-teal)", "fill-opacity": 0.25, stroke: "none" }, g);
  const trialLine = svg("line", { stroke: "var(--vt-teal)", "stroke-width": 2 }, g);
  const trialPsi = svg("path", { fill: "none", stroke: "var(--vt-teal)", "stroke-width": 2.6 }, g);
  const curve = svg("path", { fill: "none", stroke: "var(--vt-fg)", "stroke-width": 2.6, "stroke-linejoin": "round" }, g);
  const halo = "paint-order: stroke; stroke: var(--vt-card); stroke-width: 5px; stroke-linejoin: round; ";
  const exactLab = lab(PR - 6, 0, "", { "text-anchor": "end", style: halo + muted });
  const trialLab = lab(PR - 6, 0, "", { "text-anchor": "end", style: halo + "fill: var(--vt-teal)", "font-weight": 600 });

  const q = svg("g", {}, plot);
  const cK = svg("path", { fill: "none", stroke: "var(--vt-orange)", "stroke-width": 1.8 }, q);
  const cV = svg("path", { fill: "none", stroke: "var(--vt-teal)", "stroke-width": 1.8 }, q);
  const cE = svg("path", { fill: "none", stroke: "var(--vt-fg)", "stroke-width": 2.8 }, q);
  const cX = svg("line", { x1: QL, x2: QR, stroke: "var(--vt-muted)", "stroke-width": 1.6, "stroke-dasharray": "6 5" }, q);
  const dot = svg("circle", { r: 7, fill: "var(--vt-red)" }, q);
  lab(QL + 8, PT + 14, "kinetic", { style: "fill: var(--vt-orange)" });
  lab(QL + 74, PT + 14, "potential", { style: "fill: var(--vt-teal)" });
  lab(QL + 158, PT + 14, "total", { "font-weight": 600 });
  lab(QR, PT + 14, "exact", { "text-anchor": "end", style: muted });

  const status = html("div", "vt-status", root);
  if (get("status", true) === false) status.style.display = "none";
  const note = html("div", "vt-note", root);
  if (get("note", true) === false) note.style.display = "none";

  const cache = {};
  let current = WELLS[get("well", "vee")] ? get("well", "vee") : "vee";
  const state = { spring: { s: 1.3, c: 0 }, vee: { s: 1.4, c: 0 }, morse: { s: 0.9, c: 0 } };

  function update() {
    const w = WELLS[current], st = state[current];
    if (!cache[current]) cache[current] = ground(w);
    const ex = cache[current];
    const [v0, v1] = w.view, X = (x) => PL + (x - v0) / (v1 - v0) * (PR - PL);
    sW.val.textContent = st.s.toFixed(2); sC.val.textContent = st.c.toFixed(2);

    // the well
    let dc = "", dw = `M${X(v0)},${Y(0)}`;
    for (let i = 0; i <= 300; i++) {
      const x = v0 + (v1 - v0) * i / 300, v = Math.min(w.V(x), EMAX + 0.4);
      dc += (i ? "L" : "M") + X(x).toFixed(1) + "," + Y(v).toFixed(1);
      dw += "L" + X(x).toFixed(1) + "," + Y(v).toFixed(1);
    }
    curve.setAttribute("d", dc); wall.setAttribute("d", dw + `L${X(v1)},${Y(0)}Z`);

    // the exact ground state on its level
    const AMP = 0.95;
    let de = "";
    for (let i = 0, first = true; i < ex.x.length; i += 2) {
      if (ex.x[i] < v0 || ex.x[i] > v1 || ex.psi[i] < 0.004) continue;
      de += (first ? "M" : "L") + X(ex.x[i]).toFixed(1) + "," + Y(ex.E + AMP * ex.psi[i]).toFixed(1); first = false;
    }
    exactPsi.setAttribute("d", de);
    for (const [k, v] of [["x1", PL], ["x2", PR], ["y1", Y(ex.E)], ["y2", Y(ex.E)]]) exactLine.setAttribute(k, v);

    // the trial function on its level
    const en = energy(w, st.s, st.c), yE = Y(Math.min(en.E, EMAX + 1));
    let dt = "", n0 = Math.pow(2 * Math.PI * st.s * st.s, -0.25);
    const xa = Math.max(v0, st.c - 5 * st.s), xb = Math.min(v1, st.c + 5 * st.s);
    for (let i = 0; i <= 200; i++) {
      const x = xa + (xb - xa) * i / 200, f = n0 * Math.exp(-0.25 * (x - st.c) ** 2 / (st.s * st.s));
      dt += (i ? "L" : "M") + X(x).toFixed(1) + "," + Y(en.E + AMP * f).toFixed(1);
    }
    trialPsi.setAttribute("d", dt);
    trialFill.setAttribute("d", dt + `L${X(xb).toFixed(1)},${yE.toFixed(1)}L${X(xa).toFixed(1)},${yE.toFixed(1)}Z`);
    for (const [k, v] of [["x1", PL], ["x2", PR], ["y1", yE], ["y2", yE]]) trialLine.setAttribute(k, v);
    exactLab.setAttribute("y", Y(ex.E) + 19); rich(exactLab, `exact E_{0} = ${ex.E.toFixed(3)}`);
    trialLab.setAttribute("y", Math.max(yE - 9, PT + 14)); trialLab.textContent = `⟨E⟩ = ${en.E.toFixed(3)}`;

    // energy against width, for the present center
    const SX = (s) => QL + (s - SMIN) / (SMAX - SMIN) * (QR - QL), YC = (e) => Y(Math.max(-0.2, Math.min(e, EMAX + 0.3)));
    let dK = "", dV = "", dE = "";
    for (let i = 0; i <= 80; i++) {
      const s = SMIN + (SMAX - SMIN) * i / 80, e = energy(w, s, st.c), m = i ? "L" : "M";
      dK += m + SX(s).toFixed(1) + "," + YC(e.K).toFixed(1);
      dV += m + SX(s).toFixed(1) + "," + YC(e.V).toFixed(1);
      dE += m + SX(s).toFixed(1) + "," + YC(e.E).toFixed(1);
    }
    cK.setAttribute("d", dK); cV.setAttribute("d", dV); cE.setAttribute("d", dE);
    cX.setAttribute("y1", Y(ex.E)); cX.setAttribute("y2", Y(ex.E));
    dot.setAttribute("cx", SX(st.s)); dot.setAttribute("cy", YC(en.E));

    const pct = 100 * (en.E - ex.E) / ex.E, sb = bestWidth(w, st.c), eb = energy(w, sb, st.c).E;
    let s = `⟨E⟩ = ${en.E.toFixed(3)}  (kinetic ${en.K.toFixed(3)} + potential ${en.V.toFixed(3)}),  exact ${ex.E.toFixed(3)}:  `;
    s += pct < 0.02 ? "the bound is met." : `${pct < 1 ? pct.toFixed(2) : pct.toFixed(1)}% too high.`;
    if (Math.abs(st.s - sb) < 0.012) {
      s += current === "spring" && Math.abs(st.c) < 0.02 ? " This Gaussian is the exact ground state."
        : ` Best width for this center; the Gaussian family can do no better${w.center ? " without moving it" : ""}.`;
    } else s += st.s < sb ? " Too narrow: the kinetic energy is high." : " Too wide: the potential energy is high.";
    status.textContent = s;
    note.innerHTML = `${w.formula}, with ħ = m = 1. Teal: the trial function exp(−(x − x<sub>0</sub>)²/4σ²), drawn on its ` +
      "average energy. Dashed: the exact ground state on its level. The teal level never drops below the dashed one.";
  }

  function choose(key) {
    current = key;
    ORDER.forEach((k) => buttons[k].classList.toggle("vt-active", k === key));
    sC.box.style.display = WELLS[key].center ? "" : "none";
    sW.input.value = state[key].s; sC.input.value = state[key].c;
    update();
  }
  sW.input.addEventListener("input", () => { state[current].s = +sW.input.value; update(); });
  sC.input.addEventListener("input", () => { state[current].c = +sC.input.value; update(); });
  best.addEventListener("click", () => {
    best.blur();
    const w = WELLS[current], st = state[current];
    if (w.center) {                                                  // width and center in turn
      for (let it = 0; it < 12; it++) {
        st.s = bestWidth(w, st.c);
        let a = -1, b = 2;
        const gr = 0.6180339887;
        for (let k = 0; k < 40; k++) {
          const p = b - gr * (b - a), r = a + gr * (b - a);
          if (energy(w, st.s, p).E < energy(w, st.s, r).E) b = r; else a = p;
        }
        st.c = 0.5 * (a + b);
      }
    }
    st.s = bestWidth(w, st.c);
    sW.input.value = st.s; sC.input.value = st.c;
    update();
  });

  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("vt-dark")) root.classList.toggle("vt-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  choose(current);
  syncDark();
  return () => { if (obs) obs.disconnect(); };
}

export default { render };
export { ground, energy, bestWidth, WELLS };
