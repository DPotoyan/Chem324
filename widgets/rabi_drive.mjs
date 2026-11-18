// Two levels driven by light: Rabi oscillations, resonance and the limits of first-order perturbation theory.
//
// The system is a particle in a box, starting in psi_1 and driven toward psi_2 by light of frequency omega.
// Within the rotating-wave approximation the two coefficients are known exactly:
//   P_f(t) = (Omega^2 / W^2) sin^2(W t / 2),  W = sqrt(Omega^2 + delta^2),
// with the Rabi frequency Omega = |M_fi| E / hbar and the detuning delta = omega_fi - omega. Time is measured in
// units of 1 / Omega_0, the Rabi frequency at the reference field strength; the field slider sets Omega / Omega_0
// and the detuning slider sets delta / Omega_0. The density also shows the cross term, which swings at the
// frequency of the light (drawn at 16 Omega_0 so that the swing is visible).
// Left: the density in the box. Right, top: the probability of the upper level against time, exact (orange) and
// first order (purple, dashed). Right, bottom: the largest transfer against the detuning, with the present
// detuning marked.
//
// anywidget shape, export default { render({ model, el }) }, reading only model.get. No dependencies.
// Model keys, optional: fontSize (CSS size), detuning (-4 to 4), field (0.25 to 2), autoplay (false starts
// paused), status and note (false hides the verdict or the description line).

const TEAL = "#107895", CARDINAL = "#C8102E", ORANGE = "#e07b00", PURPLE = "#6a3d9a";
const SVGNS = "http://www.w3.org/2000/svg";
const TMAX = 4 * Math.PI, CARRIER = 16, STEPS = 260, TICK = 45;

// populations and the cross term of the density at time t (units of 1 / Omega_0)
function coefficients(t, om, de) {
  const W = Math.sqrt(om * om + de * de), s = Math.sin(W * t / 2), c = Math.cos(W * t / 2);
  const Pf = (om / W) ** 2 * s * s;
  const cross = (om / W) * s * (c * Math.sin(CARRIER * t) + (de / W) * s * Math.cos(CARRIER * t));
  return { Pf, Pi: 1 - Pf, cross, W };
}

const W_ = 1000, H_ = 400, AL = 40, AR = 400, PT = 30, PB = 352;
const BL = 520, BR = 975, T1 = 34, T2 = 196, D1 = 262, D2 = 352, DMAX = 4;

const CSS = `
.rd-root { --rd-fg: #212529; --rd-muted: #6c757d; --rd-border: #ced4da; --rd-btn: #f8f9fa; --rd-card: #ffffff;
  --rd-teal: ${TEAL}; --rd-orange: ${ORANGE}; --rd-purple: ${PURPLE}; --rd-red: ${CARDINAL}; --rd-on: #e7f1f4;
  color: var(--rd-fg); background: var(--rd-card); border: 1px solid var(--rd-border); border-radius: 10px;
  padding: 0.7em 1em; text-align: left; line-height: 1.4; letter-spacing: normal; font-family: inherit;
  box-sizing: border-box; max-width: 100%; margin: 0.6em 0 1.2em; }
.rd-root.rd-dark { --rd-fg: #e9ecef; --rd-muted: #adb5bd; --rd-border: #495057; --rd-btn: #2b3035; --rd-card: #1e2125;
  --rd-teal: #45a9c6; --rd-orange: #f59f3a; --rd-purple: #b08be0; --rd-red: #f05d6f; --rd-on: #1f3a44; }
.rd-controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4em 1.1em; margin: 0 0 0.3em; }
.rd-btn { font: inherit; color: var(--rd-fg); background: var(--rd-btn); border: 1px solid var(--rd-border);
  border-radius: 999px; padding: 0.12em 0.75em; cursor: pointer; line-height: 1.5; margin: 0; min-width: 4.2em; }
.rd-btn:hover { border-color: ${TEAL}; }
.rd-slider { display: flex; align-items: center; gap: 0.45em; }
.rd-slider input { width: 8.5em; accent-color: ${TEAL}; }
.rd-val { font-variant-numeric: tabular-nums; min-width: 3.6em; color: var(--rd-muted); }
.rd-plot { display: block; width: 100%; height: auto; }
.rd-plot text { font-family: inherit; fill: var(--rd-fg); }
.rd-status { font-weight: 600; margin: 0.2em 0 0; min-height: 2.8em; }
.rd-note { color: var(--rd-muted); }
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
// text with subscripts written as _{...}
function rich(t, str) {
  t.textContent = "";
  str.split(/(_\{[^}]*\})/).forEach((part) => {
    if (!part) return;
    const ts = document.createElementNS(SVGNS, "tspan"), isSub = part.startsWith("_{");
    ts.textContent = isSub ? part.slice(2, -1) : part;
    if (isSub) { ts.setAttribute("dy", "0.3em"); ts.setAttribute("font-size", "75%"); }
    else if (t.lastChild && t.lastChild.getAttribute("dy") === "0.3em") ts.setAttribute("dy", "-0.225em");
    t.appendChild(ts);
  });
}

function render({ model, el }) {
  const get = (k, d) => { try { const v = model.get(k); return v === undefined || v === null ? d : v; } catch (e) { return d; } };

  const style = html("style", null, el); style.textContent = CSS;
  const root = html("div", "rd-root", el);
  root.setAttribute("data-prevent-swipe", "");
  root.style.fontSize = get("fontSize", "15px");

  const controls = html("div", "rd-controls", root);
  const playBtn = html("button", "rd-btn", controls, "pause"); playBtn.type = "button";
  const slider = (label, min, max, step, value) => {
    const box = html("label", "rd-slider", controls);
    html("span", null, box).innerHTML = label;
    const input = html("input", null, box); input.type = "range"; input.min = min; input.max = max; input.step = step; input.value = value;
    const val = html("span", "rd-val", box);
    input.addEventListener("change", () => input.blur());
    return { input, val };
  };
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const sD = slider("detuning δ", -DMAX, DMAX, 0.05, clamp(+get("detuning", 0) || 0, -DMAX, DMAX));
  const sF = slider("field", 0.25, 2, 0.05, clamp(+get("field", 1) || 1, 0.25, 2));
  const sT = slider("time", 0, TMAX, TMAX / STEPS, 0);

  const plot = svg("svg", { viewBox: `0 0 ${W_} ${H_}`, class: "rd-plot", role: "img",
    "aria-label": "the density of a driven particle in a box, the probability of the upper level against time, and the largest transfer against detuning" }, root);
  const lab = (x, y, s, o = {}) => { const t = svg("text", Object.assign({ x, y, "font-size": 16.5 }, o), plot); rich(t, s); return t; };
  const muted = "fill: var(--rd-muted)";

  // left: the box and the density
  const XA = (x) => AL + 16 + x * (AR - AL - 32), YA = (r) => PB - r * 92;
  const dens = svg("path", { fill: "var(--rd-teal)", "fill-opacity": 0.3, stroke: "var(--rd-teal)", "stroke-width": 2.4 }, plot);
  svg("line", { x1: XA(0), x2: XA(0), y1: PT, y2: PB, stroke: "var(--rd-fg)", "stroke-width": 2.6 }, plot);
  svg("line", { x1: XA(1), x2: XA(1), y1: PT, y2: PB, stroke: "var(--rd-fg)", "stroke-width": 2.6 }, plot);
  svg("line", { x1: XA(0), x2: XA(1), y1: PB, y2: PB, stroke: "var(--rd-fg)", "stroke-width": 2.6 }, plot);
  lab(XA(0), PB + 20, "0", { "text-anchor": "middle", style: muted });
  lab(XA(1), PB + 20, "L", { "text-anchor": "middle", style: muted });
  lab(XA(0.5), PB + 20, "density |Ψ(x, t)|²", { "text-anchor": "middle", style: muted });
  const dip = svg("line", { y1: PT + 12, y2: PT + 12, stroke: "var(--rd-red)", "stroke-width": 4, "stroke-linecap": "round" }, plot);
  svg("line", { x1: XA(0.5), x2: XA(0.5), y1: PT + 4, y2: PT + 20, stroke: "var(--rd-muted)" }, plot);
  lab(XA(0.5), PT - 6, "⟨x⟩", { "text-anchor": "middle", style: "fill: var(--rd-red)" });

  // right, top: probability against time
  const XT = (t) => BL + t / TMAX * (BR - BL), YT = (p) => T2 - p * (T2 - T1);
  svg("line", { x1: BL, x2: BL, y1: T1, y2: T2, stroke: "var(--rd-muted)" }, plot);
  svg("line", { x1: BL, x2: BR, y1: T2, y2: T2, stroke: "var(--rd-muted)" }, plot);
  for (const p of [0, 0.5, 1]) {
    svg("line", { x1: BL - 6, x2: BL, y1: YT(p), y2: YT(p), stroke: "var(--rd-muted)" }, plot);
    lab(BL - 10, YT(p) + 5, String(p), { "text-anchor": "end", style: muted });
  }
  for (let k = 0; k <= 4; k++) {
    svg("line", { x1: XT(k * Math.PI), x2: XT(k * Math.PI), y1: T2, y2: T2 + 6, stroke: "var(--rd-muted)" }, plot);
    lab(XT(k * Math.PI), T2 + 21, k === 0 ? "0" : k === 1 ? "π" : `${k}π`, { "text-anchor": "middle", style: muted });
  }
  lab(BR, T2 + 41, "time (units of 1/Ω_{0})", { "text-anchor": "end", style: muted });
  lab(BL + 8, T1 - 10, "probability of the upper level:", { style: muted });
  lab(BL + 244, T1 - 10, "exact", { style: "fill: var(--rd-orange)", "font-weight": 600 });
  lab(BL + 296, T1 - 10, "first order", { style: "fill: var(--rd-purple)", "font-weight": 600 });
  const clipId = `rd-clip-${Math.random().toString(36).slice(2)}`;
  svg("rect", { x: BL, y: T1 - 2, width: BR - BL, height: T2 - T1 + 2 }, svg("clipPath", { id: clipId }, svg("defs", {}, plot)));
  const gT = svg("g", { "clip-path": `url(#${clipId})` }, plot);
  const pFirst = svg("path", { fill: "none", stroke: "var(--rd-purple)", "stroke-width": 2.2, "stroke-dasharray": "7 4" }, gT);
  const pExact = svg("path", { fill: "none", stroke: "var(--rd-orange)", "stroke-width": 2.8 }, gT);
  const tLine = svg("line", { y1: T1, y2: T2, stroke: "var(--rd-red)", "stroke-width": 1.4 }, plot);
  const tDot = svg("circle", { r: 6, fill: "var(--rd-red)" }, plot);

  // right, bottom: largest transfer against detuning
  const XD = (d) => BL + (d + DMAX) / (2 * DMAX) * (BR - BL), YD = (p) => D2 - p * (D2 - D1);
  svg("line", { x1: BL, x2: BR, y1: D2, y2: D2, stroke: "var(--rd-muted)" }, plot);
  for (let d = -4; d <= 4; d += 2) {
    svg("line", { x1: XD(d), x2: XD(d), y1: D2, y2: D2 + 6, stroke: "var(--rd-muted)" }, plot);
    lab(XD(d), D2 + 21, String(d), { "text-anchor": "middle", style: muted });
  }
  lab(BR, D2 + 41, "detuning δ (units of Ω_{0})", { "text-anchor": "end", style: muted });
  lab(BL + 8, D1 - 8, "largest transfer", { style: muted });
  const pLine = svg("path", { fill: "var(--rd-orange)", "fill-opacity": 0.2, stroke: "var(--rd-orange)", "stroke-width": 2.2 }, plot);
  const dDot = svg("circle", { r: 6, fill: "var(--rd-red)" }, plot);

  const status = html("div", "rd-status", root);
  if (get("status", true) === false) status.style.display = "none";
  const note = html("div", "rd-note", root);
  if (get("note", true) === false) note.style.display = "none";
  note.innerHTML = "A particle in a box, driven from ψ<sub>1</sub> toward ψ<sub>2</sub>. Ω<sub>0</sub> is the Rabi frequency at field 1; " +
    "the field slider multiplies it. The density sloshes at the frequency of the light while both levels are occupied.";

  let t = 0, playing = get("autoplay", true) !== false, timer = null;

  function curves() {                                                // everything that depends on the sliders only
    const om = +sF.input.value, de = +sD.input.value;
    sD.val.innerHTML = `${de.toFixed(2)} Ω<sub>0</sub>`; sF.val.textContent = `× ${om.toFixed(2)}`;
    let dx = "", d1 = "";
    for (let i = 0; i <= 300; i++) {
      const tt = TMAX * i / 300, c = coefficients(tt, om, de), m = i ? "L" : "M";
      const first = de === 0 ? (om * tt / 2) ** 2 : (om / de) ** 2 * Math.sin(de * tt / 2) ** 2;
      dx += m + XT(tt).toFixed(1) + "," + YT(c.Pf).toFixed(1);
      d1 += m + XT(tt).toFixed(1) + "," + YT(Math.min(first, 1.3)).toFixed(1);
    }
    pExact.setAttribute("d", dx); pFirst.setAttribute("d", d1);
    let dl = `M${XD(-DMAX)},${D2}`;
    for (let i = 0; i <= 200; i++) { const d = -DMAX + 2 * DMAX * i / 200; dl += "L" + XD(d).toFixed(1) + "," + YD(om * om / (om * om + d * d)).toFixed(1); }
    pLine.setAttribute("d", dl + `L${XD(DMAX)},${D2}Z`);
    dDot.setAttribute("cx", XD(de)); dDot.setAttribute("cy", YD(om * om / (om * om + de * de)));
    const max = om * om / (om * om + de * de), W = Math.sqrt(om * om + de * de);
    status.textContent = Math.abs(de) < 0.026
      ? `On resonance: the whole population reaches the upper level at t = ${(Math.PI / om).toFixed(2)} (a π pulse), then light drives it back down.`
      : `Detuned by ${Math.abs(de / om).toFixed(2)} Ω: at most ${(100 * max).toFixed(0)}% reaches the upper level, and the cycle runs ${(W / om).toFixed(2)} times faster.`;
  }

  function frame() {                                                 // everything that depends on time
    const om = +sF.input.value, de = +sD.input.value, c = coefficients(t, om, de);
    let d = `M${XA(0)},${PB}`, mean = 0;
    for (let i = 0; i <= 120; i++) {
      const x = i / 120, a = Math.SQRT2 * Math.sin(Math.PI * x), b = Math.SQRT2 * Math.sin(2 * Math.PI * x);
      const rho = c.Pi * a * a + c.Pf * b * b + 2 * c.cross * a * b;
      mean += (i === 0 || i === 120 ? 0.5 : 1) * x * rho / 120;
      d += "L" + XA(x).toFixed(1) + "," + YA(Math.max(rho, 0)).toFixed(1);
    }
    dens.setAttribute("d", d + `L${XA(1)},${PB}Z`);
    dip.setAttribute("x1", XA(0.5)); dip.setAttribute("x2", XA(0.5 + 2.2 * (mean - 0.5)));
    tLine.setAttribute("x1", XT(t)); tLine.setAttribute("x2", XT(t));
    tDot.setAttribute("cx", XT(t)); tDot.setAttribute("cy", YT(c.Pf));
    sT.val.textContent = t.toFixed(2);
  }

  function tick() {
    timer = null;
    if (!playing) return;
    t += TMAX / STEPS;
    if (t > TMAX + 1e-9) t = 0;
    sT.input.value = t;
    frame();
    timer = setTimeout(tick, TICK);
  }
  function setPlaying(on) {
    playing = on;
    playBtn.textContent = on ? "pause" : "play";
    if (timer) { clearTimeout(timer); timer = null; }
    if (on) timer = setTimeout(tick, TICK);
  }
  playBtn.addEventListener("click", () => { playBtn.blur(); setPlaying(!playing); });
  sD.input.addEventListener("input", () => { curves(); frame(); });
  sF.input.addEventListener("input", () => { curves(); frame(); });
  sT.input.addEventListener("input", () => { setPlaying(false); t = +sT.input.value; frame(); });

  const html0 = typeof document !== "undefined" ? document.documentElement : null;
  const syncDark = () => {
    const dark = !!html0 && html0.classList.contains("dark");
    if (dark !== root.classList.contains("rd-dark")) root.classList.toggle("rd-dark", dark);
  };
  const obs = html0 && typeof MutationObserver !== "undefined" ? new MutationObserver(syncDark) : null;
  if (obs) obs.observe(html0, { attributes: true, attributeFilter: ["class"] });

  curves(); frame(); syncDark();
  setPlaying(playing);
  return () => { if (obs) obs.disconnect(); if (timer) clearTimeout(timer); };
}

export default { render };
export { coefficients };
