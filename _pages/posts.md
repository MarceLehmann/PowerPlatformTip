---
layout: single
title: "All Power Platform Tips - Expert Solutions | PowerPlatformTip"
permalink: /posts/
description: "Browse all PowerPlatformTip blog posts with expert solutions for Power Apps, Power Automate, Copilot Studio and Microsoft Power Platform by MVP Marcel Lehmann."
excerpt: "Complete collection of all Power Platform expert posts with step-by-step guides, best practices and practical solutions for enterprise development."
keywords: "Power Platform Blog Posts, Power Apps Tutorials, Power Automate Guides, Copilot Studio Tips, Microsoft MVP Blog, Enterprise Solutions, Development Guides"
author_profile: false
robots: "noindex, follow"  # Nur eine Liste aller Posts, kein eigenständiger Content
sitemap: false  # Nicht in Sitemap aufnehmen
header:
  overlay_color: "#38c9c3"
  overlay_filter: "0.2"
  overlay_image: "/assets/images/hero-bg.jpg"
  cta_label: "Home"
  cta_url: "/"
  cta_class: "btn--primary"
---

# All Power Platform Expert Posts 📝

Discover our complete collection of **PowerPlatformTip** posts. Use the **search box** below to filter by keyword, or pick a **topic** to narrow things down instantly — no page reload needed.

<div class="ppt-filter">
  <input type="text" id="ppt-filter-search" class="ppt-filter__search"
         placeholder="🔍 Type to filter tips by title…" autocomplete="off" aria-label="Filter tips by title">
  <div class="ppt-filter__topics" role="group" aria-label="Filter by topic">
    <button type="button" class="ppt-filter-btn is-active" data-topic="all">All</button>
    <button type="button" class="ppt-filter-btn" data-topic="powerapps">📱 Power Apps</button>
    <button type="button" class="ppt-filter-btn" data-topic="powerautomate">⚙️ Power Automate</button>
    <button type="button" class="ppt-filter-btn" data-topic="sharepoint">🗂️ SharePoint</button>
    <button type="button" class="ppt-filter-btn" data-topic="dataverse">💾 Dataverse</button>
    <button type="button" class="ppt-filter-btn" data-topic="ai">🤖 AI &amp; Copilot</button>
  </div>
  <p class="ppt-filter__count" id="ppt-filter-count"></p>
</div>

<div id="ppt-posts">
{% for post in site.posts %}
  {% assign dtopics = "" %}
  {% for tag in post.tags %}
    {% assign nt = tag | downcase | replace: " ", "" | replace: "-", "" | replace: "_", "" %}
    {% if nt == "powerapps" or nt == "canvasapps" or nt == "modeldrivenapps" or nt == "pcf" or nt == "powerappscomponentframework" %}{% assign dtopics = dtopics | append: " powerapps" %}{% endif %}
    {% if nt == "powerautomate" or nt == "flow" or nt == "cloudflow" or nt == "desktopflow" %}{% assign dtopics = dtopics | append: " powerautomate" %}{% endif %}
    {% if nt == "sharepoint" %}{% assign dtopics = dtopics | append: " sharepoint" %}{% endif %}
    {% if nt == "dataverse" or nt == "dataverseforteams" or nt == "dv4t" or nt == "fetchxml" %}{% assign dtopics = dtopics | append: " dataverse" %}{% endif %}
    {% if nt == "ai" or nt == "aibuilder" or nt == "aiocr" or nt == "copilot" or nt == "copilotstudio" or nt == "powervirtualagents" or nt == "azuredocumentintelligence" or nt == "documentprocessing" %}{% assign dtopics = dtopics | append: " ai" %}{% endif %}
  {% endfor %}
  <div class="ppt-post-item" data-title="{{ post.title | markdownify | strip_html | strip_newlines | downcase | escape }}" data-topics="{{ dtopics | strip }}">
    {% include archive-single.html %}
  </div>
{% endfor %}
</div>

<p class="ppt-no-results" id="ppt-no-results">No tips match your filter. Try another keyword or topic.</p>

<script>
(function () {
  var search = document.getElementById('ppt-filter-search');
  var countEl = document.getElementById('ppt-filter-count');
  var noResults = document.getElementById('ppt-no-results');
  var items = Array.prototype.slice.call(document.querySelectorAll('#ppt-posts .ppt-post-item'));
  var buttons = Array.prototype.slice.call(document.querySelectorAll('.ppt-filter-btn'));
  var total = items.length;
  var activeTopic = 'all';

  function apply() {
    var q = (search.value || '').trim().toLowerCase();
    var shown = 0;
    items.forEach(function (item) {
      var title = item.getAttribute('data-title') || '';
      var topics = ' ' + (item.getAttribute('data-topics') || '') + ' ';
      var matchText = q === '' || title.indexOf(q) !== -1;
      var matchTopic = activeTopic === 'all' || topics.indexOf(' ' + activeTopic + ' ') !== -1;
      if (matchText && matchTopic) {
        item.style.display = '';
        shown++;
      } else {
        item.style.display = 'none';
      }
    });
    countEl.textContent = 'Showing ' + shown + ' of ' + total + ' tips';
    noResults.style.display = shown === 0 ? 'block' : 'none';
  }

  search.addEventListener('input', apply);
  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      activeTopic = btn.getAttribute('data-topic');
      apply();
    });
  });

  apply();
})();
</script>
