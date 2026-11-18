// Stern-Gerlach magnets in a row: measure a spin 1/2 along one axis, then along another.
//
// Atoms leave the oven with their spins unprepared. Magnet 1 measures the spin along z and only its "+" beam is
// kept, so every atom that goes on is in the state alpha. Magnet 2 measures along an axis tilted by an angle theta
// from z (theta = 0 is z again, 90 degrees is x, 180 degrees is -z): the atom comes out "+" along that axis with
// probability cos^2(theta/2). An optional third magnet along z takes the "+" beam of magnet 2 and finds +z with
// probability cos^2(theta/2) again: measuring along the tilted axis has erased what magnet 1 prepared.
// One atom or ten fly through one by one; larger batches are tallied without the flight.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get, so the same file runs in
// MyST's {anywidget} directive (ch05/03), in a reveal.js deck through a module-script loader (slides/ch05/03),
// and in Jupyter or Colab through the anywidget package. No dependencies.
// Model keys, all optional: angle (degrees, the tilt of magnet 2, default 90), third (true adds the third magnet),
// fontSize (CSS size of the controls and readout) and status (false hides the line that explains the case).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00";
const SVGNS = "http://www.w3.org/2000/svg";
const DEG = Math.PI / 180;

const CSS = `
.sg-root { --sg-fg: #212529; --sg-muted: #6c757d; --sg-border: #ced4da; --sg-btn: #f8f9fa; --sg-on: #e3f0f4;
  --sg-card: #ffffff; --sg-mag: #eef0f2; --sg-track: #e9ecef; --sg-teal: ${TEAL}; --sg-orange: ${ORANGE};
  --sg-red: ${CARDINAL}; color: var(--sg-fg); background: var(--sg-card); border: 1px solid var(--sg-border);
  border-radius: 10px; padding: 0.7em 1em 0.7em; text-align: left; line-height: 1.4; letter-spacing: normal;
  font-family: inherit; box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.sg-root.sg-dark { --sg-fg: #e9ecef; --sg-muted: #adb5bd; --sg-border: #495057; --sg-btn: #2b3035; --sg-on: #16353f;
  --sg-card: #1e2125; --sg-mag: #2b3035; --sg-track: #343a40; --sg-teal: #45a9c6; --sg-orange: #f59f3a;
  --sg-red: #f05d6f; }
.sg-svg { display: block; width: 100%; height: auto; margin: 0 0 0.2em; user-select: none; -webkit-user-select: none; }
.sg-svg text { font-family: inherit; fill: var(--sg-fg); }
.sg-svg .sg-muted { fill: var(--sg-muted); }
.sg-svg .sg-t { fill: var(--sg-teal); } .sg-svg .sg-o { fill: var(--sg-orange); }
.sg-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em; margin: 0.3em 0; }
.sg-label { color: var(--sg-muted); margin-right: 0.2em; }
.sg-gap { width: 0.8em; }
.sg-btn { font: inherit; color: var(--sg-fg); background: var(--sg-btn); border: 1px solid var(--sg-border);
  border-radius: 999px; padding: 0.15em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; }
.sg-btn:hover { border-color: ${TEAL}; }
.sg-btn.sg-on { border-color: ${TEAL}; background: var(--sg-on); font-weight: 600; }
.sg-btn.sg-go { border-color: ${TEAL}; color: #fff; background: ${TEAL}; font-weight: 600; }
.sg-btn.sg-go:hover { filter: brightness(1.1); }
.sg-slider { display: flex; align-items: center; gap: 0.4em; }
.sg-slider input { accent-color: ${TEAL}; width: 9em; margin: 0; }
.sg-slider span { min-width: 3.2em; font-variant-numeric: tabular-nums; }
.sg-readout { font-variant-numeric: tabular-nums; margin-top: 0.3em; }
.sg-readout b { font-weight: 600; }
.sg-readout .sg-t { color: var(--sg-teal); font-weight: 600; } .sg-readout .sg-o { color: var(--sg-orange); font-weight: 600; }
.sg-status { font-weight: 600; margin-top: 0.25em; min-height: 2.8em; }
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

// ---------------------------------------------------------------- geometry (viewBox 760 x 232)
const M1 = { x: 110, y: 165 }, M2 = { x: 250, y: 115 }, M3 = { x: 390, y: 65 };   // left edge and centre line of each magnet
const MW = 70, MH = 60;

function routes(third) {
  // every way through the apparatus, as polylines; "end" says what happens there
  const r = {
    in: [[60, 165], [M1.x + MW, 165]],
    b1: [[M1.x + MW, 165], [215, 205], [234, 205]],                       // magnet 1, "-": blocked
    a1: [[M1.x + MW, 165], [215, 115], [M2.x + MW, 115]],                 // magnet 1, "+": on to magnet 2
  };
  if (!third) {
    r.up = [[M2.x + MW, 115], [355, 80], [400, 80]];
    r.down = [[M2.x + MW, 115], [355, 150], [400, 150]];
  } else {
    r.b2 = [[M2.x + MW, 115], [355, 155], [374, 155]];
    r.a2 = [[M2.x + MW, 115], [355, 65], [M3.x + MW, 65]];
    r.up = [[M3.x + MW, 65], [495, 35], [540, 35]];
    r.down = [[M3.x + MW, 65], [495, 95], [540, 95]];
  }
  return r;
}

const pts = (p) => p.map((q) => q.join(",")).join(" ");

function along(path, s) {                    // the point a distance s along a polyline, or null past its end
  for (let i = 1; i < path.length; i++) {
    const [x0, y0] = path[i - 1], [x1, y1] = path[i], d = Math.hypot(x1 - x0, y1 - y0);
    if (s <= d) return [x0 + ((x1 - x0) * s) / d, y0 + ((y1 - y0) * s) / d];
    s -= d;
  }
  return null;
}

function render({ model, el }) {
  const get = (k, d) => {
    try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; }
  };
  let theta = Math.min(180, Math.max(0, +get("angle", 90) || 0));
  let third = get("third", false) === true;
  const showStatus = get("status", true) !== false;

  // ---------------------------------------------------------------- DOM
  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "sg-root", el);
  root.style.fontSize = get("fontSize", "15px");
  root.setAttribute("data-prevent-swipe", "");

  const pic = svg("svg", { viewBox: "0 0 760 232", class: "sg-svg", role: "img",
    "aria-label": "atoms from an oven pass through Stern-Gerlach magnets in a row" }, root);

  const button = (parent, cls, text, fn) => {
    const b = html("button", cls, parent, text);
    b.type = "button";
    b.addEventListener("click", () => { fn(); b.blur(); });
    return b;
  };

  const rowAxis = html("div", "sg-row", root);
  html("span", "sg-label", rowAxis, "magnet 2 along:");
  const presets = [[0, "z"], [90, "x"], [180, "−z"]].map(([a, name]) => [a, button(rowAxis, "sg-btn", name, () => setAngle(a))]);
  const wrap = html("label", "sg-slider", rowAxis);
  html("span", "sg-label", wrap, "or tilt it");
  const slider = html("input", null, wrap);
  Object.assign(slider, { type: "range", min: 0, max: 180, step: 5, value: theta });
  const tiltOut = html("span", null, wrap, "");
  slider.addEventListener("input", () => setAngle(+slider.value));
  html("span", "sg-gap", rowAxis);
  const thirdBtn = button(rowAxis, "sg-btn", "third magnet along z", () => { third = !third; reset(); });

  const rowGo = html("div", "sg-row", root);
  html("span", "sg-label", rowGo, "send atoms:");
  for (const k of [1, 10, 100, 1000]) button(rowGo, "sg-btn sg-go", `+${k}`, () => send(k));
  button(rowGo, "sg-btn", "reset", () => reset());
  const readout = html("div", "sg-readout", root);
  const status = html("div", "sg-status", root);
  if (!showStatus) status.style.display = "none";

  // ---------------------------------------------------------------- state
  let R, n, flying, timer, pending, chunk;
  const pUp = () => Math.cos((theta * DEG) / 2) ** 2;

  function reset() {
    R = routes(third);
    n = { sent: 0, b1: 0, b2: 0, up: 0, down: 0 };
    flying = []; pending = 0; chunk = 0;
    if (timer) { clearTimeout(timer); timer = 0; }
    presets.forEach(([a, b]) => b.classList.toggle("sg-on", a === theta));
    thirdBtn.classList.toggle("sg-on", third);
    slider.value = theta;
    tiltOut.textContent = `${theta}°`;
    draw();
  }

  function setAngle(a) { theta = a; reset(); }

  function fate() {                          // what one atom does: which routes it takes and where it ends
    const p = pUp(), legs = ["in"];
    if (Math.random() >= 0.5) return { legs: legs.concat("b1"), end: "b1" };
    legs.push("a1");
    const plus2 = Math.random() < p;
    if (!third) return { legs: legs.concat(plus2 ? "up" : "down"), end: plus2 ? "up" : "down" };
    if (!plus2) return { legs: legs.concat("b2"), end: "b2" };
    legs.push("a2");
    const plus3 = Math.random() < p;
    return { legs: legs.concat(plus3 ? "up" : "down"), end: plus3 ? "up" : "down" };
  }

  const tally = (f) => { n.sent++; n[f.end]++; };

  function send(k) {
    if (k <= 10) {
      for (let i = 0; i < k; i++) {
        const f = fate();
        f.path = f.legs.reduce((acc, name) => acc.concat(acc.length ? R[name].slice(1) : R[name]), []);
        f.s = -i * 46;                       // staggered: one atom every few steps
        flying.push(f);
      }
    } else {
      pending += k;
      chunk = Math.max(chunk, Math.ceil(pending / 20));     // a batch lands in about 20 steps
    }
    if (!timer) timer = setTimeout(step, 30);
  }

  function step() {
    for (const f of flying) f.s += 15;
    flying = flying.filter((f) => {
      if (f.s < 0 || along(f.path, f.s)) return true;
      tally(f);
      return false;
    });
    if (pending > 0) {
      const m = Math.min(chunk, pending);
      for (let i = 0; i < m; i++) tally(fate());
      pending -= m;
      if (!pending) chunk = 0;
    }
    draw();
    timer = flying.length || pending ? setTimeout(step, 30) : 0;
  }

  // ---------------------------------------------------------------- drawing
  function magnet(m, angle, caption) {
    svg("rect", { x: m.x, y: m.y - MH / 2, width: MW, height: MH, rx: 9, fill: "var(--sg-mag)", stroke: "var(--sg-fg)",
      "stroke-width": 1.8 }, pic);
    const cx = m.x + MW / 2, cy = m.y, ux = Math.sin(angle * DEG), uy = -Math.cos(angle * DEG), L = 19;
    svg("circle", { cx, cy, r: 22, fill: "var(--sg-card)", stroke: "var(--sg-border)", "stroke-width": 1.2 }, pic);
    svg("line", { x1: cx - L * ux, y1: cy - L * uy, x2: cx + (L - 7) * ux, y2: cy + (L - 7) * uy, stroke: "var(--sg-fg)",
      "stroke-width": 2.6, "stroke-linecap": "round" }, pic);
    const hx = cx + L * ux, hy = cy + L * uy, px = -uy, py = ux;
    svg("polygon", { points: pts([[hx, hy], [hx - 10 * ux + 5.5 * px, hy - 10 * uy + 5.5 * py],
      [hx - 10 * ux - 5.5 * px, hy - 10 * uy - 5.5 * py]]), fill: "var(--sg-fg)" }, pic);
    const t = svg("text", { x: cx, y: m.y + MH / 2 + 17, "font-size": 14, "text-anchor": "middle" }, pic);
    t.textContent = caption;
  }

  function block(x, y, count) {
    svg("line", { x1: x, y1: y - 13, x2: x, y2: y + 13, stroke: "var(--sg-fg)", "stroke-width": 5 }, pic);
    const t = svg("text", { x: x + 9, y: y + 5, "font-size": 13, class: "sg-muted" }, pic);
    t.textContent = `blocked: ${count}`;
  }

  function detector(x, y, count, total, predicted, cls, colour, sign, len) {
    svg("rect", { x, y: y - 11, width: 14, height: 22, rx: 3, fill: colour }, pic);
    const s = svg("text", { x: x + 7, y: y + 5, "font-size": 15, "font-weight": 700, "text-anchor": "middle" }, pic);
    s.textContent = sign; s.setAttribute("style", "fill: #fff");
    const x0 = x + 22;
    svg("rect", { x: x0, y: y - 8, width: len, height: 16, rx: 3, fill: "var(--sg-track)" }, pic);
    const frac = total ? count / total : 0;
    if (frac > 0) svg("rect", { x: x0, y: y - 8, width: Math.max(2, len * frac), height: 16, rx: 3, fill: colour }, pic);
    svg("line", { x1: x0 + len * predicted, y1: y - 13, x2: x0 + len * predicted, y2: y + 13, stroke: "var(--sg-red)",
      "stroke-width": 3 }, pic);
    const t = svg("text", { x: x0 + len + 9, y: y + 5, "font-size": 14, class: cls }, pic);
    t.textContent = total ? `${count.toLocaleString()} (${Math.round(100 * frac)}%)` : "0";
  }

  const caption = (a) => (a === 0 ? "z" : a === 90 ? "x" : a === 180 ? "−z" : `tilted ${a}°`);

  function draw() {
    while (pic.firstChild) pic.removeChild(pic.firstChild);
    // oven and beams
    svg("rect", { x: 14, y: 147, width: 46, height: 36, rx: 4, fill: "var(--sg-mag)", stroke: "var(--sg-muted)",
      "stroke-width": 1.4 }, pic);
    svg("text", { x: 37, y: 201, "font-size": 13, "text-anchor": "middle", class: "sg-muted" }, pic).textContent = "oven";
    const beam = (name, colour) => svg("polyline", { points: pts(R[name]), fill: "none", stroke: colour, "stroke-width": 2.4,
      "stroke-linejoin": "round", opacity: 0.85 }, pic);
    beam("in", "var(--sg-muted)");
    beam("b1", "var(--sg-orange)"); beam("a1", "var(--sg-teal)");
    if (third) { beam("b2", "var(--sg-orange)"); beam("a2", "var(--sg-teal)"); }
    beam("up", "var(--sg-teal)"); beam("down", "var(--sg-orange)");
    // magnets, blocks, detectors
    magnet(M1, 0, "z");
    magnet(M2, theta, caption(theta));
    block(234, 205, n.b1);
    const p = pUp(), total = n.up + n.down;
    if (third) {
      magnet(M3, 0, "z");
      block(374, 155, n.b2);
      detector(540, 35, n.up, total, p, "sg-t", "var(--sg-teal)", "+", 120);
      detector(540, 95, n.down, total, 1 - p, "sg-o", "var(--sg-orange)", "−", 120);
    } else {
      detector(400, 80, n.up, total, p, "sg-t", "var(--sg-teal)", "+", 240);
      detector(400, 150, n.down, total, 1 - p, "sg-o", "var(--sg-orange)", "−", 240);
    }
    const key = svg("text", { x: 746, y: 224, "font-size": 12.5, "text-anchor": "end", class: "sg-muted" }, pic);
    key.textContent = "+ spin found along the magnet's arrow · − against it · red mark: predicted";
    for (const f of flying) {
      const q = f.s >= 0 ? along(f.path, f.s) : null;
      if (q) svg("circle", { cx: q[0], cy: q[1], r: 5, fill: "var(--sg-fg)", stroke: "var(--sg-card)", "stroke-width": 1.2 }, pic);
    }

    const last = third ? 3 : 2;
    readout.innerHTML = `<b>${n.sent.toLocaleString()}</b> atom${n.sent === 1 ? "" : "s"} sent · reached magnet ${last}: <b>${total.toLocaleString()}</b>` +
      ` · found <span class="sg-t">+ ${n.up.toLocaleString()}</span> and <span class="sg-o">− ${n.down.toLocaleString()}</span>` +
      ` · predicted + : cos²(θ/2) = <b>${p.toFixed(2)}</b>`;
    if (showStatus) {
      const pc = p.toFixed(2);
      status.textContent = !third
        ? theta === 0 ? "z, then z again: every atom found + is found + again. Magnet 1 prepared the state α, and measuring Sz twice changes nothing."
        : theta === 90 ? "z, then x: half and half. A spin that is sharp along z is completely undecided along x."
        : theta === 180 ? "Magnet 2 is upside down: its + is the − of magnet 1, so no atom comes out +."
        : `Tilted by ${theta}°: + with probability cos²(θ/2) = ${pc}, between certain (0°) and a coin toss (90°).`
        : theta === 0 ? "Three magnets along z: after the first, nothing changes."
        : theta === 90 ? "z, then x, then z again: half and half. Measuring Sx erased what magnet 1 had prepared."
        : theta === 180 ? "No atom passes magnet 2, so magnet 3 sees nothing."
        : `Magnet 2 leaves the spin along its own axis, ${theta}° from z, so magnet 3 finds + with probability cos²(θ/2) = ${pc}.`;
    }
  }

  // ---------------------------------------------------------------- dark mode follows the page
  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("sg-dark")) { root.classList.toggle("sg-dark", dark); draw(); }
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  reset();
  syncDark();
  return () => { if (timer) clearTimeout(timer); if (obs) obs.disconnect(); };
}

export default { render };
