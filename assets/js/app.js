/* Core.Digital — core site behaviour (no dependencies) */
(function () {
  "use strict";
  var C = window.CD_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  window.CD = { store: store, toast: toast };

  /* ---------- Theme ---------- */
  var root = document.documentElement;
  var saved = store.get("cd-theme", null);
  if (saved) root.setAttribute("data-theme", saved);
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next); store.set("cd-theme", next);
    });
  });

  /* ---------- Mobile nav ---------- */
  var mb = $("[data-menu]"), mn = $("#mobile-nav");
  if (mb && mn) mb.addEventListener("click", function () {
    var open = mn.classList.toggle("open"); mb.setAttribute("aria-expanded", open);
  });

  /* ---------- Toast ---------- */
  function toast(msg) {
    var t = $("#toast"); if (!t) return;
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); }, 2600);
  }

  /* ---------- Hidden inbox ---------- */
  function inbox() { try { return atob(C._m[0]) + "@" + atob(C._m[1]); } catch (e) { return ""; } }
  function endpoint() { return "https://formsubmit.co/ajax/" + (C.formAlias || inbox()); }
  // "Email us" links: address is assembled only at click time, never rendered.
  $$("[data-mail]").forEach(function (a) {
    a.setAttribute("href", "contact.html");
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-mail") || "Core.Digital inquiry";
      window.location.href = "mai" + "lto:" + inbox() + "?subject=" + encodeURIComponent(subj);
    });
  });

  /* ---------- Forms (FormSubmit AJAX) ---------- */
  $$("form[data-form]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var hp = f.querySelector("[name=_honey]");
      if (hp && hp.value) return; // bot
      if (!f.checkValidity()) { f.reportValidity(); return; }
      var status = f.querySelector(".form-status") || f.parentNode.querySelector(".form-status");
      var btn = f.querySelector("[type=submit]");
      var data = {};
      new FormData(f).forEach(function (v, k) {
        if (k === "_honey") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      data._subject = "[Core.Digital] " + f.getAttribute("data-form");
      data._template = "table";
      data._captcha = "false";
      data["Page"] = location.href;
      if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
      fetch(endpoint(), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j.success) === "false") throw new Error(res.j.message || "Failed");
          var msg = f.getAttribute("data-success") || "Thank you — we received your message and will reply within 1–2 business days.";
          if (status) { status.className = "form-status ok"; status.textContent = msg; }
          f.reset(); toast("Sent ✓");
          if (window.gtag) gtag("event", "generate_lead", { form: f.getAttribute("data-form") });
          var nxt = f.getAttribute("data-next");
          if (nxt) setTimeout(function () { location.href = nxt; }, 900);
          if (f.closest(".wizard")) f.dispatchEvent(new CustomEvent("cd:sent"));
        })
        .catch(function () {
          if (status) { status.className = "form-status err"; status.textContent = "Something went wrong. Please try again in a minute, or use the contact page."; }
        })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn._t; } });
    });
  });

  /* ---------- Prefill fields from URL (?service=seo&budget=...) ---------- */
  var qs = new URLSearchParams(location.search);
  qs.forEach(function (v, k) {
    $$('[name="' + k + '"]').forEach(function (el) {
      if (el.type === "radio" || el.type === "checkbox") { if (el.value === v) el.checked = true; }
      else if (el.tagName !== "BUTTON") el.value = v;
    });
  });

  /* ---------- Multi-step wizard ---------- */
  $$(".wizard").forEach(function (w) {
    var steps = $$(".step", w), i = 0, bar = $(".progress span", w), lbl = $(".step-label", w);
    var prev = $("[data-prev]", w), next = $("[data-next-step]", w), submit = $("[data-submit]", w);
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("active", k === n); });
      if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%";
      if (lbl) lbl.textContent = "Step " + (n + 1) + " of " + steps.length + " · " + (steps[n].getAttribute("data-title") || "");
      if (prev) prev.style.visibility = n === 0 ? "hidden" : "visible";
      if (next) next.style.display = n === steps.length - 1 ? "none" : "";
      if (submit) submit.style.display = n === steps.length - 1 ? "" : "none";
    }
    function valid() {
      var ok = true;
      $$("input,select,textarea", steps[i]).forEach(function (el) {
        if (ok && !el.checkValidity()) { el.reportValidity(); ok = false; }
      });
      return ok;
    }
    if (next) next.addEventListener("click", function () { if (valid() && i < steps.length - 1) { i++; show(i); w.scrollIntoView({ behavior: "smooth", block: "start" }); } });
    if (prev) prev.addEventListener("click", function () { if (i > 0) { i--; show(i); } });
    // auto-advance on single-choice cards
    $$(".step[data-auto] input[type=radio]", w).forEach(function (r) {
      r.addEventListener("change", function () { setTimeout(function () { if (i < steps.length - 1) { i++; show(i); } }, 220); });
    });
    var form = $("form", w);
    if (form) form.addEventListener("cd:sent", function () { i = 0; show(0); });
    show(0);
  });

  /* ---------- Ads: AdSense if configured, otherwise house ads ---------- */
  var adsLoaded = false;
  function loadAdsense() {
    if (adsLoaded || !C.adsenseClient) return; adsLoaded = true;
    var s = document.createElement("script"); s.async = true; s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
    document.head.appendChild(s);
  }
  var houseAds = [
    ["Reach founders, marketers & builders.", "Sponsor this spot", "advertise.html"],
    ["Launching an AI or SaaS tool? Get listed & featured.", "Submit your tool", "submit.html"],
    ["Need a website, SEO or ads expert? Get matched free.", "Get matched", "get-matched.html"],
    ["Keep Core.Digital free & independent.", "Support us", "support.html"]
  ];
  $$("[data-ad]").forEach(function (slot, n) {
    var key = slot.getAttribute("data-ad"), id = (C.adsenseSlots || {})[key];
    if (C.adsenseClient && id) {
      slot.innerHTML = '<div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient +
        '" data-ad-slot="' + id + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      loadAdsense();
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    } else {
      if (C.adsenseClient) loadAdsense(); // Auto ads
      var h = houseAds[n % houseAds.length];
      slot.innerHTML = '<div class="ad-label">Sponsored</div><div class="house-ad"><p><strong>' + h[0] + '</strong> Your brand here — limited monthly slots.</p><a class="btn btn-sm btn-primary" href="' + h[2] + '">' + h[1] + '</a></div>';
    }
  });

  /* ---------- Cookie consent + GA4 ---------- */
  function loadGA() {
    if (!C.ga4 || window.gtag) return;
    var s = document.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date()); gtag("config", C.ga4, { anonymize_ip: true });
  }
  var consent = store.get("cd-consent", null), ck = $("#cookie");
  if (consent === "all") loadGA();
  else if (consent === null && ck) ck.classList.add("show");
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.getAttribute("data-consent"); store.set("cd-consent", v);
      if (ck) ck.classList.remove("show"); if (v === "all") loadGA();
    });
  });

  /* ---------- Modals ---------- */
  function openModal(id) { var m = document.getElementById(id); if (m) { m.classList.add("show"); var f = m.querySelector("input:not(.hp)"); if (f) f.focus(); } }
  $$("[data-open]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); openModal(b.getAttribute("data-open")); }); });
  $$(".modal").forEach(function (m) {
    m.addEventListener("click", function (e) { if (e.target === m || e.target.closest(".modal-close")) m.classList.remove("show"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") $$(".modal.show").forEach(function (m) { m.classList.remove("show"); });
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      var s = $("#q") || $("#hero-q"); if (s) { e.preventDefault(); s.focus(); } else { location.href = "directory.html"; }
    }
  });
  // Exit-intent lead magnet (desktop, once per 7 days)
  var lm = $("#leadmagnet");
  if (lm && window.matchMedia("(pointer:fine)").matches) {
    var last = store.get("cd-lm", 0);
    if (Date.now() - last > 7 * 864e5) {
      var armed = false; setTimeout(function () { armed = true; }, 8000);
      document.addEventListener("mouseout", function h(e) {
        if (armed && !e.relatedTarget && e.clientY < 10) { openModal("leadmagnet"); store.set("cd-lm", Date.now()); document.removeEventListener("mouseout", h); }
      });
    }
  }

  /* ---------- Video facades (no YouTube JS until click) ---------- */
  $$(".video[data-yt]").forEach(function (v) {
    function play() {
      var id = v.getAttribute("data-yt");
      v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.getAttribute("aria-label") || "Video") +
        '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
    }
    v.addEventListener("click", play);
    v.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); } });
  });
  if (C.youtubeChannel) $$("[data-yt-channel]").forEach(function (a) { a.href = C.youtubeChannel; a.hidden = false; });

  /* ---------- Donation / checkout buttons ---------- */
  $$("[data-pay]").forEach(function (a) {
    var key = a.getAttribute("data-pay"), grp = a.getAttribute("data-group") || "donate";
    var url = (C[grp] || {})[key];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; }
    else if (a.hasAttribute("data-hide-empty")) a.hidden = true;
  });

  /* ---------- Countdown ---------- */
  $$("[data-countdown]").forEach(function (el) {
    var end = new Date(el.getAttribute("data-countdown") || C.contestDeadline).getTime();
    function tick() {
      var d = Math.max(0, end - Date.now()), u = [864e5, 36e5, 6e4, 1e3], out = [];
      u.forEach(function (x) { out.push(Math.floor(d / x)); d %= x; });
      el.innerHTML = ["Days", "Hours", "Min", "Sec"].map(function (l, k) { return "<div><b>" + out[k] + "</b><small>" + l + "</small></div>"; }).join("");
    }
    tick(); setInterval(tick, 1000);
  });

  /* ---------- Reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { rootMargin: "0px 0px -60px" });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else $$(".reveal").forEach(function (el) { el.classList.add("in"); });

  /* ---------- Share buttons ---------- */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var u = location.href, t = document.title, k = b.getAttribute("data-share");
      if (k === "native" && navigator.share) return navigator.share({ title: t, url: u });
      if (k === "copy" || k === "native") { (navigator.clipboard ? navigator.clipboard.writeText(u) : Promise.reject()).then(function () { toast("Link copied"); }, function () { prompt("Copy link:", u); }); return; }
      var map = { x: "https://twitter.com/intent/tweet?text=" + encodeURIComponent(t) + "&url=", linkedin: "https://www.linkedin.com/sharing/share-offsite/?url=", facebook: "https://www.facebook.com/sharer/sharer.php?u=", whatsapp: "https://wa.me/?text=" };
      window.open(map[k] + encodeURIComponent(u), "_blank", "noopener,width=640,height=560");
    });
  });

  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
