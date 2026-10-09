// Measure the energy of a particle in a box, over and over.
//
// Every reading measures a freshly prepared copy of the same state psi = sum_n c_n psi_n and returns
// E_n = n^2 E_1 with probability |c_n|^2. The histogram of readings converges to |c_n|^2 and their
// running mean to <E> = sum_n |c_n|^2 E_n. A single reading leaves the measured copy in psi_n.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file
// runs in MyST's {anywidget} directive (ch03/05), in a reveal.js deck through a module-script loader
// (slides/ch03/06), and in Jupyter or Colab through the anywidget package. No dependencies.
// Model keys, all optional: state ("example", "ground", "pair", "parabola", "packet", "custom"),
// fontSize (CSS size of the controls and readout; the SVG text scales with the widget width) and
// showMean (false hides the running-mean plot, for a slide; the readout still reports the mean).

const TEAL = "#107895", CARDINAL = "#C8102E", PURPLE = "#6a3d9a";
const SVGNS = "http://www.w3.org/2000/svg";
const SUB = "₀₁₂₃₄₅₆₇₈₉";
const sub = (n) => String(n).split("").map((d) => SUB[+d]).join("");

// box states on L = 1: psi_n(x) = sqrt2 sin(n pi x), E_n = n^2 E_1
const psiN = (n, x) => Math.SQRT2 * Math.sin(n * Math.PI * x);

function parabolaAmps(nmax) {           // psi = sqrt30 x (1 - x): c_n = 8 sqrt15 / (n pi)^3 for odd n
  const c = [];
  for (let n = 1; n <= nmax; n++) c.push(n % 2 ? (8 * Math.sqrt(15)) / (n * Math.PI) ** 3 : 0);
  return c;
}

function packetAmps(nmax) {             // narrow packet at x = 0.3, |psi|^2 of width 0.045: c_n by Simpson's rule
  const M = 2000, h = 1 / M, s = 0.045;
  const f = (x) => Math.exp(-((x - 0.3) ** 2) / (4 * s * s));
  let norm = 0;
  const c = new Array(nmax).fill(0);
  for (let j = 0; j <= M; j++) {
    const x = j * h, w = j === 0 || j === M ? 1 : j % 2 ? 4 : 2, fx = f(x);
    norm += w * fx * fx;
    for (let n = 1; n <= nmax; n++) c[n - 1] += w * psiN(n, x) * fx;
  }
  norm = Math.sqrt((norm * h) / 3);
  return c.map((v) => (v * h) / 3 / norm);
}

const PRESETS = [
  { key: "example", label: "½ψ₁ + ½ψ₂ + ψ₃/√2", amps: [0.5, 0.5, Math.SQRT1_2] },
  { key: "ground", label: "ψ₁", amps: [1] },
  { key: "pair", label: "(ψ₁ + ψ₂)/√2", amps: [Math.SQRT1_2, Math.SQRT1_2] },
  { key: "parabola", label: "√30 x(L − x)", amps: parabolaAmps(7) },
  { key: "packet", label: "narrow packet", amps: packetAmps(12) },
  { key: "custom", label: "your own", amps: null },
];

const CSS = `
.mw-root { --mw-fg: #212529; --mw-muted: #6c757d; --mw-grid: #e3e6ea; --mw-border: #ced4da; --mw-btn: #f8f9fa;
  --mw-on: #e3f0f4; --mw-card: #ffffff; color: var(--mw-fg); background: var(--mw-card);
  border: 1px solid var(--mw-border); border-radius: 10px; padding: 0.8em 1em 0.7em; text-align: left;
  line-height: 1.4; letter-spacing: normal; font-family: inherit; box-sizing: border-box; max-width: 100%; }
.mw-root.mw-dark { --mw-fg: #e9ecef; --mw-muted: #adb5bd; --mw-grid: #343a40; --mw-border: #495057; --mw-btn: #2b3035;
  --mw-on: #16353f; --mw-card: #1e2125; }
.mw-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em; margin: 0.25em 0; }
.mw-label { color: var(--mw-muted); margin-right: 0.3em; }
.mw-btn { font: inherit; color: var(--mw-fg); background: var(--mw-btn); border: 1px solid var(--mw-border);
  border-radius: 999px; padding: 0.15em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.mw-btn:hover { border-color: ${TEAL}; }
.mw-btn.mw-on { border-color: ${TEAL}; background: var(--mw-on); font-weight: 600; }
.mw-btn.mw-go { border-color: ${TEAL}; color: #fff; background: ${TEAL}; font-weight: 600; }
.mw-btn.mw-go:hover { filter: brightness(1.1); }
.mw-custom { display: none; flex-wrap: wrap; gap: 0.3em 1.2em; margin: 0.2em 0 0.3em; }
.mw-custom.mw-show { display: flex; }
.mw-slider { display: flex; align-items: center; gap: 0.35em; }
.mw-slider input { accent-color: ${TEAL}; width: 7em; margin: 0; }
.mw-slider span { min-width: 2.6em; color: var(--mw-muted); font-variant-numeric: tabular-nums; }
.mw-svg { display: block; width: 100%; height: auto; margin: 0.2em 0; }
.mw-svg text { font-family: inherit; fill: var(--mw-fg); }
.mw-svg .mw-muted { fill: var(--mw-muted); }
.mw-readout { font-variant-numeric: tabular-nums; margin-top: 0.35em; }
.mw-readout b { font-weight: 600; }
.mw-last { color: var(--mw-muted); min-height: 1.4em; }
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
  let presetKey = PRESETS.some((p) => p.key === get("state", "example")) ? get("state", "example") : "example";
  const weights = [1, 1, 2, 0, 0];      // the custom state starts as the example: |c_n|^2 = 1/4, 1/4, 1/2

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "mw-root", el);
  root.style.fontSize = get("fontSize", "15px");

  const rowState = html("div", "mw-row", root);
  html("span", "mw-label", rowState, "state:");
  const presetBtns = PRESETS.map((p) => {
    const b = html("button", "mw-btn", rowState, p.label);
    b.type = "button";
    b.addEventListener("click", () => { presetKey = p.key; setState(); });
    return b;
  });

  const custom = html("div", "mw-custom", root);
  const sliders = weights.map((w, i) => {
    const wrap = html("label", "mw-slider", custom);
    html("span", null, wrap, `|c${sub(i + 1)}|²`).style.color = "inherit";
    const inp = html("input", null, wrap);
    Object.assign(inp, { type: "range", min: 0, max: 4, step: 0.05, value: w });
    const out = html("span", null, wrap, "");
    inp.addEventListener("input", () => { weights[i] = +inp.value; setState(); });
    return { inp, out };
  });

  const main = svg("svg", { viewBox: "0 0 720 250", class: "mw-svg", role: "img",
    "aria-label": "the prepared state and a histogram of energy readings" }, root);
  const meanSvg = svg("svg", { viewBox: "0 0 720 140", class: "mw-svg", role: "img",
    "aria-label": "running mean of the energy readings" }, root);
  if (get("showMean", true) === false) meanSvg.style.display = "none";

  const rowGo = html("div", "mw-row", root);
  html("span", "mw-label", rowGo, "measure:");
  for (const k of [1, 10, 100, 1000]) {
    const b = html("button", "mw-btn mw-go", rowGo, k === 1 ? "1 copy" : `${k} copies`);
    b.type = "button";
    b.addEventListener("click", () => queue(k));
  }
  const reset = html("button", "mw-btn", rowGo, "reset");
  reset.type = "button";
  reset.addEventListener("click", () => setState());
  const readout = html("div", "mw-readout", root);
  const last = html("div", "mw-last", root);

  // ---------------------------------------------------------------- state and statistics
  let amps, probs, energies, nb, Eavg, sigma, cum;
  let counts, N, sum, sumsq, hist, lastN, pending, chunk, timer;
  const X = Array.from({ length: 241 }, (_, j) => j / 240);

  function setState() {
    const preset = PRESETS.find((p) => p.key === presetKey);
    if (preset.amps) amps = preset.amps.slice();
    else {
      const tot = weights.reduce((a, b) => a + b, 0) || 1;
      amps = weights.map((w) => Math.sqrt(w / tot));
      if (!weights.some((w) => w > 0)) amps = [1, 0, 0, 0, 0];
    }
    const p = amps.map((a) => a * a), tot = p.reduce((a, b) => a + b, 0);
    probs = p.map((v) => v / tot);
    nb = Math.max(4, probs.length);
    while (probs.length < nb) { probs.push(0); amps.push(0); }
    energies = probs.map((_, i) => (i + 1) ** 2);
    Eavg = probs.reduce((a, q, i) => a + q * energies[i], 0);
    sigma = Math.sqrt(Math.max(0, probs.reduce((a, q, i) => a + q * energies[i] ** 2, 0) - Eavg ** 2));
    cum = []; probs.reduce((a, q) => (cum.push(a + q), a + q), 0);
    counts = new Array(nb).fill(0); N = 0; sum = 0; sumsq = 0; hist = []; lastN = 0; pending = 0; chunk = 0;
    presetBtns.forEach((b, i) => b.classList.toggle("mw-on", PRESETS[i].key === presetKey));
    custom.classList.toggle("mw-show", presetKey === "custom");
    sliders.forEach((s, i) => { s.out.textContent = presetKey === "custom" ? probs[i].toFixed(2) : ""; });
    draw();
  }

  function sample() {
    const r = Math.random() * cum[cum.length - 1];
    let i = 0;
    while (i < cum.length - 1 && r > cum[i]) i++;
    return i;
  }

  function take(k) {
    for (let j = 0; j < k; j++) {
      const i = sample(), E = energies[i];
      counts[i]++; N++; sum += E; sumsq += E * E;
      if (N <= 50 || j === k - 1) hist.push([N, sum / N]);
      lastN = i + 1;
    }
  }

  function queue(k) {
    if (k <= 10) { take(k); if (k > 1) lastN = 0; draw(); return; }
    pending += k;
    chunk = Math.max(chunk, Math.ceil(k / 20));     // a batch lands in about 20 frames
    if (!timer) timer = setTimeout(step, 16);
  }

  function step() {
    const n = Math.min(chunk, pending);
    take(n); pending -= n; lastN = 0;
    draw();
    if (pending > 0) timer = setTimeout(step, 16);
    else { timer = 0; chunk = 0; }
  }

  // ---------------------------------------------------------------- drawing
  const fmt = (v) => (Math.abs(v) >= 100 ? v.toFixed(0) : Math.abs(v) >= 10 ? v.toFixed(1) : v.toFixed(2));

  function draw() {
    while (main.firstChild) main.removeChild(main.firstChild);
    while (meanSvg.firstChild) meanSvg.removeChild(meanSvg.firstChild);
    const dark = root.classList.contains("mw-dark");
    const grid = dark ? "#343a40" : "#e3e6ea", axis = dark ? "#adb5bd" : "#6c757d", wall = dark ? "#dee2e6" : "#212529";

    // left: the prepared state, psi and |psi|^2 in the box
    const psi = X.map((x) => amps.reduce((a, c, i) => a + c * psiN(i + 1, x), 0));
    const show = lastN ? X.map((x) => psiN(lastN, x)) : null;
    const vals = psi.concat(psi.map((v) => v * v), show ? show.concat(show.map((v) => v * v)) : []);
    const ymax = Math.max(...vals) * 1.08, ymin = Math.min(0, ...vals) * 1.08;
    const x0 = 22, x1 = 322, ytop = 52, ybot = 214;
    const sx = (x) => x0 + (x1 - x0) * x, sy = (v) => ybot - ((v - ymin) / (ymax - ymin)) * (ybot - ytop);
    svg("text", { x: x0 - 8, y: 18, "font-size": 15, "font-weight": 600 }, main).textContent = "the prepared state";
    const leg = [[TEAL, "ψ(x)", "line"], [CARDINAL, "|ψ|²", "fill"]].concat(show ? [[PURPLE, `after the reading: ψ${sub(lastN)}`, "dash"]] : []);
    let lx = x0 - 8;
    for (const [col, lab, kind] of leg) {
      if (kind === "fill") svg("rect", { x: lx, y: 30, width: 18, height: 10, fill: col, "fill-opacity": 0.25, stroke: col }, main);
      else svg("line", { x1: lx, y1: 35, x2: lx + 18, y2: 35, stroke: col, "stroke-width": 2.5, "stroke-dasharray": kind === "dash" ? "5 3" : "" }, main);
      const t = svg("text", { x: lx + 23, y: 40, "font-size": 13 }, main); t.textContent = lab;
      lx += 32 + lab.length * 7.2;
    }
    svg("line", { x1: x0, y1: sy(0), x2: x1, y2: sy(0), stroke: axis, "stroke-width": 0.8 }, main);
    const path = (ys) => ys.map((v, j) => `${j ? "L" : "M"}${sx(X[j]).toFixed(1)},${sy(v).toFixed(1)}`).join("");
    svg("path", { d: path(psi.map((v) => v * v)) + `L${sx(1)},${sy(0)}L${sx(0)},${sy(0)}Z`, fill: CARDINAL, "fill-opacity": 0.16, stroke: "none" }, main);
    svg("path", { d: path(psi.map((v) => v * v)), fill: "none", stroke: CARDINAL, "stroke-width": 1.6 }, main);
    svg("path", { d: path(psi), fill: "none", stroke: TEAL, "stroke-width": 2.6 }, main);
    if (show) svg("path", { d: path(show), fill: "none", stroke: PURPLE, "stroke-width": 2.2, "stroke-dasharray": "6 4" }, main);
    for (const xw of [x0, x1]) svg("line", { x1: xw, y1: ybot + 6, x2: xw, y2: ytop - 4, stroke: wall, "stroke-width": 3 }, main);
    svg("line", { x1: x0, y1: ybot + 6, x2: x1, y2: ybot + 6, stroke: wall, "stroke-width": 1 }, main);
    for (const [xv, lab] of [[0, "0"], [0.5, "L/2"], [1, "L"]]) {
      const t = svg("text", { x: sx(xv), y: ybot + 24, "font-size": 13, "text-anchor": "middle", class: "mw-muted" }, main); t.textContent = lab;
    }

    // right: fraction of readings (bars) against |c_n|^2 (ticks)
    const b0 = 392, b1 = 712, slot = (b1 - b0) / nb;
    const frac = counts.map((c) => (N ? c / N : 0));
    const pmax = Math.min(1, Math.ceil(Math.max(...probs, ...frac) * 1.15 * 10) / 10 || 1);
    const by = (v) => ybot - (v / pmax) * (ybot - ytop);
    svg("text", { x: b0, y: 18, "font-size": 15, "font-weight": 600 }, main).textContent =
      N ? `${N.toLocaleString()} reading${N === 1 ? "" : "s"}` : "no readings yet";
    svg("rect", { x: b0, y: 30, width: 18, height: 10, fill: TEAL }, main);
    svg("text", { x: b0 + 23, y: 40, "font-size": 13 }, main).textContent = "fraction of readings";
    svg("line", { x1: b0 + 170, y1: 35, x2: b0 + 190, y2: 35, stroke: CARDINAL, "stroke-width": 3.5 }, main);
    svg("text", { x: b0 + 196, y: 40, "font-size": 13 }, main).textContent = "|cₙ|², predicted";
    for (const g of [0.25, 0.5, 0.75, 1]) {
      if (g > pmax + 1e-9) continue;
      svg("line", { x1: b0, y1: by(g), x2: b1, y2: by(g), stroke: grid, "stroke-width": 1 }, main);
      const t = svg("text", { x: b0 - 6, y: by(g) + 4, "font-size": 11, "text-anchor": "end", class: "mw-muted" }, main); t.textContent = g;
    }
    svg("line", { x1: b0, y1: ybot, x2: b1, y2: ybot, stroke: axis, "stroke-width": 1 }, main);
    for (let i = 0; i < nb; i++) {
      const cx = b0 + slot * (i + 0.5), w = slot * 0.62;
      if (frac[i] > 0) svg("rect", { x: cx - w / 2, y: by(frac[i]), width: w, height: ybot - by(frac[i]),
        fill: TEAL, "fill-opacity": lastN === i + 1 ? 1 : 0.8 }, main);
      if (probs[i] > 0) svg("line", { x1: cx - w * 0.62, y1: by(probs[i]), x2: cx + w * 0.62, y2: by(probs[i]),
        stroke: CARDINAL, "stroke-width": 3.5 }, main);
      const t = svg("text", { x: cx, y: ybot + 18, "font-size": nb > 8 ? 11 : 13, "text-anchor": "middle" }, main);
      t.textContent = energies[i];
    }
    const t = svg("text", { x: (b0 + b1) / 2, y: ybot + 34, "font-size": 12, "text-anchor": "middle", class: "mw-muted" }, main);
    t.textContent = "reading E (units of E₁)";

    // bottom: running mean of the readings against <E>
    const m0 = 64, m1 = 690, mt = 18, mb = 104;
    const decades = Math.max(1, Math.ceil(Math.log10(Math.max(N, 10))));
    const lx2 = (n) => m0 + (Math.log10(n) / decades) * (m1 - m0);
    const top = Math.max(2 * Eavg, energies.filter((_, i) => probs[i] > 0.005).pop() || 1);
    const my = (v) => mb - (Math.min(v, top) / top) * (mb - mt);
    svg("line", { x1: m0, y1: mb, x2: m1, y2: mb, stroke: axis, "stroke-width": 1 }, meanSvg);
    svg("line", { x1: m0, y1: mt, x2: m0, y2: mb, stroke: axis, "stroke-width": 1 }, meanSvg);
    for (let d = 0; d <= decades; d++) {
      const tx = svg("text", { x: lx2(10 ** d), y: mb + 16, "font-size": 11, "text-anchor": "middle", class: "mw-muted" }, meanSvg);
      tx.textContent = (10 ** d).toLocaleString();
    }
    const tl = svg("text", { x: (m0 + m1) / 2, y: mb + 32, "font-size": 12, "text-anchor": "middle", class: "mw-muted" }, meanSvg);
    tl.textContent = "number of readings";
    const ty = svg("text", { x: 14, y: (mt + mb) / 2, "font-size": 12, "text-anchor": "middle", class: "mw-muted",
      transform: `rotate(-90 14 ${(mt + mb) / 2})` }, meanSvg);
    ty.textContent = "mean / E₁";
    for (const v of [0, top / 2, top]) {
      const tt = svg("text", { x: m0 - 6, y: my(v) + 4, "font-size": 11, "text-anchor": "end", class: "mw-muted" }, meanSvg);
      tt.textContent = fmt(v);
    }
    svg("line", { x1: m0, y1: my(Eavg), x2: m1, y2: my(Eavg), stroke: CARDINAL, "stroke-width": 2, "stroke-dasharray": "7 4" }, meanSvg);
    const te = svg("text", { x: m1, y: my(Eavg) - 6, "font-size": 13, "text-anchor": "end" }, meanSvg);
    te.textContent = `⟨E⟩ = Σ|cₙ|²Eₙ = ${fmt(Eavg)} E₁`;
    if (hist.length) {
      const d = hist.map(([n, m], j) => `${j ? "L" : "M"}${lx2(n).toFixed(1)},${my(m).toFixed(1)}`).join("");
      svg("path", { d, fill: "none", stroke: TEAL, "stroke-width": 2.4 }, meanSvg);
      const [nl, ml] = hist[hist.length - 1];
      svg("circle", { cx: lx2(nl), cy: my(ml), r: 4, fill: TEAL }, meanSvg);
    }

    // text readout
    const mean = N ? sum / N : 0, spread = N > 1 ? Math.sqrt(Math.max(0, sumsq / N - mean * mean)) : 0;
    readout.innerHTML = N
      ? `mean of ${N.toLocaleString()} reading${N === 1 ? "" : "s"} <b>${fmt(mean)} E₁</b> (predicted ⟨E⟩ = ${fmt(Eavg)} E₁) · ` +
        `spread <b>${fmt(spread)} E₁</b> (predicted σ<sub>E</sub> = ${fmt(sigma)} E₁)`
      : `predicted ⟨E⟩ = ${fmt(Eavg)} E₁ and σ<sub>E</sub> = ${fmt(sigma)} E₁. Measure a few copies.`;
    last.textContent = lastN
      ? `Last reading: ${energies[lastN - 1]} E₁. That copy is now in ψ${sub(lastN)}: measure it again and you get ${energies[lastN - 1]} E₁ every time.`
      : N ? "Each reading used a fresh copy of the prepared state." : "";
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("mw-dark")) { root.classList.toggle("mw-dark", dark); draw(); }
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  setState();
  syncDark();
  return () => { if (timer) clearTimeout(timer); if (obs) obs.disconnect(); };
}

export default { render };
