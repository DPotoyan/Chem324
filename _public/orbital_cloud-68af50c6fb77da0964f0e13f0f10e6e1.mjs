// The real hydrogen orbitals with n <= 3 as 3D point clouds or 90% boundary surfaces (Plotly), rotatable and zoomable.
//
// "points": a sample of positions drawn from |psi|^2 (r from the radial distribution r^2 R^2 by inverse transform
// sampling, the direction by rejection against the angular density), coloured by the SIGN of psi, teal where
// psi > 0 and orange where psi < 0, so every node shows up as a change of colour: 2s is a teal core inside an orange
// shell (node at r = 2 a0), 2p_z is teal above the plane z = 0 and orange below. "surface": the boundary surface
// that encloses 90% of the probability, found on a grid by the density threshold whose region holds 90%; drawn as
// Plotly isosurfaces at psi = +c (teal) and psi = -c (orange). "cut open" drops the half with y > 0 and turns the
// camera onto the cut face, so the shells and lobes can be seen from inside (in surface view the lobes close with
// flat faces at the cut); "same scale" puts every orbital in one box of +-36 a0 so the n^2 growth of the size is
// plain (otherwise each orbital gets its own box).
//
// Plotly is loaded once from its CDN (plotly-2.35.2); this is the one widget with an external dependency, so it
// needs the internet, like the decks' KaTeX. Its stylesheets are copied into the shadow root when the widget renders
// inside one (MyST's {anywidget} directive), since Plotly only injects them into document.head.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch05/01, ch05/02), in a reveal.js deck through a module-script loader, and in Jupyter
// or Colab through the anywidget package. Model keys, optional: fontSize (CSS size), orbitals (the buttons offered,
// an array of keys from ORBITALS; default ["1s", "2s", "3s"]), orbital (the one shown first), view ("points" or
// "surface"), height (plot height in px, default 520), status (false hides the verdict line).

const TEAL = "#107895", ORANGE = "#e07b00";
const PLOTLY_SRC = "https://cdn.plot.ly/plotly-2.35.2.min.js";

// radial functions R_nl(r) for Z = 1, r in a0, in units of a0^{-3/2}
const RAD = {
  10: (r) => 2 * Math.exp(-r),
  20: (r) => (2 - r) * Math.exp(-r / 2) / (2 * Math.sqrt(2)),
  21: (r) => r * Math.exp(-r / 2) / (2 * Math.sqrt(6)),
  30: (r) => 2 * (27 - 18 * r + 2 * r * r) * Math.exp(-r / 3) / (81 * Math.sqrt(3)),
  31: (r) => 4 * (6 - r) * r * Math.exp(-r / 3) / (81 * Math.sqrt(6)),
  32: (r) => 4 * r * r * Math.exp(-r / 3) / (81 * Math.sqrt(30)),
};
// real angular functions on the unit sphere (x, y, z unit vector components), normalized on the sphere
const S0 = 1 / Math.sqrt(4 * Math.PI), P1 = Math.sqrt(3 / (4 * Math.PI)), D1 = Math.sqrt(15 / (4 * Math.PI)),
  D2 = Math.sqrt(15 / (16 * Math.PI)), D0 = Math.sqrt(5 / (16 * Math.PI));
const ANG = {
  s: (x, y, z) => S0,
  px: (x, y, z) => P1 * x, py: (x, y, z) => P1 * y, pz: (x, y, z) => P1 * z,
  dxy: (x, y, z) => D1 * x * y, dyz: (x, y, z) => D1 * y * z, dxz: (x, y, z) => D1 * x * z,
  dx2y2: (x, y, z) => D2 * (x * x - y * y), dz2: (x, y, z) => D0 * (3 * z * z - 1),
};
const SUB = (s) => s.replace(/_\{?([^}]+)\}?/g, "<sub>$1</sub>").replace(/\^2/g, "²");

const ORBITALS = {
  "1s": { n: 1, l: 0, ang: "s", label: "1s", rmax: 9, box: 6, N: 5000,
    desc: "no node, one teal ball. Most probable r: 1 a<sub>0</sub>" },
  "2s": { n: 2, l: 0, ang: "s", label: "2s", rmax: 22, box: 16, N: 7000,
    desc: "one radial node, a sphere at r = 2 a<sub>0</sub>: teal core, orange shell. Most probable r: 5.2 a<sub>0</sub>" },
  "2px": { n: 2, l: 1, ang: "px", label: "2p_x", rmax: 22, box: 16, N: 7000,
    desc: "no radial node; one angular node, the plane x = 0: teal lobe at x &gt; 0, orange at x &lt; 0" },
  "2py": { n: 2, l: 1, ang: "py", label: "2p_y", rmax: 22, box: 16, N: 7000,
    desc: "no radial node; one angular node, the plane y = 0: teal lobe at y &gt; 0, orange at y &lt; 0" },
  "2pz": { n: 2, l: 1, ang: "pz", label: "2p_z", rmax: 22, box: 16, N: 7000,
    desc: "no radial node; one angular node, the plane z = 0: teal lobe above, orange below. Most probable r: 4 a<sub>0</sub>" },
  "3s": { n: 3, l: 0, ang: "s", label: "3s", rmax: 40, box: 36, N: 9000,
    desc: "two radial nodes, spheres at r = 1.9 and 7.1 a<sub>0</sub>: teal core, orange shell, teal outer shell. Most probable r: 13.1 a<sub>0</sub>" },
  "3px": { n: 3, l: 1, ang: "px", label: "3p_x", rmax: 40, box: 36, N: 9000,
    desc: "one radial node (a sphere at r = 6 a<sub>0</sub>) and one angular node (the plane x = 0): each lobe changes sign across the sphere" },
  "3py": { n: 3, l: 1, ang: "py", label: "3p_y", rmax: 40, box: 36, N: 9000,
    desc: "one radial node (a sphere at r = 6 a<sub>0</sub>) and one angular node (the plane y = 0): each lobe changes sign across the sphere" },
  "3pz": { n: 3, l: 1, ang: "pz", label: "3p_z", rmax: 40, box: 36, N: 9000,
    desc: "one radial node (a sphere at r = 6 a<sub>0</sub>) and one angular node (the plane z = 0): each lobe changes sign across the sphere" },
  "3dxy": { n: 3, l: 2, ang: "dxy", label: "3d_{xy}", rmax: 40, box: 36, N: 9000,
    desc: "no radial node; two angular nodes, the planes x = 0 and y = 0: four lobes between the axes, signs alternating" },
  "3dyz": { n: 3, l: 2, ang: "dyz", label: "3d_{yz}", rmax: 40, box: 36, N: 9000,
    desc: "no radial node; two angular nodes, the planes y = 0 and z = 0: four lobes between the y and z axes" },
  "3dxz": { n: 3, l: 2, ang: "dxz", label: "3d_{xz}", rmax: 40, box: 36, N: 9000,
    desc: "no radial node; two angular nodes, the planes x = 0 and z = 0: four lobes between the x and z axes" },
  "3dx2y2": { n: 3, l: 2, ang: "dx2y2", label: "3d_{x^2-y^2}", rmax: 40, box: 36, N: 9000,
    desc: "no radial node; two angular nodes, the planes x = y and x = -y: four lobes along the x and y axes" },
  "3dz2": { n: 3, l: 2, ang: "dz2", label: "3d_{z^2}", rmax: 40, box: 36, N: 9000,
    desc: "no radial node; two angular nodes, the cones at 54.7° to z: two lobes along z (teal) and a ring in the xy plane (orange)" },
};
const DEFAULT_ORDER = ["1s", "2s", "3s"];
const BIGBOX = 36;

const psiOf = (o) => { const R = RAD[10 * o.n + o.l], f = ANG[o.ang]; return (x, y, z) => {
  const r = Math.hypot(x, y, z); if (r < 1e-9) return R(0) * (o.ang === "s" ? S0 : 0);
  return R(r) * f(x / r, y / r, z / r); }; };

// ------------------------------------------------------------------ sampling |psi|^2
// a small deterministic generator (mulberry32), so the clouds look the same every time; a plain linear
// congruential generator correlated the direction draw with the accept draw and biased 2p_z to 67% teal
function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function sample(key) {
  const o = ORBITALS[key], R = RAD[10 * o.n + o.l], f = ANG[o.ang], M = 4000, rand = rng(20261109 + 10 * o.n + o.l);
  const r = new Float64Array(M + 1), cdf = new Float64Array(M + 1);
  for (let i = 0; i <= M; i++) {
    r[i] = o.rmax * i / M;
    const Ri = R(r[i]);
    cdf[i] = (i ? cdf[i - 1] : 0) + r[i] * r[i] * Ri * Ri;
  }
  for (let i = 0; i <= M; i++) cdf[i] /= cdf[M];
  let fmax = 0;                                                      // the largest angular density, for rejection
  for (let i = 0; i <= 60; i++) for (let j = 0; j < 120; j++) {
    const t = Math.PI * i / 60, p = 2 * Math.PI * j / 120, v = f(Math.sin(t) * Math.cos(p), Math.sin(t) * Math.sin(p), Math.cos(t));
    fmax = Math.max(fmax, v * v);
  }
  const x = new Float64Array(o.N), y = new Float64Array(o.N), z = new Float64Array(o.N), sign = new Int8Array(o.N);
  for (let k = 0; k < o.N; k++) {
    const u = rand();
    let lo = 0, hi = M;                                              // inverse transform: first i with cdf[i] >= u
    while (lo < hi) { const m = (lo + hi) >> 1; if (cdf[m] < u) lo = m + 1; else hi = m; }
    const rr = r[lo];
    let cz, sz, ph, fv;
    do {                                                             // a direction, accepted with probability f^2 / fmax
      cz = 2 * rand() - 1; ph = 2 * Math.PI * rand(); sz = Math.sqrt(1 - cz * cz);
      fv = f(sz * Math.cos(ph), sz * Math.sin(ph), cz);
    } while (rand() * fmax > fv * fv);
    x[k] = rr * sz * Math.cos(ph); y[k] = rr * sz * Math.sin(ph); z[k] = rr * cz;
    sign[k] = R(rr) * fv >= 0 ? 1 : -1;
  }
  return { x, y, z, sign };
}

// ------------------------------------------------------------------ the 90% boundary surface on a grid
// psi on a G^3 grid, and the density threshold whose region holds 90% of the probability. "half" zeroes psi for
// y > 0, so the isosurfaces close with flat faces at the cut (a Plotly cap would paint the whole face instead and
// hide the lobes behind a nodal plane such as 3d_xy's y = 0).
function field(key, box, half) {
  const o = ORBITALS[key], psi = psiOf(o), G = 45;
  const xs = new Float64Array(G * G * G), ys = new Float64Array(G * G * G), zs = new Float64Array(G * G * G), vs = new Float64Array(G * G * G);
  let q = 0;
  for (let i = 0; i < G; i++) for (let j = 0; j < G; j++) for (let k = 0; k < G; k++) {
    const x = -box + 2 * box * i / (G - 1), y = -box + 2 * box * j / (G - 1), z = -box + 2 * box * k / (G - 1);
    xs[q] = x; ys[q] = y; zs[q] = z; vs[q] = psi(x, y, z); q++;
  }
  const d = Array.from(vs, (v) => v * v).sort((a, b) => b - a);
  const dV = Math.pow(2 * box / (G - 1), 3);
  let acc = 0, c = d[d.length - 1];
  for (let i = 0; i < d.length; i++) { acc += d[i] * dV; if (acc >= 0.9) { c = d[i]; break; } }
  if (half) for (let i = 0; i < vs.length; i++) if (ys[i] > 1e-9) vs[i] = 0;
  return { xs: Array.from(xs), ys: Array.from(ys), zs: Array.from(zs), vs: Array.from(vs), c: Math.sqrt(c) };
}

// ------------------------------------------------------------------ Plotly
function loadPlotly() {
  if (typeof window === "undefined") return Promise.reject(new Error("no window"));
  if (window.Plotly) return Promise.resolve(window.Plotly);
  if (!window.__chem3240PlotlyLoading) {
    window.__chem3240PlotlyLoading = new Promise((resolve, reject) => {
      const s = document.createElement("script");
      s.src = PLOTLY_SRC; s.async = true;
      s.onload = () => resolve(window.Plotly);
      s.onerror = () => reject(new Error("Plotly did not load"));
      document.head.appendChild(s);
    });
  }
  return window.__chem3240PlotlyLoading;
}

// Plotly puts its CSS in document.head; inside a shadow root it has to be copied in
function adoptPlotlyStyles(el) {
  const root = el.getRootNode && el.getRootNode();
  if (!root || !(typeof ShadowRoot !== "undefined" && root instanceof ShadowRoot)) return;
  document.querySelectorAll('style[id^="plotly.js-style"]').forEach((st) => {
    if (!root.querySelector(`style[data-copy="${st.id}"]`)) {
      const c = st.cloneNode(true); c.removeAttribute("id"); c.setAttribute("data-copy", st.id); root.appendChild(c);
    }
  });
}

const CSS = `
.oc-root { --oc-fg: #212529; --oc-muted: #6c757d; --oc-border: #ced4da; --oc-btn: #f8f9fa; --oc-card: #ffffff; --oc-on: #e7f1f4;
  color: var(--oc-fg); background: var(--oc-card); border: 1px solid var(--oc-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.oc-root.oc-dark { --oc-fg: #e9ecef; --oc-muted: #adb5bd; --oc-border: #495057; --oc-btn: #2b3035; --oc-card: #1e2125; --oc-on: #1f3a44; }
.oc-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.3em; margin: 0 0 0.3em; }
.oc-group { display: flex; flex-wrap: wrap; align-items: center; gap: 0.35em; }
.oc-lab { color: var(--oc-muted); }
.oc-btn { font: inherit; color: var(--oc-fg); background: var(--oc-btn); border: 1px solid var(--oc-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.oc-btn sub { font-size: 70%; }
.oc-btn:hover { border-color: ${TEAL}; }
.oc-btn.oc-active { border-color: ${TEAL}; background: var(--oc-on); font-weight: 600; }
.oc-plot { width: 100%; }
.oc-status { font-weight: 600; margin: 0.2em 0 0; min-height: 1.4em; }
.oc-note { color: var(--oc-muted); }
.oc-wait { color: var(--oc-muted); padding: 2em 0; text-align: center; }
`;

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

  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "oc-root", el);
  root.setAttribute("data-prevent-swipe", "");
  root.style.fontSize = get("fontSize", "15px");

  const wanted = get("orbitals", DEFAULT_ORDER);
  const ORDER = (Array.isArray(wanted) ? wanted : DEFAULT_ORDER).filter((k) => ORBITALS[k]);
  if (!ORDER.length) ORDER.push(...DEFAULT_ORDER);

  const controls = html("div", "oc-controls", root);
  const og = html("div", "oc-group", controls); html("span", "oc-lab", og, "orbital:");
  const obtns = {};
  ORDER.forEach((key) => {
    const b = html("button", "oc-btn", og); b.type = "button"; b.innerHTML = SUB(ORBITALS[key].label);
    b.addEventListener("click", () => { b.blur(); current = key; update(); });
    obtns[key] = b;
  });
  const vg = html("div", "oc-group", controls); html("span", "oc-lab", vg, "view:");
  const ptsBtn = html("button", "oc-btn", vg, "points"); ptsBtn.type = "button";
  ptsBtn.addEventListener("click", () => { ptsBtn.blur(); surface = false; update(); });
  const surfBtn = html("button", "oc-btn", vg, "90% surface"); surfBtn.type = "button";
  surfBtn.addEventListener("click", () => { surfBtn.blur(); surface = true; update(); });
  const cutBtn = html("button", "oc-btn", vg, "cut open"); cutBtn.type = "button";
  cutBtn.addEventListener("click", () => { cutBtn.blur(); cut = !cut; update(); });
  const sameBtn = html("button", "oc-btn", vg, "same scale"); sameBtn.type = "button";
  sameBtn.addEventListener("click", () => { sameBtn.blur(); same = !same; update(); });

  const plotDiv = html("div", "oc-plot", root);
  const height = +get("height", 520);
  plotDiv.style.height = `${height}px`;
  const wait = html("div", "oc-wait", plotDiv, "loading Plotly from cdn.plot.ly ...");

  const status = html("div", "oc-status", root);
  if (get("status", true) === false) status.style.display = "none";
  const note = html("div", "oc-note", root);

  let current = ORBITALS[get("orbital", ORDER[0])] && ORDER.includes(get("orbital", ORDER[0])) ? get("orbital", ORDER[0]) : ORDER[0];
  let cut = false, same = false, surface = get("view", "points") === "surface", Plotly = null, dark = false;
  const clouds = {}, fields = {};

  const isDark = () => typeof document !== "undefined" && document.documentElement.classList.contains("dark");

  function layout(box) {
    const fg = dark ? "#e9ecef" : "#212529", grid = dark ? "#495057" : "#dee2e6", zero = dark ? "#868e96" : "#adb5bd";
    const axis = (title) => ({ range: [-box, box], title: { text: title, font: { size: 13 } }, gridcolor: grid, zerolinecolor: zero,
      showbackground: false, tickfont: { size: 11 }, color: fg });
    return {
      width: plotDiv.clientWidth || 1000, height, margin: { l: 0, r: 0, t: 0, b: 0 },
      paper_bgcolor: "rgba(0,0,0,0)", plot_bgcolor: "rgba(0,0,0,0)", font: { color: fg },
      showlegend: false,
      scene: {
        aspectmode: "cube", xaxis: axis("x (a₀)"), yaxis: axis("y (a₀)"), zaxis: axis("z (a₀)"),
        camera: cut ? { eye: { x: 0.08, y: 2.0, z: 0.45 }, up: { x: 0, y: 0, z: 1 } } : { eye: { x: 1.35, y: 1.35, z: 0.9 } },
      },
    };
  }

  function update() {
    ORDER.forEach((k) => obtns[k].classList.toggle("oc-active", k === current));
    ptsBtn.classList.toggle("oc-active", !surface); surfBtn.classList.toggle("oc-active", surface);
    cutBtn.classList.toggle("oc-active", cut); sameBtn.classList.toggle("oc-active", same);
    const o = ORBITALS[current];
    status.innerHTML = `<b>${SUB(o.label)}</b>: ${o.desc}` + (same ? ". Same box for every orbital: the size grows as n²." : ".");
    note.innerHTML = surface ?
      `The surface encloses 90% of the probability; <span style="color:${TEAL}">teal</span> where ψ &gt; 0, ` +
      `<span style="color:${ORANGE}">orange</span> where ψ &lt; 0. Drag to turn, scroll to zoom.` :
      `Each point is one position drawn from |ψ|²; <span style="color:${TEAL}">teal</span> where ψ &gt; 0, ` +
      `<span style="color:${ORANGE}">orange</span> where ψ &lt; 0. Drag to turn, scroll to zoom.`;
    if (!Plotly) return;
    const box = same ? BIGBOX : o.box;
    let trace;
    if (surface) {
      const fk = `${current}:${box}:${cut ? 1 : 0}`;
      if (!fields[fk]) fields[fk] = field(current, box, cut);
      const F = fields[fk];
      trace = { type: "isosurface", x: F.xs, y: F.ys, z: F.zs, value: F.vs, isomin: -F.c, isomax: F.c,
        surface: { count: 2, fill: 1 }, caps: { x: { show: false }, y: { show: false }, z: { show: false } },
        colorscale: [[0, ORANGE], [0.5, dark ? "#1e2125" : "#ffffff"], [1, TEAL]], cmin: -F.c, cmax: F.c, showscale: false,
        hoverinfo: "skip", lighting: { ambient: 0.65, diffuse: 0.8, specular: 0.15, roughness: 0.6 }, lightposition: { x: 100, y: 200, z: 150 } };
    } else {
      if (!clouds[current]) clouds[current] = sample(current);
      const c = clouds[current];
      const xs = [], ys = [], zs = [], cols = [];
      for (let k = 0; k < c.x.length; k++) {
        if (cut && c.y[k] > 0) continue;
        xs.push(c.x[k]); ys.push(c.y[k]); zs.push(c.z[k]); cols.push(c.sign[k] > 0 ? TEAL : ORANGE);
      }
      trace = { type: "scatter3d", mode: "markers", x: xs, y: ys, z: zs, hoverinfo: "skip",
        marker: { size: current === "1s" ? 3.4 : 3.0, color: cols, opacity: 0.8 } };
    }
    Plotly.react(plotDiv, [trace], layout(box), { displayModeBar: false, responsive: false, staticPlot: false })
      .then(() => adoptPlotlyStyles(el));
  }

  update();
  loadPlotly().then((P) => {
    Plotly = P; dark = isDark();
    if (wait.parentNode) wait.remove();
    update();
    adoptPlotlyStyles(el);
  }).catch(() => { wait.textContent = "Plotly could not be loaded (no internet?)."; });

  // dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const d = isDark();
    root.classList.toggle("oc-dark", d);
    if (d !== dark) { dark = d; if (Plotly) update(); }
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });
  syncDark();

  // reveal.js hides other slides with display: none; redraw when this one appears
  const onShow = () => { if (Plotly && plotDiv.offsetParent !== null) Plotly.Plots.resize(plotDiv); };
  let revealOff = null;
  if (typeof window !== "undefined" && window.Reveal && window.Reveal.on) {
    window.Reveal.on("slidechanged", onShow); revealOff = () => window.Reveal.off && window.Reveal.off("slidechanged", onShow);
  }

  return () => { if (obs) obs.disconnect(); if (revealOff) revealOff(); if (Plotly) Plotly.purge(plotDiv); };
}

export { sample, field, ORBITALS };
export default { render };
