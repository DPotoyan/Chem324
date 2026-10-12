// Two mirrors in either order: the letter F under F (flip, a mirror in the x axis) and S (swap, a mirror in
// the line y = x).
//
// Press F or S to apply a mirror. The letter turns over the mirror line like a card: the part across the line
// shrinks through zero and comes back reversed. The panel keeps the running product of the matrices, written
// right to left like operators (S first, then F, is the product F S), and says what it does to the letter.
// "S, then F" and "F, then S" reset and play the two orders; the result of the previous play stays as a dotted
// ghost, so after both plays the two outcomes, a quarter turn clockwise and one counterclockwise, sit side by
// side. More to try: F twice, S twice, F S twice.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch03/05), in a reveal.js deck through a module-script loader, and in Jupyter or
// Colab through the anywidget package. No dependencies. Model key, optional: fontSize (CSS size; the plane is
// 20em wide).

const TEAL = "#107895", CARDINAL = "#C8102E", PURPLE = "#6a3d9a";
const SVGNS = "http://www.w3.org/2000/svg";
const DEG = Math.PI / 180;
const W = 400, C0 = W / 2, R = 1.65, PX = (C0 - 8) / R;    // viewBox W x W, origin in the middle, px per unit
const X = (x) => C0 + PX * x, Y = (y) => C0 - PX * y;

const LETTER = [[[0.25, 0.2], [0.25, 1.0]], [[0.25, 1.0], [0.8, 1.0]], [[0.25, 0.6], [0.65, 0.6]]];
const MIRRORS = {
  F: { M: [[1, 0], [0, -1]], d: [1, 0], line: "the x axis" },
  S: { M: [[0, 1], [1, 0]], d: [Math.SQRT1_2, Math.SQRT1_2], line: "the line y = x" },
};
const I2 = [[1, 0], [0, 1]];

const PAL = {
  light: { teal: TEAL, red: CARDINAL, purple: PURPLE, ghost: "#6c757d", axis: "#adb5bd", card: "#ffffff" },
  dark: { teal: "#45a9c6", red: "#f05d6f", purple: "#b08be0", ghost: "#adb5bd", axis: "#6c757d", card: "#1e2125" },
};

const CSS = `
.fs-root { --fs-fg: #212529; --fs-muted: #6c757d; --fs-border: #ced4da; --fs-btn: #f8f9fa; --fs-card: #ffffff;
  --fs-teal: ${TEAL}; --fs-red: ${CARDINAL}; --fs-purple: ${PURPLE};
  display: flex; flex-wrap: wrap; align-items: flex-start; gap: 0.6em 1.4em; color: var(--fs-fg);
  background: var(--fs-card); border: 1px solid var(--fs-border); border-radius: 10px; padding: 0.8em 1em;
  text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit; box-sizing: border-box;
  max-width: 100%; margin: 0.6em 0 1.2em; }
.fs-root.fs-dark { --fs-fg: #e9ecef; --fs-muted: #adb5bd; --fs-border: #495057; --fs-btn: #2b3035; --fs-card: #1e2125;
  --fs-teal: #45a9c6; --fs-red: #f05d6f; --fs-purple: #b08be0; }
.fs-plane { display: block; flex: 0 1 auto; width: 20em; max-width: 100%; height: auto; user-select: none;
  -webkit-user-select: none; }
.fs-plane text { font-family: inherit; }
.fs-side { flex: 1 1 14em; min-width: 12em; }
.fs-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em; margin: 0.15em 0 0.5em; }
.fs-label { color: var(--fs-muted); margin-right: 0.2em; }
.fs-btn { font: inherit; color: var(--fs-fg); background: var(--fs-btn); border: 1px solid var(--fs-border);
  border-radius: 999px; padding: 0.15em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.fs-btn:hover { border-color: ${TEAL}; }
.fs-btn:disabled { opacity: 0.5; cursor: default; }
.fs-btn.fs-op { font-weight: 700; color: var(--fs-purple); border-color: var(--fs-purple); }
.fs-btn.fs-go { border-color: ${TEAL}; color: #fff; background: ${TEAL}; font-weight: 600; }
.fs-btn.fs-go:hover { filter: brightness(1.1); }
.fs-mrow { display: flex; flex-wrap: wrap; align-items: center; gap: 0.2em 0.5em; margin: 0.3em 0; }
.fs-mat { display: inline-grid; grid-template-columns: auto auto; column-gap: 1em; padding: 0.1em 0.5em;
  border-left: 2px solid currentColor; border-right: 2px solid currentColor; border-radius: 0.6em;
  font-variant-numeric: tabular-nums; text-align: right; }
.fs-line { margin: 0.1em 0; }
.fs-status { font-weight: 600; margin: 0.5em 0 0.2em; min-height: 2.8em; }
.fs-muted { color: var(--fs-muted); font-weight: normal; }
.fs-red { color: var(--fs-red); } .fs-purple { color: var(--fs-purple); }
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
const mm = (A, B) => [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                      [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]];
const mv = (M, v) => [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]];
// part of the way through a mirror: the component along the mirror line d stays, the one across it scales by c
const partial = (d, c) => [[(1 - c) * d[0] * d[0] + c, (1 - c) * d[0] * d[1]], [(1 - c) * d[0] * d[1], (1 - c) * d[1] * d[1] + c]];
const minus = (v) => (v < 0 ? "−" : "") + String(Math.abs(Math.round(v)));
const product = (seq) => (seq.length ? seq.slice().reverse().join(" ") : "I");
const order = (seq) => seq.join(", then ");

function describe(M) {                                            // what an exact product of F and S does
  const det = M[0][0] * M[1][1] - M[0][1] * M[1][0];
  if (det < 0) {
    const a = Math.round(Math.atan2(M[1][0], M[0][0]) / DEG / 2);
    const line = { 0: "the x axis", 45: "the line y = x", 90: "the y axis", "-90": "the y axis", "-45": "the line y = −x" }[a];
    return { kind: "mirror", text: `one mirror, in ${line}` };
  }
  const th = Math.round(Math.atan2(M[1][0], M[0][0]) / DEG);
  if (th === 0) return { kind: "id", turn: 0, text: "nothing: the identity" };
  if (Math.abs(th) === 180) return { kind: "turn", turn: 180, text: "a half turn" };
  return { kind: "turn", turn: th, text: `a quarter turn ${th < 0 ? "clockwise" : "counterclockwise"}` };
}

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "fs-root", el);
  root.setAttribute("data-prevent-swipe", "");                    // reveal.js: clicks must not change slides
  root.style.fontSize = get("fontSize", "15px");
  const plane = svg("svg", { viewBox: `0 0 ${W} ${W}`, class: "fs-plane", role: "img",
    "aria-label": "the letter F and its images under the mirrors F and S" }, root);
  const side = html("div", "fs-side", root);
  const buttons = [];
  const button = (parent, label, cls, act) => {
    const b = html("button", "fs-btn" + (cls ? " " + cls : ""), parent, label);
    b.type = "button";
    b.addEventListener("click", () => { b.blur(); if (!busy) act(); });   // blur: keys go back to the page or deck
    buttons.push(b);
    return b;
  };
  html("div", "fs-line fs-muted", side).innerHTML =
    `<b class="fs-purple">F</b> mirrors in the x axis, <b class="fs-purple">S</b> in the line y = x.`;
  const rowOp = html("div", "fs-row", side);
  html("span", "fs-label", rowOp, "apply:");
  button(rowOp, "F", "fs-op", () => step("F"));
  button(rowOp, "S", "fs-op", () => step("S"));
  const rowPlay = html("div", "fs-row", side);
  html("span", "fs-label", rowPlay, "play:");
  button(rowPlay, "S, then F", "fs-go", () => play(["S", "F"]));
  button(rowPlay, "F, then S", "fs-go", () => play(["F", "S"]));
  button(rowPlay, "reset", "", reset);
  const matEl = html("div", null, side);
  const status = html("div", "fs-status", side);

  // ---------------------------------------------------------------- state
  let M = I2, seq = [], anim = null, ghost = null, last = null, timer = 0, busy = false;
  const setBusy = (b) => { busy = b; buttons.forEach((x) => { x.disabled = b; }); };
  const stop = () => { if (timer) { clearTimeout(timer); timer = 0; } };

  function reset() {
    stop(); setBusy(false);
    M = I2; seq = []; anim = null; ghost = null; last = null;
    draw();
  }

  function step(op, done) {                                       // one mirror, about 0.6 s
    const { M: Rm, d } = MIRRORS[op], N = 22;
    let k = 0;
    setBusy(true);
    const tick = () => {
      k += 1;
      const s = 0.5 - 0.5 * Math.cos((Math.PI * k) / N);           // eased
      anim = { op, T: partial(d, Math.cos(Math.PI * s)) };
      if (k < N) { draw(); timer = setTimeout(tick, 28); return; }
      anim = null; M = mm(Rm, M); seq = seq.concat(op); timer = 0;
      draw();
      if (done) done(); else setBusy(false);
    };
    timer = setTimeout(tick, 28);
  }

  function play(ops) {                                            // reset, then the two mirrors in this order
    stop();
    if (last) ghost = last;                                       // the previous play stays as a dotted ghost
    M = I2; seq = []; anim = null;
    setBusy(true); draw();
    let j = 0;
    const next = () => {
      if (j >= ops.length) { last = { M, label: product(seq) }; setBusy(false); draw(); return; }
      const op = ops[j++];
      step(op, () => { timer = setTimeout(next, 420); });
    };
    timer = setTimeout(next, 350);
  }

  // ---------------------------------------------------------------- drawing
  const pal = () => PAL[root.classList.contains("fs-dark") ? "dark" : "light"];
  const line = (p, q, col, w, extra) => svg("line", Object.assign({ x1: X(p[0]).toFixed(1), y1: Y(p[1]).toFixed(1),
    x2: X(q[0]).toFixed(1), y2: Y(q[1]).toFixed(1), stroke: col, "stroke-width": w, "stroke-linecap": "round" }, extra || {}), plane);
  const text = (p, s, col, size, extra) => {                    // with a halo in the card colour
    const t = svg("text", Object.assign({ x: X(p[0]).toFixed(1), y: Y(p[1]).toFixed(1), fill: col, "font-size": size,
      "font-weight": 700, "text-anchor": "middle", "dominant-baseline": "central", stroke: pal().card, "stroke-width": 5,
      "stroke-linejoin": "round", "paint-order": "stroke" }, extra || {}), plane);
    t.textContent = s;
  };
  const letter = (T, col, w, extra) => LETTER.forEach(([p, q]) => line(mv(T, p), mv(T, q), col, w, extra));

  function turnArc(deg, col) {                                    // the net turn, drawn outside the letters
    const r = 1.38, a0 = (deg > 0 ? 72 : 80) * DEG, a1 = a0 + deg * DEG, n = 48;   // radius and start as in the still
    const pts = Array.from({ length: n + 1 }, (_, j) => {
      const a = a0 + ((a1 - a0) * j) / n;
      return [r * Math.cos(a), r * Math.sin(a)];
    });
    svg("path", { d: pts.map((p, j) => `${j ? "L" : "M"}${X(p[0]).toFixed(1)},${Y(p[1]).toFixed(1)}`).join(""),
      fill: "none", stroke: col, "stroke-width": 2.4 }, plane);
    const e = pts[n], t = deg > 0 ? [-Math.sin(a1), Math.cos(a1)] : [Math.sin(a1), -Math.cos(a1)];   // tangent at the end
    const tip = [X(e[0]), Y(e[1])], u = [t[0], -t[1]], nrm = [-u[1], u[0]], hl = 13, hw = 6;
    svg("polygon", { points: [[tip[0] + u[0] * 4, tip[1] + u[1] * 4], [tip[0] - u[0] * hl + nrm[0] * hw, tip[1] - u[1] * hl + nrm[1] * hw],
      [tip[0] - u[0] * hl - nrm[0] * hw, tip[1] - u[1] * hl - nrm[1] * hw]].map((p) => p.map((v) => v.toFixed(1)).join(",")).join(" "),
      fill: col }, plane);
  }

  function draw() {
    const P = pal();
    while (plane.firstChild) plane.removeChild(plane.firstChild);
    line([-R, 0], [R, 0], P.axis, 1.2); line([0, -R], [0, R], P.axis, 1.2);
    for (const op of ["F", "S"]) {                                // the two mirror lines; the active one stands out
      const active = anim && anim.op === op, d = MIRRORS[op].d, t = R / Math.max(d[0], d[1]);
      line([-t * d[0], -t * d[1]], [t * d[0], t * d[1]], P.purple, active ? 3 : 1.6,
        { "stroke-dasharray": "9 7", "stroke-linecap": "butt", opacity: active ? 1 : 0.45 });
      text(op === "F" ? [1.53, 0.14] : [0.93, 1.25], op, P.purple, 22, { opacity: active ? 1 : 0.7 });   // outside the turn arc
    }
    letter(I2, P.teal, 10, { opacity: 0.25 });                    // where the letter started
    if (ghost) {
      letter(ghost.M, P.ghost, 5, { "stroke-dasharray": "1 8" });
      const c = LETTER.flat().map((p) => mv(ghost.M, p)).reduce((s, p) => [s[0] + p[0] / 6, s[1] + p[1] / 6], [0, 0]);
      const L = Math.hypot(c[0], c[1]) || 1;
      text([c[0] + (0.52 * c[0]) / L, c[1] + (0.52 * c[1]) / L], ghost.label, P.ghost, 20);   // just outside the ghost
    }
    const moved = seq.length > 0 || anim !== null;
    letter(anim ? mm(anim.T, M) : M, moved ? P.red : P.teal, 10);
    const info = describe(M);
    if (!anim && info.kind === "turn") turnArc(info.turn === 180 ? 180 : info.turn, P.red);

    matEl.innerHTML = `<div class="fs-mrow"><span>product</span><b class="fs-red">${product(seq)}</b><span>=</span>` +
      `<span class="fs-mat">${[0, 1].map((r) => [0, 1].map((c) => `<span>${minus(M[r][c])}</span>`).join("")).join("")}</span></div>`;
    let s;
    if (anim) s = `<span class="fs-purple">${anim.op}: mirror in ${MIRRORS[anim.op].line}</span>`;
    else if (!seq.length) s = `<span class="fs-muted">Press F or S to mirror the letter, or play the two orders.</span>`;
    else if (info.kind === "id") s = seq.length === 2 && seq[0] === seq[1]
      ? `Back to the start: ${seq[0]} undoes itself, ${seq[0]} ${seq[0]} = I.` : "Back to the start: the product is I.";
    else s = `${order(seq)} is the product ${product(seq)}: ${info.text}.`;
    const g = ghost && describe(ghost.M);
    if (!anim && g && g.kind === "turn" && info.kind === "turn" && g.turn === -info.turn && Math.abs(info.turn) === 90 && seq.length === 2)
      s += ` <span class="fs-red">Same two mirrors, opposite turns: F S ≠ S F.</span>`;
    status.innerHTML = s;
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("fs-dark")) { root.classList.toggle("fs-dark", dark); draw(); }
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  reset();
  syncDark();
  return () => { stop(); if (obs) obs.disconnect(); };
}

export default { render };
