// The transition dipole as an antenna: a harmonic bond in the superposition (psi_0 + psi_v')/sqrt(2), and a
// dipole function M(x) built from three switchable terms.
//
// Units hbar = mu = omega = 1, x in units of 1/sqrt(alpha) (Lecture 4.2). M(x) = M_e + M'x + (1/2)M''x^2 with
// M_e = 1, M' = 0.6, (1/2)M'' = 0.2. Buttons pick v' = 1, 2 or 3; toggles switch each term of M(x) on or off.
// Left panel: the density |Psi(x, t)|^2 (teal) and the dipole function M(x) (orange), whose product, integrated,
// is <M>(t). Middle: the swing of <M>(t) about its average, whose amplitude is exactly <v'|M|0> (both coefficients
// are 1/sqrt(2)). Right: the strength |<v'|M|0>|^2 of the lines 0 -> 1, 2, 3, scaled so the fundamental with the
// slope on is 1. Teaches: a constant dipole does nothing (orthogonality), the slope drives 0 -> 1, the curvature
// 0 -> 2, and nothing in a harmonic bond reaches 0 -> 3.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch04/03), in a reveal.js deck through a module-script loader, and in Jupyter or
// Colab through the anywidget package. No dependencies. Model keys, optional: fontSize (CSS size), status (false
// hides the one-line verdict under the panels).

const TEAL = "#107895", ORANGE = "#e07b00", PURPLE = "#6a3d9a";
const SVGNS = "http://www.w3.org/2000/svg";

// physics
const TERMS = { c: 1.0, l: 0.6, q: 0.2 };                          // M_e, M', M''/2
const NX = 401, XMAX = 5;
const XS = Array.from({ length: NX }, (_, i) => -XMAX + (2 * XMAX * i) / (NX - 1));
const DX = XS[1] - XS[0];
const NV = 4;                                                      // states v = 0..3
const PSI = (() => {
  const p = [XS.map((x) => Math.PI ** -0.25 * Math.exp((-x * x) / 2))];
  p.push(XS.map((x, i) => Math.SQRT2 * x * p[0][i]));
  for (let v = 1; v < NV - 1; v++) {
    p.push(XS.map((x, i) => Math.sqrt(2 / (v + 1)) * x * p[v][i] - Math.sqrt(v / (v + 1)) * p[v - 1][i]));
  }
  return p;
})();
const REF = (TERMS.l * Math.SQRT1_2) ** 2;                         // the fundamental with the slope on: a full bar
const PERIOD = 2.4;                                                // real seconds per vibration period
const FRAME = 33;                                                  // ms

// drawing
const SW = 300, SH = 190, SB = 168;                                // state panel, density baseline
const sx = (x) => 14 + ((x + 4) / 8) * 272;
const sy = (d) => SB - d * 150;
const my = (m) => 140 - m * 27;                                    // M(x), its own vertical scale
const TW = 236, TH = 190, TC = 92;                                 // trace panel, center line
const tx = (s) => 14 + s * 214;                                    // s = fraction of the two-period window
const ty = (m) => TC - m * 120;
const BW = 186, BH = 190, BB = 140, BMAX = 104;                    // bar panel
const BX = [22, 80, 138];

const CSS = `
.td-root { --td-fg: #212529; --td-muted: #6c757d; --td-border: #ced4da; --td-btn: #f8f9fa; --td-card: #ffffff;
  --td-teal: ${TEAL}; --td-orange: ${ORANGE}; --td-purple: ${PURPLE}; --td-ghost: #e9ecef; --td-faint: #f3d9b8;
  --td-on: #e3f1f5;
  color: var(--td-fg); background: var(--td-card); border: 1px solid var(--td-border); border-radius: 10px;
  padding: 0.8em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.td-root.td-dark { --td-fg: #e9ecef; --td-muted: #adb5bd; --td-border: #495057; --td-btn: #2b3035; --td-card: #1e2125;
  --td-teal: #45a9c6; --td-orange: #f59f3a; --td-purple: #b08be0; --td-ghost: #343a40; --td-faint: #6b4a22;
  --td-on: #173a45; }
.td-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.35em; margin: 0 0 0.45em; }
.td-label { color: var(--td-muted); margin-right: 0.3em; }
.td-btn { font: inherit; color: var(--td-fg); background: var(--td-btn); border: 1px solid var(--td-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.td-btn:hover { border-color: var(--td-teal); }
.td-btn.td-on { background: var(--td-on); border-color: var(--td-teal); color: var(--td-teal); font-weight: 600; }
.td-panels { display: flex; flex-wrap: wrap; gap: 0.6em 1.1em; margin-top: 0.3em; }
.td-panel { display: flex; flex-direction: column; min-width: 10em; }
.td-p1 { flex: 1.3 1 17em; } .td-p2 { flex: 1 1 13em; } .td-p3 { flex: 0.8 1 10.5em; }
.td-head { font-weight: 600; }
.td-eq { color: var(--td-muted); margin: 0.1em 0 0.2em; }
.td-svg { display: block; width: 100%; height: auto; margin-top: auto; }
.td-p1 .td-svg { max-width: 26em; } .td-p2 .td-svg { max-width: 20em; } .td-p3 .td-svg { max-width: 16em; }
.td-svg text { font-family: inherit; fill: var(--td-fg); }
.td-status { font-weight: 600; margin: 0.45em 0 0; min-height: 1.4em; }
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

function txt(parent, x, y, s, attrs = {}) {
  const t = svg("text", { x, y, "font-size": 12.5, ...attrs }, parent);
  t.textContent = s;
  return t;
}

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "td-root", el);
  root.setAttribute("data-prevent-swipe", "");
  root.style.fontSize = get("fontSize", "15px");

  const button = (row, label, act) => {
    const b = html("button", "td-btn", row, label); b.type = "button";
    b.addEventListener("click", () => { b.blur(); act(); });
    return b;
  };
  const row1 = html("div", "td-row", root);
  html("span", "td-label", row1, "superposition of v = 0 and");
  const vBtns = [1, 2, 3].map((v) => button(row1, `v′ = ${v}`, () => { vp = v; refresh(); }));
  const row2 = html("div", "td-row", root);
  html("span", "td-label", row2, "dipole M(x) =");
  const tBtns = {
    c: button(row2, "Mₑ", () => toggle("c")),
    l: button(row2, "+ M′x", () => toggle("l")),
    q: button(row2, "+ ½M″x²", () => toggle("q")),
  };
  const pauseBtn = button(row2, "pause", () => { running ? stop() : start(); });
  pauseBtn.style.marginLeft = "0.8em";

  const panels = html("div", "td-panels", root);
  const panel = (cls, head, eq, w, h, label) => {
    const p = html("div", `td-panel ${cls}`, panels);
    html("div", "td-head", p, head);
    const e = html("div", "td-eq", p, eq);
    const s = svg("svg", { viewBox: `0 0 ${w} ${h}`, class: "td-svg", role: "img", "aria-label": label }, p);
    return [s, e];
  };
  const [ps] = panel("td-p1", "The state and the dipole", "⟨M⟩(t) = ∫ M(x) |Ψ(x, t)|² dx", SW, SH,
    "probability density of the superposition and the dipole function");
  const [pt, teq] = panel("td-p2", "The dipole swings", "", TW, TH, "the oscillating part of the average dipole");
  const [pb] = panel("td-p3", "Lines from v = 0", "strength ∝ |⟨v′|M|0⟩|²", BW, BH, "line strengths");
  const status = html("div", "td-status", root);
  if (get("status", true) === false) status.style.display = "none";

  // state panel
  svg("line", { x1: 8, x2: SW - 8, y1: SB, y2: SB, stroke: "var(--td-muted)", "stroke-width": 1 }, ps);
  txt(ps, SW / 2, SB + 16, "stretch x", { "text-anchor": "middle", style: "fill: var(--td-muted)" });
  const fill = svg("path", { fill: "var(--td-teal)", "fill-opacity": 0.22, stroke: "none" }, ps);
  const dline = svg("path", { fill: "none", stroke: "var(--td-teal)", "stroke-width": 2.2 }, ps);
  const mline = svg("path", { fill: "none", stroke: "var(--td-orange)", "stroke-width": 2.4 }, ps);
  const mlab = txt(ps, 0, 0, "M(x)", { style: "fill: var(--td-orange)", "font-weight": 600 });
  txt(ps, 14, 40, "|Ψ|²", { style: "fill: var(--td-teal)", "font-weight": 600 });

  // trace panel
  svg("line", { x1: tx(0), x2: tx(1), y1: TC, y2: TC, stroke: "var(--td-muted)", "stroke-width": 1 }, pt);
  const ghost = svg("path", { fill: "none", stroke: "var(--td-faint)", "stroke-width": 2 }, pt);
  const trace = svg("path", { fill: "none", stroke: "var(--td-orange)", "stroke-width": 2.6 }, pt);
  const tdot = svg("circle", { r: 4.5, fill: "var(--td-orange)" }, pt);
  txt(pt, TW / 2, TH - 26, "time, two vibration periods", { "text-anchor": "middle", style: "fill: var(--td-muted)" });
  const amp = txt(pt, TW / 2, TH - 6, "", { "text-anchor": "middle", "font-weight": 600 });

  // bar panel
  const sel = svg("rect", { y: 10, width: 46, height: BB + 44 - 10, rx: 6, fill: "var(--td-ghost)" }, pb);
  svg("line", { x1: 8, x2: BW - 8, y1: BB, y2: BB, stroke: "var(--td-muted)", "stroke-width": 1 }, pb);
  const bars = BX.map((x) => svg("rect", { x: x + 6, width: 34, rx: 2, fill: "var(--td-orange)" }, pb));
  const vals = BX.map((x) => txt(pb, x + 23, 0, "", { "text-anchor": "middle", style: "fill: var(--td-orange)" }));
  const names = BX.map((x, i) => txt(pb, x + 23, BB + 17, `0 → ${i + 1}`, { "text-anchor": "middle" }));
  BX.forEach((x, i) => txt(pb, x + 23, BB + 34, i === 0 ? "at ω" : `at ${i + 1}ω`,
    { "text-anchor": "middle", style: "fill: var(--td-muted)" }));

  // ---------------------------------------------------------------- state
  let vp = 1, t = 0, timer = null, running = false, last = 0;
  const on = { c: true, l: true, q: false };
  let Mx = [], mel = [], A = 0;                                     // M on the grid, <v'|M|0>, amplitude of the swing

  const pathOf = (pts) => pts.map(([a, b], i) => `${i ? "L" : "M"}${a.toFixed(1)},${b.toFixed(1)}`).join("");

  function physics() {
    Mx = XS.map((x) => (on.c ? TERMS.c : 0) + (on.l ? TERMS.l * x : 0) + (on.q ? TERMS.q * x * x : 0));
    mel = [1, 2, 3].map((v) => XS.reduce((s, _, i) => s + PSI[v][i] * Mx[i] * PSI[0][i], 0) * DX);
    A = mel[vp - 1];                                                // 2 c_0 c_v' <v'|M|0> with c = 1/sqrt(2)
  }

  function drawStatic() {
    const pts = [];
    XS.forEach((x, i) => { if (Math.abs(x) <= 3.0) pts.push([sx(x), my(Mx[i])]); });
    mline.setAttribute("d", pathOf(pts));
    const [lx, ly] = pts[pts.length - 1];
    mlab.setAttribute("x", Math.min(lx - 30, SW - 40)); mlab.setAttribute("y", Math.max(14, Math.min(ly - 8, SB - 30)));
    const g = [];
    for (let k = 0; k <= 160; k++) { const s = k / 160; g.push([tx(s), ty(A * Math.cos(vp * s * 4 * Math.PI))]); }
    ghost.setAttribute("d", pathOf(g));
    teq.textContent = `swing of ⟨M⟩(t) = ⟨${vp}|M|0⟩ cos ${vp === 1 ? "" : vp}ωt`;
    amp.textContent = Math.abs(A) < 1e-6 ? "⟨M⟩ never moves" : `amplitude ⟨${vp}|M|0⟩ = ${Math.abs(A).toFixed(2)}`;
    amp.style.fill = Math.abs(A) < 1e-6 ? "var(--td-muted)" : "var(--td-orange)";
    mel.forEach((m, i) => {
      const f = (m * m) / REF, h = Math.min(1.05, f) * BMAX;
      bars[i].setAttribute("y", BB - h); bars[i].setAttribute("height", h);
      vals[i].setAttribute("y", BB - h - 5);
      vals[i].textContent = f < 1e-9 ? "0" : f > 0.995 ? "1" : f.toFixed(2);
      names[i].setAttribute("font-weight", i === vp - 1 ? 700 : 400);
    });
    sel.setAttribute("x", BX[vp - 1]);
    vBtns.forEach((b, i) => b.classList.toggle("td-on", i === vp - 1));
    Object.keys(tBtns).forEach((k) => tBtns[k].classList.toggle("td-on", on[k]));
    status.textContent = verdict();
  }

  function verdict() {
    const moves = Math.abs(A) > 1e-6;
    if (!on.c && !on.l && !on.q) return "M = 0 at every stretch, as for N₂: the light has nothing to push on.";
    if (!on.l && !on.q) return "A constant dipole is the same at every stretch, so moving the density cannot change ⟨M⟩. No line: that is orthogonality.";
    if (vp === 1) return moves
      ? "ψ₀ + ψ₁ sloshes at ω, and the slope of M(x) turns the slosh into a swinging dipole: light at ω drives 0 → 1, the fundamental."
      : "ψ₀ + ψ₁ sloshes, but a symmetric M(x) gains on one side what it loses on the other. 0 → 1 needs the slope M′.";
    if (vp === 2) return moves
      ? "ψ₀ + ψ₂ breathes at 2ω, and the curvature of M(x) feels the width change: light at 2ω drives 0 → 2, a weak overtone."
      : "ψ₀ + ψ₂ breathes with its center fixed, so a straight M(x) never swings: 0 → 2 is forbidden. Turn on the curvature.";
    return "ψ₀ + ψ₃ moves too, but x reaches one rung and x² two, so ⟨3|M|0⟩ = 0. A real 0 → 3 line needs anharmonic states, and is weaker still.";
  }

  function drawFrame() {
    const c = Math.cos(vp * t), p0 = PSI[0], pv = PSI[vp];
    const pts = [];
    XS.forEach((x, i) => {
      if (Math.abs(x) <= 4) pts.push([sx(x), sy(0.5 * (p0[i] * p0[i] + pv[i] * pv[i]) + p0[i] * pv[i] * c)]);
    });
    const d = pathOf(pts);
    dline.setAttribute("d", d);
    fill.setAttribute("d", `${d}L${sx(4)},${SB}L${sx(-4)},${SB}Z`);
    const s = (t % (4 * Math.PI)) / (4 * Math.PI), tr = [];
    for (let k = 0; k <= 160 && k / 160 <= s; k++) { const u = k / 160; tr.push([tx(u), ty(A * Math.cos(vp * u * 4 * Math.PI))]); }
    tr.push([tx(s), ty(A * c)]);
    trace.setAttribute("d", pathOf(tr));
    tdot.setAttribute("cx", tx(s)); tdot.setAttribute("cy", ty(A * c));
  }

  function refresh() { physics(); drawStatic(); drawFrame(); }
  function toggle(k) { on[k] = !on[k]; refresh(); }

  const tick = () => {
    const now = performance.now();
    t += (Math.min(now - last, 100) / 1000) * (2 * Math.PI / PERIOD);
    last = now;
    drawFrame();
    timer = setTimeout(tick, FRAME);
  };
  function start() { if (running) return; running = true; pauseBtn.textContent = "pause"; last = performance.now(); timer = setTimeout(tick, FRAME); }
  function stop() { running = false; pauseBtn.textContent = "play"; if (timer) clearTimeout(timer); timer = null; }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("td-dark")) root.classList.toggle("td-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  refresh();
  syncDark();
  start();
  return () => { stop(); if (obs) obs.disconnect(); };
}

export default { render };
