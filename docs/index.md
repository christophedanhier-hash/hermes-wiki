# 🛡️ Portail LEO — Écosystème Hermès

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

<a href="https://christophedanhier-hash.github.io/hermes-wiki/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🛡️</div>
    <div class="title">Wiki LEO</div>
    <div class="desc">Documentation Hermes Agent — config, crons, dashboards, architecture, guide complet</div>
    <div class="url">hermes-wiki</div>
</a>

<a href="https://christophedanhier-hash.github.io/BAVI_LEO/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🏛️</div>
    <div class="title">BAVI LEO</div>
    <div class="desc">Bureaux Agentiques Virtuels — PRO (Solidaris) & PRIVÉ (T600, Voyages, Admin)</div>
    <div class="url">BAVI_LEO</div>
</a>

<a href="https://christophedanhier-hash.github.io/wiki-oca/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🔭</div>
    <div class="title">Wiki OCA — T600</div>
    <div class="desc">Projet T600, Bureau Gérard — documentation technique du télescope OCA</div>
    <div class="url">wiki-oca</div>
</a>

<a href="https://christophedanhier-hash.github.io/voyages-wiki/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🧭</div>
    <div class="title">Wiki Voyages</div>
    <div class="desc">Roadbooks camping-car — Italie 09/2026, Scandinavie, Canet</div>
    <div class="url">voyages-wiki</div>
</a>

</div>

<div class="section-title"><span class="emoji">📊</span>Dashboards & Monitoring</div>

<div class="portail-grid">

<a href="https://christophedanhier-hash.github.io/dashboard-leo/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🤖</div>
    <div class="title">Dashboard LEO</div>
    <div class="desc">KPI Hermes — sessions, tokens, coûts DeepSeek, utilisation par source, bots</div>
    <div class="url">dashboard-leo</div>
</a>

<a href="https://christophedanhier-hash.github.io/leo-metrics/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">💻</div>
    <div class="title">Machines</div>
    <div class="desc">CPU, RAM, disque, uptime — 3 machines : LEO, Yoga, Penguin</div>
    <div class="url">leo-metrics</div>
</a>

<a href="https://christophedanhier-hash.github.io/crons-dashboard/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">⏰</div>
    <div class="title">Crons</div>
    <div class="desc">État et historique des crons automatisés — runs, succès, échecs</div>
    <div class="url">crons-dashboard</div>
</a>

<a href="https://christophedanhier-hash.github.io/github-dashboard/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🐙</div>
    <div class="title">GitHub</div>
    <div class="desc">Activité des repos — commits, déploiements, stats par projet</div>
    <div class="url">github-dashboard</div>
</a>

<a href="https://christophedanhier-hash.github.io/bavi-leo-dashboard/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🏛️</div>
    <div class="title">BAVI LEO</div>
    <div class="desc">KPIs Bureaux Virtuels — usage PRO/PRIVÉ, coûts, performances</div>
    <div class="url">bavi-leo-dashboard</div>
</a>

</div>

<div class="section-title"><span class="emoji">🏗️</span>Architecture & Communication</div>

<div class="portail-grid">

<a href="hermes/architecture-communication/" class="portail-card">
    <div class="icon">🏗️</div>
    <div class="title">Agent vs Bots</div>
    <div class="desc">Comprendre l'architecture : LEO (agent Hermes) ≠ bot Telegram. Gateway, profils, isolation</div>
    <div class="url">Architecture détaillée</div>
</a>

<a href="https://christophedanhier-hash.github.io/BAVI_LEO/wiki/prive/bot-voyages/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🧭</div>
    <div class="title">BAVI LEO Voyages Bot</div>
    <div class="desc">Bot autonome — roadbooks camping-car, cartes, coûts, export PDF/DOCX</div>
    <div class="url">@bavi_leo_voyages_bot</div>
</a>

</div>

<div class="section-title"><span class="emoji">🏢</span>Bureaux Virtuels (BAVI LEO)</div>

<div class="portail-grid">

<a href="https://christophedanhier-hash.github.io/BAVI_LEO/wiki/pro/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🏢</div>
    <div class="title">PRO — Solidaris</div>
    <div class="desc">Robert (Conseil IT), Sophie (Finance IT), Assurance Obligatoire</div>
    <div class="url">BAVI_LEO/PRO</div>
</a>

<a href="https://christophedanhier-hash.github.io/BAVI_LEO/wiki/prive/" class="portail-card" target="_blank" rel="noreferrer noopener">
    <div class="icon">🏠</div>
    <div class="title">PRIVÉ — Personnel</div>
    <div class="desc">Gérard (T600), Sylvie (Voyages), LEO Admin (Infrastructure)</div>
    <div class="url">BAVI_LEO/PRIVÉ</div>
</a>

</div>

---

<div class="section-title"><span class="emoji">⚡</span>Accès rapide</div>

| Ressource | Lien |
|-----------|------|
| 🛡️ Guide Hermes Agent | [Présentation](hermes/index.md) |
| 🏗️ Architecture LEO | [État des lieux](hermes/etat-des-lieux.md) |
| ⏰ Crons & planification | [Tâches automatisées](hermes/utilisation/crons.md) |
| 💰 Budget DeepSeek | [Suivi des coûts](./hermes/utilisation/dashboards.md) |
| 🚀 Routage LLM | [DeepSeek → Ollama → Gemini](./hermes/configuration/providers.md) |
| 🔭 T600 OCA | [Wiki OCA](https://christophedanhier-hash.github.io/wiki-oca/) |
| 🧭 Voyages Italie | [Roadbook 09/2026](https://christophedanhier-hash.github.io/voyages-wiki/italie/) |

---

**Propulsé par [Hermes Agent](https://hermes-agent.nousresearch.com)** · Mis à jour en continu par LEO · 🦁
