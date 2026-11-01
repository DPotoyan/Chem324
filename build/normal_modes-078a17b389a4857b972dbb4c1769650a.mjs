// CO2's two stretching modes, watched atom by atom and mode by mode.
//
// O, C, O on a line, one spring per bond (masses 16, 12, 16 u). Two sliders set how much of each normal mode the
// molecule holds; it starts from rest and vibrates. Left panel: the energy split atom by atom, three kinetic energies
// and two springs. It sloshes, because in these coordinates the Hamiltonian has cross terms. Right panel: the energy
// of each normal mode, split into its kinetic and potential parts. The split inside a mode sloshes, but each mode's
// total never changes: in normal coordinates the Hamiltonian is a sum of independent oscillators. Presets: pure
// symmetric, pure antisymmetric, and "pull the left O", which holds a mix of both.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch04/03), in a reveal.js deck through a module-script loader, and in Jupyter or
// Colab through the anywidget package. No dependencies. Model keys, optional: fontSize (CSS size), status (false
// hides the one-line verdict under the panels, to save height on a slide).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00", PURPLE = "#6a3d9a";
const SVGNS = "http://www.w3.org/2000/svg";

// physics, in units with k = 1 and masses in u
const MASS = [16, 12, 16], K = 1;
const SQ = MASS.map(Math.sqrt);
const W_S = Math.sqrt(K / MASS[0]);                                 // symmetric stretch
const W_A = W_S * Math.sqrt(1 + 2 * MASS[0] / MASS[1]);             // antisymmetric stretch
const U_S = [-Math.SQRT1_2, 0, Math.SQRT1_2];                       // mass-weighted mode vectors, unit length
const UA0 = [SQ[0], -2 * MASS[0] / SQ[1], SQ[2]];
const U_A = UA0.map((v) => v / Math.hypot(...UA0));
const PERIOD = 2.6;                                                 // real seconds per symmetric period
const TSCALE = (2 * Math.PI / W_S) / PERIOD;                        // simulation time per real second
const FRAME = 33;                                                   // ms

// "pull the left O": displace it, keep the center of mass, project onto the modes
const PULL = (() => {
  const x = [-1, 0, 0], M = MASS[0] + MASS[1] + MASS[2];
  const com = (MASS[0] * x[0] + MASS[1] * x[1] + MASS[2] * x[2]) / M;
  const q = x.map((v, i) => SQ[i] * (v - com));
  const s = q.reduce((a, v, i) => a + v * U_S[i], 0), a = q.reduce((b, v, i) => b + v * U_A[i], 0);
  const n = Math.max(Math.abs(s), Math.abs(a));
  return [s / n, a / n];
})();

// drawing
const MW = 600, MH = 128, CX = MW / 2, BOND = 140, PX = 165;        // molecule view; px per unit displacement
const PW = 330, PH = 188, BASE = 150, BMAX = 138;                    // energy panels

const CSS = `
.nm-root { --nm-fg: #212529; --nm-muted: #6c757d; --nm-border: #ced4da; --nm-btn: #f8f9fa; --nm-card: #ffffff;
  --nm-teal: ${TEAL}; --nm-red: ${CARDINAL}; --nm-orange: ${ORANGE}; --nm-purple: ${PURPLE}; --nm-c: #495057;
  --nm-ghost: #ced4da; --nm-bond: #adb5bd; --nm-total: #868e96;
  color: var(--nm-fg); background: var(--nm-card); border: 1px solid var(--nm-border); border-radius: 10px;
  padding: 0.8em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.nm-root.nm-dark { --nm-fg: #e9ecef; --nm-muted: #adb5bd; --nm-border: #495057; --nm-btn: #2b3035; --nm-card: #1e2125;
  --nm-teal: #45a9c6; --nm-red: #f05d6f; --nm-orange: #f59f3a; --nm-purple: #b08be0; --nm-c: #adb5bd;
  --nm-ghost: #495057; --nm-bond: #6c757d; --nm-total: #adb5bd; }
.nm-mol { display: block; width: 100%; max-width: 32em; height: auto; margin: 0 auto; }
.nm-mol text, .nm-bars text { font-family: inherit; fill: var(--nm-fg); }
.nm-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.2em; margin: 0.3em 0 0.6em; }
.nm-slider { display: flex; align-items: center; gap: 0.5em; }
.nm-slider input { width: 9em; accent-color: ${TEAL}; }
.nm-val { font-variant-numeric: tabular-nums; min-width: 2.8em; color: var(--nm-muted); }
.nm-btns { display: flex; flex-wrap: wrap; gap: 0.35em; }
.nm-btn { font: inherit; color: var(--nm-fg); background: var(--nm-btn); border: 1px solid var(--nm-border);
  border-radius: 999px; padding: 0.12em 0.7em; cursor: pointer; line-height: 1.5; margin: 0; }
.nm-btn:hover { border-color: ${TEAL}; }
.nm-panels { display: flex; flex-wrap: wrap; gap: 0.6em 1.4em; }
.nm-panel { flex: 1 1 16em; min-width: 14em; display: flex; flex-direction: column; }
.nm-head { font-weight: 600; }
.nm-eq { color: var(--nm-muted); margin: 0.1em 0 0.2em; }
.nm-bars { display: block; width: 100%; max-width: 21em; height: auto; margin-top: auto; }
.nm-key { display: inline-block; width: 0.8em; height: 0.8em; border-radius: 2px; margin: 0 0.25em 0 0.6em;
  vertical-align: -0.05em; }
.nm-status { font-weight: 600; margin: 0.4em 0 0; min-height: 1.4em; }
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

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "nm-root", el);
  root.setAttribute("data-prevent-swipe", "");                     // reveal.js: drags must not change slides
  root.style.fontSize = get("fontSize", "15px");

  // the molecule
  const mol = svg("svg", { viewBox: `0 0 ${MW} ${MH}`, class: "nm-mol", role: "img",
    "aria-label": "CO2 vibrating along its axis" }, root);
  const X0 = [CX - BOND, CX, CX + BOND], R = [27, 23, 27], Y0 = 54;
  X0.forEach((x, i) => svg("circle", { cx: x, cy: Y0, r: R[i], fill: "none", stroke: "var(--nm-ghost)",
    "stroke-width": 1.5, "stroke-dasharray": "4 3" }, mol));
  const bonds = [0, 1].map(() => svg("line", { y1: Y0, y2: Y0, stroke: "var(--nm-bond)", "stroke-width": 9,
    "stroke-linecap": "round" }, mol));
  const atoms = X0.map((x, i) => svg("circle", { cy: Y0, r: R[i], fill: i === 1 ? "var(--nm-c)" : "var(--nm-red)",
    stroke: "#000", "stroke-width": 1 }, mol));
  const labels = ["O", "C", "O"].map((s) => svg("text", { y: Y0 + 5, "text-anchor": "middle", "font-size": 15,
    "font-weight": 700, style: "fill: #fff" }, mol));
  labels.forEach((t, i) => { t.textContent = ["O", "C", "O"][i]; });
  ["left O", "C", "right O"].forEach((s, i) => {
    const t = svg("text", { x: X0[i], y: 112, "text-anchor": "middle", "font-size": 14, style: "fill: var(--nm-muted)" }, mol);
    t.textContent = s;
  });

  // controls
  const controls = html("div", "nm-controls", root);
  const sliders = {};
  const slider = (key, label, color) => {
    const box = html("label", "nm-slider", controls);
    const name = html("span", null, box, label); name.style.color = color;
    const input = html("input", null, box); input.type = "range"; input.min = -1; input.max = 1; input.step = 0.05;
    const val = html("span", "nm-val", box);
    input.addEventListener("input", () => { setAmps(key === "s" ? +input.value : amp.s, key === "a" ? +input.value : amp.a); });
    input.addEventListener("change", () => input.blur());           // arrow keys go back to the deck
    sliders[key] = { input, val };
  };
  slider("s", "symmetric", "var(--nm-teal)");
  slider("a", "antisymmetric", "var(--nm-purple)");
  const btns = html("div", "nm-btns", controls);
  const button = (label, act) => {
    const b = html("button", "nm-btn", btns, label); b.type = "button";
    b.addEventListener("click", () => { b.blur(); act(); });
    return b;
  };
  button("pure symmetric", () => setAmps(1, 0));
  button("pure antisymmetric", () => setAmps(0, 1));
  button("pull the left O", () => setAmps(PULL[0], PULL[1]));
  const pauseBtn = button("pause", () => { running ? stop() : start(); });

  // the two energy panels
  const panels = html("div", "nm-panels", root);
  const panel = (head, eq) => {
    const p = html("div", "nm-panel", panels);
    html("div", "nm-head", p, head);
    html("div", "nm-eq", p, eq);
    return svg("svg", { viewBox: `0 0 ${PW} ${PH}`, class: "nm-bars", role: "img" }, p);
  };
  const left = panel("Atom by atom: the energy sloshes",
    "H = Σ pᵢ²/2mᵢ + ½k(x₂ − x₁)² + ½k(x₃ − x₂)², with cross terms x₁x₂, x₂x₃");
  const right = panel("Mode by mode: each total stays put",
    "H = (½Pₛ² + ½ωₛ²Qₛ²) + (½Pₐ² + ½ωₐ²Qₐ²): no cross terms");
  const keys = html("div", "nm-eq", root);
  keys.innerHTML = `bars show the fraction of the total energy:` +
    `<span class="nm-key" style="background: var(--nm-orange)"></span>kinetic` +
    `<span class="nm-key" style="background: var(--nm-teal)"></span>potential` +
    `<span class="nm-key" style="background: var(--nm-total)"></span>total`;
  const status = html("div", "nm-status", root);
  if (get("status", true) === false) status.style.display = "none";

  const axis = (g) => svg("line", { x1: 12, x2: PW - 6, y1: BASE, y2: BASE, stroke: "var(--nm-muted)", "stroke-width": 1 }, g);
  axis(left); axis(right);
  const barLabel = (g, x, s1, s2) => {
    const t = svg("text", { x, y: BASE + 17, "text-anchor": "middle", "font-size": 13 }, g); t.textContent = s1;
    if (s2) { const u = svg("text", { x, y: BASE + 32, "text-anchor": "middle", "font-size": 12, style: "fill: var(--nm-muted)" }, g); u.textContent = s2; }
  };
  const rect = (g, fill) => svg("rect", { width: 30, rx: 2, fill }, g);
  const LX = [24, 72, 120, 178, 230, 288];                          // left: KE O, KE C, KE O, bond 1, bond 2, total
  const leftBars = LX.map((x, i) => rect(left, i < 3 ? "var(--nm-orange)" : i < 5 ? "var(--nm-teal)" : "var(--nm-total)"));
  [["O", "kinetic"], ["C", "kinetic"], ["O", "kinetic"], ["bond 1", "spring"], ["bond 2", "spring"], ["total", ""]]
    .forEach(([a, b], i) => barLabel(left, LX[i] + 15, a, b));
  const RX = [70, 170, 270];                                        // right: symmetric, antisymmetric, total
  const rightBars = [[rect(right, "var(--nm-teal)"), rect(right, "var(--nm-orange)")],
    [rect(right, "var(--nm-teal)"), rect(right, "var(--nm-orange)")], [rect(right, "var(--nm-total)")]];
  rightBars.forEach((pair) => pair.forEach((r) => r.setAttribute("width", 52)));
  [["symmetric", "mode"], ["antisymmetric", "mode"], ["total", ""]].forEach(([a, b], i) => barLabel(right, RX[i] + 26, a, b));
  const setBar = (r, x, y0, frac) => {                              // a bar from height y0 (fraction) up by frac
    const h = Math.max(0, frac) * BMAX;
    r.setAttribute("x", x); r.setAttribute("y", BASE - (y0 * BMAX) - h); r.setAttribute("height", h);
  };

  // ---------------------------------------------------------------- state and motion
  const amp = { s: 0, a: 0 };
  let t = 0, timer = null, running = false, last = 0;

  const draw = () => {
    const cs = Math.cos(W_S * t), ca = Math.cos(W_A * t), ss = Math.sin(W_S * t), sa = Math.sin(W_A * t);
    const Qs = amp.s * cs, Qa = amp.a * ca, Ps = -amp.s * W_S * ss, Pa = -amp.a * W_A * sa;
    const x = [0, 1, 2].map((i) => (Qs * U_S[i] + Qa * U_A[i]) / SQ[i]);
    const ke = [0, 1, 2].map((i) => 0.5 * (Ps * U_S[i] + Pa * U_A[i]) ** 2);
    const pe = [0.5 * K * (x[1] - x[0]) ** 2, 0.5 * K * (x[2] - x[1]) ** 2];
    const E = 0.5 * W_S ** 2 * amp.s ** 2 + 0.5 * W_A ** 2 * amp.a ** 2;
    const px = X0.map((x0, i) => x0 + PX * x[i]);
    atoms.forEach((c, i) => c.setAttribute("cx", px[i]));
    labels.forEach((l, i) => l.setAttribute("x", px[i]));
    bonds.forEach((b, i) => { b.setAttribute("x1", px[i]); b.setAttribute("x2", px[i + 1]); });
    const f = E > 1e-12 ? 1 / E : 0;
    [...ke, ...pe, E].forEach((v, i) => setBar(leftBars[i], LX[i], 0, v * f));
    const modes = [[0.5 * W_S ** 2 * Qs ** 2, 0.5 * Ps ** 2], [0.5 * W_A ** 2 * Qa ** 2, 0.5 * Pa ** 2]];
    modes.forEach(([v, k], j) => { setBar(rightBars[j][0], RX[j], 0, v * f); setBar(rightBars[j][1], RX[j], v * f, k * f); });
    setBar(rightBars[2][0], RX[2], 0, E * f);
  };

  const tick = () => {
    const now = performance.now();
    t += Math.min(now - last, 100) / 1000 * TSCALE;
    last = now;
    draw();
    timer = setTimeout(tick, FRAME);
  };
  function start() { if (running) return; running = true; pauseBtn.textContent = "pause"; last = performance.now(); timer = setTimeout(tick, FRAME); }
  function stop() { running = false; pauseBtn.textContent = "play"; if (timer) clearTimeout(timer); timer = null; }

  function setAmps(s, a) {
    amp.s = s; amp.a = a; t = 0;                                     // released from rest
    sliders.s.input.value = s; sliders.a.input.value = a;
    sliders.s.val.textContent = s.toFixed(2); sliders.a.val.textContent = a.toFixed(2);
    const one = Math.abs(s) < 0.025 || Math.abs(a) < 0.025;
    status.textContent = s === 0 && a === 0 ? "Set a slider or press a preset." :
      one ? "One mode only: every atom moves at one frequency, in a fixed pattern, and the energy split between atoms repeats." :
      "Both modes: the energy of each atom and spring wanders, but each mode keeps its own total. No energy passes between modes.";
    draw();
    start();
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("nm-dark")) root.classList.toggle("nm-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  setAmps(PULL[0], PULL[1]);
  syncDark();
  return () => { stop(); if (obs) obs.disconnect(); };
}

export default { render };
