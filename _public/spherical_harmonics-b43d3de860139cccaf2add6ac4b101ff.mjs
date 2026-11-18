// Spherical harmonics on a globe, beside the vector model of the same l and m.
//
// Left: Y_l^m(θ, φ) painted on a sphere seen from outside (orthographic view, the north pole tipped 22° toward the
// viewer). "real part" colours Re Y teal where it is positive and orange where it is negative, white near zero, and
// draws the nodes as dark lines. "density |Y|²" paints |Y|² from white to purple; it does not depend on φ, so only
// bands around the z axis are left: the nodes through the poles belong to the real part. Drag to turn the globe; a
// double click or "reset view" brings the first view back. Right: the vector model of the same l (every allowed
// cone in light purple, the current m in purple) and the readouts L², |L|, L_z, the angle to z and the node count.
//
// Math, with the Condon-Shortley phase of scipy.special.sph_harm_y: Y_l^m = N P_l^m(cos θ) e^{imφ} for m >= 0 and
// Y_l^{-m} = (-1)^m conj(Y_l^m). No trig per pixel: P_l^m(cos θ) = (sin θ)^m q(cos θ) with q from the three-term
// recurrence, and (sin θ)^m e^{imφ} = (x + iy)^m on the unit sphere. ylm(l, m, θ, φ) is exported for tests.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch04/04), in a reveal.js deck through a module-script loader, and in Jupyter or
// Colab through the anywidget package. No dependencies. Model keys, optional: fontSize (CSS size), l (0 to 5) and
// m (the state shown first), view ("wave" for the real part, or "density"), status (false hides the verdict line),
// size (the globe's side in CSS px, default 300).

const TEAL = "#107895", ORANGE = "#e07b00", PURPLE = "#6a3d9a", GRAY = "#6c757d";
const SVGNS = "http://www.w3.org/2000/svg";
const DEG = Math.PI / 180;

const LMAX = 5;
const EL0 = 22 * DEG, AZ0 = -55 * DEG, ELMAX = 85 * DEG;             // first view; elevation limit for drags
const BOX = 2.4, TOP = 1.34;                                         // globe box: 2.4 radii wide, top edge at v = 1.34
const STUB = 1.28;                                                   // the z axis sticks out of the pole to 1.28 radii
const LINE = 1.5;                                                    // nodal line width, CSS px
const TILT = -42 * DEG;                                              // where the arrow meets its cone's rim
const LIGHT = (() => { const v = [-0.45, 0.55, 0.7], n = Math.hypot(...v); return v.map((c) => c / n); })();

const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
const PIX = {                                                        // globe colours, painted pixel by pixel
  light: { base: [255, 255, 255], pos: hex(TEAL), neg: hex(ORANGE), dens: hex(PURPLE), node: hex("#212529") },
  dark: { base: hex("#343a40"), pos: hex("#45a9c6"), neg: hex("#f59f3a"), dens: hex("#b08be0"), node: hex("#e9ecef") },
};

// ------------------------------------------------------------------ Y_l^m
// Everything that depends only on (l, m): the recurrence coefficients and the largest |Y| on the sphere.
function harmonic(l, m) {
  const a = Math.abs(m);
  let ratio = 1;                                                     // (l - a)! / (l + a)!
  for (let k = l - a + 1; k <= l + a; k++) ratio /= k;
  const N = Math.sqrt((2 * l + 1) / (4 * Math.PI) * ratio);
  let dfact = 1;                                                     // (2a - 1)!!
  for (let k = 2 * a - 1; k > 1; k -= 2) dfact *= k;
  // P_a^a = (-1)^a (2a - 1)!! (sin θ)^a. For m < 0, Y_l^{-a} = (-1)^a conj(Y_l^a): the two signs cancel.
  const c0 = N * dfact * (m >= 0 && a % 2 ? -1 : 1);
  const A = new Float64Array(l + 1), B = new Float64Array(l + 1);
  for (let L = a + 1; L <= l; L++) { A[L] = (2 * L - 1) / (L - a); B[L] = (L + a - 1) / (L - a); }
  const h = { l, m, a, c0, A, B, max: 0, k: 1 };
  for (let i = 0; i <= 600; i++) {                                   // |Y| = |q(cos θ)| sin^a θ, largest over θ
    const t = Math.PI * i / 600;
    h.max = Math.max(h.max, Math.abs(qval(h, Math.cos(t))) * Math.sin(t) ** a);
  }
  h.k = 1 / h.max;                                                   // scales Re Y and |Y| to at most 1
  return h;
}

// q(z), with N P_l^a(z) = ± (1 - z²)^{a/2} q(z): q_a = c0, q_{a-1} = 0, (L - a) q_L = (2L - 1) z q_{L-1} - (L + a - 1) q_{L-2}
function qval(h, z) {
  let q0 = 0, q1 = h.c0;
  for (let L = h.a + 1; L <= h.l; L++) { const q2 = h.A[L] * z * q1 - h.B[L] * q0; q0 = q1; q1 = q2; }
  return q1;
}

// Y_l^m(θ, φ) as [re, im], built from the same pieces the globe uses (for tests against scipy)
export function ylm(l, m, theta, phi) {
  const h = harmonic(l, m), x = Math.sin(theta) * Math.cos(phi), y = Math.sin(theta) * Math.sin(phi);
  let re = 1, im = 0;
  for (let k = 0; k < h.a; k++) { const t = re * x - im * y; im = re * y + im * x; re = t; }
  const q = qval(h, Math.cos(theta));
  return [q * re, (m < 0 ? -1 : 1) * q * im];
}

// ------------------------------------------------------------------ drawing
const CSS = `
.sh-root { --sh-fg: #212529; --sh-muted: ${GRAY}; --sh-border: #ced4da; --sh-btn: #f8f9fa; --sh-card: #ffffff;
  --sh-teal: ${TEAL}; --sh-orange: ${ORANGE}; --sh-purple: ${PURPLE}; --sh-cone: #cdb9e3;
  --sh-rim: #868e96; --sh-axis: #495057; --sh-hidden: #adb5bd; --sh-level: #adb5bd; --sh-on: #e7f1f4; --sh-base: #ffffff;
  color: var(--sh-fg); background: var(--sh-card); border: 1px solid var(--sh-border); border-radius: 10px;
  padding: 0.6em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.sh-root.sh-dark { --sh-fg: #e9ecef; --sh-muted: #adb5bd; --sh-border: #495057; --sh-btn: #2b3035; --sh-card: #1e2125;
  --sh-teal: #45a9c6; --sh-orange: #f59f3a; --sh-purple: #b08be0; --sh-cone: #5e4d78;
  --sh-rim: #868e96; --sh-axis: #ced4da; --sh-hidden: #6c757d; --sh-level: #6c757d; --sh-on: #1f3a44; --sh-base: #343a40; }
.sh-root sub { font-size: 0.72em; line-height: 0; vertical-align: -0.25em; }
.sh-controls { display: flex; flex-direction: column; gap: 0.35em; margin: 0 0 0.5em; }
.sh-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.35em 0.6em; }
.sh-lab { min-width: 1em; color: var(--sh-muted); }
.sh-btns { display: flex; flex-wrap: wrap; gap: 0.35em; }
.sh-views { margin-left: auto; }
.sh-btn { font: inherit; color: var(--sh-fg); background: var(--sh-btn); border: 1px solid var(--sh-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; min-width: 2.7em; }
.sh-btn:hover { border-color: ${TEAL}; }
.sh-btn.sh-active { border-color: var(--sh-teal); background: var(--sh-on); font-weight: 600; }
.sh-main { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 0.6em 1.4em; }
.sh-globe { position: relative; flex: 0 0 auto; max-width: 100%; }
.sh-globe canvas { display: block; width: 100%; height: auto; touch-action: none; cursor: grab; }
.sh-globe canvas.sh-grabbing { cursor: grabbing; }
.sh-over { position: absolute; left: 0; top: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible; }
.sh-over text { font-family: inherit; }
.sh-cap { position: absolute; left: 0; top: 0; pointer-events: none; }
.sh-key { position: absolute; right: 0; top: 0.15em; font-size: 0.8em; line-height: 1.35; color: var(--sh-muted);
  pointer-events: none; }
.sh-sw { display: inline-block; width: 0.75em; height: 0.75em; border-radius: 2px; margin-right: 0.35em;
  vertical-align: -0.05em; }
.sh-ramp { display: inline-block; width: 3em; height: 0.7em; border-radius: 2px; margin: 0 0.35em; vertical-align: -0.05em;
  background: linear-gradient(to right, var(--sh-base), var(--sh-purple)); border: 1px solid var(--sh-border); }
.sh-hint { position: absolute; left: 0; bottom: 0; font-size: 0.75em; color: var(--sh-muted); pointer-events: none; }
.sh-btn.sh-reset { position: absolute; right: 0; bottom: 0; font-size: 0.75em; min-width: 0; padding: 0.02em 0.6em; }
.sh-vec { display: block; flex: 0 0 auto; max-width: 100%; height: auto; }
.sh-vec text { font-family: inherit; fill: var(--sh-fg); }
.sh-read { flex: 1 1 11em; align-self: center; display: grid; grid-template-columns: repeat(auto-fill, minmax(10.5em, 1fr));
  gap: 0.2em 1.2em; }
.sh-read .sh-wide { grid-column: 1 / -1; }
.sh-status { font-weight: 600; margin: 0.45em 0 0; min-height: 1.4em; }
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

const clampInt = (v, lo, hi) => Math.min(hi, Math.max(lo, Math.round(+v) || 0));
const signed = (k) => (k > 0 ? `+${k}` : k < 0 ? `−${-k}` : "0");
const SUB = "₀₁₂₃₄₅", SUP = "⁰¹²³⁴⁵";
const yName = (l, m) => `<i>Y</i>${SUB[l]}${m < 0 ? "⁻" : ""}${SUP[Math.abs(m)]}`;

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };
  const S = Math.round(Math.min(640, Math.max(160, +get("size", 300) || 300)));   // globe side, CSS px
  const VW = Math.round(1.15 * S);                                                 // vector model width
  const RG = S / BOX, CX = S / 2, CY = S * TOP / BOX;                              // globe radius and center, CSS px

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "sh-root", el);
  root.setAttribute("data-prevent-swipe", "");                       // reveal.js: drags must not change slides
  root.style.fontSize = get("fontSize", "15px");
  let fpx = /px$/.test(root.style.fontSize) ? parseFloat(root.style.fontSize) : NaN;
  if (!(fpx > 0)) { try { fpx = parseFloat(getComputedStyle(root).fontSize); } catch (e) { /* not attached yet */ } }
  if (!(fpx > 0)) fpx = 15;

  const button = (parent, label, act, cls) => {
    const b = html("button", "sh-btn" + (cls ? " " + cls : ""), parent, label); b.type = "button";
    b.addEventListener("click", () => { b.blur(); act(); });         // blur: keys go back to the page or deck
    return b;
  };

  const controls = html("div", "sh-controls", root);
  const rowL = html("div", "sh-row", controls), rowM = html("div", "sh-row", controls);
  html("span", "sh-lab", rowL).innerHTML = "<i>l</i>";
  const lBox = html("div", "sh-btns", rowL);
  const vBox = html("div", "sh-btns sh-views", rowL);
  html("span", "sh-lab", rowM).innerHTML = "<i>m</i>";
  const mBox = html("div", "sh-btns", rowM);
  const lButtons = [];
  for (let k = 0; k <= LMAX; k++) lButtons.push(button(lBox, String(k), () => choose(k, m)));
  const vWave = button(vBox, "real part", () => { view = "wave"; update(); });
  const vDens = button(vBox, "density |Y|²", () => { view = "density"; update(); });

  const main = html("div", "sh-main", root);
  const globe = html("div", "sh-globe", main);
  globe.style.width = S + "px";
  const canvas = html("canvas", null, globe);
  canvas.setAttribute("role", "img");
  const ctx = canvas.getContext("2d");
  const over = svg("svg", { class: "sh-over", viewBox: `0 0 ${S} ${S}`, "aria-hidden": "true" }, globe);
  const equator = svg("path", { fill: "none", stroke: "var(--sh-rim)", "stroke-width": 1.1, "stroke-dasharray": "0.5 3.5",
    "stroke-linecap": "round" }, over);
  svg("circle", { cx: CX, cy: CY, r: RG, fill: "none", stroke: "var(--sh-rim)", "stroke-width": 1 }, over);
  const axisHidden = svg("line", { stroke: "var(--sh-axis)", "stroke-width": 1.4, "stroke-dasharray": "2.5 2.5",
    opacity: 0.5 }, over);
  const axisLine = svg("line", { stroke: "var(--sh-axis)", "stroke-width": 1.6 }, over);
  const axisLab = svg("text", { "font-size": "0.85em", "font-style": "italic" }, over);
  axisLab.textContent = "z";
  const cap = html("div", "sh-cap", globe);
  const key = html("div", "sh-key", globe);
  html("div", "sh-hint", globe, "drag to turn");
  button(globe, "reset view", () => resetView(), "sh-reset");

  const vec = svg("svg", { class: "sh-vec", viewBox: `0 0 ${VW} ${S}`, width: VW, height: S, role: "img" }, main);
  const read = html("div", "sh-read", main);

  const status = html("div", "sh-status", root);
  if (get("status", true) === false) status.style.display = "none";

  // ---------------------------------------------------------------- state
  let l = clampInt(get("l", 2), 0, LMAX);
  let m = clampInt(get("m", 1), -l, l);
  let view = get("view", "wave") === "density" ? "density" : "wave";
  let h = harmonic(l, m);
  let az = AZ0, el0 = EL0;                                           // camera azimuth and elevation (radians)
  let dark = false;

  // ---------------------------------------------------------------- the globe
  // The backing store matches the globe's size on screen (reveal.js scales whole slides) times devicePixelRatio, and
  // is halved while dragging. Two buffers, full and fast; s holds Re Y / max (or |Y|² / max) and NaN off the globe.
  const bufs = {};
  const wantN = (fast) => {
    const dpr = Math.min(3, Math.max(1, (typeof window !== "undefined" && window.devicePixelRatio) || 1));
    let w = S;
    try { const r = canvas.getBoundingClientRect(); if (r.width > S) w = Math.min(r.width, 2.5 * S); } catch (e) { /* detached */ }
    return Math.max(48, Math.min(1600, Math.round(w * dpr * (fast ? 0.5 : 1))));
  };

  function paintGlobe(fast) {
    const n = wantN(fast), slot = fast ? "fast" : "full";
    if (!bufs[slot] || bufs[slot].n !== n) bufs[slot] = { n, s: new Float32Array(n * n).fill(NaN), img: ctx.createImageData(n, n) };
    if (canvas.width !== n || canvas.height !== n) { canvas.width = n; canvas.height = n; }
    const { s, img } = bufs[slot], data = img.data, wave = view === "wave", a = h.a, kn = h.k;
    // pixel (i, j) shows the sphere point u ex + v ey + w cam, u right, v up, w toward the viewer, all in radii;
    // rows and columns 0 and n - 1 stay empty, so every pixel on the globe has four neighbours in the buffer
    const R = n / BOX, cx = n / 2, cy = n * TOP / BOX, reach = 1 + 0.5 / R;   // reach: the antialiased rim
    const j0 = Math.max(1, Math.floor(cy - reach * R)), j1 = Math.min(n - 2, Math.ceil(cy + reach * R));
    const cols = (v) => { const t = reach * reach - v * v, half = t > 0 ? Math.sqrt(t) * R : -1;
      return [Math.max(1, Math.floor(cx - half)), Math.min(n - 2, Math.ceil(cx + half))]; };

    // cam = (cos el cos az, cos el sin az, sin el), ex = (-sin az, cos az, 0), ey = cam × ex
    const ce = Math.cos(el0), se = Math.sin(el0), ca = Math.cos(az), sa = Math.sin(az);
    const exx = -sa, exy = ca, eyx = -se * ca, eyy = -se * sa, eyz = ce, czx = ce * ca, czy = ce * sa, czz = se;
    for (let j = j0; j <= j1; j++) {
      const v0 = (cy - j - 0.5) / R, [i0, i1] = cols(v0);
      for (let i = i0; i <= i1; i++) {
        let u = (i + 0.5 - cx) / R, v = v0;
        const r = Math.sqrt(u * u + v * v);
        if (r >= reach) continue;
        if (r > 1) { u /= r; v /= r; }                               // the rim: points on the limb
        const w = Math.sqrt(Math.max(0, 1 - u * u - v * v));
        const x = u * exx + v * eyx + w * czx, y = u * exy + v * eyy + w * czy, z = v * eyz + w * czz;
        const q = qval(h, z) * kn;
        if (wave) {                                                  // Re Y / max: q Re[(x + iy)^a]
          let re = 1, im = 0;
          for (let k = 0; k < a; k++) { const t = re * x - im * y; im = re * y + im * x; re = t; }
          s[j * n + i] = q * re;
        } else {                                                     // |Y|² / max: q² (x² + y²)^a
          const rr = x * x + y * y;
          let p = q * q;
          for (let k = 0; k < a; k++) p *= rr;
          s[j * n + i] = p;
        }
      }
    }

    const P = PIX[dark ? "dark" : "light"], hw = 0.5 * LINE * n / S;
    const [b0, b1, b2] = P.base, [d0, d1, d2] = P.node, [L0, L1, L2] = LIGHT;
    for (let j = j0; j <= j1; j++) {
      const v0 = (cy - j - 0.5) / R, [i0, i1] = cols(v0);
      for (let i = i0; i <= i1; i++) {
        let u = (i + 0.5 - cx) / R, v = v0;
        const r = Math.sqrt(u * u + v * v);
        if (r >= reach) continue;
        const cover = Math.min(1, (1 - r) * R + 0.5);
        if (r > 1) { u /= r; v /= r; }
        const w = Math.sqrt(Math.max(0, 1 - u * u - v * v)), sh = 0.5 + 0.5 * Math.max(0, u * L0 + v * L1 + w * L2);
        const k = j * n + i, sv = s[k];
        let c0, c1, c2;
        if (wave) {
          const c = sv >= 0 ? P.pos : P.neg, f = Math.min(1, Math.abs(sv));
          c0 = (b0 + f * (c[0] - b0)) * sh; c1 = (b1 + f * (c[1] - b1)) * sh; c2 = (b2 + f * (c[2] - b2)) * sh;
          if (l > 0) {
            // the nodal line: |s| / |grad s| is the distance to the nearest zero of Re Y in pixels; it sets the coverage
            const sl = s[k - 1], sr = s[k + 1], su = s[k - n], sd = s[k + n];
            const hl = sl === sl, hr = sr === sr, hu = su === su, hd = sd === sd;     // NaN: off the globe
            const gx = hl && hr ? 0.5 * (sr - sl) : hr ? sr - sv : hl ? sv - sl : 0;
            const gy = hu && hd ? 0.5 * (sd - su) : hd ? sd - sv : hu ? sv - su : 0;
            const gr = Math.sqrt(gx * gx + gy * gy);
            const ink = gr > 0 ? Math.min(1, Math.max(0, hw + 0.5 - Math.abs(sv) / gr)) : 0;
            if (ink > 0) { c0 += ink * (d0 - c0); c1 += ink * (d1 - c1); c2 += ink * (d2 - c2); }
          }
        } else {
          const c = P.dens, f = Math.min(1, sv);
          c0 = (b0 + f * (c[0] - b0)) * sh; c1 = (b1 + f * (c[1] - b1)) * sh; c2 = (b2 + f * (c[2] - b2)) * sh;
        }
        const o = 4 * k;
        data[o] = c0; data[o + 1] = c1; data[o + 2] = c2; data[o + 3] = 255 * cover;
      }
    }
    ctx.putImageData(img, 0, 0);
    overlay();
  }

  // the visible half of the equator, and the z axis leaving the north pole (dashed where the globe hides it)
  function overlay() {
    const ce = Math.cos(el0), se = Math.sin(el0);
    let d = "";
    for (let i = 0; i <= 48; i++) {                                  // ψ = φ - az from -90° to 90°: u = sin ψ, v = -sin(el) cos ψ
      const p = -Math.PI / 2 + Math.PI * i / 48;
      d += (i ? "L" : "M") + (CX + RG * Math.sin(p)).toFixed(1) + "," + (CY + RG * se * Math.cos(p)).toFixed(1);
    }
    equator.setAttribute("d", d);
    equator.style.display = view === "wave" && (l - Math.abs(m)) % 2 ? "none" : "";   // P_l^m(0) = 0: already a node
    const Yt = (t) => CY - RG * t * ce;                              // the point t z of the axis, on screen
    const tv = se >= 0 ? 1 : Math.min(STUB, Math.max(1, 1 / ce));    // seen from below, the stub hides behind the globe
    const seg = (e, t0, t1) => {
      e.style.display = t1 > t0 + 1e-6 ? "" : "none";
      e.setAttribute("x1", CX); e.setAttribute("x2", CX);
      e.setAttribute("y1", Yt(t0).toFixed(1)); e.setAttribute("y2", Yt(t1).toFixed(1));
    };
    seg(axisLine, tv, STUB);
    seg(axisHidden, 1, tv);
    axisLab.setAttribute("x", (CX + 6).toFixed(1));
    axisLab.setAttribute("y", (Yt(STUB) + 0.32 * fpx).toFixed(1));
    axisLab.style.fill = tv < STUB ? "var(--sh-axis)" : "var(--sh-hidden)";
  }

  // ---------------------------------------------------------------- the vector model
  function drawVector() {
    vec.innerHTML = "";
    const RM = Math.sqrt(LMAX * (LMAX + 1)), pad = 4, lab = 2.6 * 0.85 * fpx;   // one scale for every l
    const U = Math.min((S - 2 * pad) / (2 * RM + 0.95), (VW - 2 * pad - lab) / (2 * RM + 0.45));
    const AX = (VW - (2 * RM + 0.45) * U - lab) / 2 + (RM + 0.1) * U, OY = pad + (RM + 0.62) * U;
    const X = (x) => (AX + x * U).toFixed(1), Y = (y) => (OY - y * U).toFixed(1);
    const text = (x, y, str, attrs) => { const t = svg("text", Object.assign({ x, y }, attrs || {}), vec); t.textContent = str; return t; };

    text(pad, (pad + 0.8 * fpx).toFixed(1), "vector model", { "font-size": "0.85em", style: "fill: var(--sh-muted)" });
    const top = RM + 0.55, bot = -(RM + 0.3);                        // the z axis
    svg("line", { x1: X(0), x2: X(0), y1: Y(bot), y2: (OY - top * U + 8).toFixed(1), stroke: "var(--sh-fg)",
      "stroke-width": 1.5 }, vec);
    const ty = OY - top * U;
    svg("polygon", { points: `${X(0)},${ty.toFixed(1)} ${(AX - 4.5).toFixed(1)},${(ty + 10).toFixed(1)} ` +
      `${(AX + 4.5).toFixed(1)},${(ty + 10).toFixed(1)}`, fill: "var(--sh-fg)" }, vec);
    text((AX + 8).toFixed(1), (ty + 0.7 * fpx).toFixed(1), "z", { "font-size": "0.9em", "font-style": "italic" });

    if (l === 0) {                                                   // no vector at all
      svg("circle", { cx: X(0), cy: Y(0), r: 4.5, fill: "var(--sh-purple)" }, vec);
      const t = text((AX + 10).toFixed(1), (OY + 0.3 * fpx).toFixed(1), "", { "font-size": "0.85em", style: "fill: var(--sh-purple)" });
      svg("tspan", { "font-style": "italic" }, t).textContent = "L";
      svg("tspan", {}, t).textContent = " = 0";
      return;
    }
    const R = Math.sqrt(l * (l + 1));
    svg("circle", { cx: X(0), cy: Y(0), r: (R * U).toFixed(1), fill: "none", stroke: "var(--sh-muted)", "stroke-width": 1,
      "stroke-dasharray": "1.5 3" }, vec);
    const cone = (k, col, w1, w2) => {                               // rim at height k and the two sides from the origin
      const r = Math.sqrt(R * R - k * k);
      svg("ellipse", { cx: X(0), cy: Y(k), rx: (r * U).toFixed(1), ry: (0.2 * r * U).toFixed(1), fill: "none", stroke: col,
        "stroke-width": w1 }, vec);
      svg("path", { d: `M${X(-r)},${Y(k)}L${X(0)},${Y(0)}L${X(r)},${Y(k)}`, fill: "none", stroke: col, "stroke-width": w2,
        "stroke-linejoin": "round" }, vec);
      return r;
    };
    for (let k = -l; k <= l; k++) {
      svg("line", { x1: (AX + 3).toFixed(1), x2: X(R + 0.25), y1: Y(k), y2: Y(k), stroke: "var(--sh-level)", "stroke-width": 0.9,
        "stroke-dasharray": "2 3" }, vec);
    }
    for (let k = -l; k <= l; k++) if (k !== m) cone(k, "var(--sh-cone)", 1.4, 1.1);
    const r = cone(m, "var(--sh-purple)", 2.2, 1.6);
    const x1 = AX, y1 = OY, x2 = AX + r * Math.cos(TILT) * U, y2 = OY - (m + 0.2 * r * Math.sin(TILT)) * U;
    const len = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / len, uy = (y2 - y1) / len, hl = Math.min(11, 0.45 * len);
    svg("line", { x1: x1.toFixed(1), y1: y1.toFixed(1), x2: (x2 - ux * hl * 0.8).toFixed(1), y2: (y2 - uy * hl * 0.8).toFixed(1),
      stroke: "var(--sh-purple)", "stroke-width": 2.4 }, vec);
    const bx = x2 - ux * hl, by = y2 - uy * hl;
    svg("polygon", { points: `${x2.toFixed(1)},${y2.toFixed(1)} ${(bx - uy * 4.5).toFixed(1)},${(by + ux * 4.5).toFixed(1)} ` +
      `${(bx + uy * 4.5).toFixed(1)},${(by - ux * 4.5).toFixed(1)}`, fill: "var(--sh-purple)" }, vec);
    svg("circle", { cx: X(0), cy: Y(m), r: 4, fill: "var(--sh-purple)" }, vec);
    for (let k = -l; k <= l; k++) {                                  // labels last, on top
      const y = (OY - k * U + 0.3 * 0.85 * fpx).toFixed(1);
      if (k === m) {
        const t = text(X(R + 0.35), y, "", { "font-size": "0.85em", style: "fill: var(--sh-purple); font-weight: 700" });
        svg("tspan", { "font-style": "italic" }, t).textContent = "m";
        svg("tspan", {}, t).textContent = ` = ${signed(k)}`;
      } else {
        text(X(R + 0.35), y, signed(k), { "font-size": "0.85em", style: "fill: var(--sh-muted)" });
      }
    }
  }

  // ---------------------------------------------------------------- words
  const angle = () => Math.acos(m / Math.sqrt(l * (l + 1))) / DEG;

  function readouts() {
    const L2 = l * (l + 1), a = Math.abs(m);
    const lz = m === 0 ? "0" : `${m > 0 ? "+" : "−"}${a === 1 ? "" : a}ħ`;
    const items = [
      `<i>L</i>² = <i>l</i>(<i>l</i> + 1)ħ² = ${L2 ? L2 + "ħ²" : "0"}`,
      `|<i>L</i>| = ${l ? `√${L2} ħ = ${Math.sqrt(L2).toFixed(2)}ħ` : "0"}`,
      `<i>L<sub>z</sub></i> = <i>m</i>ħ = ${lz}`,
      `angle to <i>z</i>: ${l ? angle().toFixed(1) + "°" : "none (<i>L</i> = 0)"}`,
    ];
    read.innerHTML = items.map((s) => `<div>${s}</div>`).join("") +
      `<div class="sh-wide">nodes: ${l - a} around the axis + ${a} through the poles = ${l}</div>`;
  }

  function verdict() {
    const a = Math.abs(m), one = l === 1;
    if (l === 0) return `<i>l</i> = 0: no angular momentum. ${yName(0, 0)} is the same everywhere on the sphere, with no nodes.`;
    if (view === "density") {
      return m === 0 ? "<i>m</i> = 0: <i>Y</i> is real, so its density keeps the same circles of nodes." :
        "|<i>Y</i>|² does not depend on φ: a state with sharp <i>L<sub>z</sub></i> is symmetric about <i>z</i>. " +
        "The nodes through the poles belong to the real part only.";
    }
    if (m === 0) {
      return `<i>m</i> = 0: nothing depends on φ. ${one ? "Its one node is a circle" : `All ${l} nodes are circles`} around ` +
        "the <i>z</i> axis, and <i>L</i> lies flat, perpendicular to <i>z</i>.";
    }
    if (a === l) {                                                   // m = -l leans toward -z by the same angle
      return `|<i>m</i>| = <i>l</i>: <i>L</i> leans as close to ${m < 0 ? "−" : ""}<i>z</i> as it can, ` +
        `${(m < 0 ? 180 - angle() : angle()).toFixed(1)}° away. ${one ? "Its one node passes" : `All ${l} nodes pass`} through the poles.`;
    }
    const k = l - a;
    return `${k} node${k === 1 ? "" : "s"} around the axis and ${a} through the poles: <i>l</i> = ${l} in all.`;
  }

  // ---------------------------------------------------------------- updates
  function update() {
    lButtons.forEach((b, k) => b.classList.toggle("sh-active", k === l));
    vWave.classList.toggle("sh-active", view === "wave");
    vDens.classList.toggle("sh-active", view === "density");
    mBox.innerHTML = "";
    for (let k = -l; k <= l; k++) button(mBox, signed(k), () => choose(l, k)).classList.toggle("sh-active", k === m);
    cap.innerHTML = view === "wave" ? `Re ${yName(l, m)}` : `|${yName(l, m)}|²`;
    key.innerHTML = view === "wave" ?
      '<span class="sh-sw" style="background: var(--sh-teal)"></span>positive<br>' +
      '<span class="sh-sw" style="background: var(--sh-orange)"></span>negative' :
      '0<span class="sh-ramp"></span>max';
    canvas.setAttribute("aria-label", `${view === "wave" ? "the real part of" : "the density of"} the spherical harmonic ` +
      `with l = ${l} and m = ${m}, on a sphere`);
    paintGlobe(false);
    drawVector();
    readouts();
    status.innerHTML = verdict();
  }

  function choose(nl, nm) {
    if (nl !== l) { l = nl; m = Math.max(-l, Math.min(l, nm)); } else m = nm;   // |m| > l: clamp, keeping the sign
    h = harmonic(l, m);
    update();
  }

  function resetView() { az = AZ0; el0 = EL0; paintGlobe(false); }

  // ---------------------------------------------------------------- dragging turns the globe
  let drag = null, timer = 0;
  const schedule = () => { if (!timer) timer = setTimeout(() => { timer = 0; paintGlobe(true); }, 16); };
  canvas.addEventListener("pointerdown", (e) => {
    if (e.button > 0) return;
    drag = { x: e.clientX, y: e.clientY, az, el: el0, moved: false };
    try { canvas.setPointerCapture(e.pointerId); } catch (err) { /* synthetic events have no capturable pointer */ }
    canvas.classList.add("sh-grabbing");
    e.preventDefault();
  });
  canvas.addEventListener("pointermove", (e) => {
    if (!drag) return;
    e.preventDefault();
    const r = canvas.getBoundingClientRect();                        // includes the scaling reveal.js applies to slides
    if (!r.width) return;
    const k = S / r.width, dx = (e.clientX - drag.x) * k, dy = (e.clientY - drag.y) * k;
    if (Math.abs(dx) + Math.abs(dy) > 1) drag.moved = true;
    az = drag.az - dx / RG;                                          // drag right: the surface follows the pointer
    el0 = Math.max(-ELMAX, Math.min(ELMAX, drag.el + dy / RG));      // drag down: the north pole tips toward you
    schedule();
  });
  const release = (e) => {
    if (!drag) return;
    const moved = drag.moved;
    drag = null;
    try { canvas.releasePointerCapture(e.pointerId); } catch (err) { /* already released */ }
    canvas.classList.remove("sh-grabbing");
    clearTimeout(timer); timer = 0;
    if (moved) paintGlobe(false);                                    // full resolution again
  };
  canvas.addEventListener("pointerup", release);
  canvas.addEventListener("pointercancel", release);
  canvas.addEventListener("dblclick", (e) => { e.preventDefault(); resetView(); });

  // ---------------------------------------------------------------- sharp at any slide scale
  // A deck lays a slide out before showing it and rescales it with the window: repaint at the new size when the
  // globe comes into view, after a resize, or when the pointer arrives.
  const refresh = () => { if (!drag && wantN(false) !== canvas.width) paintGlobe(false); };
  const io = typeof IntersectionObserver !== "undefined" ?
    new IntersectionObserver((es) => { if (es.some((e) => e.isIntersecting)) refresh(); }) : null;
  if (io) io.observe(canvas);
  let later = 0;
  const onResize = () => { clearTimeout(later); later = setTimeout(refresh, 200); };
  if (typeof window !== "undefined") window.addEventListener("resize", onResize);
  canvas.addEventListener("pointerenter", refresh);

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const isDark = () => !!html0 && html0.classList.contains("dark");
  const syncDark = () => {
    if (isDark() === dark) return;
    dark = !dark;
    root.classList.toggle("sh-dark", dark);
    paintGlobe(false);                                               // the globe's colours are baked into pixels
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  dark = isDark();
  root.classList.toggle("sh-dark", dark);
  update();
  return () => {
    if (obs) obs.disconnect();
    if (io) io.disconnect();
    if (typeof window !== "undefined") window.removeEventListener("resize", onResize);
    clearTimeout(timer); clearTimeout(later);
  };
}

export default { render };
