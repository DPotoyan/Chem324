// Squeeze and widen a Gaussian, and see which plane waves it is made of.
//
// psi(x) = (2 pi sx^2)^(-1/4) exp(-x^2 / 4 sx^2) exp(i p0 x / hbar) has the momentum wavefunction
// phi(p) = (2 pi sp^2)^(-1/4) exp(-(p - p0)^2 / 4 sp^2) with sp = hbar / 2 sx (hbar = 1 here). One slider sets sx.
// Wide, the packet is nearly one plane wave (an eigenfunction of p); narrow, nearly a spike (an eigenfunction of x)
// built from many momenta. The optional top panel draws seven of the plane waves, Re e^{i p x}, at p0 + u sp with
// amplitudes exp(-u^2/4), and marks them in the momentum panel in matching colours.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch03/06) and in a reveal.js deck through a module-script loader (slides/ch03/06).
// Model keys, all optional: waves (true: start with the plane-wave panel shown), toggle (false hides the
// show/hide button, for a slide), fontSize (CSS size of the controls; the SVG text scales with the width).

const TEAL = "#107895", PURPLE = "#6a3d9a", ORANGE = "#e07b00";
const SVGNS = "http://www.w3.org/2000/svg";
const P0 = 3, SMIN = 0.15, SMAX = 4;
const U = [-2.4, -1.6, -0.8, 0, 0.8, 1.6, 2.4];
const mix = (f) => {                    // purple -> orange, the colours of the seven waves
  const a = [0x6a, 0x3d, 0x9a], b = [0xe0, 0x7b, 0x00];
  return `rgb(${a.map((v, i) => Math.round(v + (b[i] - v) * f)).join(",")})`;
};
const WCOL = U.map((_, k) => mix(k / (U.length - 1)));

const CSS = `
.mw-root { --mw-fg: #212529; --mw-muted: #6c757d; --mw-border: #ced4da; --mw-btn: #f8f9fa; --mw-card: #ffffff;
  color: var(--mw-fg); background: var(--mw-card); border: 1px solid var(--mw-border); border-radius: 10px;
  padding: 0.7em 1em 0.6em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; }
.mw-root.mw-dark { --mw-fg: #e9ecef; --mw-muted: #adb5bd; --mw-border: #495057; --mw-btn: #2b3035; --mw-card: #1e2125; }
.mw-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5em 0.8em; margin: 0.2em 0; }
.mw-label { color: var(--mw-muted); }
.mw-range { accent-color: ${TEAL}; flex: 1 1 12em; max-width: 26em; margin: 0; }
.mw-num { font-variant-numeric: tabular-nums; }
.mw-btn { font: inherit; color: var(--mw-fg); background: var(--mw-btn); border: 1px solid var(--mw-border);
  border-radius: 999px; padding: 0.1em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.mw-btn:hover { border-color: ${TEAL}; }
.mw-status { font-weight: 600; min-height: 1.5em; }
.mw-svg { display: block; width: 100%; height: auto; margin: 0.15em 0; touch-action: pan-y; }
.mw-svg text { font-family: inherit; fill: var(--mw-fg); }
.mw-svg .mw-muted { fill: var(--mw-muted); }
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
  let showWaves = get("waves", true) !== false;

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "mw-root", el);
  root.style.fontSize = get("fontSize", "15px");
  root.setAttribute("data-prevent-swipe", "");

  const row = html("div", "mw-row", root);
  html("span", "mw-label", row, "squeeze or widen:");
  const range = html("input", "mw-range", row);
  Object.assign(range, { type: "range", min: 0, max: 1000, step: 1, value: 0 });
  const nums = html("span", "mw-num", row);
  let btn = null;
  if (get("toggle", true) !== false) {
    btn = html("button", "mw-btn", row, "");
    btn.type = "button";
    btn.addEventListener("click", () => { showWaves = !showWaves; draw(); btn.blur(); });
  }
  const status = html("div", "mw-status", root);
  const pic = svg("svg", { class: "mw-svg", role: "img",
    "aria-label": "a Gaussian in position and its momentum distribution" }, root);

  const toS = (v) => SMIN * (SMAX / SMIN) ** (v / 1000);              // log slider
  range.value = String(Math.round((1000 * Math.log(1 / SMIN)) / Math.log(SMAX / SMIN)));   // start at sx = 1
  range.addEventListener("input", draw);
  range.addEventListener("change", () => range.blur());                // let reveal's arrow keys work again

  // ---------------------------------------------------------------- drawing
  const NX = 500, NP = 300;
  const XS = Array.from({ length: NX }, (_, j) => -8 + (16 * j) / (NX - 1));
  const PS = Array.from({ length: NP }, (_, j) => -6 + (18 * j) / (NP - 1));

  function draw() {
    const s = toS(+range.value), sp = 0.5 / s;
    const dark = root.classList.contains("mw-dark");
    const axis = dark ? "#adb5bd" : "#6c757d", base = dark ? "#495057" : "#ced4da";
    nums.textContent = `σₓ = ${s.toFixed(2)}  ·  σₚ = ħ/2σₓ = ${sp.toFixed(2)}  ·  σₓσₚ = ħ/2`;
    nums.style.whiteSpace = "pre";
    if (btn) btn.textContent = showWaves ? "hide the plane waves" : "show the plane waves";
    if (s > 2) { status.textContent = "Wide: nearly ONE plane wave, an eigenfunction of p̂ (sharp momentum)"; status.style.color = ORANGE; }
    else if (s < 0.4) { status.textContent = "Narrow: nearly a spike, an eigenfunction of x̂ (sharp position), built from MANY momenta"; status.style.color = TEAL; }
    else { status.textContent = "In between: a wave packet, a bundle of plane waves near p₀"; status.style.color = dark ? "#adb5bd" : "#6c757d"; }

    while (pic.firstChild) pic.removeChild(pic.firstChild);
    const top = showWaves ? 150 : 0, H = 230 + top;
    pic.setAttribute("viewBox", `0 0 720 ${H}`);
    const x0 = 12, x1 = 430, q0 = 470, q1 = 712;
    const sx = (x) => x0 + ((x + 8) / 16) * (x1 - x0), sq = (p) => q0 + ((p + 6) / 18) * (q1 - q0);
    const path = (xs, ys, fx, fy) => xs.map((v, j) => `${j ? "L" : "M"}${fx(v).toFixed(1)},${fy(ys[j]).toFixed(1)}`).join("");
    const text = (x, y, str, attrs = {}) => { const t = svg("text", { x, y, "font-size": 14, ...attrs }, pic); t.textContent = str; return t; };

    // optional: seven of the plane waves, stacked
    if (showWaves) {
      const t = text(x0, 18, "seven of the plane waves, Re e", { "font-weight": 600 });
      svg("tspan", { dy: -6, "font-size": 10 }, t).textContent = "ipx/ħ";
      svg("tspan", { dy: 6 }, t).textContent = ", sized by weight";
      const gap = 17, ybase = 140;
      svg("line", { x1: sx(0), y1: 26, x2: sx(0), y2: ybase + 10, stroke: axis, "stroke-width": 1, "stroke-dasharray": "2 3" }, pic);
      U.forEach((u, k) => {
        const pk = P0 + u * sp, a = Math.exp(-u * u / 4), y = ybase - k * gap;
        const ys = XS.map((x) => y - 7 * a * Math.cos(pk * x));
        svg("path", { d: path(XS, ys, sx, (v) => v), fill: "none", stroke: WCOL[k], "stroke-width": 1.6 }, pic);
      });
      text(sx(0) + 6, 34, "all in step at x = 0", { "font-size": 12, class: "mw-muted" });
    }

    // position: Re psi and its envelope
    const yt = top + 46, yb = top + 196, ym = (yt + yb) / 2, amp = (yb - yt) / 2;
    text(x0, top + 22, "position: Re ψ(x), the Gaussian", { "font-weight": 600 });
    svg("line", { x1: x0, y1: ym, x2: x1, y2: ym, stroke: base, "stroke-width": 1 }, pic);
    const env = XS.map((x) => Math.exp(-(x * x) / (4 * s * s)));
    for (const sgn of [1, -1]) svg("path", { d: path(XS, env.map((v) => ym - sgn * amp * v), sx, (v) => v), fill: "none",
      stroke: axis, "stroke-width": 1, "stroke-dasharray": "4 3" }, pic);
    svg("path", { d: path(XS, XS.map((x, j) => ym - amp * env[j] * Math.cos(P0 * x)), sx, (v) => v), fill: "none",
      stroke: TEAL, "stroke-width": 2.4 }, pic);
    svg("line", { x1: x0, y1: yb + 8, x2: x1, y2: yb + 8, stroke: axis, "stroke-width": 1 }, pic);
    for (const xv of [-8, -4, 0, 4, 8]) text(sx(xv), yb + 24, String(xv).replace("-", "−"), { "font-size": 12, "text-anchor": "middle", class: "mw-muted" });

    // momentum: |phi(p)|^2, fixed scale so a wide band flattens
    const pt = 46, pb = top + 196, ymax = 3.3;
    const py = (v) => pb - (Math.min(v, ymax) / ymax) * (pb - pt);
    text(q0, 22, "momentum: |φ(p)|²", { "font-weight": 600 });
    const rho = PS.map((p) => Math.exp(-((p - P0) ** 2) / (2 * sp * sp)) / Math.sqrt(2 * Math.PI * sp * sp));
    svg("path", { d: path(PS, rho, sq, py) + `L${sq(12)},${pb}L${sq(-6)},${pb}Z`, fill: ORANGE, "fill-opacity": 0.2, stroke: "none" }, pic);
    svg("path", { d: path(PS, rho, sq, py), fill: "none", stroke: ORANGE, "stroke-width": 2.2 }, pic);
    if (showWaves) U.forEach((u, k) => {
      const pk = P0 + u * sp, h = Math.exp(-u * u / 2) / Math.sqrt(2 * Math.PI * sp * sp);
      svg("line", { x1: sq(pk), y1: pb, x2: sq(pk), y2: py(h), stroke: WCOL[k], "stroke-width": 3 }, pic);
    });
    svg("line", { x1: q0, y1: pb + 8, x2: q1, y2: pb + 8, stroke: axis, "stroke-width": 1 }, pic);
    for (const [pv, lab] of [[0, "0"], [P0, "p₀"], [6, "6"], [9, "9"]]) text(sq(pv), pb + 24, lab, { "font-size": 12, "text-anchor": "middle", class: "mw-muted" });
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("mw-dark")) { root.classList.toggle("mw-dark", dark); draw(); }
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  draw();
  syncDark();
  return () => { if (obs) obs.disconnect(); };
}

export default { render };
