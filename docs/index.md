# 🛡️ Wiki LEO — Christophe

Bienvenue sur le **Wiki LEO**, documentation complète de l'écosystème **Hermes Agent** et de l'infrastructure personnelle de Christophe (Tofdan).

---

## 🛡️ Hermes Agent

Assistant IA autonome : configuration, crons, dashboards, outils, profils, providers LLM, dépannage.

- [Présentation](hermes/index.md)
- [Architecture système](hermes/architecture.md)
- [Crons & planification](hermes/utilisation/crons.md)
- [Dashboards](hermes/utilisation/dashboards.md)
- [Changelog](hermes/changelog.md)
- [Exemple LEO](hermes/leo-architecture.md)

---

<style>
.portail-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}
.portail-card {
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 1.3rem 1rem;
    text-decoration: none !important;
    color: inherit !important;
    transition: all 0.25s ease;
    background: #f5f6fa;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.portail-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    border-color: #7c4dff;
    background: #f0edff;
}
.portail-card .icon {
    font-size: 2.4rem;
    margin-bottom: 0.5rem;
    line-height: 1;
}
.portail-card .title {
    font-weight: 700;
    font-size: 1.05rem;
    margin-bottom: 0.2rem;
    color: #1a1a2e;
}
.portail-card .desc {
    font-size: 0.8rem;
    color: #666;
    line-height: 1.3;
}
</style>

## 📊 Dashboards

<div class="portail-grid">

<a href="https://christophedanhier-hash.github.io/dashboard-leo/" target="_blank" class="portail-card" rel="noreferrer noopener">
    <div class="icon">🤖</div>
    <div class="title">Dashboard LEO</div>
    <div class="desc">KPI Hermes : sessions, tokens, coûts, balance DeepSeek, Ollama, Gemini</div>
</a>

<a href="https://christophedanhier-hash.github.io/crons-dashboard/" target="_blank" class="portail-card" rel="noreferrer noopener">
    <div class="icon">⏰</div>
    <div class="title">Crons</div>
    <div class="desc">État et historique des 11 crons automatisés</div>
</a>

<a href="https://christophedanhier-hash.github.io/github-dashboard/" target="_blank" class="portail-card" rel="noreferrer noopener">
    <div class="icon">🐙</div>
    <div class="title">GitHub</div>
    <div class="desc">Activité des 17 repos, stats langages, catégories</div>
</a>

<a href="https://christophedanhier-hash.github.io/leo-metrics/" target="_blank" class="portail-card" rel="noreferrer noopener">
    <div class="icon">📈</div>
    <div class="title">Metrics LEO</div>
    <div class="desc">CPU, RAM, disque, uptime 3 machines (LEO, Yoga, Penguin)</div>
</a>

</div>

---

*Documentation vivante — mise à jour hebdomadaire.*
