// How temperature shapes a rotational spectrum.
//
// Left: the populations N_J / N of the rotational levels of v = 0, as bars (the most populated level purple). Right:
// the spectrum those populations make, as sticks scaled to the strongest line. "microwave" is pure rotation,
// J -> J + 1 in v = 0 (purple sticks). "infrared" is the fundamental band v = 0 -> 1: the P branch (teal, J -> J - 1)
// below the band origin, the R branch (orange, J -> J + 1) above it, and no Q line at the origin itself. HCl shows
// H35Cl and H37Cl (natural abundance 76 : 24, the lighter shade), so every HCl line is a doublet; CO and HBr show one
// isotopologue. "rigid rotor" sets B0 = B1 = Be and D = 0; "real molecule" uses the measured B0, B1 and D, so the R
// lines crowd together and the P lines spread apart (B1 < B0) and the high-J levels sag (centrifugal stretching).
//
// Wavenumbers in cm^-1, hc/k_B = 1.438777 cm K, term values F_v(J) = B_v J(J+1) - D J^2 (J+1)^2.
//   populations   N_J / N = (2J + 1) exp(-hc F_0(J) / k_B T) / q, q summed to J = 120
//   infrared      R(J) = nu0 + F_1(J + 1) - F_0(J), P(J) = nu0 + F_1(J - 1) - F_0(J); strength (J + 1) for R(J) and J
//                 for P(J) (Honl-London factors, the 2J + 1 cancels) times exp(-hc F_0(J) / k_B T) / q
//   microwave     J -> J + 1 at F_0(J + 1) - F_0(J); strength nu (J + 1) exp(-hc F_0(J) / k_B T) (1 - exp(-hc nu / k_B T)) / q,
//                 the photon energy times the absorption left over after stimulated emission
// Each molecule keeps one wavenumber window per spectrum, wide enough for every line of its J range in both models, so
// the axis stays put while T changes or the model is toggled.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch04/05), in a reveal.js deck through a module-script loader, and in Jupyter or
// Colab through the anywidget package. No dependencies. Model keys, optional: fontSize (CSS size), molecule ("HCl",
// "CO" or "HBr"), mode ("infrared" or "microwave"), T (kelvin, 10 to 1500, default 300), real (false starts on the
// rigid rotor), status (false hides the status line). spectrum() and windowOf() are exported for tests.

const TEAL = "#107895", ORANGE = "#e07b00", PURPLE = "#6a3d9a", GRAY = "#6c757d";
const SVGNS = "http://www.w3.org/2000/svg";

// ------------------------------------------------------------------ physics
const HCK = 1.438777;                                                // hc / k_B, cm K
const QJ = 120;                                                      // the partition function is summed to here
const TMIN = 10, TMAX = 1500, STEPS = 1000;                          // log temperature slider

// ab = natural abundance; nu0 = band origin; Be, B0, B1 and D in cm^-1. Jmax = the J range shown; Jstep = J ticks;
// ir = the J of the outer P and R labels; mw = how many of the first visible microwave lines get a J -> J + 1 label.
const MOLECULES = {
  HCl: { Jmax: 20, Jstep: 5, ir: 7, mw: 3, iso: [
    { ab: 0.7576, nu0: 2885.98, Be: 10.593, B0: 10.440, B1: 10.136, D: 5.3e-4 },          // H35Cl
    { ab: 0.2424, nu0: 2883.88, Be: 10.577, B0: 10.424, B1: 10.121, D: 5.3e-4 },          // H37Cl
  ] },
  CO: { Jmax: 45, Jstep: 10, ir: 15, mw: 2, iso: [
    { ab: 1, nu0: 2143.27, Be: 1.9313, B0: 1.9225, B1: 1.9050, D: 6.1e-6 },               // 12C16O
  ] },
  HBr: { Jmax: 20, Jstep: 5, ir: 7, mw: 3, iso: [
    { ab: 1, nu0: 2558.53, Be: 8.465, B0: 8.348, B1: 8.115, D: 3.5e-4 },                  // H79Br
  ] },
};
const NAMES = ["HCl", "CO", "HBr"];

const F = (B, D, J) => { const x = J * (J + 1); return B * x - D * x * x; };
const consts = (c, real) => (real ? { B0: c.B0, B1: c.B1, D: c.D } : { B0: c.Be, B1: c.Be, D: 0 });

function partition(B, D, kT) {
  let q = 0, last = -1;
  for (let J = 0; J <= QJ; J++) {
    const f = F(B, D, J);
    if (f < last) break;                                             // the D series has turned over: no physics past here
    q += (2 * J + 1) * Math.exp(-f / kT);
    last = f;
  }
  return q;
}

// Populations of v = 0 for J = 0..Jmax (main isotopologue) and every line of the J range, heights h scaled to the
// strongest line. branch: "R", "P" or "M" (microwave); J is the lower level; iso 0 is the main isotopologue.
export function spectrum(molecule, mode, T, real) {
  const m = MOLECULES[molecule], kT = T / HCK, lines = [];
  let pops = [];
  m.iso.forEach((c, k) => {
    const { B0, B1, D } = consts(c, real), q = partition(B0, D, kT);
    const boltz = (J) => Math.exp(-F(B0, D, J) / kT) / q;
    if (k === 0) pops = Array.from({ length: m.Jmax + 1 }, (_, J) => (2 * J + 1) * boltz(J));
    for (let J = 0; J <= m.Jmax; J++) {
      if (mode === "infrared") {
        lines.push({ branch: "R", J, iso: k, nu: c.nu0 + F(B1, D, J + 1) - F(B0, D, J), s: c.ab * (J + 1) * boltz(J) });
        if (J > 0) lines.push({ branch: "P", J, iso: k, nu: c.nu0 + F(B1, D, J - 1) - F(B0, D, J), s: c.ab * J * boltz(J) });
      } else {
        const nu = F(B0, D, J + 1) - F(B0, D, J);
        lines.push({ branch: "M", J, iso: k, nu, s: c.ab * nu * (J + 1) * boltz(J) * (1 - Math.exp(-nu / kT)) });
      }
    }
  });
  const top = lines.reduce((a, l) => Math.max(a, l.s), 0);
  lines.forEach((l) => { l.h = l.s / top; });
  return { pops, lines };
}

// The wavenumber window [lo, hi] of one molecule and spectrum: every line of the J range, rigid and real.
const WINDOWS = {};
export function windowOf(molecule, mode) {
  const key = `${molecule} ${mode}`;
  if (WINDOWS[key]) return WINDOWS[key];
  let lo = Infinity, hi = -Infinity;
  [true, false].forEach((real) => spectrum(molecule, mode, 300, real).lines.forEach((l) => {
    lo = Math.min(lo, l.nu); hi = Math.max(hi, l.nu);
  }));
  const pad = 0.03 * (hi - lo);
  WINDOWS[key] = mode === "microwave" ? [0, Math.ceil(1.04 * hi / 5) * 5]
    : [Math.floor((lo - pad) / 10) * 10, Math.ceil((hi + pad) / 10) * 10];
  return WINDOWS[key];
}

// ------------------------------------------------------------------ drawing
const W = 1000, H = 306;
const PT = 46, PB = 254;                                             // plot top and baseline, both panels
const AL = 72, AR = 324;                                             // population panel
const BL = 396, BR = 988;                                            // spectrum panel
const FT = 18, FA = 19, FL = 18;                                     // font sizes: ticks, axis titles, line labels
const STICK = 2.4;

const CSS = `
.rs-root { --rs-fg: #212529; --rs-muted: ${GRAY}; --rs-border: #ced4da; --rs-btn: #f8f9fa; --rs-card: #ffffff;
  --rs-teal: ${TEAL}; --rs-orange: ${ORANGE}; --rs-purple: ${PURPLE}; --rs-on: #e7f1f4;
  --rs-teal2: #93c2cf; --rs-orange2: #f1c48c; --rs-purple2: #bca8d2; --rs-bar: #d3c3e6; --rs-axis: #868e96;
  color: var(--rs-fg); background: var(--rs-card); border: 1px solid var(--rs-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.rs-root.rs-dark { --rs-fg: #e9ecef; --rs-muted: #adb5bd; --rs-border: #495057; --rs-btn: #2b3035; --rs-card: #1e2125;
  --rs-teal: #45a9c6; --rs-orange: #f59f3a; --rs-purple: #b08be0; --rs-on: #1f3a44;
  --rs-teal2: #2f6474; --rs-orange2: #87602f; --rs-purple2: #635281; --rs-bar: #54456b; --rs-axis: #868e96; }
.rs-root sub { font-size: 0.72em; line-height: 0; vertical-align: -0.25em; }
.rs-acc { position: relative; display: inline-block; }
.rs-acc::after { content: "~"; position: absolute; left: 0; right: 0; top: -0.5em; text-align: center; font-weight: 400; }
.rs-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.45em 1.2em; margin: 0 0 0.35em; }
.rs-btns { display: flex; flex-wrap: wrap; gap: 0.35em; }
.rs-btn { font: inherit; color: var(--rs-fg); background: var(--rs-btn); border: 1px solid var(--rs-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.rs-btn:hover { border-color: var(--rs-teal); }
.rs-btn.rs-active { border-color: var(--rs-teal); background: var(--rs-on); font-weight: 600; }
.rs-slider { display: flex; align-items: center; gap: 0.5em; margin: 0; color: var(--rs-muted); }
.rs-slider input { width: 12em; accent-color: ${TEAL}; margin: 0; }
.rs-val { font-variant-numeric: tabular-nums; min-width: 3.6em; color: var(--rs-fg); font-weight: 600; }
.rs-plot { display: block; width: 100%; height: auto; max-width: 100%; max-height: none; margin: 0; }
.rs-plot text { font-family: inherit; fill: var(--rs-fg); }
.rs-status { font-weight: 600; margin: 0.25em 0 0; min-height: 1.4em; }
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

function txt(parent, x, y, s, size, fill, attrs = {}) {
  const t = svg("text", { x, y, "font-size": size, style: `fill: ${fill}`, ...attrs }, parent);
  t.textContent = s;
  return t;
}

// Text width estimate in em (no layout needed, so it works in hidden slides): Helvetica-like advance widths.
const CW = { " ": 0.28, "(": 0.34, ")": 0.34, "→": 1.0, "=": 0.6, P: 0.67, R: 0.72, J: 0.5, Q: 0.78, l: 0.23, i: 0.23 };
const textW = (s, size) => [...s].reduce((w, c) => w + (CW[c] ?? 0.57), 0) * size * 1.04;

// Steps for the axes: a few round ticks across the window; a round top for the population bars.
function ticks(lo, hi) {
  for (const s of [5, 10, 20, 25, 50, 100, 200, 250, 500]) {
    const a = Math.ceil(lo / s), b = Math.floor(hi / s);
    if (b - a + 1 <= 6) return Array.from({ length: b - a + 1 }, (_, i) => (a + i) * s);
  }
  return [lo, hi];
}
function popAxis(pmax) {
  for (const s of [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.25]) {
    const n = Math.ceil(pmax / s - 1e-9);
    if (n <= 4) return { top: n * s, step: s, n };
  }
  return { top: 1, step: 0.25, n: 4 };
}
const frac = (v, s) => (v === 0 ? "0" : v.toFixed(s < 0.01 ? 3 : s < 0.1 || s === 0.25 ? 2 : 1).replace(/\.?0+$/, ""));
const ratioText = (r) => (r >= 10 ? String(Math.round(r)) : r >= 1 ? r.toFixed(1) : r.toFixed(2));
const snapT = (T) => { const e = 10 ** (Math.floor(Math.log10(T)) - 1); return Math.round(T / e) * e; };
const lineName = (l) => (l.branch === "M" ? `${l.J} → ${l.J + 1}` : `${l.branch}(${l.J})`);
const tOf = (u) => TMIN * (TMAX / TMIN) ** (u / STEPS);
const uOf = (T) => STEPS * Math.log(T / TMIN) / Math.log(TMAX / TMIN);

// Line labels, in order of importance: each goes as low as it can above its own line, clear of every stick under it
// and of the labels already placed (and of any fixed box, like "no Q line"). A centered label may instead sit to the
// right or the left of its line when that keeps it clearly lower. A label lifted well above its line gets a dotted
// leader; a label with no room left is dropped.
function placeLabels(cands, sticks, fixed) {
  const boxes = fixed.slice(), out = [];
  const asc = 0.74 * FL, desc = 0.24 * FL;
  const spot = (c, anchor, w) => {
    const want = anchor === "middle" ? c.x - w / 2 : anchor === "end" ? c.x - 5 - w : c.x + 5;
    const x0 = Math.max(BL - 10, Math.min(BR + 10 - w, want)), x1 = x0 + w;
    if (anchor !== "middle" && x0 !== want) return null;            // a side label pushed off its line is no use
    let y = c.top - desc - 3;
    sticks.forEach((s) => { if (s.x > x0 - 2.5 && s.x < x1 + 2.5) y = Math.min(y, s.top - desc - 3); });
    for (let again = true; again;) {
      again = false;
      boxes.forEach((b) => {
        if (x0 < b.x1 + 4 && x1 > b.x0 - 4 && y + desc > b.y - asc - 2 && y - asc < b.y + desc + 2) {
          y = b.y - asc - desc - 3; again = true;
        }
      });
    }
    return y - asc < 1 ? null : { x0, x1, y, anchor };
  };
  for (const c of cands) {
    const w = textW(c.text, FL);
    let best = null;
    (c.anchor === "middle" ? ["middle", "start", "end"] : [c.anchor]).forEach((a) => {
      const s = spot(c, a, w);
      if (s && (!best || s.y > best.y + (best.anchor === "middle" ? 6 : 0))) best = s;
    });
    if (!best) continue;
    boxes.push(best);
    out.push({ ...c, x0: best.x0, x1: best.x1, y: best.y, lift: c.top - desc - 3 - best.y });
  }
  return out;
}

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };
  const flag = (v) => !(v === false || v === 0 || v === "false" || v === "0");
  const pick = (v, keys, d) => keys.find((k) => k.toLowerCase() === String(v).toLowerCase()) || d;

  let molecule = pick(get("molecule", "HCl"), NAMES, "HCl");
  let mode = pick(get("mode", "infrared"), ["infrared", "microwave"], "infrared");
  let real = flag(get("real", true));
  let T = Math.round(Math.min(TMAX, Math.max(TMIN, +get("T", 300) || 300)));

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "rs-root", el);
  root.setAttribute("data-prevent-swipe", "");                       // reveal.js: drags must not change slides
  const fs = get("fontSize", "15px");
  root.style.fontSize = /^\d+(\.\d+)?$/.test(String(fs)) ? `${fs}px` : fs;    // a bare number means px

  const controls = html("div", "rs-controls", root);
  const pill = (group, label, act) => {
    const b = html("button", "rs-btn", group, label); b.type = "button";
    b.addEventListener("click", () => { b.blur(); act(); update(); });
    return b;
  };
  const g1 = html("div", "rs-btns", controls), g2 = html("div", "rs-btns", controls), g3 = html("div", "rs-btns", controls);
  const molBtns = NAMES.map((k) => [k, pill(g1, k, () => { molecule = k; })]);
  const modeBtns = ["microwave", "infrared"].map((k) => [k, pill(g2, k, () => { mode = k; })]);
  const realBtns = [[false, "rigid rotor"], [true, "real molecule"]].map(([k, s]) => [k, pill(g3, s, () => { real = k; })]);
  const box = html("label", "rs-slider", controls);
  html("span", null, box, "temperature");
  const input = html("input", null, box);
  input.type = "range"; input.min = 0; input.max = STEPS; input.step = 1; input.value = uOf(T);
  input.setAttribute("aria-label", "temperature");
  const readout = html("span", "rs-val", box);
  input.addEventListener("input", () => { T = snapT(tOf(+input.value)); update(); });
  input.addEventListener("change", () => input.blur());             // arrow keys go back to the deck

  const plot = svg("svg", { viewBox: `0 0 ${W} ${H}`, class: "rs-plot", role: "img",
    "aria-label": "populations of the rotational levels beside the rotational spectrum they produce" }, root);
  const gl = svg("g", {}, plot), gr = svg("g", {}, plot);
  const status = html("div", "rs-status", root);
  if (!flag(get("status", true))) status.style.display = "none";

  // ---------------------------------------------------------------- populations
  function drawPops(m, pops, jpk) {
    gl.textContent = "";
    const n = pops.length, slot = (AR - AL) / n, bw = Math.max(2, 0.72 * slot);
    const bx = (J) => AL + (J + 0.5) * slot;
    const ax = popAxis(pops[jpk]), Y = (p) => PB - (p / ax.top) * (PB - PT);
    for (let i = 0; i <= ax.n; i++) {
      const y = Y(i * ax.step);
      svg("line", { x1: AL - 6, x2: AL, y1: y, y2: y, stroke: "var(--rs-axis)", "stroke-width": 1.2 }, gl);
      txt(gl, AL - 10, y + 6, frac(i * ax.step, ax.step), FT, "var(--rs-muted)", { "text-anchor": "end" });
    }
    pops.forEach((p, J) => {
      const y = Y(p);
      svg("rect", { x: bx(J) - bw / 2, y, width: bw, height: Math.max(0, PB - y),
        fill: J === jpk ? "var(--rs-purple)" : "var(--rs-bar)" }, gl);
    });
    svg("line", { x1: AL, x2: AL, y1: PT - 4, y2: PB, stroke: "var(--rs-axis)", "stroke-width": 1.2 }, gl);
    svg("line", { x1: AL, x2: AR, y1: PB, y2: PB, stroke: "var(--rs-axis)", "stroke-width": 1.2 }, gl);
    for (let J = 0; J <= m.Jmax; J += m.Jstep) {
      svg("line", { x1: bx(J), x2: bx(J), y1: PB, y2: PB + 6, stroke: "var(--rs-axis)", "stroke-width": 1.2 }, gl);
      txt(gl, bx(J), PB + 22, String(J), FT, "var(--rs-muted)", { "text-anchor": "middle" });
    }
    txt(gl, (AL + AR) / 2, PB + 46, "J", FA, "var(--rs-muted)", { "text-anchor": "middle", "font-style": "italic" });
    const yc = (PT + PB) / 2;
    txt(gl, 18, yc, "population", FA, "var(--rs-muted)", { "text-anchor": "middle", transform: `rotate(-90 18 ${yc})` });
    const s = `J = ${jpk}`, w = textW(s, FA);
    const cx = Math.max(AL + w / 2 + 2, Math.min(AR - w / 2, bx(jpk)));
    txt(gl, cx, Y(pops[jpk]) - 8, s, FA, "var(--rs-purple)", { "text-anchor": "middle", "font-weight": 700 });
  }

  // ---------------------------------------------------------------- spectrum
  function drawSpectrum(m, lines, best) {
    gr.textContent = "";
    const [lo, hi] = windowOf(molecule, mode);
    const X = (nu) => BL + ((nu - lo) / (hi - lo)) * (BR - BL), Y = (h) => PB - h * (PB - PT);
    ticks(lo, hi).forEach((v) => {
      svg("line", { x1: X(v), x2: X(v), y1: PB, y2: PB + 6, stroke: "var(--rs-axis)", "stroke-width": 1.2 }, gr);
      txt(gr, X(v), PB + 22, String(v), FT, "var(--rs-muted)", { "text-anchor": "middle" });
    });
    txt(gr, (BL + BR) / 2, PB + 46, "wavenumber (cm⁻¹)", FA, "var(--rs-muted)", { "text-anchor": "middle" });
    const yc = (PT + PB) / 2;
    txt(gr, BL - 20, yc, "relative intensity", FA, "var(--rs-muted)",
      { "text-anchor": "middle", transform: `rotate(-90 ${BL - 20} ${yc})` });

    const fixed = [];
    if (mode === "infrared") {                                        // the band origin
      const x = X(m.iso[0].nu0), s = "no Q line", w = textW(s, 16);
      svg("line", { x1: x, x2: x, y1: PB, y2: 23, stroke: "var(--rs-muted)", "stroke-width": 1.4, "stroke-dasharray": "5 4" }, gr);
      txt(gr, x, 17, s, 16, "var(--rs-muted)", { "text-anchor": "middle" });
      fixed.push({ x0: x - w / 2, x1: x + w / 2, y: 17 });
    }

    const hue = (l) => (l.branch === "P" ? "teal" : l.branch === "R" ? "orange" : "purple");
    const sticks = [];
    lines.slice().sort((a, b) => b.iso - a.iso).forEach((l) => {     // the lighter isotopologue goes behind
      const x = X(l.nu);
      if (x < BL - 1 || x > BR + 1) return;
      const y = Y(l.h);
      svg("line", { x1: x, x2: x, y1: PB, y2: y, stroke: `var(--rs-${hue(l)}${l.iso ? "2" : ""})`, "stroke-width": STICK }, gr);
      sticks.push({ x, top: y });
    });
    svg("line", { x1: BL, x2: BR, y1: PB, y2: PB, stroke: "var(--rs-axis)", "stroke-width": 1.2 }, gr);

    // labels, most important first: R(0) and P(1) flank the gap, one more line out in each branch; in microwave the
    // first visible lines, then the strongest line (the one the status line names)
    const main = lines.filter((l) => l.iso === 0), seen = (l) => l.h >= 0.015;
    const find = (branch, J) => main.find((l) => l.branch === branch && l.J === J);
    let cands;
    if (mode === "infrared") {
      cands = [[find("R", 0), "R(0)", "start"], [find("P", 1), "P(1)", "end"],
        [find("R", m.ir), `R(${m.ir})`, "middle"], [find("P", m.ir), `P(${m.ir})`, "middle"]];
    } else {
      const first = main.filter(seen).slice(0, m.mw);
      if (!first.includes(best)) first.push(best);
      cands = first.map((l) => [l, lineName(l), "middle"]);
    }
    const placed = placeLabels(cands.filter(([l]) => l && seen(l)).map(([l, text, anchor]) =>
      ({ text, anchor, x: X(l.nu), top: Y(l.h), hue: hue(l) })), sticks, fixed);
    placed.forEach((p) => {
      const col = `var(--rs-${p.hue})`;
      if (p.lift > 9) {
        const inside = p.x >= p.x0 && p.x <= p.x1;
        svg("line", { x1: p.x, x2: p.x, y1: p.top - 3, y2: inside ? p.y + 0.24 * FL + 1 : p.y - 0.3 * FL,
          stroke: "var(--rs-muted)", "stroke-width": 1, "stroke-dasharray": "2 3" }, gr);
      }
      txt(gr, p.x0, p.y, p.text, FL, col, { "font-weight": 600 });
    });
  }

  // ---------------------------------------------------------------- status
  function verdict(m, pops, jpk, best) {
    const c = m.iso[0], B = real ? c.B0 : c.Be, Bt = (s) => `<span class="rs-acc">B</span>${s}`, sub = real ? "₀" : "";
    const r = `k<sub>B</sub>T/hc${Bt(sub)} = ${ratioText(T / HCK / B)}`;
    const gap = `2${Bt(sub)} = ${(2 * B).toFixed(1)} cm⁻¹`;
    const heights = "heights include the photon energy and stimulated emission";
    if (pops[0] > 0.5) {                                              // cold: the ground level holds most molecules
      return best.J === 0 ? `${T} K: most molecules are still in J = 0 (${r}), so ${lineName(best)} is the strongest line.`
        : `${T} K: most molecules are still in J = 0 (${r}), yet ${lineName(best)} is the strongest line: ${heights}.`;
    }
    const head = `${T} K: J = ${jpk} holds the most molecules (${r})`;
    if (mode === "infrared") {
      return real ? `${head}. The R lines crowd together and the P lines spread apart: the bond is longer on average in v = 1 (${Bt("₁")} &lt; ${Bt("₀")}).`
        : `${head}; lines are ${gap} apart.`;
    }
    const tail = best.J > jpk ? ` The strongest is ${lineName(best)}, not ${jpk} → ${jpk + 1}: ${heights}.`
      : ` ${heights[0].toUpperCase()}${heights.slice(1)}.`;
    return `${head}; lines are ${gap} apart.${tail}`;
  }

  function update() {
    molBtns.forEach(([k, b]) => b.classList.toggle("rs-active", k === molecule));
    modeBtns.forEach(([k, b]) => b.classList.toggle("rs-active", k === mode));
    realBtns.forEach(([k, b]) => b.classList.toggle("rs-active", k === real));
    readout.textContent = `${T} K`;
    const m = MOLECULES[molecule], { pops, lines } = spectrum(molecule, mode, T, real);
    let jpk = 0;
    pops.forEach((p, J) => { if (p > pops[jpk]) jpk = J; });
    const best = lines.filter((l) => l.iso === 0).reduce((a, l) => (l.h > a.h ? l : a));
    drawPops(m, pops, jpk);
    drawSpectrum(m, lines, best);
    status.innerHTML = verdict(m, pops, jpk, best);
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("rs-dark")) root.classList.toggle("rs-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  update();
  syncDark();
  return () => { if (obs) obs.disconnect(); };
}

export default { render };
