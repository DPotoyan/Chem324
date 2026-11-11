// A particle going around a circle, drawn in 3D: the angular velocity omega along the axis, the position r, and the
// velocity v = omega x r, tangent to the circle, with a right-angle mark between r and v. The angle phi (from the x
// axis) and the arc s = R phi grow as the particle goes around.
//
// Play/pause and a slider for phi. Drag the picture to turn the view (elevation 10 to 90 degrees); "from above"
// looks straight down the axis, where omega points out of the screen and is drawn as a dot in a circle.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive and in a reveal.js deck through a module-script loader. No dependencies.
// Model keys, optional: fontSize (CSS size), width (CSS px of the drawing, default 640), status (false hides the line
// under the controls), autoplay (false starts paused).

const TEAL = "#107895", PURPLE = "#6a3d9a", ORANGE = "#e07b00";
const SVGNS = "http://www.w3.org/2000/svg";
const W = 640, H = 410;                                              // drawing units (the viewBox)
const CX = 300, S = 150;                                             // screen x of the center, pixels per radius
const EL0 = 24, AZ0 = -68;                                           // default camera, degrees
const STEP = 3, TICK = 45;                                           // degrees per tick, milliseconds per tick

const CSS = `
.cv-root { --cv-fg: #212529; --cv-muted: #6c757d; --cv-border: #ced4da; --cv-btn: #f8f9fa; --cv-card: #ffffff;
  --cv-teal: ${TEAL}; --cv-purple: ${PURPLE}; --cv-orange: ${ORANGE}; --cv-disc: #f1f3f5; --cv-line: #adb5bd;
  --cv-on: #e7f1f4;
  color: var(--cv-fg); background: var(--cv-card); border: 1px solid var(--cv-border); border-radius: 10px;
  padding: 0.5em 0.9em 0.6em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em auto 1.2em; }
.cv-root.cv-dark { --cv-fg: #e9ecef; --cv-muted: #adb5bd; --cv-border: #495057; --cv-btn: #2b3035; --cv-card: #1e2125;
  --cv-teal: #45a9c6; --cv-purple: #b08be0; --cv-orange: #f59f3a; --cv-disc: #2b3035; --cv-line: #6c757d;
  --cv-on: #1f3a44; }
.cv-plot { display: block; width: 100%; height: auto; touch-action: none; cursor: grab; user-select: none; }
.cv-plot.cv-drag { cursor: grabbing; }
.cv-plot text { font-family: inherit; }
.cv-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 0.9em; margin-top: 0.2em; }
.cv-btn { font: inherit; color: var(--cv-fg); background: var(--cv-btn); border: 1px solid var(--cv-border);
  border-radius: 999px; padding: 0.1em 0.8em; cursor: pointer; line-height: 1.5; margin: 0; }
.cv-btn:hover { border-color: ${TEAL}; }
.cv-btn.cv-active { border-color: var(--cv-teal); background: var(--cv-on); font-weight: 600; }
.cv-slider { display: flex; align-items: center; gap: 0.5em; flex: 1 1 14em; }
.cv-slider input { flex: 1 1 auto; min-width: 8em; accent-color: ${TEAL}; }
.cv-val { font-variant-numeric: tabular-nums; min-width: 4.4em; color: var(--cv-muted); }
.cv-hint { color: var(--cv-muted); }
.cv-status { color: var(--cv-muted); margin: 0.3em 0 0; min-height: 1.4em; }
`;

const rad = (d) => (d * Math.PI) / 180;
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];

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

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "cv-root", el);
  root.setAttribute("data-prevent-swipe", "");                       // reveal.js: drags must not change slides
  root.style.fontSize = get("fontSize", "15px");
  root.style.width = `${get("width", 640)}px`;

  const plot = svg("svg", { viewBox: `0 0 ${W} ${H}`, class: "cv-plot", role: "img",
    "aria-label": "a particle going around a circle, with its angular velocity, position and velocity vectors" }, root);
  const gDisc = svg("g", {}, plot);                                  // plane of the circle, far half of the rim
  const gBack = svg("g", {}, plot);                                  // the particle and its vectors when behind the axis
  const gAxis = svg("g", {}, plot);                                  // omega and its curl
  const gFront = svg("g", {}, plot);
  const gMove = svg("g", {}, gFront);                                // r, v, the particle (moved between back and front)

  const disc = svg("path", { style: "fill: var(--cv-disc); stroke: none" }, gDisc);
  const rimFar = svg("path", { fill: "none", style: "stroke: var(--cv-line)", "stroke-width": 1.6, "stroke-dasharray": "5 5" }, gDisc);
  const rimNear = svg("path", { fill: "none", style: "stroke: var(--cv-line)", "stroke-width": 1.8 }, gDisc);
  const ref = svg("line", { style: "stroke: var(--cv-line)", "stroke-width": 1.3 }, gDisc);
  const arcS = svg("path", { fill: "none", style: "stroke: var(--cv-teal)", "stroke-width": 6, "stroke-linecap": "butt" }, gDisc);
  const arcP = svg("path", { fill: "none", style: "stroke: var(--cv-fg)", "stroke-width": 1.4 }, gDisc);
  const labS = svg("text", { "font-size": 21, "font-style": "italic", "text-anchor": "middle", "dominant-baseline": "middle",
    style: "fill: var(--cv-teal)" }, gDisc); labS.textContent = "s";
  const labP = svg("text", { "font-size": 20, "font-style": "italic", "text-anchor": "middle", "dominant-baseline": "middle",
    style: "fill: var(--cv-fg)" }, gDisc); labP.textContent = "φ";

  const wLine = svg("line", { style: "stroke: var(--cv-purple)", "stroke-width": 4 }, gAxis);
  const wHead = svg("polygon", { style: "fill: var(--cv-purple)" }, gAxis);
  const wDotRing = svg("circle", { r: 10, fill: "none", style: "stroke: var(--cv-purple)", "stroke-width": 2.4 }, gAxis);
  const wDot = svg("circle", { r: 3.2, style: "fill: var(--cv-purple)" }, gAxis);
  const curl = svg("path", { fill: "none", style: "stroke: var(--cv-muted)", "stroke-width": 1.6 }, gAxis);
  const curlHead = svg("polygon", { style: "fill: var(--cv-muted)" }, gAxis);
  const labW = svg("text", { "font-size": 23, "font-style": "italic", "dominant-baseline": "middle",
    style: "fill: var(--cv-purple)" }, gAxis); labW.textContent = "ω";

  const rLine = svg("line", { style: "stroke: var(--cv-fg)", "stroke-width": 2.6 }, gMove);
  const rHead = svg("polygon", { style: "fill: var(--cv-fg)" }, gMove);
  const vLine = svg("line", { style: "stroke: var(--cv-orange)", "stroke-width": 3.4 }, gMove);
  const vHead = svg("polygon", { style: "fill: var(--cv-orange)" }, gMove);
  const corner = svg("path", { fill: "none", style: "stroke: var(--cv-muted)", "stroke-width": 1.3 }, gMove);
  const ball = svg("circle", { r: 8, style: `fill: var(--cv-purple); stroke: var(--cv-fg)`, "stroke-width": 1.2 }, gMove);
  const labR = svg("text", { "font-size": 21, "font-style": "italic", "text-anchor": "middle", "dominant-baseline": "middle",
    style: "fill: var(--cv-fg)" }, gMove); labR.textContent = "r";
  const labV = svg("text", { "font-size": 21, "font-style": "italic", "text-anchor": "middle", "dominant-baseline": "middle",
    style: "fill: var(--cv-orange)" }, gMove); labV.textContent = "v";

  const controls = html("div", "cv-controls", root);
  const playBtn = html("button", "cv-btn", controls, "❚❚ pause"); playBtn.type = "button";
  const box = html("label", "cv-slider", controls);
  html("span", null, box, "φ");
  const input = html("input", null, box); input.type = "range"; input.min = 0; input.max = 360; input.step = 1;
  const val = html("span", "cv-val", box);
  const aboveBtn = html("button", "cv-btn", controls, "from above"); aboveBtn.type = "button";
  const resetBtn = html("button", "cv-btn", controls, "3D view"); resetBtn.type = "button";
  const status = html("div", "cv-status", root);
  if (get("status", true) === false) status.style.display = "none";

  // ---------------------------------------------------------------- state and drawing
  let phi = 60, el0 = EL0, az0 = AZ0, playing = get("autoplay", true) !== false, timer = null;
  let cam = null, cy = H / 2;

  const setCamera = () => {
    const e = rad(el0), a = rad(az0);
    const c = [Math.cos(e) * Math.cos(a), Math.cos(e) * Math.sin(a), Math.sin(e)];
    const ex = [-Math.sin(a), Math.cos(a), 0];
    cam = { c, ex, ey: cross(c, ex) };
    const top = Math.max(1.32 * Math.cos(e), 1.22 * Math.sin(e)), bot = Math.max(1.25 * Math.sin(e), 0.25);
    cy = H / 2 + ((top - bot) * S) / 2;                              // keep the drawing centered for any tilt
  };
  const P2 = (p) => [CX + S * dot(p, cam.ex), cy - S * dot(p, cam.ey)];          // world point -> screen point
  const depth = (p) => dot(p, cam.c);
  const pathOf = (pts) => pts.map((q, i) => (i ? "L" : "M") + q[0].toFixed(1) + "," + q[1].toFixed(1)).join("");
  const onCircle = (r, a, z = 0) => [r * Math.cos(a), r * Math.sin(a), z];

  // a straight arrow from screen point A to B: the line stops at the base of a triangular head
  const arrow = (line, head, A, B, size) => {
    const dx = B[0] - A[0], dy = B[1] - A[1], L = Math.hypot(dx, dy) || 1e-9;
    const ux = dx / L, uy = dy / L, h = Math.min(size, 0.6 * L);
    const bx = B[0] - h * ux, by = B[1] - h * uy, nx = -uy * 0.45 * h, ny = ux * 0.45 * h;
    line.setAttribute("x1", A[0]); line.setAttribute("y1", A[1]); line.setAttribute("x2", bx); line.setAttribute("y2", by);
    head.setAttribute("points", `${B[0]},${B[1]} ${bx + nx},${by + ny} ${bx - nx},${by - ny}`);
  };

  function draw() {
    const a = rad(phi);
    // the plane and the rim, the far half dashed
    const rim = [];
    for (let i = 0; i <= 120; i++) rim.push(onCircle(1, (2 * Math.PI * i) / 120));
    disc.setAttribute("d", pathOf(rim.map(P2)) + "Z");
    let far = "", near = "";
    rim.forEach((p, i) => {
      if (i === 0) return;
      const seg = "M" + P2(rim[i - 1]).map((v) => v.toFixed(1)).join(",") + "L" + P2(p).map((v) => v.toFixed(1)).join(",");
      if (depth(p) + depth(rim[i - 1]) < 0) far += seg; else near += seg;
    });
    rimFar.setAttribute("d", far); rimNear.setAttribute("d", near);
    const O = P2([0, 0, 0]), X1 = P2([1, 0, 0]);
    ref.setAttribute("x1", O[0]); ref.setAttribute("y1", O[1]); ref.setAttribute("x2", X1[0]); ref.setAttribute("y2", X1[1]);

    // the arc covered, s = R phi, and the angle phi
    const sPts = [], pPts = [];
    for (let i = 0; i <= 90; i++) {
      const t = (a * i) / 90;
      sPts.push(P2(onCircle(1, t))); pPts.push(P2(onCircle(0.3, t)));
    }
    arcS.setAttribute("d", pathOf(sPts)); arcP.setAttribute("d", pathOf(pPts));
    const sl = P2(onCircle(1.17, a / 2)), pl = P2(onCircle(0.46, a / 2));
    labS.setAttribute("x", sl[0]); labS.setAttribute("y", sl[1]); labS.style.display = phi > 8 ? "" : "none";
    labP.setAttribute("x", pl[0]); labP.setAttribute("y", pl[1]); labP.style.display = phi > 14 ? "" : "none";

    // omega along the axis; seen nearly end on, a dot in a circle
    const Wt = P2([0, 0, 1.25]), wLen = Math.hypot(Wt[0] - O[0], Wt[1] - O[1]);
    const endOn = wLen < 22;
    [wLine, wHead].forEach((e) => (e.style.display = endOn ? "none" : ""));
    [wDotRing, wDot].forEach((e) => { e.style.display = endOn ? "" : "none"; e.setAttribute("cx", O[0]); e.setAttribute("cy", O[1]); });
    if (!endOn) arrow(wLine, wHead, O, Wt, 18);
    labW.setAttribute("x", (endOn ? O[0] + 12 : Wt[0] + 10)); labW.setAttribute("y", (endOn ? O[1] - 16 : Wt[1] + 4));
    [curl, curlHead].forEach((e) => (e.style.display = endOn ? "none" : ""));
    const cPts = [];                                                  // the curl: counterclockwise seen from above
    for (let i = 0; i <= 60; i++) cPts.push(P2(onCircle(0.2, rad(200 + (300 * i) / 60), 0.9)));
    curl.setAttribute("d", pathOf(cPts.slice(0, -3)));
    const c1 = cPts[cPts.length - 4], c2 = cPts[cPts.length - 1];
    const cdx = c2[0] - c1[0], cdy = c2[1] - c1[1], cl = Math.hypot(cdx, cdy) || 1e-9;
    const cux = cdx / cl, cuy = cdy / cl;
    curlHead.setAttribute("points", `${c2[0]},${c2[1]} ${c1[0] - 4 * cuy},${c1[1] + 4 * cux} ${c1[0] + 4 * cuy},${c1[1] - 4 * cux}`);

    // r, v = omega x r, the right angle and the particle
    const P = onCircle(1, a), T = [-Math.sin(a), Math.cos(a), 0];
    const Ps = P2(P), Vt = P2([P[0] + 0.62 * T[0], P[1] + 0.62 * T[1], 0]);
    arrow(rLine, rHead, O, Ps, 15);
    arrow(vLine, vHead, Ps, Vt, 17);
    const q = 0.11, k1 = P2([P[0] - q * P[0], P[1] - q * P[1], 0]), k2 = P2([P[0] - q * P[0] + q * T[0], P[1] - q * P[1] + q * T[1], 0]);
    const k3 = P2([P[0] + q * T[0], P[1] + q * T[1], 0]);
    corner.setAttribute("d", pathOf([k1, k2, k3]));
    ball.setAttribute("cx", Ps[0]); ball.setAttribute("cy", Ps[1]);
    const rl = P2([0.55 * P[0] + 0.14 * T[0], 0.55 * P[1] + 0.14 * T[1], 0]);   // outside the angle phi
    labR.setAttribute("x", rl[0]); labR.setAttribute("y", rl[1]);
    const vl = P2([P[0] + 0.8 * T[0], P[1] + 0.8 * T[1], 0]);
    labV.setAttribute("x", vl[0]); labV.setAttribute("y", vl[1] - 4);
    (depth(P) < -0.05 ? gBack : gFront).appendChild(gMove);        // behind the axis on the far half

    input.value = Math.round(phi);
    val.textContent = `${Math.round(phi)}°`;
    status.textContent = `φ = ${Math.round(phi)}°, so the particle has covered s = rφ = ${a.toFixed(2)} r. ` +
      "v = ω × r stays perpendicular to r and to ω: tangent, with length rω.";
    aboveBtn.classList.toggle("cv-active", el0 >= 89.5);
    resetBtn.classList.toggle("cv-active", el0 === EL0 && az0 === AZ0);
  }

  const tick = () => {
    timer = null;
    if (!playing) return;
    phi = (phi + STEP) % 360;
    draw();
    timer = setTimeout(tick, TICK);
  };
  const setPlaying = (on) => {
    playing = on;
    playBtn.textContent = on ? "❚❚ pause" : "▶ play";
    if (timer) { clearTimeout(timer); timer = null; }
    if (on) timer = setTimeout(tick, TICK);
  };

  playBtn.addEventListener("click", () => { playBtn.blur(); setPlaying(!playing); });
  input.addEventListener("input", () => { setPlaying(false); phi = +input.value; draw(); });
  input.addEventListener("change", () => input.blur());
  aboveBtn.addEventListener("click", () => { aboveBtn.blur(); el0 = 90; setCamera(); draw(); });
  resetBtn.addEventListener("click", () => { resetBtn.blur(); el0 = EL0; az0 = AZ0; setCamera(); draw(); });

  // drag to turn the view
  let drag = null;
  plot.addEventListener("pointerdown", (ev) => {
    drag = { x: ev.clientX, y: ev.clientY, el: el0, az: az0 };
    plot.setPointerCapture(ev.pointerId); plot.classList.add("cv-drag");
  });
  plot.addEventListener("pointermove", (ev) => {
    if (!drag) return;
    const r = plot.getBoundingClientRect(), k = 360 / Math.max(200, r.width);    // a full drag across turns ~half a turn
    az0 = drag.az - (ev.clientX - drag.x) * k * 0.5;
    el0 = Math.max(10, Math.min(90, drag.el + (ev.clientY - drag.y) * k * 0.5));
    setCamera(); draw();
  });
  const endDrag = (ev) => {
    if (!drag) return;
    drag = null; plot.classList.remove("cv-drag");
    try { plot.releasePointerCapture(ev.pointerId); } catch (e) { /* already released */ }
  };
  plot.addEventListener("pointerup", endDrag);
  plot.addEventListener("pointercancel", endDrag);

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("cv-dark")) root.classList.toggle("cv-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  setCamera();
  draw();
  syncDark();
  setPlaying(playing);
  return () => {
    playing = false;
    if (timer) clearTimeout(timer);
    if (obs) obs.disconnect();
  };
}

export default { render };
