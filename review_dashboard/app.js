/* Daily Krishna Stories — editorial review dashboard */
'use strict';

const state = { stories: [], factChecks: {}, selection: {}, review: {}, arcs: [] };
let filters = { status: '', stage: '', arc: '', source: '', theme: '' };
let current = null;

const $ = (sel) => document.querySelector(sel);
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

async function load() {
  const res = await fetch('/api/data');
  const data = await res.json();
  state.stories = data.stories || [];
  state.factChecks = data.fact_checks || {};
  state.selection = data.selection || {};
  state.review = data.review || {};
  state.arcs = data.arcs || [];
  buildFilterOptions();
  render();
}

function buildFilterOptions() {
  const set = (id, values, label) => {
    const el = $(id);
    el.innerHTML = `<option value="">${label}</option>` +
      [...new Set(values)].sort().map((v) => `<option value="${esc(v)}">${esc(v)}</option>`).join('');
  };
  set('#f-status', ['unreviewed', 'approved', 'needs_revision', 'rejected'], 'All statuses');
  set('#f-stage', state.stories.map((s) => s.life_stage), 'All life stages');
  set('#f-arc', state.stories.map((s) => s.story_arc), 'All arcs');
  set('#f-source', state.stories.map((s) => s.sources?.[0]?.work).filter(Boolean), 'All sources');
  set('#f-theme', state.stories.flatMap((s) => s.themes || []), 'All themes');
}

const STATUS_LABEL = { unreviewed: 'Unreviewed', approved: 'Approved', needs_revision: 'Needs Revision', rejected: 'Rejected' };

function statusOf(id) { return state.review[id]?.status || 'unreviewed'; }

function render() {
  renderProgress();
  renderTable();
}

function renderProgress() {
  const counts = { unreviewed: 0, approved: 0, needs_revision: 0, rejected: 0 };
  state.stories.forEach((s) => { counts[statusOf(s.id)] += 1; });
  $('#progress').innerHTML =
    `<span><b>${state.stories.length}</b> Pilot Stories</span>` +
    `<span><span class="num">${counts.unreviewed}</span> Unreviewed</span>` +
    `<span><span class="num">${counts.approved}</span> Approved</span>` +
    `<span><span class="num">${counts.needs_revision}</span> Needs Revision</span>` +
    `<span><span class="num">${counts.rejected}</span> Rejected</span>`;
}

function filtered() {
  const q = ($('#search').value || '').toLowerCase().trim();
  return state.stories.filter((s) => {
    if (filters.status && statusOf(s.id) !== filters.status) return false;
    if (filters.stage && s.life_stage !== filters.stage) return false;
    if (filters.arc && s.story_arc !== filters.arc) return false;
    if (filters.source && s.sources?.[0]?.work !== filters.source) return false;
    if (filters.theme && !(s.themes || []).includes(filters.theme)) return false;
    if (q) {
      const hay = `${s.id} ${s.title} ${(s.characters || []).join(' ')} ${s.subtitle || ''}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  }).sort((a, b) => a.id.localeCompare(b.id));
}

function renderTable() {
  const rows = filtered().map((s) => {
    const st = statusOf(s.id);
    const fc = state.factChecks[s.id];
    const fid = fc ? fc.source_fidelity_score : '—';
    const src = s.sources?.[0]?.work || '—';
    const ref = s.sources?.[0]?.reference || '';
    return `<tr data-id="${esc(s.id)}">
      <td class="id">${esc(s.id)}</td>
      <td class="title">${esc(s.title)}</td>
      <td>${esc(s.life_stage)}</td>
      <td>${esc(s.story_arc)}</td>
      <td>${esc(src)} ${esc(ref)}</td>
      <td>${s.estimated_read_minutes ?? '—'}′</td>
      <td>${fid === '—' ? '—' : esc(String(fid))}</td>
      <td><span class="pill ${st}">${STATUS_LABEL[st]}</span></td>
    </tr>`;
  }).join('');
  $('#story-table tbody').innerHTML = rows || `<tr><td colspan="8" style="color:var(--muted)">No stories match.</td></tr>`;
  document.querySelectorAll('#story-table tbody tr[data-id]').forEach((tr) => {
    tr.addEventListener('click', () => openReader(tr.dataset.id));
  });
}

function openReader(id) {
  const s = state.stories.find((x) => x.id === id);
  if (!s) return;
  current = s;
  $('#list-view').classList.add('hidden');
  $('#reader-view').classList.remove('hidden');
  window.scrollTo(0, 0);

  $('#r-title').textContent = s.title;
  $('#r-subtitle').textContent = s.subtitle || '';
  $('#r-story').innerHTML = (s.story || '').split(/\n{2,}/).map((p) => `<p>${esc(p)}</p>`).join('');
  $('#r-reflection').innerHTML = s.reflection ? `<b>Reflection</b>${esc(s.reflection)}` : '';

  const srcs = (s.sources || []).map((x) => `${x.work} ${x.reference}${x.role === 'primary' ? '' : ' (also)'}`).join(' · ');
  $('#r-sources').innerHTML = `<b>Source</b> ${esc(srcs) || '—'}`;
  $('#r-tradition').innerHTML = s.tradition_note ? `<b>Tradition note</b> ${esc(s.tradition_note)}` : '';
  $('#r-next').innerHTML = s.next_story_tease
    ? `<b>Continue Krishna's Story →</b> ${esc(s.next_story_tease)}${s.next_story_id ? ` <a href="#" data-next="${esc(s.next_story_id)}">(${esc(s.next_story_id)})</a>` : ''}`
    : '';

  $('#reader-meta').innerHTML =
    `<span>${esc(s.life_stage)}</span><span>${esc(s.story_arc)}</span>` +
    `<span>${s.estimated_read_minutes ?? '—'} min read · ${s.estimated_audio_minutes ?? '—'} min audio</span>` +
    (s.content_note ? `<span class="pill needs_revision">content note</span>` : '');

  const fc = state.factChecks[id];
  $('#evidence-body').innerHTML = evidenceHtml(s, fc);
  const panel = $('#evidence-panel');
  panel.removeAttribute('open');

  renderReviewControls();
}

function evidenceHtml(s, fc) {
  const sel = (state.selection.stories || []).find((x) => x.id === s.id);
  let html = '';
  if (sel) html += `<h4>Why selected</h4><p>${esc(sel.reason)}</p>`;
  html += `<h4>Canonical event</h4><p>${esc(s.generation_metadata?.source_event_id || '—')}</p>`;
  html += `<h4>Exact references</h4><p>${(s.sources || []).map((x) => esc(`${x.work} ${x.reference} (${x.role})`)).join('<br>')}</p>`;
  if (s.tradition_note) html += `<h4>Tradition note</h4><p>${esc(s.tradition_note)}</p>`;
  if (s.variant_notes) html += `<h4>Variant notes (corpus)</h4><p>${esc(s.variant_notes)}</p>`;
  if (fc) {
    html += `<h4>Fact check</h4><p>${fc.statements.map((st) =>
      `<div class="fc fc-${st.verdict === 'SUPPORTED' ? 'ok' : (st.verdict === 'REASONABLE_CONNECTIVE_NARRATION' ? 'ok' : 'warn')}">${esc(st.verdict)} — ${esc(st.claim)}</div>`).join('')}</p>`;
    html += `<p><b>Source fidelity score: ${fc.source_fidelity_score}/5</b></p>`;
    if (fc.notes) html += `<p>${esc(fc.notes)}</p>`;
  } else {
    html += `<p class="fc fc-warn">No fact check yet.</p>`;
  }
  return html;
}

function renderReviewControls() {
  if (!current) return;
  const st = statusOf(current.id);
  document.querySelectorAll('.status-buttons button[data-status]').forEach((b) => {
    b.classList.toggle('active', b.dataset.status === st);
  });
  const comments = state.review[current.id]?.comments || [];
  $('#comments').innerHTML = comments.map((c) =>
    `<div class="comment"><span class="ts">${esc(c.ts)}</span><br>${esc(c.text)}</div>`).join('') ||
    '<div style="color:#a99f93">No comments yet.</div>';
  $('#comment').value = '';
}

async function saveReview(body) {
  const res = await fetch('/api/review', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const rec = await res.json();
  state.review[current.id] = rec;
  renderProgress();
  renderTable();
  renderReviewControls();
}

/* events */
$('#search').addEventListener('input', renderTable);
['#f-status', '#f-stage', '#f-arc', '#f-source', '#f-theme'].forEach((sel) => {
  $(sel).addEventListener('change', (e) => {
    filters[sel.slice(2)] = e.target.value;
    renderTable();
  });
});
$('#f-clear').addEventListener('click', () => {
  filters = { status: '', stage: '', arc: '', source: '', theme: '' };
  ['#f-status', '#f-stage', '#f-arc', '#f-source', '#f-theme'].forEach((s) => { $(s).value = ''; });
  $('#search').value = '';
  renderTable();
});
$('#back').addEventListener('click', () => {
  $('#reader-view').classList.add('hidden');
  $('#list-view').classList.remove('hidden');
  current = null;
});
document.querySelectorAll('.status-buttons button[data-status]').forEach((b) => {
  b.addEventListener('click', () => saveReview({ story_id: current.id, status: b.dataset.status }));
});
$('#comment-send').addEventListener('click', () => {
  const text = $('#comment').value.trim();
  if (!text) return;
  saveReview({ story_id: current.id, comment: text });
});
document.addEventListener('click', (e) => {
  const a = e.target.closest('a[data-next]');
  if (a) { e.preventDefault(); openReader(a.dataset.next); }
});

load();
