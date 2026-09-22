/* Core.Digital — free tools (all client-side) */
(function () {
  "use strict";
  var $ = function (s) { return document.querySelector(s); };
  var num = function (id) { var v = parseFloat(($(id) || {}).value); return isNaN(v) ? 0 : v; };
  var usd = function (n) { return "$" + Math.round(n).toLocaleString("en-US"); };
  var on = function (id, fn) { var f = $(id); if (!f) return; f.addEventListener("input", fn); f.addEventListener("change", fn); fn(); };

  /* 1. Website cost estimator */
  on("#calc-cost", function () {
    var base = { landing: [500, 2500], business: [2000, 8000], content: [3000, 12000], store: [5000, 25000], app: [15000, 80000] }[$("#cc-type").value];
    var pages = num("#cc-pages"), lo = base[0], hi = base[1];
    if (pages > 5) { lo += (pages - 5) * 150; hi += (pages - 5) * 400; }
    document.querySelectorAll("#calc-cost [data-add]:checked").forEach(function (c) { var r = c.getAttribute("data-add").split("-"); lo += +r[0]; hi += +r[1]; });
    var m = { freelancer: .65, studio: 1, agency: 1.5 }[$("#cc-who").value]; lo *= m; hi *= m;
    $("#cc-out").innerHTML = "<small>Indicative build range</small><b>" + usd(lo) + " – " + usd(hi) + "</b><small>Ongoing (hosting, maintenance, content): ~" + usd(lo * .15 / 12) + "–" + usd(hi * .2 / 12) + "/month</small>";
    var b = hi < 2500 ? "under-2.5k" : hi < 10000 ? "2.5k-10k" : hi < 25000 ? "10k-25k" : hi < 50000 ? "25k-50k" : "50k-plus";
    $("#cc-cta").href = "get-matched.html?service=website&budget=" + b;
  });

  /* 2. Ad ROI / ROAS */
  on("#calc-roas", function () {
    var spend = num("#r-spend"), cpc = num("#r-cpc"), cr = num("#r-cr") / 100, aov = num("#r-aov"), margin = num("#r-margin") / 100;
    var clicks = cpc ? spend / cpc : 0, conv = clicks * cr, rev = conv * aov, roas = spend ? rev / spend : 0, profit = rev * margin - spend, cpa = conv ? spend / conv : 0;
    var be = margin ? 1 / margin : 0;
    $("#r-out").innerHTML = '<div class="grid g2"><div><small>Clicks</small><b>' + Math.round(clicks).toLocaleString() + '</b></div><div><small>Conversions</small><b>' + conv.toFixed(1) + '</b></div>' +
      '<div><small>Revenue</small><b>' + usd(rev) + '</b></div><div><small>ROAS</small><b style="color:' + (roas >= be ? "var(--ok)" : "var(--accent)") + '">' + roas.toFixed(2) + 'x</b></div>' +
      '<div><small>Cost per acquisition</small><b>' + usd(cpa) + '</b></div><div><small>Profit after ad spend</small><b>' + usd(profit) + '</b></div></div>' +
      '<p class="form-note">Break-even ROAS at ' + Math.round(margin * 100) + '% margin: ' + be.toFixed(2) + 'x.</p>';
  });

  /* 3. SERP preview */
  on("#calc-serp", function () {
    var t = $("#s-title").value, d = $("#s-desc").value, u = $("#s-url").value || "https://example.com/page";
    $("#s-prev").innerHTML = '<div class="u">' + u.replace(/[<>]/g, "") + '</div><div class="t">' + (t || "Your page title").replace(/[<>]/g, "").slice(0, 70) + (t.length > 70 ? "…" : "") + '</div><div class="d">' + (d || "Your meta description appears here.").replace(/[<>]/g, "").slice(0, 160) + (d.length > 160 ? "…" : "") + "</div>";
    var tm = $("#s-tm"), dm = $("#s-dm");
    tm.textContent = t.length + " characters " + (t.length >= 30 && t.length <= 60 ? "✓ good length" : "· aim for 30–60");
    tm.className = "meter " + (t.length >= 30 && t.length <= 60 ? "good" : "bad");
    dm.textContent = d.length + " characters " + (d.length >= 70 && d.length <= 155 ? "✓ good length" : "· aim for 70–155");
    dm.className = "meter " + (d.length >= 70 && d.length <= 155 ? "good" : "bad");
  });

  /* 4. UTM builder */
  on("#calc-utm", function () {
    var base = $("#u-url").value.trim(), out = $("#u-out");
    try {
      var x = new URL(base || "https://example.com");
      ["source", "medium", "campaign", "term", "content"].forEach(function (k) { var v = $("#u-" + k).value.trim(); if (v) x.searchParams.set("utm_" + k, v.toLowerCase().replace(/\s+/g, "-")); });
      out.value = x.toString();
    } catch (e) { out.value = "Enter a full URL starting with https://"; }
  });
  var cp = $("#u-copy"); if (cp) cp.addEventListener("click", function () { var o = $("#u-out"); o.select(); try { navigator.clipboard.writeText(o.value); } catch (e) { document.execCommand("copy"); } if (window.CD) CD.toast("UTM link copied"); });

  /* 5. AI API cost estimator */
  on("#calc-ai", function () {
    var inT = num("#a-in"), outT = num("#a-out"), req = num("#a-req"), pin = num("#a-pin"), pout = num("#a-pout");
    var perReq = inT / 1e6 * pin + outT / 1e6 * pout, month = perReq * req * 30;
    $("#a-res").innerHTML = "<small>Per request</small><b>$" + perReq.toFixed(4) + "</b><small>Per month (" + (req * 30).toLocaleString() + " requests)</small><b>" + usd(month) + "</b><small>Per year: " + usd(month * 12) + "</small>";
  });
})();
