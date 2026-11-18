// Hunt for the eigenvectors of a 2x2 matrix, or turn the axes until the matrix is diagonal.
//
// mode "hunt": v is a unit arrow (teal), aimed by dragging anywhere on the plane, and Av is drawn in red.
// Most arrows come out turned. Within 3 degrees of an eigen-direction v snaps onto it (Av = λv lies on the
// line of v) and the direction stays marked, dashed purple. "sweep" carries v once around the circle,
// pausing on each eigen-direction, and traces the tips of Av: the image of the circle.
// mode "axes": two perpendicular unit axes u1, u2 (teal), turned by dragging. The panel shows the same
// matrix in those axes, A'_mn = <u_m|A|u_n>. Each red arrow Au_n splits into a part along its own axis
// (purple, the diagonal entry) and a part along the other axis (orange, the off-diagonal entry). Trace and
// determinant never change, and the matrix is diagonal when the axes are eigenvectors (snap within 2 degrees).
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs
// in MyST's {anywidget} directive (ch03/04, ch03/05), in a reveal.js deck through a module-script loader
// (slides/ch03/05, 05b), and in Jupyter or Colab through the anywidget package. No dependencies.
// Model keys, all optional: mode ("hunt" or "axes"; anything else means hunt), matrix ([[a, b], [c, d]],
// real; default [[2, 1], [1, 2]]), presets (true: buttons for a symmetric matrix, one that is not, and a
// rotation; hunt mode only, replaces matrix) and fontSize (CSS size; the plane is 22em wide).

const TEAL = "#107895", CARDINAL = "#C8102E", PURPLE = "#6a3d9a", ORANGE = "#e07b00";
const SVGNS = "http://www.w3.org/2000/svg";
const DEG = Math.PI / 180;
const W = 400, C0 = W / 2;              // the plane's viewBox is W x W, origin in the middle

const PRESETS = [
  { label: "symmetric", m: [[2, 1], [1, 2]], start: 0 },
  { label: "not symmetric", m: [[1, 1], [0, 2]], start: 100 },
  { label: "rotation", m: [[0, 1], [-1, 0]], start: 30 },      // the two-point d/dx of Operators 2
];

const PAL = {
  light: { teal: TEAL, red: CARDINAL, purple: PURPLE, orange: ORANGE, grid: "#eceef1", axis: "#adb5bd", card: "#ffffff" },
  dark: { teal: "#45a9c6", red: "#f05d6f", purple: "#b08be0", orange: "#f5a142", grid: "#2f3439", axis: "#6c757d", card: "#1e2125" },
};

const CSS = `
.mx-root { --mx-fg: #212529; --mx-muted: #6c757d; --mx-border: #ced4da; --mx-btn: #f8f9fa; --mx-on: #e3f0f4;
  --mx-card: #ffffff; --mx-teal: ${TEAL}; --mx-red: ${CARDINAL}; --mx-purple: ${PURPLE}; --mx-orange: #b85f00;
  display: flex; flex-wrap: wrap; align-items: flex-start; gap: 0.6em 1.4em; color: var(--mx-fg);
  background: var(--mx-card); border: 1px solid var(--mx-border); border-radius: 10px; padding: 0.8em 1em;
  text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit; box-sizing: border-box;
  max-width: 100%; margin: 0.6em 0 1.2em; }
.mx-root.mx-dark { --mx-fg: #e9ecef; --mx-muted: #adb5bd; --mx-border: #495057; --mx-btn: #2b3035; --mx-on: #16353f;
  --mx-card: #1e2125; --mx-teal: #45a9c6; --mx-red: #f05d6f; --mx-purple: #b08be0; --mx-orange: #f5a142; }
.mx-plane { display: block; flex: 0 1 auto; width: 22em; max-width: 100%; height: auto; touch-action: none;
  cursor: crosshair; user-select: none; -webkit-user-select: none; }
.mx-plane text { font-family: inherit; }
.mx-side { flex: 1 1 13em; min-width: 12em; }
.mx-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em; margin: 0.15em 0 0.5em; }
.mx-label { color: var(--mx-muted); margin-right: 0.2em; }
.mx-btn { font: inherit; color: var(--mx-fg); background: var(--mx-btn); border: 1px solid var(--mx-border);
  border-radius: 999px; padding: 0.15em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.mx-btn:hover { border-color: ${TEAL}; }
.mx-btn.mx-on { border-color: ${TEAL}; background: var(--mx-on); font-weight: 600; }
.mx-btn.mx-go { border-color: ${TEAL}; color: #fff; background: ${TEAL}; font-weight: 600; }
.mx-btn.mx-go:hover { filter: brightness(1.1); }
.mx-mrow { display: flex; flex-wrap: wrap; align-items: center; gap: 0.2em 0.5em; margin: 0.3em 0; }
.mx-mat { display: inline-grid; grid-template-columns: auto auto; column-gap: 1em; padding: 0.1em 0.5em;
  border-left: 2px solid currentColor; border-right: 2px solid currentColor; border-radius: 0.6em;
  font-variant-numeric: tabular-nums; text-align: right; }
.mx-line { font-variant-numeric: tabular-nums; margin: 0.1em 0; }
.mx-status { font-weight: 600; margin: 0.5em 0 0.2em; min-height: 2.8em; }
.mx-found { margin: 0.2em 0 0.5em; min-height: 2.8em; }
.mx-found:empty { min-height: 0; margin: 0; }
.mx-muted { color: var(--mx-muted); font-weight: normal; }
.mx-teal { color: var(--mx-teal); } .mx-red { color: var(--mx-red); }
.mx-purple { color: var(--mx-purple); } .mx-orange { color: var(--mx-orange); }
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

// ---------------------------------------------------------------- 2x2 algebra
const mul = (M, v) => [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]];
const dot = (a, b) => a[0] * b[0] + a[1] * b[1];
const dir = (deg) => [Math.cos(deg * DEG), Math.sin(deg * DEG)];
const wrap = (x, p) => x - p * Math.round(x / p);                 // into [-p/2, p/2]

function asMatrix(m) {
  if (!Array.isArray(m) || m.length !== 2) return null;
  const rows = m.map((r) => (Array.isArray(r) && r.length === 2 ? r.map(Number) : null));
  return rows.every((r) => r && r.every(Number.isFinite)) ? rows : null;
}

function sigmaMax([[a, b], [c, d]]) {                              // the longest Av for a unit v
  const T = a * a + b * b + c * c + d * d, D = (a * d - b * c) ** 2;
  return Math.sqrt((T + Math.sqrt(Math.max(0, T * T - 4 * D))) / 2);
}

// eigenvalues and eigen-directions (angles in [0, 180)) of a real 2x2 matrix
function analyze(M) {
  const [[a, b], [c, d]] = M, tr = a + d, det = a * d - b * c, disc = tr * tr - 4 * det;
  const tol = 1e-12 * Math.max(1, a * a + b * b + c * c + d * d);
  if (Math.abs(b) < 1e-12 && Math.abs(c) < 1e-12 && Math.abs(a - d) < 1e-12) return { kind: "scalar", lam: a, dirs: [] };
  if (disc < -tol) return { kind: "complex", re: tr / 2, im: Math.sqrt(-disc) / 2, dirs: [] };
  const r = Math.sqrt(Math.max(0, disc));
  const lams = r < 1e-9 ? [tr / 2] : [(tr + r) / 2, (tr - r) / 2];
  const dirs = lams.map((lam) => {
    const r1 = [a - lam, b], r2 = [c, d - lam];                     // v is perpendicular to the rows of A - λI
    const row = Math.hypot(r1[0], r1[1]) >= Math.hypot(r2[0], r2[1]) ? r1 : r2;
    const ang = Math.atan2(row[0], -row[1]) / DEG;
    return { lam, ang: ((ang % 180) + 180) % 180 };
  });
  return { kind: dirs.length === 2 ? "two" : "one", dirs };
}

// ---------------------------------------------------------------- number formats (Unicode minus)
const minus = (s) => s.replace("-", "−");
const num = (v) => minus(Math.abs(v - Math.round(v)) < 1e-9 ? String(Math.round(v)) : v.toFixed(2));
const fix = (v) => minus((Math.abs(v) < 0.005 ? 0 : v).toFixed(2));
const times = (lam) => (Math.abs(lam) < 1e-9 ? "0" : Math.abs(lam - 1) < 1e-9 ? "v" : Math.abs(lam + 1) < 1e-9 ? "−v" : `${num(lam)}v`);
const cnum = (re, im) => {
  const i = Math.abs(im - 1) < 1e-9 ? "i" : `${num(im)}i`;
  return Math.abs(re) < 1e-9 ? `±${i}` : `${num(re)} ± ${i}`;
};
const matHTML = (M, f, cls) => `<span class="mx-mat">${[0, 1].map((r) => [0, 1].map((c) =>
  `<span class="${cls ? cls[r][c] : ""}">${f(M[r][c])}</span>`).join("")).join("")}</span>`;

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };
  const mode = get("mode", "hunt") === "axes" ? "axes" : "hunt";
  const presets = mode === "hunt" && get("presets", false) === true;
  const given = asMatrix(get("matrix", null)) || [[2, 1], [1, 2]];
  const R = 1.12 * Math.max(1.25, ...(presets ? PRESETS.map((p) => sigmaMax(p.m)) : [sigmaMax(given)]));
  const S = (C0 - 14) / R;                                        // px per unit
  const X = (x) => C0 + S * x, Y = (y) => C0 - S * y;

  let A, info, start, phi, theta = 0, found, trace, swept, timer = 0, which = 0;

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "mx-root", el);
  root.setAttribute("data-prevent-swipe", "");                   // reveal.js: dragging must not change slides
  root.style.fontSize = get("fontSize", "15px");
  const plane = svg("svg", { viewBox: `0 0 ${W} ${W}`, class: "mx-plane", role: "img", "aria-label": mode === "hunt"
    ? "a unit arrow v and its image Av; drag to aim v" : "two perpendicular axes and the images of their unit arrows; drag to turn the axes" }, root);
  const side = html("div", "mx-side", root);
  const button = (parent, label, cls, act) => {
    const b = html("button", "mx-btn" + (cls ? " " + cls : ""), parent, label);
    b.type = "button";
    b.addEventListener("click", () => { b.blur(); act(); });      // blur: keys go back to the page or deck
    return b;
  };
  let presetBtns = [];
  if (presets) {
    const row = html("div", "mx-row", side);
    html("span", "mx-label", row, "matrix:");
    presetBtns = PRESETS.map((p, i) => button(row, p.label, "", () => { which = i; setMatrix(); }));
  }
  const mats = html("div", null, side);
  const lines = html("div", null, side);
  const status = html("div", "mx-status", side);
  const foundEl = html("div", "mx-found", side);
  const rowGo = html("div", "mx-row", side);
  if (mode === "hunt") button(rowGo, "sweep v around", "mx-go", sweep);
  else button(rowGo, "turn 90°", "mx-go", turn);
  button(rowGo, "reset", "", () => { stop(); setMatrix(); });

  // ---------------------------------------------------------------- state
  function setMatrix() {
    stop();
    A = presets ? PRESETS[which].m : given;
    info = analyze(A);
    start = presets ? PRESETS[which].start : [0, 100, 30, 60].find((s) => info.dirs.every((d) => Math.abs(wrap(s - d.ang, 180)) > 10));
    phi = start; theta = 0; found = new Set(); trace = []; swept = false;
    presetBtns.forEach((b, i) => b.classList.toggle("mx-on", i === which));
    draw();
  }

  const stop = () => { if (timer) { clearTimeout(timer); timer = 0; } };
  const onLine = (ang, psi) => Math.abs(wrap(ang - psi, 180)) < 1e-6;
  // perpendicular axes that make A diagonal: u1 along an eigen-direction whose partner u2 is one too
  const diagAngles = () => info.dirs.map((d) => d.ang).filter((psi) => {
    const u1 = dir(psi), u2 = dir(psi + 90);
    return Math.abs(dot(u1, mul(A, u2))) + Math.abs(dot(u2, mul(A, u1))) < 1e-9;
  });

  // next angle psi + 180 m strictly after a and no later than b, or null
  const nextHit = (angles, a, b) => {
    let hit = null;
    for (const psi of angles) {
      const h = psi + 180 * (Math.floor((a - psi) / 180 + 1e-9) + 1);
      if (h > a + 1e-9 && h <= b + 1e-9 && (hit === null || h < hit)) hit = h;
    }
    return hit;
  };

  function sweep() {                                              // v once around the circle, pausing on eigenvectors
    stop();
    const a0 = phi;
    trace = [mul(A, dir(phi))]; swept = false;
    const step = () => {
      const a = phi, b = Math.min(a0 + 360, a + 2.5);
      const hit = nextHit(info.dirs.map((d) => d.ang), a, b);
      phi = hit === null ? b : hit;
      if (hit !== null) info.dirs.forEach((d, k) => { if (onLine(phi, d.ang)) found.add(k); });
      trace.push(mul(A, dir(phi)));
      if (phi >= a0 + 360 - 1e-9) { timer = 0; swept = true; draw(); return; }
      draw();
      timer = setTimeout(step, hit === null ? 25 : 700);
    };
    timer = setTimeout(step, 25);
  }

  function turn() {                                               // the axes turn 90°, pausing where A is diagonal
    stop();
    const t0 = theta, angles = diagAngles();
    const step = () => {
      const a = theta, b = Math.min(t0 + 90, a + 1);
      const hit = nextHit(angles, a, b);
      theta = hit === null ? b : hit;
      draw();
      if (theta >= t0 + 90 - 1e-9) { timer = 0; return; }
      timer = setTimeout(step, hit === null ? 30 : 1100);
    };
    timer = setTimeout(step, 30);
  }

  // ---------------------------------------------------------------- pointer: aim v, or turn the axes
  let dragging = false;
  const aim = (e) => {
    const r = plane.getBoundingClientRect();                      // includes the scaling reveal.js applies to slides
    if (!r.width || !r.height) return;
    const x = ((e.clientX - r.left) / r.width) * W - C0, y = C0 - ((e.clientY - r.top) / r.height) * W;
    if (Math.hypot(x, y) < 4) return;
    let ang = Math.atan2(y, x) / DEG;
    if (mode === "hunt") {
      info.dirs.forEach((d, k) => {
        const off = wrap(ang - d.ang, 180);
        if (Math.abs(off) < 3) { ang -= off; found.add(k); }
      });
      phi = ang;
    } else {
      for (const psi of diagAngles()) { const off = wrap(ang - psi, 180); if (Math.abs(off) < 2) ang -= off; }
      theta = ((ang % 360) + 360) % 360;
    }
    draw();
  };
  plane.addEventListener("pointerdown", (e) => {
    if (e.button > 0) return;
    dragging = true; stop();
    try { plane.setPointerCapture(e.pointerId); } catch (err) { /* synthetic events have no capturable pointer */ }
    e.preventDefault(); aim(e);
  });
  plane.addEventListener("pointermove", (e) => { if (dragging) { e.preventDefault(); aim(e); } });
  const release = (e) => {
    if (!dragging) return;
    dragging = false;
    try { plane.releasePointerCapture(e.pointerId); } catch (err) { /* already released */ }
  };
  plane.addEventListener("pointerup", release);
  plane.addEventListener("pointercancel", release);

  // ---------------------------------------------------------------- drawing
  const pal = () => PAL[root.classList.contains("mx-dark") ? "dark" : "light"];
  const reach = (u) => R / Math.max(Math.abs(u[0]), Math.abs(u[1]));   // where the line along u leaves the square
  const along = (u, t) => [t * u[0], t * u[1]];
  const line = (p, q, col, w, extra) => svg("line", Object.assign({ x1: X(p[0]).toFixed(1), y1: Y(p[1]).toFixed(1),
    x2: X(q[0]).toFixed(1), y2: Y(q[1]).toFixed(1), stroke: col, "stroke-width": w }, extra || {}), plane);

  function arrow(p, col, w) {                                     // shaft plus a polygon head (no marker ids)
    const x1 = X(p[0]), y1 = Y(p[1]), L = Math.hypot(x1 - C0, y1 - C0);
    if (L < 1) return;
    const ux = (x1 - C0) / L, uy = (y1 - C0) / L, hl = Math.min(L, 10 + 2 * w), hw = 3.5 + 1.3 * w;
    const bx = x1 - ux * hl, by = y1 - uy * hl;
    svg("line", { x1: C0, y1: C0, x2: (bx + ux).toFixed(1), y2: (by + uy).toFixed(1), stroke: col, "stroke-width": w }, plane);
    svg("polygon", { points: `${x1.toFixed(1)},${y1.toFixed(1)} ${(bx - uy * hw).toFixed(1)},${(by + ux * hw).toFixed(1)} ` +
      `${(bx + uy * hw).toFixed(1)},${(by - ux * hw).toFixed(1)}`, fill: col }, plane);
  }

  function label(p, side, s, col, halo) {                         // past the tip, pushed to one side of the arrow
    const L = Math.hypot(p[0], p[1]), d = L > 1e-9 ? [p[0] / L, p[1] / L] : [1, 0];
    const n = [-d[1] * side, d[0] * side];
    const x = Math.min(W - 22, Math.max(22, X(p[0]) + 15 * (d[0] + n[0])));
    const y = Math.min(W - 12, Math.max(12, Y(p[1]) - 15 * (d[1] + n[1])));
    const t = svg("text", { x: x.toFixed(1), y: y.toFixed(1), "font-size": 18, "font-weight": 700, fill: col,
      "text-anchor": "middle", "dominant-baseline": "central", stroke: halo, "stroke-width": 5,
      "stroke-linejoin": "round", "paint-order": "stroke" }, plane);
    t.textContent = s;
  }

  function grid(P) {
    while (plane.firstChild) plane.removeChild(plane.firstChild);
    for (let k = -Math.floor(R); k <= R; k++) {
      if (k === 0) continue;
      line([k, -R], [k, R], P.grid, 1); line([-R, k], [R, k], P.grid, 1);
    }
    line([-R, 0], [R, 0], P.axis, 1.2); line([0, -R], [0, R], P.axis, 1.2);
    svg("circle", { cx: C0, cy: C0, r: S.toFixed(1), fill: "none", stroke: P.axis, "stroke-width": 1.3, "stroke-dasharray": "2 4" }, plane);
  }

  function drawHunt() {
    const P = pal();
    grid(P);
    const pts = swept ? Array.from({ length: 145 }, (_, j) => mul(A, dir(j * 2.5))) : trace;
    if (pts.length > 1) svg("path", { d: pts.map((p, j) => `${j ? "L" : "M"}${X(p[0]).toFixed(1)},${Y(p[1]).toFixed(1)}`).join(""),
      fill: "none", stroke: P.red, "stroke-width": 1.6, "stroke-dasharray": "3 4", opacity: 0.85 }, plane);
    const v = dir(phi), Av = mul(A, v), ang = Math.atan2(v[0] * Av[1] - v[1] * Av[0], dot(v, Av)) / DEG;
    for (const k of found) {                                      // the eigen-directions found so far
      const { ang: psi, lam } = info.dirs[k], d = dir(psi), t = reach(d);
      line(along(d, -t), along(d, t), P.purple, 2.2, { "stroke-dasharray": "8 5" });
      const end = onLine(phi, psi) && lam * dot(v, d) > 0 ? -0.75 * t : 0.75 * t;   // the end away from Av's tip
      label(along(d, end), -1, `λ = ${num(lam)}`, P.purple, P.card);
    }
    if (Math.abs(ang) > 4 && Math.abs(ang) < 176 && Math.hypot(Av[0], Av[1]) > 0.3) {   // the turn from v to Av
      const r = 0.45 * S, a1 = phi * DEG, a2 = (phi + ang) * DEG;
      svg("path", { d: `M${(C0 + r * Math.cos(a1)).toFixed(1)},${(C0 - r * Math.sin(a1)).toFixed(1)} A${r.toFixed(1)},${r.toFixed(1)} 0 0 ` +
        `${ang > 0 ? 0 : 1} ${(C0 + r * Math.cos(a2)).toFixed(1)},${(C0 - r * Math.sin(a2)).toFixed(1)}`,
        fill: "none", stroke: P.axis, "stroke-width": 2 }, plane);
    }
    arrow(Av, P.red, 4.2); arrow(v, P.teal, 3);
    label(v, -1, "v", P.teal, P.card); label(Av, 1, "Av", P.red, P.card);

    const k = info.dirs.findIndex((d) => onLine(phi, d.ang)), nAv = Math.hypot(Av[0], Av[1]);
    mats.innerHTML = `<div class="mx-mrow"><span>A =</span>${matHTML(A, num)}</div>`;
    lines.innerHTML = `<div class="mx-line"><b class="mx-teal">v</b> = (${fix(v[0])}, ${fix(v[1])})</div>` +
      `<div class="mx-line"><b class="mx-red">Av</b> = (${fix(Av[0])}, ${fix(Av[1])})</div>` +
      `<div class="mx-line mx-muted">${nAv < 1e-9 ? "Av = 0" : Math.abs(ang) > 179.5 ? "Av points the opposite way"
        : `Av is turned ${Math.round(Math.abs(ang))}° from v`}</div>`;
    status.innerHTML = info.kind === "scalar" ? `<span class="mx-purple">Every v is an eigenvector: Av = ${times(info.lam)}</span>`
      : k >= 0 ? `<span class="mx-purple">Eigenvector! Av = ${times(info.dirs[k].lam)}</span>`
      : `<span class="mx-muted">Drag on the plane to aim v. Hunt for the directions where Av stays on the line of v.</span>`;
    let f = "";
    if (info.kind === "two" && found.size === 2) {
      const gap = Math.round(Math.abs(wrap(info.dirs[0].ang - info.dirs[1].ang, 180)));
      f = `Found both: λ = ${num(info.dirs[0].lam)} and λ = ${num(info.dirs[1].lam)}, ${gap}° apart` +
        (gap === 90 ? ": perpendicular." : ", not perpendicular.");
    } else if (found.size === 1) {
      const lam = num(info.dirs[[...found][0]].lam);
      f = info.kind === "two" ? `Found λ = ${lam}. One more direction to find.` : `Found λ = ${lam}. This matrix has no second eigen-direction.`;
    } else if (info.kind === "complex" && swept) {
      f = `No direction survives: Av is always turned. The eigenvalues are complex, ${cnum(info.re, info.im)}.`;
    }
    foundEl.textContent = f;
  }

  function drawAxes() {
    const P = pal();
    grid(P);
    const u1 = dir(theta), u2 = dir(theta + 90), Au1 = mul(A, u1), Au2 = mul(A, u2);
    const m = [[dot(u1, Au1), dot(u1, Au2)], [dot(u2, Au1), dot(u2, Au2)]];
    for (const u of [u1, u2]) line(along(u, -reach(u)), along(u, reach(u)), P.teal, 1.3, { opacity: 0.5 });
    const along1 = [m[0][0] * u1[0], m[0][0] * u1[1]], along2 = [m[1][1] * u2[0], m[1][1] * u2[1]];
    line([0, 0], along1, P.purple, 8, { opacity: 0.45 }); line([0, 0], along2, P.purple, 8, { opacity: 0.45 });
    line(along1, Au1, P.orange, 4.5, { "stroke-linecap": "round" }); line(along2, Au2, P.orange, 4.5, { "stroke-linecap": "round" });
    arrow(Au1, P.red, 4.2); arrow(Au2, P.red, 4.2);
    arrow(u1, P.teal, 2.8); arrow(u2, P.teal, 2.8);
    label(along(u1, 0.86 * reach(u1)), -1, "u₁", P.teal, P.card); label(along(u2, 0.86 * reach(u2)), -1, "u₂", P.teal, P.card);
    label(Au1, 1, "Au₁", P.red, P.card); label(Au2, 1, "Au₂", P.red, P.card);

    const diag = info.kind === "scalar" || diagAngles().some((psi) => onLine(theta, psi));
    const cls = [["mx-purple", "mx-orange"], ["mx-orange", "mx-purple"]];
    mats.innerHTML = `<div class="mx-mrow"><span class="mx-label">in the x, y axes</span><span>A =</span>${matHTML(A, num)}</div>` +
      `<div class="mx-mrow"><span class="mx-label">in the axes u₁, u₂</span><span>A′ =</span>${matHTML(m, fix, cls)}</div>`;
    lines.innerHTML = `<div class="mx-line mx-muted">A′ₘₙ = ⟨uₘ|A|uₙ⟩: each Au splits into a part along its own axis ` +
      `(<span class="mx-purple">purple</span>, diagonal) and a part off it (<span class="mx-orange">orange</span>, off-diagonal).</div>` +
      `<div class="mx-line">axes turned by ${Math.round(((theta % 360) + 360) % 360) % 360}° · trace ${fix(m[0][0] + m[1][1])} · ` +
      `determinant ${fix(m[0][0] * m[1][1] - m[0][1] * m[1][0])}</div>`;
    status.innerHTML = diag
      ? `<span class="mx-purple">Diagonal! u₁ and u₂ are eigenvectors, and the diagonal holds the eigenvalues ${num(m[0][0])} and ${num(m[1][1])}.</span>`
      : `<span class="mx-muted">Drag on the plane to turn the axes. The trace and determinant never change.</span>`;
    foundEl.textContent = !diag && diagAngles().length === 0 ? "No pair of perpendicular axes makes this matrix diagonal." : "";
  }

  const draw = () => (mode === "hunt" ? drawHunt() : drawAxes());

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("mx-dark")) { root.classList.toggle("mx-dark", dark); draw(); }
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  setMatrix();
  syncDark();
  return () => { stop(); if (obs) obs.disconnect(); };
}

export default { render };
