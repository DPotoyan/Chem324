// The harmonic oscillator as the reference for every other well.
//
// Four wells, all with the same curvature at the bottom (units hbar = mu = 1, so the parabola fitted at each minimum
// has omega = 1 and energies come out in hbar omega): harmonic, Morse D(1 - e^{-ax})^2, quartic x^2/2 + lambda x^4,
// and the double well (x^2 - a^2)^2 / 8a^2 with barrier height B = a^2/8. One knob per well (Morse depth, lambda,
// barrier height). The states are solved live on a grid: Sturm-sequence bisection for the energies, inverse iteration
// for the states. Left: the well, its states drawn on their levels, the classically forbidden region shaded and the
// fitted parabola dashed. Right: the parabola's ladder (v + 1/2) wired to the actual levels, so the steps shrinking
// (Morse), growing (quartic) or pairing up (double well, tunneling) show at a glance.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive, in a reveal.js deck through a module-script loader, and in Jupyter or Colab through
// the anywidget package. No dependencies. Model keys, optional: fontSize (CSS size), well ("harmonic", "morse",
// "quartic" or "double", the one shown first), status (false hides the verdict line).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00", PURPLE = "#6a3d9a";
const SVGNS = "http://www.w3.org/2000/svg";

const N = 800, EMAX = 6.3, NMAX = 8;                                 // grid points, top of the plot, states drawn

const WELLS = {
  harmonic: {
    name: "harmonic", grid: [-7, 7], view: [-5, 5], sym: true, knob: null,
    V: (x) => 0.5 * x * x, mins: () => [0], formula: () => "V = ½x²",
  },
  morse: {
    name: "Morse", grid: [-4, 40], view: [-3, 12], sym: false,
    knob: { label: "well depth D", min: 1.5, max: 10, step: 0.1, value: 4, unit: " ħω" },
    V: (x, D) => { const e = 1 - Math.exp(-x / Math.sqrt(2 * D)); return D * e * e; },
    mins: () => [0], formula: () => "V = D(1 − e^(−ax))²",
  },
  quartic: {
    name: "quartic", grid: [-6, 6], view: [-4, 4], sym: true,
    knob: { label: "λ", min: 0, max: 1, step: 0.01, value: 0.25, unit: "" },
    V: (x, l) => 0.5 * x * x + l * x ** 4, mins: () => [0], formula: () => "V = ½x² + λx⁴",
  },
  double: {
    name: "double well", grid: [-14, 14], view: [-9.5, 9.5], sym: true,
    knob: { label: "barrier height B", min: 0.1, max: 4.5, step: 0.05, value: 2.5, unit: " ħω" },
    V: (x, B) => { const a2 = 8 * B; return (x * x - a2) ** 2 / (8 * a2); },
    mins: (B) => [-Math.sqrt(8 * B), Math.sqrt(8 * B)], formula: () => "V = B(x²/a² − 1)²",
  },
};
const ORDER = ["harmonic", "morse", "quartic", "double"];

// ------------------------------------------------------------------ the eigenproblem
// H = -1/2 d^2/dx^2 + V on N interior points: diagonal 1/dx^2 + V_i, off-diagonal -1/(2 dx^2)
function solve(w, p) {
  const [lo, hi] = w.grid, dx = (hi - lo) / (N + 1);
  const x = new Float64Array(N), d = new Float64Array(N);
  for (let i = 0; i < N; i++) { x[i] = lo + (i + 1) * dx; d[i] = 1 / (dx * dx) + w.V(x[i], p); }
  const off = -0.5 / (dx * dx), e2 = off * off;
  const count = (lam) => {                                           // eigenvalues below lam (Sturm sequence)
    let c = 0, q = d[0] - lam;
    if (q < 0) c++;
    for (let i = 1; i < N; i++) {
      q = d[i] - lam - e2 / (q === 0 ? 1e-300 : q);
      if (q < 0) c++;
    }
    return c;
  };
  const top = w.name === "Morse" ? Math.min(EMAX, p) : EMAX;         // Morse: bound states only
  const bound = w.name === "Morse" ? count(p) : null;
  const n = Math.min(count(top), NMAX);
  const E = [], psi = [];
  let vmin = Infinity;
  for (let i = 0; i < N; i++) vmin = Math.min(vmin, d[i] + 2 * off);
  for (let k = 0; k < n; k++) {
    let a = vmin, b = top;
    for (let it = 0; it < 64 && b - a > 1e-14; it++) {
      const m = 0.5 * (a + b);
      if (count(m) > k) b = m; else a = m;
    }
    const lam = 0.5 * (a + b);
    E.push(lam);
    // inverse iteration, (H - sigma) y = b by the Thomas algorithm
    const sig = lam - 1e-12 * Math.max(1, Math.abs(lam));
    let y = new Float64Array(N);
    for (let i = 0; i < N; i++) y[i] = 1 + 0.5 * Math.sin(1.3 * i + 0.7);
    const cp = new Float64Array(N), dp = new Float64Array(N);
    for (let it = 0; it < 3; it++) {
      let m = d[0] - sig;
      cp[0] = off / m; dp[0] = y[0] / m;
      for (let i = 1; i < N; i++) {
        m = d[i] - sig - off * cp[i - 1];
        if (m === 0) m = 1e-300;
        cp[i] = off / m; dp[i] = (y[i] - off * dp[i - 1]) / m;
      }
      const z = new Float64Array(N);
      z[N - 1] = dp[N - 1];
      for (let i = N - 2; i >= 0; i--) z[i] = dp[i] - cp[i] * z[i + 1];
      let s = 0;
      for (let i = 0; i < N; i++) s = Math.max(s, Math.abs(z[i]));
      for (let i = 0; i < N; i++) y[i] = z[i] / s;
    }
    if (w.sym) {                                                     // state k has parity (-1)^k
      const sgn = k % 2 === 0 ? 1 : -1, z = new Float64Array(N);
      for (let i = 0; i < N; i++) z[i] = 0.5 * (y[i] + sgn * y[N - 1 - i]);
      y = z;
    }
    let mx = 0;
    for (let i = 0; i < N; i++) mx = Math.max(mx, Math.abs(y[i]));
    let j = N - 1;                                                   // outermost right lobe points up
    while (j > 0 && Math.abs(y[j]) < 0.3 * mx) j--;
    const s = (y[j] < 0 ? -1 : 1) / mx;
    for (let i = 0; i < N; i++) y[i] *= s;
    psi.push(y);
  }
  return { x, E, psi, bound };
}

// ------------------------------------------------------------------ drawing
const W = 1000, H = 400;
const PL = 62, PR = 690, PT = 34, PB = 372;                          // well panel
const LA = 742, LB = 852, RUNG = 62;                                 // ladder: parabola column, actual column

const CSS = `
.ws-root { --ws-fg: #212529; --ws-muted: #6c757d; --ws-border: #ced4da; --ws-btn: #f8f9fa; --ws-card: #ffffff;
  --ws-teal: ${TEAL}; --ws-purple: ${PURPLE}; --ws-orange: ${ORANGE}; --ws-red: ${CARDINAL};
  --ws-wall: #e9ecef; --ws-ghost: #adb5bd; --ws-level: #ced4da; --ws-on: #e7f1f4;
  color: var(--ws-fg); background: var(--ws-card); border: 1px solid var(--ws-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.ws-root.ws-dark { --ws-fg: #e9ecef; --ws-muted: #adb5bd; --ws-border: #495057; --ws-btn: #2b3035; --ws-card: #1e2125;
  --ws-teal: #45a9c6; --ws-purple: #b08be0; --ws-orange: #f59f3a; --ws-red: #f05d6f;
  --ws-wall: #2b3035; --ws-ghost: #868e96; --ws-level: #495057; --ws-on: #1f3a44; }
.ws-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.2em; margin: 0 0 0.3em; }
.ws-btns { display: flex; flex-wrap: wrap; gap: 0.35em; }
.ws-btn { font: inherit; color: var(--ws-fg); background: var(--ws-btn); border: 1px solid var(--ws-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.ws-btn:hover { border-color: ${TEAL}; }
.ws-btn.ws-active { border-color: var(--ws-teal); background: var(--ws-on); font-weight: 600; }
.ws-slider { display: flex; align-items: center; gap: 0.5em; }
.ws-slider input { width: 11em; accent-color: ${TEAL}; }
.ws-val { font-variant-numeric: tabular-nums; min-width: 4.2em; color: var(--ws-muted); }
.ws-eq { color: var(--ws-muted); }
.ws-plot { display: block; width: 100%; height: auto; }
.ws-plot text { font-family: inherit; fill: var(--ws-fg); }
.ws-status { font-weight: 600; margin: 0.2em 0 0; min-height: 1.4em; }
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

const SUP = (s) => s.replace(/[-0-9]/g, (c) => "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"["-0123456789".indexOf(c)]);
const small = (v) => {
  if (v >= 0.01) return v.toFixed(2);
  const ex = Math.floor(Math.log10(v));
  return `${(v / 10 ** ex).toFixed(1)} × 10${SUP(String(ex))}`;
};

let uid = 0;

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "ws-root", el);
  root.setAttribute("data-prevent-swipe", "");                       // reveal.js: drags must not change slides
  root.style.fontSize = get("fontSize", "15px");

  const controls = html("div", "ws-controls", root);
  const btns = html("div", "ws-btns", controls);
  const buttons = {};
  ORDER.forEach((key) => {
    const b = html("button", "ws-btn", btns, WELLS[key].name); b.type = "button";
    b.addEventListener("click", () => { b.blur(); choose(key); });
    buttons[key] = b;
  });
  const box = html("label", "ws-slider", controls);
  const knobName = html("span", null, box);
  const input = html("input", null, box); input.type = "range";
  const knobVal = html("span", "ws-val", box);
  const noKnob = html("span", "ws-eq", controls, "no knob: this is the reference");
  input.addEventListener("input", () => { values[current] = +input.value; update(); });
  input.addEventListener("change", () => input.blur());             // arrow keys go back to the deck

  const plot = svg("svg", { viewBox: `0 0 ${W} ${H}`, class: "ws-plot", role: "img",
    "aria-label": "a potential well with its energy levels and states, beside the harmonic ladder" }, root);
  const clipId = `ws-clip-${uid++}`;
  const defs = svg("defs", {}, plot);
  const clip = svg("clipPath", { id: clipId }, defs);
  svg("rect", { x: PL, y: PT, width: PR - PL, height: PB - PT }, clip);

  // energy axis
  for (let e = 0; e <= 6; e++) {
    const y = PB - (e / EMAX) * (PB - PT);
    svg("line", { x1: PL - 6, x2: PL, y1: y, y2: y, stroke: "var(--ws-muted)", "stroke-width": 1 }, plot);
    const t = svg("text", { x: PL - 10, y: y + 5, "text-anchor": "end", "font-size": 14, style: "fill: var(--ws-muted)" }, plot);
    t.textContent = e;
  }
  svg("line", { x1: PL, x2: PL, y1: PT, y2: PB, stroke: "var(--ws-muted)", "stroke-width": 1 }, plot);
  const ylab = svg("text", { x: 18, y: (PT + PB) / 2, "text-anchor": "middle", "font-size": 15,
    transform: `rotate(-90 18 ${(PT + PB) / 2})`, style: "fill: var(--ws-muted)" }, plot);
  ylab.textContent = "energy (ħω)";
  const xlab = svg("text", { x: PR - 4, y: PB + 20, "text-anchor": "end", "font-size": 14, style: "fill: var(--ws-muted)" }, plot);
  xlab.textContent = "x →";

  const g = svg("g", { "clip-path": `url(#${clipId})` }, plot);
  const wall = svg("path", { fill: "var(--ws-wall)", stroke: "none" }, g);
  const parab = svg("path", { fill: "none", stroke: "var(--ws-ghost)", "stroke-width": 1.6, "stroke-dasharray": "6 5" }, g);
  const dissoc = svg("line", { stroke: "var(--ws-red)", "stroke-width": 1.4, "stroke-dasharray": "3 4" }, g);
  const levelG = svg("g", {}, g);
  const psiG = svg("g", {}, g);
  const curve = svg("path", { fill: "none", stroke: "var(--ws-fg)", "stroke-width": 2.6, "stroke-linejoin": "round" }, g);
  const dissocLab = svg("text", { "text-anchor": "end", "font-size": 14, style: "fill: var(--ws-red)" }, plot);
  const key = svg("text", { x: PL + 12, y: PT + 18, "font-size": 14 }, plot);

  // ladder panel
  const head = (x, s, c) => { const t = svg("text", { x, y: PT - 12, "text-anchor": "middle", "font-size": 15, style: `fill: ${c}` }, plot); t.textContent = s; };
  head(LA + RUNG / 2, "parabola", "var(--ws-muted)");
  head(LB + RUNG / 2, "this well", "var(--ws-teal)");
  const ladderG = svg("g", {}, plot);

  const status = html("div", "ws-status", root);
  if (get("status", true) === false) status.style.display = "none";
  const eq = html("div", "ws-eq", root);

  // ---------------------------------------------------------------- state
  const values = {};
  ORDER.forEach((k) => { if (WELLS[k].knob) values[k] = WELLS[k].knob.value; });
  let current = WELLS[get("well", "double")] ? get("well", "double") : "double";

  const Y = (e) => PB - (e / EMAX) * (PB - PT);

  function update() {
    const w = WELLS[current], p = values[current];
    const [v0, v1] = w.view, X = (x) => PL + (x - v0) / (v1 - v0) * (PR - PL);
    if (w.knob) knobVal.textContent = (w.knob.step < 0.05 ? p.toFixed(2) : p.toFixed(w.knob.step < 1 ? 2 : 0)) + w.knob.unit;
    eq.textContent = `${w.formula(p)}. Same curvature at every bottom: the dashed parabola is the same spring. Shaded: V > E.`;

    // the well, sampled across the view
    const M = 360, xs = [], vs = [];
    for (let i = 0; i <= M; i++) { const x = v0 + (v1 - v0) * i / M; xs.push(x); vs.push(w.V(x, p)); }
    const top = EMAX + 0.4;
    let dc = "", dw = `M${X(v0)},${Y(0)}`;                           // shade under the curve: V > E, forbidden
    xs.forEach((x, i) => {
      const v = Math.min(vs[i], top);
      dc += (i ? "L" : "M") + X(x).toFixed(1) + "," + Y(v).toFixed(1);
      dw += "L" + X(x).toFixed(1) + "," + Y(v).toFixed(1);
    });
    dw += `L${X(v1)},${Y(0)}Z`;
    curve.setAttribute("d", dc); wall.setAttribute("d", dw);

    // the fitted parabola(s), omega = 1 at every minimum
    let dp = "";
    if (current !== "harmonic") {
      w.mins(p).forEach((m) => {
        const r = Math.sqrt(2 * top);
        for (let i = 0; i <= 80; i++) {
          const x = m - r + 2 * r * i / 80;
          dp += (i ? "L" : "M") + X(x).toFixed(1) + "," + Y(0.5 * (x - m) ** 2).toFixed(1);
        }
      });
    }
    parab.setAttribute("d", dp);

    // dissociation
    const showD = current === "morse" && p < EMAX;
    dissoc.style.display = showD ? "" : "none";
    dissocLab.style.display = showD ? "" : "none";
    if (showD) {
      dissoc.setAttribute("x1", PL); dissoc.setAttribute("x2", PR);
      dissoc.setAttribute("y1", Y(p)); dissoc.setAttribute("y2", Y(p));
      dissocLab.setAttribute("x", PR - 6); dissocLab.setAttribute("y", Y(p) - 7);
      dissocLab.textContent = "the bond breaks";
    }

    // states
    const { x, E, psi, bound } = solve(w, p);
    const color = (k) => (w.sym && k % 2 ? "var(--ws-purple)" : "var(--ws-teal)");
    key.innerHTML = "";
    if (w.sym) {
      const a = svg("tspan", { style: "fill: var(--ws-teal)" }, key); a.textContent = "even";
      const b = svg("tspan", { style: "fill: var(--ws-muted)" }, key); b.textContent = " and ";
      const c = svg("tspan", { style: "fill: var(--ws-purple)" }, key); c.textContent = "odd";
      const d = svg("tspan", { style: "fill: var(--ws-muted)" }, key); d.textContent = " states";
    }
    levelG.innerHTML = ""; psiG.innerHTML = "";
    E.forEach((en, k) => {
      // level line where the motion is classically allowed
      let seg = null;
      const close = (xe) => { svg("line", { x1: X(seg), x2: X(xe), y1: Y(en), y2: Y(en), stroke: "var(--ws-level)",
        "stroke-width": 1.2, "stroke-dasharray": "4 3" }, levelG); seg = null; };
      xs.forEach((xx, i) => {
        if (vs[i] <= en && seg === null) seg = xx;
        if (vs[i] > en && seg !== null) close(xx);
      });
      if (seg !== null) close(v1);
      // the state on its level, height set by the room to its neighbors (a tunneling partner does not count)
      const gaps = [];
      if (k > 0) gaps.push(en - E[k - 1]);
      if (k < E.length - 1) gaps.push(E[k + 1] - en);
      const wide = current === "double" ? gaps.filter((v) => v > 0.15) : gaps;
      const room = wide.length ? wide.reduce((s, v) => s + v, 0) / wide.length : 1;
      const amp = Math.min(0.36, 0.45 * room, 0.45 * (EMAX - en) + 0.05);
      if (amp < 0.1) return;                                         // crowded near dissociation: the level only
      const y = psi[k];
      let i0 = 0, i1 = N - 1;                                        // drop the tails once the state has died away
      while (i0 < N - 1 && (Math.abs(y[i0]) < 0.02 || x[i0] < v0)) i0++;
      while (i1 > 0 && (Math.abs(y[i1]) < 0.02 || x[i1] > v1)) i1--;
      let d = "";
      for (let i = i0; i <= i1; i++) d += (i > i0 ? "L" : "M") + X(x[i]).toFixed(1) + "," + Y(en + amp * y[i]).toFixed(1);
      svg("path", { d, fill: "none", stroke: color(k), "stroke-width": 2.2, "stroke-linejoin": "round" }, psiG);
    });

    // the ladder: parabola rungs (v + 1/2) wired to the actual levels
    ladderG.innerHTML = "";
    const pairs = current === "double";
    const rungs = [];
    for (let v = 0; v + 0.5 < EMAX; v++) rungs.push(v + 0.5);
    rungs.forEach((r) => svg("line", { x1: LA, x2: LA + RUNG, y1: Y(r), y2: Y(r), stroke: "var(--ws-ghost)", "stroke-width": 2.6,
      "stroke-linecap": "round" }, ladderG));
    if (pairs) rungs.forEach((r) => { const t = svg("text", { x: LA - 6, y: Y(r) + 5, "text-anchor": "end", "font-size": 13,
      style: "fill: var(--ws-muted)" }, ladderG); t.textContent = "×2"; });
    E.forEach((en, k) => {
      const r = rungs[pairs ? Math.floor(k / 2) : k];
      if (r !== undefined) svg("line", { x1: LA + RUNG + 3, x2: LB - 3, y1: Y(r), y2: Y(en), stroke: "var(--ws-ghost)",
        "stroke-width": 1 }, ladderG);
      const [a, b] = !pairs ? [LB, LB + RUNG] : k % 2 ? [LB + RUNG / 2 + 3, LB + RUNG] : [LB, LB + RUNG / 2 - 3];
      svg("line", { x1: a, x2: b, y1: Y(en), y2: Y(en), stroke: color(k), "stroke-width": 2.6, "stroke-linecap": "round" }, ladderG);
    });
    if (current === "morse" && p < EMAX) {
      svg("line", { x1: LA - 4, x2: LB + RUNG + 4, y1: Y(p), y2: Y(p), stroke: "var(--ws-red)", "stroke-width": 1.2,
        "stroke-dasharray": "3 4" }, ladderG);
    }

    // verdict
    const gaps = E.slice(1).map((en, k) => en - E[k]);
    if (current === "harmonic") {
      status.textContent = "Equal steps of ħω, starting ½ħω above the bottom: the reference ladder.";
    } else if (current === "morse") {
      status.textContent = `Softer than the parabola: the steps shrink from ${gaps[0].toFixed(2)} ħω to ` +
        `${gaps[gaps.length - 1].toFixed(2)} ħω, and the ladder ends after ${bound} levels.`;
    } else if (current === "quartic") {
      status.textContent = p < 0.005 ? "λ = 0 is the harmonic oscillator. Turn λ up." :
        `Stiffer than the parabola: the steps grow from ${gaps[0].toFixed(2)} ħω to ${gaps[gaps.length - 1].toFixed(2)} ħω.`;
    } else {
      status.textContent = p < E[0] ? "The barrier sits below the zero-point energy: one well with a bump, no pairs." :
        `Below the barrier: even and odd pairs, split by tunneling (lowest pair ${small(E[1] - E[0])} ħω).`;
    }
  }

  function choose(key) {
    current = key;
    ORDER.forEach((k) => buttons[k].classList.toggle("ws-active", k === key));
    const w = WELLS[key];
    box.style.display = w.knob ? "" : "none";
    noKnob.style.display = w.knob ? "none" : "";
    if (w.knob) {
      knobName.textContent = w.knob.label;
      input.min = w.knob.min; input.max = w.knob.max; input.step = w.knob.step; input.value = values[key];
    }
    update();
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("ws-dark")) root.classList.toggle("ws-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  choose(current);
  syncDark();
  return () => { if (obs) obs.disconnect(); };
}

export default { render };
