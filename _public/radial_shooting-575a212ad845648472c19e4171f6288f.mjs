// Shooting the radial equation of the hydrogen atom: tune the energy and watch the tail.
//
// Atomic units (hbar = m_e = e = 4 pi eps0 = 1, so lengths are in a0 and energies in E_h, Z = 1). For a chosen l
// and E the radial equation -u''/2 + (-1/r + l(l+1)/2r^2) u = E u is integrated outward from u(0) = 0 with the
// Numerov recursion. Left: u(r) = r R(r), normalized to its largest value inside the classically allowed region
// (dotted line: the outer turning point, where V_eff = E). At almost every E the tail blows up; only at the
// grid's own eigenvalues, E = -1/2n^2 with n > l, does it die, and then the curve turns teal. Right: the energy
// ladder with the allowed levels of this l and the current E. The buttons jump to a level exactly (the slider can
// only come within a step, and snaps when it is within 0.0015 E_h); "sweep" raises E slowly and pauses on each hit.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch05/01), in a reveal.js deck through a module-script loader, and in Jupyter or
// Colab through the anywidget package. No dependencies. Model keys, optional: fontSize (CSS size), l (0 to 2,
// the angular momentum shown first), energy (the first E), status (false hides the verdict line).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00", PURPLE = "#6a3d9a", GRAY = "#6c757d";
const SVGNS = "http://www.w3.org/2000/svg";

const DR = 0.01, RMAX = 70, N = Math.round(RMAX / DR);               // grid: r_j = (j + 1) dr, j = 0 .. N - 1
const RVIEW = 50;                                                    // r drawn, in a0
const EMIN = -0.62, EMAX = -0.012, ESTEP = 0.0005, SNAP = 0.0015;    // slider range and step, snap radius (E_h)
const LMAX = 2, NMAX = 5;                                            // l buttons, levels on the ladder
const LETTER = "spd";
const LCOL = [TEAL, PURPLE, ORANGE];

// ------------------------------------------------------------------ the radial equation on the grid
const r = new Float64Array(N);
for (let j = 0; j < N; j++) r[j] = (j + 1) * DR;

// outer turning point of V_eff = -1/r + L/r^2 at energy E (L = l(l+1)/2), or null below the bottom of the well
function turning(l, E) {
  const L = l * (l + 1) / 2;
  if (L === 0) return -1 / E;
  const disc = 1 + 4 * E * L;
  return disc < 0 ? null : (1 + Math.sqrt(disc)) / (-2 * E);
}

// near the nucleus u = r^{l+1} (1 - r/(l+1) + ...): the two-term series starts the recursion accurately
const start = (l, rr) => Math.pow(rr, l + 1) * (1 - rr / (l + 1));

// Numerov outward from u(0) = 0; fills u. Returns {rt, cut, nodes}:
// the turning point, the index past which the (normalized) tail was dropped as dead, and the node count.
function shoot(l, E, u) {
  const L = l * (l + 1) / 2, h2 = DR * DR;
  const f = new Float64Array(N);
  for (let j = 0; j < N; j++) f[j] = 1 + h2 * 2 * (E + 1 / r[j] - L / (r[j] * r[j])) / 12;
  u[0] = start(l, r[0]); u[1] = start(l, r[1]);
  for (let j = 1; j < N - 1; j++) u[j + 1] = ((12 - 10 * f[j]) * u[j] - f[j - 1] * u[j - 1]) / f[j + 1];
  const rt = turning(l, E);
  const jt = rt === null ? 0 : Math.min(N - 1, Math.round(rt / DR));
  let m = 0;
  for (let j = 0; j <= Math.max(jt, 10); j++) m = Math.max(m, Math.abs(u[j]));
  for (let j = 0; j < N; j++) u[j] /= m;
  let cut = N;                                                       // beyond the turning point, once |u| < 1e-4: dead
  for (let j = jt + 1; j < N; j++) if (Math.abs(u[j]) < 1e-4) { cut = j; break; }
  for (let j = cut; j < N; j++) u[j] = 0;
  let nodes = 0, last = 0;
  for (let j = 0; j < cut; j++) {
    const s = u[j] > 1e-9 ? 1 : u[j] < -1e-9 ? -1 : 0;
    if (s !== 0 && last !== 0 && s !== last) nodes++;
    if (s !== 0) last = s;
  }
  return { rt, cut, nodes };
}

// the grid's own eigenvalues for each l, by bisection on the sign of the tail (it flips at every level)
const LEVELS = [];
{
  const u = new Float64Array(N);
  const tail = (l, E) => {
    const L = l * (l + 1) / 2, h2 = DR * DR;
    const f = new Float64Array(N);
    for (let j = 0; j < N; j++) f[j] = 1 + h2 * 2 * (E + 1 / r[j] - L / (r[j] * r[j])) / 12;
    u[0] = start(l, r[0]); u[1] = start(l, r[1]);
    const rt = turning(l, E);
    const jend = Math.min(N - 1, Math.round((4 * (rt || 1) + 6) / DR));   // read the sign where round-off is still small
    for (let j = 1; j < jend; j++) u[j + 1] = ((12 - 10 * f[j]) * u[j] - f[j - 1] * u[j - 1]) / f[j + 1];
    return u[jend] > 0 ? 1 : -1;
  };
  for (let l = 0; l <= LMAX; l++) {
    const row = {};
    for (let n = l + 1; n <= NMAX + 1; n++) {
      const E0 = -0.5 / (n * n), d = 0.25 * (0.5 / (n * n) - 0.5 / ((n + 1) * (n + 1)));
      let a = E0 - d, b = E0 + d;
      const sa = tail(l, a);
      if (tail(l, b) === sa) { row[n] = E0; continue; }               // should not happen; keep the exact value
      for (let it = 0; it < 70 && b - a > 1e-13; it++) {
        const c = 0.5 * (a + b);
        if (tail(l, c) === sa) a = c; else b = c;
      }
      row[n] = 0.5 * (a + b);
    }
    LEVELS.push(row);
  }
}

// ------------------------------------------------------------------ drawing
const W = 1000, H = 420;
const PL = 64, PR = 690, PT = 30, PB = 376;                          // u(r) panel
const LX = 790, LW = 110;                                            // ladder: x of the rungs and their width
const ELO = -0.64, EHI = 0.03;                                       // ladder axis
const UMAX = 1.5;                                                    // u axis: -1.5 .. 1.5

const CSS = `
.rs-root { --rs-fg: #212529; --rs-muted: #6c757d; --rs-border: #ced4da; --rs-btn: #f8f9fa; --rs-card: #ffffff;
  --rs-teal: ${TEAL}; --rs-purple: ${PURPLE}; --rs-orange: ${ORANGE}; --rs-red: ${CARDINAL};
  --rs-level: #adb5bd; --rs-zero: #ced4da; --rs-on: #e7f1f4;
  color: var(--rs-fg); background: var(--rs-card); border: 1px solid var(--rs-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.rs-root.rs-dark { --rs-fg: #e9ecef; --rs-muted: #adb5bd; --rs-border: #495057; --rs-btn: #2b3035; --rs-card: #1e2125;
  --rs-teal: #45a9c6; --rs-purple: #b08be0; --rs-orange: #f59f3a; --rs-red: #f05d6f;
  --rs-level: #868e96; --rs-zero: #495057; --rs-on: #1f3a44; }
.rs-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.1em; margin: 0 0 0.3em; }
.rs-group { display: flex; align-items: center; gap: 0.35em; }
.rs-lab { color: var(--rs-muted); }
.rs-btn { font: inherit; color: var(--rs-fg); background: var(--rs-btn); border: 1px solid var(--rs-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.rs-btn:hover { border-color: ${TEAL}; }
.rs-btn:disabled { opacity: 0.4; cursor: default; }
.rs-btn.rs-active { border-color: var(--rs-teal); background: var(--rs-on); font-weight: 600; }
.rs-slider { display: flex; align-items: center; gap: 0.5em; }
.rs-slider input { width: 13em; accent-color: ${TEAL}; }
.rs-val { font-variant-numeric: tabular-nums; min-width: 7.5em; }
.rs-plot { display: block; width: 100%; height: auto; }
.rs-plot text { font-family: inherit; fill: var(--rs-fg); }
.rs-status { font-weight: 600; margin: 0.2em 0 0; min-height: 1.4em; }
.rs-note { color: var(--rs-muted); }
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

const EH = "E<sub>h</sub>";
const fmtE = (E) => (E < 0 ? "−" : "") + Math.abs(E).toFixed(4);
const frac = (n) => (n === 1 ? `−${EH}/2` : `−${EH}/${2 * n * n}`);

// SVG text with a subscript: sub(el, "E", "h") writes E_h
function sub(t, main, s) {
  t.textContent = "";
  const a = document.createElementNS(SVGNS, "tspan"); a.textContent = main; t.appendChild(a);
  const b = document.createElementNS(SVGNS, "tspan"); b.textContent = s;
  b.setAttribute("dy", "0.3em"); b.setAttribute("font-size", "75%"); t.appendChild(b);
  const c = document.createElementNS(SVGNS, "tspan"); c.textContent = "​";
  c.setAttribute("dy", "-0.3em"); t.appendChild(c);
  return t;
}

let uid = 0;

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "rs-root", el);
  root.setAttribute("data-prevent-swipe", "");                       // reveal.js: drags must not change slides
  root.style.fontSize = get("fontSize", "15px");

  const controls = html("div", "rs-controls", root);
  const lgroup = html("div", "rs-group", controls);
  html("span", "rs-lab", lgroup, "l =");
  const lbtns = [];
  for (let l = 0; l <= LMAX; l++) {
    const b = html("button", "rs-btn", lgroup, `${l} (${LETTER[l]})`); b.type = "button";
    b.addEventListener("click", () => { b.blur(); setL(l); });
    lbtns.push(b);
  }
  const box = html("label", "rs-slider", controls);
  html("span", "rs-lab", box, "E");
  const input = html("input", null, box); input.type = "range";
  input.min = EMIN; input.max = EMAX; input.step = ESTEP;
  const readout = html("span", "rs-val", box);
  input.addEventListener("input", () => { stopSweep(); setE(+input.value, true); });
  input.addEventListener("change", () => input.blur());             // arrow keys go back to the deck

  const controls2 = html("div", "rs-controls", root);
  const ngroup = html("div", "rs-group", controls2);
  html("span", "rs-lab", ngroup, "jump to a level:");
  const nbtns = {};
  for (let n = 1; n <= NMAX; n++) {
    const b = html("button", "rs-btn", ngroup, `n = ${n}`); b.type = "button";
    b.addEventListener("click", () => { b.blur(); stopSweep(); setE(LEVELS[curL][n], false); });
    nbtns[n] = b;
  }
  const sweep = html("button", "rs-btn", controls2, "sweep"); sweep.type = "button";
  sweep.addEventListener("click", () => { sweep.blur(); sweeping ? stopSweep() : startSweep(); });

  const plot = svg("svg", { viewBox: `0 0 ${W} ${H}`, class: "rs-plot", role: "img",
    "aria-label": "the radial function u(r) for the chosen energy, beside the ladder of allowed energies" }, root);
  const clipId = `rs-clip-${uid++}`;
  const clip = svg("clipPath", { id: clipId }, svg("defs", {}, plot));
  svg("rect", { x: PL, y: PT, width: PR - PL, height: PB - PT }, clip);

  const X = (rr) => PL + (rr / RVIEW) * (PR - PL);
  const Yu = (v) => (PT + PB) / 2 - (v / UMAX) * (PB - PT) / 2;
  const Ye = (E) => PB - ((E - ELO) / (EHI - ELO)) * (PB - PT);

  // u(r) panel: axes
  svg("line", { x1: PL, x2: PR, y1: Yu(0), y2: Yu(0), stroke: "var(--rs-zero)", "stroke-width": 1.2 }, plot);
  svg("line", { x1: PL, x2: PL, y1: PT, y2: PB, stroke: "var(--rs-muted)", "stroke-width": 1 }, plot);
  svg("line", { x1: PL, x2: PR, y1: PB, y2: PB, stroke: "var(--rs-muted)", "stroke-width": 1 }, plot);
  [-1, 0, 1].forEach((v) => {
    svg("line", { x1: PL - 6, x2: PL, y1: Yu(v), y2: Yu(v), stroke: "var(--rs-muted)", "stroke-width": 1 }, plot);
    const t = svg("text", { x: PL - 10, y: Yu(v) + 5, "text-anchor": "end", "font-size": 14, style: "fill: var(--rs-muted)" }, plot);
    t.textContent = v;
  });
  for (let rr = 0; rr <= RVIEW; rr += 10) {
    svg("line", { x1: X(rr), x2: X(rr), y1: PB, y2: PB + 6, stroke: "var(--rs-muted)", "stroke-width": 1 }, plot);
    const t = svg("text", { x: X(rr), y: PB + 22, "text-anchor": "middle", "font-size": 14, style: "fill: var(--rs-muted)" }, plot);
    t.textContent = rr;
  }
  const xlab = svg("text", { x: (PL + PR) / 2, y: PB + 42, "text-anchor": "middle", "font-size": 15, style: "fill: var(--rs-muted)" }, plot);
  sub(xlab, "r (units of a", "0"); xlab.appendChild(document.createTextNode(")"));
  const ylab = svg("text", { x: 18, y: (PT + PB) / 2, "text-anchor": "middle", "font-size": 15,
    transform: `rotate(-90 18 ${(PT + PB) / 2})`, style: "fill: var(--rs-muted)" }, plot);
  ylab.textContent = "u(r) = r R(r)";
  const g = svg("g", { "clip-path": `url(#${clipId})` }, plot);
  const turn = svg("line", { y1: PT, y2: PB, stroke: "var(--rs-level)", "stroke-width": 1.2, "stroke-dasharray": "3 4" }, g);
  const curve = svg("path", { fill: "none", "stroke-width": 2.6, "stroke-linejoin": "round" }, g);
  const tag = svg("text", { x: PR - 8, y: PT + 20, "text-anchor": "end", "font-size": 16, "font-weight": 600 }, plot);
  const turnLab = svg("text", { y: PT + 16, "font-size": 13, style: "fill: var(--rs-muted)" }, plot);
  turnLab.textContent = "turning point";

  // ladder panel
  const lhead = svg("text", { x: LX + LW / 2, y: PT - 8, "text-anchor": "middle", "font-size": 15, style: "fill: var(--rs-muted)" }, plot);
  sub(lhead, "E (units of E", "h"); lhead.appendChild(document.createTextNode(")"));
  svg("line", { x1: LX - 14, x2: LX - 14, y1: Ye(EHI), y2: Ye(ELO), stroke: "var(--rs-muted)", "stroke-width": 1 }, plot);
  [-0.6, -0.4, -0.2, 0].forEach((E) => {
    svg("line", { x1: LX - 20, x2: LX - 14, y1: Ye(E), y2: Ye(E), stroke: "var(--rs-muted)", "stroke-width": 1 }, plot);
    const t = svg("text", { x: LX - 24, y: Ye(E) + 5, "text-anchor": "end", "font-size": 13, style: "fill: var(--rs-muted)" }, plot);
    t.textContent = E === 0 ? "0: free" : E.toFixed(1).replace("-", "−");
  });
  svg("line", { x1: LX - 14, x2: LX + LW + 10, y1: Ye(0), y2: Ye(0), stroke: "var(--rs-zero)", "stroke-width": 1.2, "stroke-dasharray": "2 3" }, plot);
  const rungG = svg("g", {}, plot);
  const marker = svg("line", { x1: LX - 8, x2: LX + LW + 8, "stroke-width": 3.5, "stroke-linecap": "round" }, plot);
  const mtri = svg("path", { d: `M${LX - 22},-6 L${LX - 10},0 L${LX - 22},6 Z` }, plot);

  const status = html("div", "rs-status", root);
  if (get("status", true) === false) status.style.display = "none";
  html("div", "rs-note", root).innerHTML = `Atomic units: lengths in a<sub>0</sub> = 52.9 pm, energies in ${EH} = 27.2 eV. Z = 1.`;

  // ---------------------------------------------------------------- state
  const u = new Float64Array(N);
  let curL = Math.min(LMAX, Math.max(0, Math.round(get("l", 0))));
  let curE = Math.min(EMAX, Math.max(EMIN, +get("energy", -0.3)));
  let sweeping = false, timer = null;

  function nearest(l, E) {                                           // the level of this l closest to E
    let best = null;
    for (const n in LEVELS[l]) {
      if (best === null || Math.abs(LEVELS[l][n] - E) < Math.abs(LEVELS[l][best] - E)) best = +n;
    }
    return best;
  }

  function draw() {
    const lv = LEVELS[curL];
    const n0 = nearest(curL, curE);
    const hit = Math.abs(lv[n0] - curE) < 1e-9;
    const { rt, cut, nodes } = shoot(curL, curE, u);
    let d = "";
    for (let j = 0; j < Math.min(cut + 1, N); j += 1) {
      if (r[j] > RVIEW) break;
      const v = Math.max(-9, Math.min(9, u[j]));
      d += (j ? "L" : "M") + X(r[j]).toFixed(1) + "," + Yu(v).toFixed(1);
      if (Math.abs(u[j]) > 8) break;                                 // off the chart: stop drawing
    }
    curve.setAttribute("d", d);
    const col = hit ? "var(--rs-teal)" : "var(--rs-red)";
    curve.setAttribute("stroke", col);
    tag.setAttribute("style", `fill: ${col}`);
    sub(tag, `E = ${fmtE(curE)} E`, "h");
    const showT = rt !== null && rt <= RVIEW;
    turn.style.display = showT ? "" : "none"; turnLab.style.display = showT ? "" : "none";
    if (showT) {                                                     // label inside the allowed region, where |u| <= 1
      turn.setAttribute("x1", X(rt)); turn.setAttribute("x2", X(rt));
      const left = rt > 0.16 * RVIEW;
      turnLab.setAttribute("x", X(rt) + (left ? -6 : 6));
      turnLab.setAttribute("text-anchor", left ? "end" : "start");
    }
    // ladder (the top rungs crowd: their labels are nudged apart)
    rungG.innerHTML = "";
    const nudge = { 3: 7, 4: 5, 5: -9 };
    for (let n = curL + 1; n <= NMAX; n++) {
      const found = curE >= lv[n] - 1e-9;
      svg("line", { x1: LX, x2: LX + LW, y1: Ye(lv[n]), y2: Ye(lv[n]), stroke: found ? LCOL[curL] : "var(--rs-level)",
        "stroke-width": found ? 3 : 1.4, "stroke-dasharray": found ? "" : "4 3", "stroke-linecap": "round" }, rungG);
      const t = svg("text", { x: LX + LW + 16, y: Ye(lv[n]) + 5 + (nudge[n] || 0), "font-size": 13,
        style: `fill: ${found ? LCOL[curL] : "var(--rs-muted)"}` }, rungG);
      t.textContent = `n = ${n}`;
    }
    marker.setAttribute("y1", Ye(curE)); marker.setAttribute("y2", Ye(curE)); marker.setAttribute("stroke", col);
    mtri.setAttribute("transform", `translate(0 ${Ye(curE)})`); mtri.setAttribute("fill", col);
    // verdict
    const bottom = curL ? -1 / (2 * curL * (curL + 1)) : -Infinity;
    if (hit) {
      status.innerHTML = `E = ${fmtE(curE)} ${EH} = ${frac(n0)}: a <b style="color:${LCOL[curL]}">bound state</b>, ` +
        `n = ${n0}, l = ${curL} (${n0}${LETTER[curL]}), ${nodes} radial node${nodes === 1 ? "" : "s"}. The tail dies.`;
    } else if (curE < bottom) {
      status.innerHTML = `E lies below the bottom of V<sub>eff</sub> for l = ${curL} (${fmtE(bottom)} ${EH}): ` +
        "no classically allowed region, and u only grows.";
    } else {
      const dir = curE < lv[n0] ? "below" : "above";
      status.innerHTML = `E = ${fmtE(curE)} ${EH}: not allowed. The tail blows up ${dir} the level n = ${n0} ` +
        `(${fmtE(lv[n0])} ${EH}), with ${nodes} node${nodes === 1 ? "" : "s"} before it does.`;
    }
    for (let n = 1; n <= NMAX; n++) {
      nbtns[n].disabled = n <= curL;
      nbtns[n].classList.toggle("rs-active", hit && n === n0);
    }
  }

  function setE(E, fromSlider) {
    let v = Math.min(EMAX, Math.max(EMIN, E));
    const n0 = nearest(curL, v);
    if (Math.abs(LEVELS[curL][n0] - v) < SNAP) v = LEVELS[curL][n0];  // snap onto a level
    curE = v;
    if (!fromSlider) input.value = Math.min(EMAX, Math.max(EMIN, v));
    readout.innerHTML = `= ${fmtE(curE)} ${EH}`;
    draw();
  }

  function setL(l) {
    curL = l;
    lbtns.forEach((b, k) => b.classList.toggle("rs-active", k === l));
    stopSweep();
    setE(curE, false);
  }

  function startSweep() {
    sweeping = true; sweep.textContent = "stop";
    if (curE >= EMAX - 1e-9) curE = EMIN;
    const step = () => {
      if (!sweeping) return;
      const was = curE;
      setE(curE + 0.0025, false);
      const hit = Math.abs(LEVELS[curL][nearest(curL, curE)] - curE) < 1e-9;
      if (curE >= EMAX - 1e-9) { stopSweep(); return; }
      timer = setTimeout(step, hit && Math.abs(curE - was) > 1e-9 ? 900 : 70);
    };
    step();
  }

  function stopSweep() {
    sweeping = false; sweep.textContent = "sweep";
    if (timer) { clearTimeout(timer); timer = null; }
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("rs-dark")) root.classList.toggle("rs-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  lbtns.forEach((b, k) => b.classList.toggle("rs-active", k === curL));
  setE(curE, false);
  syncDark();
  return () => { stopSweep(); if (obs) obs.disconnect(); };
}

export default { render };
