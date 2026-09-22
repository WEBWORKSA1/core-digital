/* Core.Digital — directory rendering (homepage + directory page) */
(function () {
  "use strict";
  var T = window.CD_TOOLS || [], S = (window.CD && CD.store) || { get: function (k, d) { return d; }, set: function () {} };
  var $ = function (s) { return document.querySelector(s); };
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var cats = T.reduce(function (a, t) { a[t.c] = (a[t.c] || 0) + 1; return a; }, {});
  var catNames = Object.keys(cats).sort();
  var saved = S.get("cd-saved", []);
  var hues = [250, 200, 330, 160, 20, 280, 45, 185];

  function color(n) { var h = 0; for (var i = 0; i < n.length; i++) h = (h * 31 + n.charCodeAt(i)) >>> 0; var hue = hues[h % hues.length]; return "linear-gradient(135deg,hsl(" + hue + " 80% 58%),hsl(" + (hue + 40) + " 80% 48%))"; }
  function withRef(u) { try { var x = new URL(u); x.searchParams.set("ref", "core.digital"); return x.toString(); } catch (e) { return u; } }
  function card(t) {
    var isSaved = saved.indexOf(t.n) > -1, cls = (t.p || "").toLowerCase().replace(/\s/g, "");
    var badgeCls = cls === "opensource" ? "free" : cls;
    return '<article class="card tool' + (t.f ? " featured" : "") + '">' +
      '<div class="tool-top"><div class="tool-logo" style="background:' + color(t.n) + '" aria-hidden="true">' + esc(t.n.charAt(0)) + '</div>' +
      '<div><h3>' + esc(t.n) + (t.v ? ' <span title="Verified listing" style="color:var(--brand-2)">✓</span>' : "") + '</h3><span class="result-count">' + esc(t.c) + '</span></div></div>' +
      '<p>' + esc(t.d) + '</p>' +
      '<div class="meta">' + (t.f ? '<span class="badge sponsored">Sponsored</span>' : "") + '<span class="badge ' + badgeCls + '">' + esc(t.p) + '</span>' +
      (t.t || []).slice(0, 2).map(function (x) { return '<span class="badge">#' + esc(x) + '</span>'; }).join("") + '</div>' +
      '<div class="tool-actions"><a class="btn btn-sm btn-ghost" href="' + esc(withRef(t.u)) + '" target="_blank" rel="nofollow noopener' + (t.f ? " sponsored" : "") + '">Visit ↗</a>' +
      '<button class="save-btn' + (isSaved ? " saved" : "") + '" data-save="' + esc(t.n) + '" aria-pressed="' + isSaved + '">' + (isSaved ? "♥ Saved" : "♡ Save") + '</button></div></article>';
  }
  function bindSave(scope) {
    Array.prototype.forEach.call(scope.querySelectorAll("[data-save]"), function (b) {
      b.addEventListener("click", function () {
        var n = b.getAttribute("data-save"), i = saved.indexOf(n);
        if (i > -1) saved.splice(i, 1); else saved.push(n);
        S.set("cd-saved", saved);
        var on = i === -1; b.classList.toggle("saved", on); b.setAttribute("aria-pressed", on); b.textContent = on ? "♥ Saved" : "♡ Save";
        if (window.CD) CD.toast(on ? "Saved to your list" : "Removed");
      });
    });
  }

  // Stats
  var st = $("#stat-tools"); if (st) st.textContent = T.length + "+";
  var sc = $("#stat-cats"); if (sc) sc.textContent = catNames.length;

  // Home: category chips + highlighted tools
  var hc = $("#home-cats");
  if (hc) hc.innerHTML = catNames.map(function (c) { return '<a class="chip" href="directory.html?cat=' + encodeURIComponent(c) + '">' + esc(c) + ' <span class="badge">' + cats[c] + '</span></a>'; }).join("");
  var ht = $("#home-tools");
  if (ht) {
    var seen = {}, picks = T.filter(function (t) { if (t.f) return true; if (seen[t.c]) return false; seen[t.c] = 1; return true; }).slice(0, 8);
    ht.innerHTML = picks.map(card).join(""); bindSave(ht);
  }

  // Directory page
  var grid = $("#dir-grid"); if (!grid) return;
  var q = $("#q"), sort = $("#sort"), cBox = $("#f-cats"), pBox = $("#f-price"), count = $("#dir-count"), onlySaved = $("#f-saved");
  var params = new URLSearchParams(location.search);
  cBox.innerHTML = catNames.map(function (c) { return '<label><input type="checkbox" value="' + esc(c) + '"' + (params.get("cat") === c ? " checked" : "") + '> ' + esc(c) + ' <span class="result-count">(' + cats[c] + ')</span></label>'; }).join("");
  if (params.get("q")) q.value = params.get("q");
  function checked(box) { return Array.prototype.map.call(box.querySelectorAll("input:checked"), function (i) { return i.value; }); }
  function render() {
    var term = q.value.trim().toLowerCase(), cs = checked(cBox), ps = checked(pBox);
    var list = T.filter(function (t) {
      if (cs.length && cs.indexOf(t.c) < 0) return false;
      if (ps.length && ps.indexOf(t.p) < 0) return false;
      if (onlySaved && onlySaved.checked && saved.indexOf(t.n) < 0) return false;
      if (!term) return true;
      return (t.n + " " + t.c + " " + t.d + " " + (t.t || []).join(" ")).toLowerCase().indexOf(term) > -1;
    });
    var s = sort.value;
    list.sort(function (a, b) {
      if (!!b.f - !!a.f) return !!b.f - !!a.f; // sponsored first, always labelled
      if (s === "az") return a.n.localeCompare(b.n);
      if (s === "za") return b.n.localeCompare(a.n);
      if (s === "cat") return a.c.localeCompare(b.c) || a.n.localeCompare(b.n);
      if (s === "free") return (a.p === "Free" || a.p === "Open source" ? 0 : a.p === "Freemium" ? 1 : 2) - (b.p === "Free" || b.p === "Open source" ? 0 : b.p === "Freemium" ? 1 : 2);
      return 0;
    });
    count.textContent = list.length + " tool" + (list.length === 1 ? "" : "s");
    grid.innerHTML = list.length ? list.map(card).join("") :
      '<div class="card" style="grid-column:1/-1"><h3>No match yet</h3><p>Know a great tool we\'re missing? <a href="submit.html">Submit it</a> — or <a href="get-matched.html">get matched with an expert</a> who can recommend one.</p></div>';
    bindSave(grid);
    var u = new URL(location.href); if (term) u.searchParams.set("q", term); else u.searchParams.delete("q"); history.replaceState(null, "", u);
  }
  [q, sort].forEach(function (el) { el.addEventListener("input", render); });
  [cBox, pBox].forEach(function (el) { el.addEventListener("change", render); });
  if (onlySaved) onlySaved.addEventListener("change", render);
  var reset = $("#f-reset"); if (reset) reset.addEventListener("click", function () { q.value = ""; document.querySelectorAll(".filters input").forEach(function (i) { i.checked = false; }); render(); });
  render();
})();
