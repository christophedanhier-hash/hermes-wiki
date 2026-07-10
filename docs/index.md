# 🛡️ Portail LEO

Bienvenue sur le **portail central** de l'écosystème **Hermes Agent** dirigé par **LEO** — votre assistant IA personnel.

<style>
/* ─── Hero ─── */
.hero {
    background: linear-gradient(135deg, #e8eaf6 0%, #f3e5f5 100%);
    border: 1px solid #7c4dff40;
    border-radius: 16px;
    padding: 2rem 2rem 1.5rem;
    text-align: center;
    margin: 1.5rem 0;
}
.hero h2 {
    font-size: 2rem;
    color: #1a237e;
    margin: 0 0 .3rem 0;
}
.hero .sub {
    color: #5c6bc0;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}
.hero .badges {
    display: flex;
    justify-content: center;
    gap: .5rem;
    flex-wrap: wrap;
}
.hero .badge {
    background: #fff;
    border: 1px solid #7c4dff30;
    border-radius: 20px;
    padding: .25rem .8rem;
    font-size: .8rem;
    color: #3949ab;
}

/* ─── Grille de cartes ─── */
.portail-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: .9rem;
    margin: .8rem 0;
}
.portail-card {
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 1.2rem 1rem;
    text-decoration: none !important;
    color: inherit !important;
    transition: all .2s ease;
    background: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0,0,0,.06);
}
.portail-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0,0,0,.1);
    border-color: #7c4dff;
}
.portail-card .icon {
    font-size: 2rem;
    margin-bottom: .4rem;
    line-height: 1;
}
.portail-card .title {
    font-weight: 700;
    font-size: .95rem;
    margin-bottom: .2rem;
    color: #1a237e;
}
.portail-card .desc {
    font-size: .75rem;
    color: #666;
    line-height: 1.3;
}
.portail-card .url {
    font-size: .65rem;
    color: #999;
    margin-top: .3rem;
    word-break: break-all;
}

/* ─── Sections ─── */
.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    margin: 1.8rem 0 .4rem 0;
    padding-bottom: .3rem;
    border-bottom: 2px solid #7c4dff20;
    color: #1a237e;
    display: flex;
    align-items: center;
    gap: .5rem;
}
.section-title .emoji {
    font-size: 1.3rem;
}
</style>

<div class="hero">
<h2>🤖 LEO — Votre Majordome Digital</h2>
<div class="sub">Assistant IA autonome · Planification · Monitoring · Bureaux Virtuels</div>
<div class="badges">
    <span class="badge">✅ Gateway Actif</span>
    <span class="badge">🤖 DeepSeek v4 Flash</span>
    <span class="badge">🏠 Ollama qwen2.5:7b</span>
    <span class="badge">⚡ Gemini fallback</span>
    <span class="badge">📱 Telegram</span>
</div>
</div>

<div class="section-title"><span class="emoji">📚</span>Wikis & Documentation</div>

<div class="portail-grid">

<a href="https://christophedanhier-hash.github.io/hermes-wiki/hermes/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🛡️</div>
    <div class="title">Wiki LEO</div>
    <div class="desc">Documentation Hermes Agent — config, crons, dashboards, architecture, guide complet</div>
    <div class="url">hermes-wiki/hermes</div>
</a>

<a href="https://christophedanhier-hash.github.io/voyages-wiki/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🧭</div>
    <div class="title">Voyages</div>
    <div class="desc">Roadbooks camping-car — Sylvia, itinéraires, cartes Folium, budget</div>
    <div class="url">voyages-wiki</div>
</a>

<a href="https://christophedanhier-hash.github.io/wiki-oca/t600/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🔭</div>
    <div class="title">Wiki OCA — T600</div>
    <div class="desc">Documentation télescope T600 — technique, formation, sources, Bureau Gérard</div>
    <div class="url">wiki-oca/t600</div>
</a>

<a href="https://christophedanhier-hash.github.io/BAVI_LEO/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🏛️</div>
    <div class="title">Wiki BAVI</div>
    <div class="desc">Bureaux Agentiques Virtuels — PRO (Solidaris), OCA (T600), Voyages, Général</div>
    <div class="url">BAVI_LEO/wiki</div>
</a>

<a href="https://christophedanhier-hash.github.io/emile-wiki/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🎓</div>
    <div class="title">Wiki Émile — Mémoire</div>
    <div class="desc">Assistant pédagogique — mémoire de fin d'études en sciences de l'éducation</div>
    <div class="url">emile-wiki</div>
</a>

</div>

<div class="section-title"><span class="emoji">📊</span>Dashboards & Monitoring</div>

<div class="portail-grid">

<a href="http://100.92.102.28:8765/dashboard?token=leo-panel-2026" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🦁</div>
    <div class="title">LEO Dashboard Unifié</div>
    <div class="desc">Budget live, sessions, crons, infra, BAVI — 4 onglets, 1 source de vérité</div>
    <div class="url">100.92.102.28:8765</div>
</a>

</div>

---

> 🕐 **Dernière mise en ligne : 11/07/2026 01:00**  
> *Propulsé par [Hermes Agent](https://hermes-agent.nousresearch.com) · 🦁 LEO*
