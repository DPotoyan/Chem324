// Perturbation theory with a dial: a particle in a box, plus a bump or a slope whose strength you set.
//
// Units: box length L = 1, energies in units of the unperturbed ground-state energy E_1 (so E_n = n^2). Two
// perturbations: a bump of height s on the middle fifth of the floor (0.4 L to 0.6 L), and a slope s (x - L/2).
// Matrix elements between box states are analytic. "Exact" means the Hamiltonian on a grid of 900 points (Sturm
// bisection for the levels, inverse iteration for the ground state). First order is the diagonal element; second
// order the sum over the other 39 box states.
// Left: the box with its perturbation, the unperturbed ground state (dashed), the exact one (thick) and the
// first-order one (purple). Right: the three lowest levels against the strength, exact, first order and second
// order, with a marker at the present strength.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get. No dependencies.
// Model keys, optional: fontSize (CSS size), shape ("bump" or "slope"), strength (0 to 8), status and note (false hides
// the verdict line or the description).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00", PURPLE = "#6a3d9a";
const SVGNS = "http://www.w3.org/2000/svg";
const K = 40, SMAX = 8, NS = 40, PI = Math.PI;

// <m|shape|n> for box states sqrt(2) sin(n pi x), m and n counted from 1
const ELEMENT = {
  bump: (m, n) => {
    const a = 0.4, b = 0.6;
    const F = (k) => (Math.sin(k * PI * b) - Math.sin(k * PI * a)) / (k * PI);
    return m === n ? (b - a) - F(2 * n) : F(m - n) - F(m + n);
  },
  slope: (m, n) => ((m + n) % 2 === 0 ? 0 : -8 * m * n / (PI * PI * (m * m - n * n) ** 2)),
};
const SHAPES = {                                                     // units as SVG text (_{...} is a subscript) and as HTML
  bump: { name: "bump", unit: "E_{1}", unitHtml: "E<sub>1</sub>", what: "bump height" },
  slope: { name: "slope", unit: "E_{1}/L", unitHtml: "E<sub>1</sub>/L", what: "slope" },
};

function matrix(shape) {
  const M = [];
  for (let m = 1; m <= K; m++) { const row = new Float64Array(K); for (let n = 1; n <= K; n++) row[n - 1] = ELEMENT[shape](m, n); M.push(row); }
  return M;
}

// exact levels and ground state on a grid: H = -1/2 d^2/dx^2 + s E_1 shape(x) with walls at 0 and 1,
// energies by Sturm bisection, the ground state by inverse iteration; returned in units of E_1
const NG = 900, DX = 1 / NG, E1 = PI * PI / 2;
// the bump's edges fall on grid points, which get half weight so that the grid bump is exactly 0.2 wide
const PROFILE = { bump: (x) => (Math.abs(x - 0.5) < 0.1 - 1e-9 ? 1 : Math.abs(x - 0.5) < 0.1 + 1e-9 ? 0.5 : 0), slope: (x) => x - 0.5 };

function solve(shape, s) {
  const N = NG - 1, d = new Float64Array(N), off = -0.5 / (DX * DX), e2 = off * off;
  for (let i = 0; i < N; i++) d[i] = 1 / (DX * DX) + s * E1 * PROFILE[shape]((i + 1) * DX);
  const count = (lam) => {
    let c = 0, q = d[0] - lam;
    if (q < 0) c++;
    for (let i = 1; i < N; i++) { q = d[i] - lam - e2 / (q === 0 ? 1e-300 : q); if (q < 0) c++; }
    return c;
  };
  const E = [];
  for (let k = 0; k < 3; k++) {
    let a = -6 * E1, b = 30 * E1;
    for (let it = 0; it < 56; it++) { const m = 0.5 * (a + b); if (count(m) > k) b = m; else a = m; }
    E.push(0.5 * (a + b));
  }
  const sig = E[0] - 1e-9, cp = new Float64Array(N), dp = new Float64Array(N);
  let y = new Float64Array(N).fill(1);
  for (let it = 0; it < 3; it++) {
    let m = d[0] - sig;
    cp[0] = off / m; dp[0] = y[0] / m;
    for (let i = 1; i < N; i++) { m = d[i] - sig - off * cp[i - 1]; cp[i] = off / m; dp[i] = (y[i] - off * dp[i - 1]) / m; }
    const z = new Float64Array(N);
    z[N - 1] = dp[N - 1];
    for (let i = N - 2; i >= 0; i--) z[i] = dp[i] - cp[i] * z[i + 1];
    let nrm = 0;
    for (let i = 0; i < N; i++) nrm += z[i] * z[i] * DX;
    nrm = Math.sqrt(nrm);
    for (let i = 0; i < N; i++) y[i] = Math.abs(z[i]) / nrm;
  }
  return { E: E.map((v) => v / E1), ground: y };
}

function orders(H1, n) {                                             // first- and second-order coefficients of level n (1-based)
  let e2 = 0;
  for (let k = 1; k <= K; k++) if (k !== n) e2 += H1[k - 1][n - 1] ** 2 / (n * n - k * k);
  return { e1: H1[n - 1][n - 1], e2 };
}

const W = 1000, H = 400, AL = 40, AR = 420, PT = 30, PB = 350, BL = 540, BR = 975, EMAXV = 12;

const CSS = `
.pd-root { --pd-fg: #212529; --pd-muted: #6c757d; --pd-border: #ced4da; --pd-btn: #f8f9fa; --pd-card: #ffffff;
  --pd-teal: ${TEAL}; --pd-orange: ${ORANGE}; --pd-purple: ${PURPLE}; --pd-red: ${CARDINAL}; --pd-on: #e7f1f4;
  color: var(--pd-fg); background: var(--pd-card); border: 1px solid var(--pd-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.pd-root.pd-dark { --pd-fg: #e9ecef; --pd-muted: #adb5bd; --pd-border: #495057; --pd-btn: #2b3035; --pd-card: #1e2125;
  --pd-teal: #45a9c6; --pd-orange: #f59f3a; --pd-purple: #b08be0; --pd-red: #f05d6f; --pd-on: #1f3a44; }
.pd-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.2em; margin: 0 0 0.3em; }
.pd-btns { display: flex; flex-wrap: wrap; gap: 0.35em; }
.pd-btn { font: inherit; color: var(--pd-fg); background: var(--pd-btn); border: 1px solid var(--pd-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.pd-btn:hover { border-color: ${TEAL}; }
.pd-btn.pd-active { border-color: var(--pd-teal); background: var(--pd-on); font-weight: 600; }
.pd-slider { display: flex; align-items: center; gap: 0.5em; }
.pd-slider input { width: 13em; accent-color: ${TEAL}; }
.pd-val { font-variant-numeric: tabular-nums; min-width: 5em; color: var(--pd-muted); }
.pd-plot { display: block; width: 100%; height: auto; }
.pd-plot text { font-family: inherit; fill: var(--pd-fg); }
.pd-status { font-weight: 600; margin: 0.2em 0 0; min-height: 2.8em; }
.pd-note { color: var(--pd-muted); }
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

function render({ model, el }) {
  const get = (k, d) => { try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; } };

  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "pd-root", el);
  root.setAttribute("data-prevent-swipe", "");
  root.style.fontSize = get("fontSize", "15px");

  const controls = html("div", "pd-controls", root);
  const btns = html("div", "pd-btns", controls);
  const buttons = {};
  Object.keys(SHAPES).forEach((key) => {
    const b = html("button", "pd-btn", btns, SHAPES[key].name); b.type = "button";
    b.addEventListener("click", () => { b.blur(); choose(key); });
    buttons[key] = b;
  });
  const box = html("label", "pd-slider", controls);
  const knobName = html("span", null, box);
  const input = html("input", null, box); input.type = "range"; input.min = 0; input.max = SMAX; input.step = 0.05;
  const knobVal = html("span", "pd-val", box);
  input.addEventListener("change", () => input.blur());

  const plot = svg("svg", { viewBox: `0 0 ${W} ${H}`, class: "pd-plot", role: "img",
    "aria-label": "a box with a perturbation and its ground state, beside the energy levels against the strength" }, root);
  const lab = (x, y, s, o = {}) => { const t = svg("text", Object.assign({ x, y, "font-size": 16.5 }, o), plot); t.textContent = s; return t; };
  const muted = "fill: var(--pd-muted)";

  // left: the box
  const floorY = PB - 34, zeroY = PB - 150, AMP = 105;                // floor of the box, baseline and scale of the functions
  const XA = (x) => AL + 20 + x * (AR - AL - 40);
  const pert = svg("path", { fill: "var(--pd-orange)", "fill-opacity": 0.8, stroke: "none" }, plot);
  svg("line", { x1: XA(0), x2: XA(0), y1: PT + 8, y2: floorY + 34, stroke: "var(--pd-fg)", "stroke-width": 2.6 }, plot);
  svg("line", { x1: XA(1), x2: XA(1), y1: PT + 8, y2: floorY + 34, stroke: "var(--pd-fg)", "stroke-width": 2.6 }, plot);
  const floor = svg("path", { fill: "none", stroke: "var(--pd-fg)", "stroke-width": 2.6 }, plot);
  svg("line", { x1: XA(0), x2: XA(1), y1: zeroY, y2: zeroY, stroke: "var(--pd-muted)", "stroke-width": 1, "stroke-dasharray": "2 4" }, plot);
  const pUn = svg("path", { fill: "none", stroke: "var(--pd-muted)", "stroke-width": 2, "stroke-dasharray": "6 5" }, plot);
  const pEx = svg("path", { fill: "none", stroke: "var(--pd-fg)", "stroke-width": 6, "stroke-opacity": 0.3 }, plot);
  const pFi = svg("path", { fill: "none", stroke: "var(--pd-purple)", "stroke-width": 2.4 }, plot);
  lab(XA(0), PT - 8, "ground state:", { style: muted });
  lab(XA(0) + 108, PT - 8, "unperturbed", { style: muted });
  lab(XA(0) + 208, PT - 8, "exact", { "font-weight": 600 });
  lab(XA(0) + 260, PT - 8, "first order", { style: "fill: var(--pd-purple)", "font-weight": 600 });
  lab(XA(0), floorY + 52, "0", { "text-anchor": "middle", style: muted });
  lab(XA(1), floorY + 52, "L", { "text-anchor": "middle", style: muted });

  // right: levels against strength
  const XB = (s) => BL + s / SMAX * (BR - BL), YB = (e) => PB - e / EMAXV * (PB - PT);
  svg("line", { x1: BL, x2: BL, y1: PT, y2: PB, stroke: "var(--pd-muted)" }, plot);
  svg("line", { x1: BL, x2: BR, y1: PB, y2: PB, stroke: "var(--pd-muted)" }, plot);
  for (const e of [1, 4, 9]) {
    svg("line", { x1: BL - 6, x2: BL, y1: YB(e), y2: YB(e), stroke: "var(--pd-muted)" }, plot);
    lab(BL - 10, YB(e) + 5, `n = ${Math.sqrt(e)}`, { "text-anchor": "end", style: muted });
  }
  for (let s = 0; s <= SMAX; s += 2) {
    svg("line", { x1: XB(s), x2: XB(s), y1: PB, y2: PB + 6, stroke: "var(--pd-muted)" }, plot);
    lab(XB(s), PB + 22, s, { "text-anchor": "middle", style: muted });
  }
  const xlab = lab((BL + BR) / 2, PB + 39, "", { "text-anchor": "middle", style: muted });
  lab(BL + 10, PT - 8, "exact", { "font-weight": 600 });
  lab(BL + 66, PT - 8, "first order", { style: "fill: var(--pd-purple)", "font-weight": 600 });
  lab(BL + 164, PT - 8, "second order", { style: "fill: var(--pd-orange)", "font-weight": 600 });
  const clipId = `pd-clip-${Math.random().toString(36).slice(2)}`;
  svg("rect", { x: BL, y: PT, width: BR - BL, height: PB - PT }, svg("clipPath", { id: clipId }, svg("defs", {}, plot)));
  const curves = svg("g", { "clip-path": `url(#${clipId})` }, plot);
  const marker = svg("line", { y1: PT, y2: PB, stroke: "var(--pd-red)", "stroke-width": 1.6 }, plot);
  const dots = svg("g", {}, plot);

  const status = html("div", "pd-status", root);
  if (get("status", true) === false) status.style.display = "none";
  const note = html("div", "pd-note", root);
  if (get("note", true) === false) note.style.display = "none";

  const cache = {};
  let current = SHAPES[get("shape", "bump")] ? get("shape", "bump") : "bump";
  const strength = { bump: 2, slope: 3 };
  const s0 = +get("strength", NaN);
  if (!Number.isNaN(s0)) strength[current] = Math.max(0, Math.min(SMAX, s0));

  function prepare(shape) {                                          // matrix, perturbation coefficients, exact curves
    const H1 = matrix(shape), ord = [1, 2, 3].map((n) => orders(H1, n)), ex = [];
    for (let i = 0; i <= NS; i++) ex.push(solve(shape, SMAX * i / NS).E);
    cache[shape] = { H1, ord, ex };
  }

  function drawCurves(c) {
    curves.innerHTML = "";
    for (let n = 1; n <= 3; n++) {
      let d1 = "", d2 = "", dx = "";
      for (let i = 0; i <= NS; i++) {
        const s = SMAX * i / NS, m = i ? "L" : "M", o = c.ord[n - 1];
        d1 += m + XB(s).toFixed(1) + "," + YB(n * n + o.e1 * s).toFixed(1);
        d2 += m + XB(s).toFixed(1) + "," + YB(n * n + o.e1 * s + o.e2 * s * s).toFixed(1);
        dx += m + XB(s).toFixed(1) + "," + YB(c.ex[i][n - 1]).toFixed(1);
      }
      svg("path", { d: d1, fill: "none", stroke: "var(--pd-purple)", "stroke-width": 2, "stroke-dasharray": "7 4" }, curves);
      svg("path", { d: d2, fill: "none", stroke: "var(--pd-orange)", "stroke-width": 2.2, "stroke-dasharray": "2 4" }, curves);
      svg("path", { d: dx, fill: "none", stroke: "var(--pd-fg)", "stroke-width": 2.6 }, curves);
    }
  }

  function update() {
    const c = cache[current], s = strength[current], sh = SHAPES[current];
    knobVal.innerHTML = `${s.toFixed(2)} ${sh.unitHtml}`;
    rich(xlab, `${sh.what} (units of ${sh.unit})`);

    // the perturbation, drawn on the floor of the box (height scale: 9 px per unit of E_1)
    const hpx = 9;
    if (current === "bump") {
      pert.setAttribute("d", `M${XA(0.4)},${floorY}L${XA(0.4)},${floorY - hpx * s}L${XA(0.6)},${floorY - hpx * s}L${XA(0.6)},${floorY}Z`);
      floor.setAttribute("d", `M${XA(0)},${floorY}L${XA(1)},${floorY}`);
    } else {
      pert.setAttribute("d", "");
      floor.setAttribute("d", `M${XA(0)},${floorY + 0.5 * hpx * s * 0.45}L${XA(1)},${floorY - 0.5 * hpx * s * 0.45}`);
    }

    // ground states: unperturbed, exact (grid), first order
    const { E, ground } = solve(current, s);
    const first = new Float64Array(K); first[0] = 1;
    for (let k = 2; k <= K; k++) first[k - 1] = s * c.H1[k - 1][0] / (1 - k * k);
    const path = (coef) => {
      let d = "";
      for (let i = 0; i <= 160; i++) {
        const x = i / 160;
        let f = 0;
        for (let k = 1; k <= K; k++) if (coef[k - 1] !== 0) f += coef[k - 1] * Math.SQRT2 * Math.sin(k * PI * x);
        d += (i ? "L" : "M") + XA(x).toFixed(1) + "," + (zeroY - AMP * f).toFixed(1);
      }
      return d;
    };
    const un = new Float64Array(K); un[0] = 1;
    let dg = `M${XA(0)},${zeroY}`;
    for (let i = 0; i < ground.length; i += 5) dg += "L" + XA((i + 1) * DX).toFixed(1) + "," + (zeroY - AMP * ground[i]).toFixed(1);
    pUn.setAttribute("d", path(un)); pEx.setAttribute("d", dg + `L${XA(1)},${zeroY}`); pFi.setAttribute("d", path(first));

    marker.setAttribute("x1", XB(s)); marker.setAttribute("x2", XB(s));
    dots.innerHTML = "";
    for (let n = 1; n <= 3; n++) svg("circle", { cx: XB(s), cy: YB(Math.min(E[n - 1], EMAXV)), r: 5, fill: "var(--pd-red)" }, dots);

    const o = c.ord[0], e1 = 1 + o.e1 * s, e2 = e1 + o.e2 * s * s, pc = (v) => `${(100 * Math.abs(v - E[0]) / E[0]).toFixed(v === e2 ? 2 : 1)}%`;
    let txt = `Ground state, in units of E<sub>1</sub>: exact ${E[0].toFixed(3)}, first order ${e1.toFixed(3)} (off by ${pc(e1)}), ` +
      `second order ${e2.toFixed(3)} (off by ${pc(e2)}). `;
    if (s < 0.03) txt += "No perturbation: every order agrees.";
    else if (current === "slope") txt += s < 4 ? "First order is zero by symmetry; the whole shift is second order."
      : "A slope this steep mixes many states; second order overshoots.";
    else txt += s < 3 ? `The bump is ${(s / 3).toFixed(2)} of the gap between the two lowest levels: a small perturbation.`
      : `The bump is ${(s / 3).toFixed(1)} times the gap between the two lowest levels: no longer small.`;
    status.innerHTML = txt;
    note.textContent = current === "bump"
      ? "A bump on the middle fifth of the floor. First order: the bump times the chance of finding the particle on it. " +
        "Exact: solved numerically on a grid."
      : "A floor that rises to the right. The ground state leans to the low side by mixing in the next state. " +
        "Exact: solved numerically on a grid.";
  }

  function choose(key) {
    current = key;
    Object.keys(SHAPES).forEach((k) => buttons[k].classList.toggle("pd-active", k === key));
    if (!cache[key]) prepare(key);
    knobName.textContent = SHAPES[key].what;
    input.value = strength[key];
    drawCurves(cache[key]);
    update();
  }
  input.addEventListener("input", () => { strength[current] = +input.value; update(); });

  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("pd-dark")) root.classList.toggle("pd-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  choose(current);
  syncDark();
  return () => { if (obs) obs.disconnect(); };
}

export default { render };
export { matrix, solve, orders };
