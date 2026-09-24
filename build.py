# -*- coding: utf-8 -*-
"""Builds the restructured INNO-SCREW site into /home/claude/site."""
import os

OUT = "../"  # writes into the repository root

NAV = [
    ("index.html", "Startseite", "Home"),
    ("project.html", "Projekt", "Project"),
    ("infrastructure.html", "Infrastruktur", "Infrastructure"),
    ("data.html", "Forschungsdaten", "Research Data"),
    ("publications.html", "Publikationen", "Publications"),
    ("news.html", "Aktuelles", "News"),
    ("contact.html", "Kontakt", "Contact"),
]


def nav_html():
    items = []
    for href, de, en in NAV:
        items.append(
            '    <li><a href="%s" data-de="%s" data-en="%s">%s</a></li>' % (href, de, en, de)
        )
    return "\n".join(items)


HEAD = """<!DOCTYPE html>
<html lang="de" data-theme="light">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#x1F529;</text></svg>"/>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<nav>
<div class="nw">
  <a href="index.html" class="logo" style="padding:2px 0;display:flex;align-items:center">
    <img src="assets/logo.png" alt="INNO-SCREW" style="height:38px;width:auto;display:block">
  </a>
  <ul class="nl" id="nl">
{nav}
  </ul>
  <div class="nc">
    <button class="blng" id="blng" title="Switch language" aria-label="Switch language">EN</button>
    <button class="bthm" id="bthm" title="Toggle dark mode" aria-label="Toggle dark mode"></button>
    <button class="ham" id="ham" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</div>
</nav>
"""

FUNDING = """
<div class="sec" id="foerderhinweis" style="background:var(--bg2);border-top:1px solid var(--bd);padding:2rem">
<div class="wrap" style="max-width:960px;display:flex;flex-wrap:wrap;gap:2rem;align-items:center">
  <img src="assets/bmwe.jpg" alt="Bundesministerium f&uuml;r Wirtschaft und Energie" style="height:78px;width:auto;object-fit:contain;flex-shrink:0">
  <div style="flex:1;min-width:240px">
    <div style="font-family:'JetBrains Mono',monospace;font-size:.62rem;color:var(--gd2);letter-spacing:.1em;margin-bottom:.5rem" data-de="F&ouml;rderhinweis" data-en="Funding notice">F&ouml;rderhinweis</div>
    <p class="de-block" style="font-size:.84rem;color:var(--mu);line-height:1.75;margin:0">Das Vorhaben <strong style="color:var(--tk)">INNO-SCREW</strong> wird im Rahmen des F&ouml;rderprogramms <em>Innovationskompetenz INNO-KOM</em> durch das <strong style="color:var(--tk)">Bundesministerium f&uuml;r Wirtschaft und Energie (BMWE)</strong> gef&ouml;rdert. Die Verantwortung f&uuml;r den Inhalt liegt bei den Autorinnen und Autoren.</p>
    <p class="en-block" style="font-size:.84rem;color:var(--mu);line-height:1.75;margin:0;display:none">The <strong style="color:var(--tk)">INNO-SCREW</strong> project is funded under the <em>Innovation Competence INNO-KOM</em> programme of the <strong style="color:var(--tk)">Federal Ministry for Economic Affairs and Energy (BMWE)</strong>. The authors bear sole responsibility for the content.</p>
  </div>
</div></div>
"""

FOOTER = """<footer>
<div class="fin">
  <strong>INNO-SCREW</strong> &mdash; <span class="de-block">Innovationszentrum f&uuml;r intelligentes Qualit&auml;tsmanagement in industriellen Schraubprozessen</span><span class="en-block" style="display:none">Innovation Centre for Intelligent Quality Management in Industrial Screw Fastening Processes</span>
  <div style="margin-top:.5rem;font-size:.83rem;color:rgba(255,255,255,.65)">
    RIF Institut f&uuml;r Forschung und Transfer e.V. &middot; Institut f&uuml;r Produktionssysteme, TU Dortmund
  </div>
  <div style="margin-top:.85rem;display:flex;gap:1.3rem;justify-content:center;flex-wrap:wrap">
    <a href="contact.html#impressum" data-de="Impressum" data-en="Legal Notice">Impressum</a>
    <a href="contact.html#datenschutz" data-de="Datenschutz" data-en="Privacy">Datenschutz</a>
    <a href="mailto:inno-screw@rif-ev.de">inno-screw@rif-ev.de</a>
    <a href="https://ips.mb.tu-dortmund.de/en/research-consult/research-projects/" target="_blank" rel="noopener">IPS TU Dortmund</a>
  </div>
  <div class="fcpy">Copyright &copy; RIF e.V. &amp; IPS TU Dortmund 2025 &ndash; 2027 &middot; INNO-KOM / BMWE</div>
</div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
"""


def page(filename, title, desc, body, funding=True):
    html = HEAD.format(title=title, desc=desc, nav=nav_html())
    html += body
    if funding:
        html += FUNDING
    html += FOOTER
    with open(OUT + filename, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", filename, len(html))


def phdr(h1_de, h1_en, p_de, p_en):
    return """<div class="phdr">
  <h1 data-de="%s" data-en="%s">%s</h1>
  <p data-de="%s" data-en="%s">%s</p>
</div>
""" % (h1_de, h1_en, h1_de, p_de, p_en, p_de)


# --------------------------------------------------------------------------
# Shared blocks
# --------------------------------------------------------------------------

PROJECT_STATUS = """
<div class="sec sec-a" id="status"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Projektstatus" data-en="Project status">Projektstatus</div>
    <h2 data-de="Stand des Vorhabens" data-en="Current state of the project">Stand des Vorhabens</h2>
    <div class="sr"></div>
  </div>
  <div class="status">
    <div class="status-grid">
      <div class="status-cell">
        <div class="status-k" data-de="Projektlaufzeit" data-en="Project duration">Projektlaufzeit</div>
        <div class="status-v"><span class="de-block">Dez 2024 &ndash; Mai 2027</span><span class="en-block" style="display:none">Dec 2024 &ndash; May 2027</span></div>
      </div>
      <div class="status-cell">
        <div class="status-k" data-de="Aktuelle Projektphase" data-en="Current research phase">Aktuelle Projektphase</div>
        <div class="status-v"><span class="de-block">Datenanalyse &amp; offene Forschungsdaten</span><span class="en-block" style="display:none">Data analysis &amp; open research data</span></div>
      </div>
      <div class="status-cell">
        <div class="status-k" data-de="Experimentelle Infrastruktur" data-en="Experimental infrastructure">Experimentelle Infrastruktur</div>
        <div class="status-v"><span class="num">5</span><span class="de-block">Schraubsysteme</span><span class="en-block" style="display:none">screwdriving systems</span></div>
      </div>
      <div class="status-cell">
        <div class="status-k" data-de="Aufgezeichnete Prozessdaten" data-en="Recorded process data">Aufgezeichnete Prozessdaten</div>
        <div class="status-v"><span class="num de-block">34.082</span><span class="num en-block" style="display:none">34,082</span><span class="de-block">Schraubvorg&auml;nge</span><span class="en-block" style="display:none">process recordings</span></div>
      </div>
      <div class="status-cell">
        <div class="status-k" data-de="Offene Datens&auml;tze" data-en="Open datasets">Offene Datens&auml;tze</div>
        <div class="status-v"><span class="num">6</span><span class="de-block">ver&ouml;ffentlichte Szenarien</span><span class="en-block" style="display:none">published scenarios</span></div>
      </div>
      <div class="status-cell">
        <div class="status-k" data-de="Publikationen" data-en="Publications">Publikationen</div>
        <div class="status-v"><span class="num">5</span><span class="de-block">Vorarbeiten &middot; INNO-SCREW in Vorbereitung</span><span class="en-block" style="display:none">related research &middot; INNO-SCREW in preparation</span></div>
      </div>
      <div class="status-cell">
        <div class="status-k" data-de="Letzte Aktualisierung" data-en="Last update">Letzte Aktualisierung</div>
        <div class="status-v"><span class="de-block">September 2026</span><span class="en-block" style="display:none">September 2026</span></div>
      </div>
      <div class="status-cell">
        <div class="status-k" data-de="F&ouml;rderung" data-en="Funding">F&ouml;rderung</div>
        <div class="status-v">BMWE &middot; INNO-KOM</div>
      </div>
    </div>
    <div class="status-focus">
      <h4 data-de="Aktueller Forschungsschwerpunkt" data-en="Current research focus">Aktueller Forschungsschwerpunkt</h4>
      <p class="de-block">Analyse von Schraubprozessdaten, Anomalieerkennung, &Uuml;bertragbarkeit zwischen
      Schraubsystemen sowie Vorbereitung offener Forschungsdatens&auml;tze.</p>
      <p class="en-block" style="display:none">Analysis of screwdriving process data, anomaly detection,
      transferability across screwdriving systems and preparation of open research datasets.</p>
    </div>
  </div>
</div></div>
"""

ID_SCHEME = """
  <div class="idkey">
    <div>
      <code>ASS, RSS, MSS, DSS, KSS</code>
      <span class="de-block">Kennungen der f&uuml;nf physischen Schraubsysteme der Forschungsinfrastruktur.</span>
      <span class="en-block" style="display:none">Identifiers of the five physical screwdriving systems in the research infrastructure.</span>
    </div>
    <div>
      <code>S01 &hellip; S06</code>
      <span class="de-block">Experimentelle Szenarien &mdash; jeweils eine definierte Versuchsreihe mit eigenem Fehlerbild.</span>
      <span class="en-block" style="display:none">Experimental scenarios &mdash; each a defined series of trials with its own set of process deviations.</span>
    </div>
    <div>
      <code>DS-2025-01, DS-2026-01 &hellip;</code>
      <span class="de-block">Datens&auml;tze bzw. Messkampagnen mit eigener Version, Lizenz und DOI.</span>
      <span class="en-block" style="display:none">Datasets and measurement campaigns, each with its own version, licence and DOI.</span>
    </div>
  </div>
"""

# --------------------------------------------------------------------------
# HOME
# --------------------------------------------------------------------------

home = """
<div class="hero">
  <div class="hbg"></div><div class="hgl"></div>
  <div class="hi">
    <div class="hk">Forschungsprojekt &middot; RIF Institut &middot; TU Dortmund</div>
    <h1>INNO-SCREW</h1>
    <h2 data-de="Innovationszentrum f&uuml;r intelligentes Qualit&auml;tsmanagement in industriellen Schraubprozessen"
        data-en="Innovation Centre for Intelligent Quality Management in Industrial Screw Fastening Processes">
      Innovationszentrum f&uuml;r intelligentes Qualit&auml;tsmanagement in industriellen Schraubprozessen
    </h2>
    <p class="hlead de-block">
      INNO-SCREW baut ein Innovationszentrum f&uuml;r das Qualit&auml;tsmanagement industrieller
      Schraubprozesse auf. Untersucht wird, wie sich fehlerhafte Schraubverbindungen mit
      maschinellen Lernverfahren aus Drehmoment- und Winkeldaten erkennen lassen. Die dabei
      entstehenden Messdaten werden als offene Forschungsdaten bereitgestellt.
    </p>
    <p class="hlead en-block" style="display:none">
      INNO-SCREW is building an innovation centre for quality management in industrial screw
      fastening. The project investigates how faulty connections can be identified from torque
      and angle data using machine-learning methods, and publishes the resulting measurement
      data as open research data.
    </p>
    <div class="hbtns">
      <a href="infrastructure.html" class="btn btn-g" data-de="Forschungsinfrastruktur" data-en="Research infrastructure">Forschungsinfrastruktur</a>
      <a href="data.html" class="btn btn-w" data-de="Forschungsdaten" data-en="Research data">Forschungsdaten</a>
    </div>
    <div class="hst">
      <div><div class="stn">5</div><div class="stl de-block">Schraubsysteme</div><div class="stl en-block" style="display:none">Screwdriving systems</div></div>
      <div><div class="stn de-block">34.082</div><div class="stn en-block" style="display:none">34,082</div><div class="stl de-block">Schraubvorg&auml;nge</div><div class="stl en-block" style="display:none">Process recordings</div></div>
      <div><div class="stn">6</div><div class="stl de-block">Versuchsszenarien</div><div class="stl en-block" style="display:none">Experimental scenarios</div></div>
      <div><div class="stn">BMWE</div><div class="stl de-block">INNO-KOM</div><div class="stl en-block" style="display:none">INNO-KOM</div></div>
    </div>
  </div>
</div>

<div class="strip"><div class="sg">
  <a href="infrastructure.html" class="si" style="text-decoration:none;display:block">
    <span class="sico">&#x1f529;</span>
    <div class="stag">ASS &middot; RSS &middot; MSS &middot; DSS &middot; KSS</div>
    <h3 data-de="F&uuml;nf Schraubsysteme" data-en="Five screwdriving systems">F&uuml;nf Schraubsysteme</h3>
    <p class="de-block">Automatische, roboterbasierte, manuelle, doppelspindlige und kabellose Schraubsysteme mit durchg&auml;ngiger Datenerfassung.</p>
    <p class="en-block" style="display:none">Automatic, robot-based, manual, dual-spindle and cordless screwdriving systems with continuous data acquisition.</p>
  </a>
  <a href="data.html" class="si" style="text-decoration:none;display:block">
    <span class="sico">&#x1f4ca;</span>
    <div class="stag">S01 &hellip; S06</div>
    <h3 data-de="Experimentelle Szenarien" data-en="Experimental scenarios">Experimentelle Szenarien</h3>
    <p class="de-block">Definierte Versuchsreihen zu Gewindesch&auml;digung, Oberfl&auml;chenreibung, Montagebedingungen und Bauteilvarianz.</p>
    <p class="en-block" style="display:none">Defined series of trials covering thread degradation, surface friction, assembly conditions and workpiece variation.</p>
  </a>
  <a href="data.html#datensaetze" class="si" style="text-decoration:none;display:block">
    <span class="sico">&#x1f5c3;&#xfe0f;</span>
    <div class="stag">DS-2025-01 &hellip;</div>
    <h3 data-de="Offene Forschungsdaten" data-en="Open research data">Offene Forschungsdaten</h3>
    <p class="de-block">Zeitreihen aus realen Schraubprozessen mit Metadaten, OK/NOK-Labels, Lizenz und DOI.</p>
    <p class="en-block" style="display:none">Time-series data from real screwdriving processes with metadata, OK/NOK labels, licence and DOI.</p>
  </a>
  <a href="publications.html" class="si" style="text-decoration:none;display:block">
    <span class="sico">&#x1f4d6;</span>
    <div class="stag">PyScrew</div>
    <h3 data-de="Publikationen &amp; Software" data-en="Publications &amp; software">Publikationen &amp; Software</h3>
    <p class="de-block">Peer-reviewed Vorarbeiten zur Anomalieerkennung sowie die Open-Source-Bibliothek PyScrew.</p>
    <p class="en-block" style="display:none">Peer-reviewed preliminary work on anomaly detection and the open-source library PyScrew.</p>
  </a>
</div></div>
""" + PROJECT_STATUS + """
<div class="sec" id="problem"><div class="wrsm">
  <div class="sh">
    <div class="skk" data-de="Problemstellung" data-en="Problem statement">Problemstellung</div>
    <h2 data-de="Herausforderung in der Qualit&auml;tssicherung" data-en="Challenges in quality assurance">Herausforderung in der Qualit&auml;tssicherung</h2>
    <div class="sr"></div>
  </div>
  <div class="prose de-block">
    <p>Schrauben ist eines der wichtigsten F&uuml;geverfahren der industriellen Fertigung. Die derzeit
    eingesetzten Methoden der statistischen Prozess&uuml;berwachung (SPC) sto&szlig;en bei komplexen
    Anwendungsf&auml;llen jedoch an ihre Grenzen.</p>
    <p>Fehlerhafte Schraubprozesse werden dadurch nicht vollst&auml;ndig erkannt und k&ouml;nnen in den Umlauf
    gelangen. Die Folgen sind Demontagema&szlig;nahmen, R&uuml;ckrufaktionen und Gew&auml;hrleistungskosten.</p>
    <p>Die zunehmende Individualisierung in der Produktion verst&auml;rkt diese Problematik, da die Vielfalt
    m&ouml;glicher Fehlerf&auml;lle w&auml;chst.</p>
    <div class="cq"><p>Zugleich fehlen &ouml;ffentlich verf&uuml;gbare Datens&auml;tze mit realen Messdaten, die f&uuml;r die
    Entwicklung und Validierung neuer Qualit&auml;tssicherungsmethoden erforderlich sind.</p></div>
  </div>
  <div class="prose en-block" style="display:none">
    <p>Screw fastening is one of the most important joining processes in industrial manufacturing.
    Current statistical process control (SPC) methods, however, reach their limits in complex
    applications.</p>
    <p>As a result, faulty screwdriving processes are not fully detected and may enter circulation,
    leading to disassembly measures, recalls and warranty costs.</p>
    <p>Increasing individualisation in production intensifies the problem, as the variety of possible
    fault cases grows.</p>
    <div class="cq"><p>At the same time, publicly available datasets with real measurement data &mdash;
    required to develop and validate new quality assurance methods &mdash; are lacking.</p></div>
  </div>
</div></div>

<div class="sec sec-a" id="vorgehen"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Forschungsansatz" data-en="Research approach">Forschungsansatz</div>
    <h2 data-de="Vom Versuchsaufbau zum offenen Datensatz" data-en="From experimental setup to open dataset">Vom Versuchsaufbau zum offenen Datensatz</h2>
    <div class="sr"></div>
    <p class="de-block">Die Projektarbeit gliedert sich in vier aufeinander aufbauende Arbeitsschwerpunkte.</p>
    <p class="en-block" style="display:none">The work is organised in four consecutive areas of activity.</p>
  </div>
  <div class="approach">
    <div class="stage">
      <div class="stage-n">01</div>
      <h4 data-de="Forschungsinfrastruktur" data-en="Research infrastructure">Forschungsinfrastruktur</h4>
      <p class="de-block">Aufbau und Datenanbindung von f&uuml;nf Schraubsystemen mit einheitlicher Messdatenerfassung.</p>
      <p class="en-block" style="display:none">Setting up five screwdriving systems and connecting them to a uniform data acquisition infrastructure.</p>
    </div>
    <div class="stage">
      <div class="stage-n">02</div>
      <h4 data-de="Experimentelle Untersuchungen" data-en="Experimental investigations">Experimentelle Untersuchungen</h4>
      <p class="de-block">Durchf&uuml;hrung definierter Versuchsreihen mit fehlerfreien und gezielt abweichenden Schraubprozessen.</p>
      <p class="en-block" style="display:none">Conducting defined series of trials with fault-free and deliberately deviating screwdriving processes.</p>
    </div>
    <div class="stage">
      <div class="stage-n">03</div>
      <h4 data-de="Datengetriebene Qualit&auml;tssicherung" data-en="Data-driven quality assurance">Datengetriebene Qualit&auml;tssicherung</h4>
      <p class="de-block">Entwicklung und Bewertung von Verfahren zur Anomalieerkennung sowie Pr&uuml;fung der &Uuml;bertragbarkeit zwischen Systemen.</p>
      <p class="en-block" style="display:none">Developing and evaluating anomaly detection methods and examining transferability across systems.</p>
    </div>
    <div class="stage">
      <div class="stage-n">04</div>
      <h4 data-de="Offene Forschung &amp; Transfer" data-en="Open research &amp; transfer">Offene Forschung &amp; Transfer</h4>
      <p class="de-block">Ver&ouml;ffentlichung von Datens&auml;tzen und Software sowie Austausch mit Industrie und Fachgemeinschaft.</p>
      <p class="en-block" style="display:none">Publishing datasets and software and exchanging results with industry and the research community.</p>
    </div>
  </div>
  <div style="text-align:center;margin-top:2.4rem">
    <a href="project.html" class="btn btn-b" data-de="Zum Projekt" data-en="About the project">Zum Projekt</a>
  </div>
</div></div>

<div class="sec" id="news"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Aktuelles" data-en="News">Aktuelles</div>
    <h2 data-de="Neues aus dem Projekt" data-en="Latest from the project">Neues aus dem Projekt</h2>
    <div class="sr"></div>
  </div>
  <div class="ng">
    <a href="news.html#ein-jahr-inno-screw" class="ncard">
      <div class="nm"><span>01. Dez 2025</span> &middot; <span class="ncat" data-de="Projektupdate" data-en="Project Update">Projektupdate</span></div>
      <h3 data-de="Ein Jahr INNO-SCREW" data-en="One year of INNO-SCREW">Ein Jahr INNO-SCREW</h3>
      <p class="de-block">Stand der experimentellen Infrastruktur und der ersten ver&ouml;ffentlichten Datens&auml;tze.</p>
      <p class="en-block" style="display:none">Status of the experimental infrastructure and the first published datasets.</p>
      <div class="nmore" data-de="Weiterlesen" data-en="Read more">Weiterlesen</div>
    </a>
    <a href="news.html#dataset-v123" class="ncard">
      <div class="nm"><span>Jul 2025</span> &middot; <span class="ncat" data-de="Datenver&ouml;ffentlichung" data-en="Dataset Release">Datenver&ouml;ffentlichung</span></div>
      <h3 data-de="Datensatzsammlung v1.2.3 auf Zenodo" data-en="Dataset collection v1.2.3 on Zenodo">Datensatzsammlung v1.2.3 auf Zenodo</h3>
      <p class="de-block">Sechs Versuchsszenarien mit 34.082 Schraubvorg&auml;ngen unter CC BY 4.0 ver&ouml;ffentlicht.</p>
      <p class="en-block" style="display:none">Six experimental scenarios with 34,082 process recordings released under CC BY 4.0.</p>
      <div class="nmore" data-de="Weiterlesen" data-en="Read more">Weiterlesen</div>
    </a>
    <a href="news.html#schraubtec-2025" class="ncard">
      <div class="nm"><span>16. Mai 2025</span> &middot; <span class="ncat" data-de="Konferenz" data-en="Conference">Konferenz</span></div>
      <h3 data-de="SchraubTec Landshut 2025" data-en="SchraubTec Landshut 2025">SchraubTec Landshut 2025</h3>
      <p class="de-block">Vorstellung der Projektziele und der offenen Datens&auml;tze vor Fachpublikum aus der Industrie.</p>
      <p class="en-block" style="display:none">Presentation of the project objectives and open datasets to a specialist industrial audience.</p>
      <div class="nmore" data-de="Weiterlesen" data-en="Read more">Weiterlesen</div>
    </a>
  </div>
  <div style="text-align:center;margin-top:2.2rem">
    <a href="news.html" class="btn btn-b" data-de="Alle Meldungen" data-en="All news">Alle Meldungen</a>
  </div>
</div></div>
"""

page("index.html",
     "INNO-SCREW &mdash; Intelligentes Qualit\u00e4tsmanagement in industriellen Schraubprozessen",
     "INNO-SCREW: Forschungsprojekt zu maschinellem Lernen in der Qualitaetssicherung industrieller Schraubprozesse. RIF Institut und IPS TU Dortmund.",
     home)

# --------------------------------------------------------------------------
# PROJECT
# --------------------------------------------------------------------------

project = phdr("&Uuml;ber das Projekt", "About the project",
               "Forschungsteam, Institutionen und wissenschaftliche Grundlage von INNO-SCREW",
               "Research team, institutions and scientific foundation of INNO-SCREW") + """
<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk">INNO-SCREW</div>
    <h2 data-de="Das Vorhaben" data-en="The project">Das Vorhaben</h2>
    <div class="sr"></div>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;align-items:start" class="two-col">
    <div class="prose">
      <p class="de-block"><strong>INNO-SCREW</strong> steht f&uuml;r &bdquo;Innovationszentrum f&uuml;r
      intelligentes Qualit&auml;tsmanagement in industriellen Schraubprozessen mithilfe maschineller
      Lernverfahren&ldquo;. Das Vorhaben wird im Rahmen des Programms INNO-KOM durch das
      Bundesministerium f&uuml;r Wirtschaft und Energie (BMWE) gef&ouml;rdert.</p>
      <p class="de-block">Ziel ist der Aufbau eines Innovationszentrums am RIF Institut f&uuml;r
      Forschung und Transfer e.V. in Kooperation mit dem Institut f&uuml;r Produktionssysteme (IPS)
      der TU Dortmund. Das Zentrum entwickelt und erprobt Verfahren zur Erkennung von
      Qualit&auml;tsabweichungen in Schraubprozessen und stellt die zugrunde liegenden Messdaten als
      offene Forschungsdaten bereit.</p>
      <p class="de-block">Die Forschungsinfrastruktur umfasst f&uuml;nf Schraubsysteme unterschiedlicher
      Bauart. Sie bilden die Bandbreite industrieller Anwendungsf&auml;lle ab &mdash; von der
      vollautomatischen Station bis zum kabellosen Handschrauber.</p>
      <p class="en-block" style="display:none"><strong>INNO-SCREW</strong> stands for
      &ldquo;Innovation Centre for Intelligent Quality Management in Industrial Screw Fastening
      Processes Using Machine Learning Methods&rdquo;. The project is funded under the INNO-KOM
      programme by the Federal Ministry for Economic Affairs and Energy (BMWE).</p>
      <p class="en-block" style="display:none">The objective is to establish an innovation centre at
      RIF Institut f&uuml;r Forschung und Transfer e.V. in cooperation with the Institute of
      Production Systems (IPS) at TU Dortmund. The centre develops and evaluates methods for
      detecting quality deviations in screwdriving processes and publishes the underlying
      measurement data as open research data.</p>
      <p class="en-block" style="display:none">The research infrastructure comprises five
      screwdriving systems of different designs, covering the range of industrial use cases &mdash;
      from a fully automatic station to a cordless hand-held tool.</p>
    </div>
    <div>
      <div style="background:var(--cd);border:1px solid var(--bd);border-radius:10px;padding:1.7rem;box-shadow:var(--sh)">
        <div style="display:flex;flex-direction:column;gap:.85rem">
%s
        </div>
      </div>
    </div>
  </div>
</div></div>
""" % "\n".join(
    """          <div style="display:flex;gap:.8rem;font-size:.875rem">
            <span style="color:var(--fa);width:112px;flex-shrink:0;font-family:'JetBrains Mono',monospace;font-size:.73rem" data-de="%s" data-en="%s">%s</span>
            <span style="color:var(--tk);font-weight:500">%s</span>
          </div>""" % (de, en, de, val)
    for de, en, val in [
        ("Laufzeit", "Duration", "01.12.2024 &ndash; 31.05.2027"),
        ("Dauer", "Length", "30 Monate / months"),
        ("F&ouml;rderprogramm", "Programme", "INNO-KOM"),
        ("F&ouml;rdergeber", "Funding body", "BMWE"),
        ("Projekttr&auml;ger", "Project sponsor", "EURONORM GmbH, Berlin"),
        ("Durchf&uuml;hrung", "Executed by", "RIF e.V. &amp; IPS TU Dortmund"),
        ("Projektleitung", "Project lead", "Michelle Henkies, M.Sc."),
        ("Bearbeitung", "Researcher", "Robert Mura, M.Sc."),
        ("Leitung IPS", "Head of IPS", "Univ.-Prof. Dr.-Ing. J. Deuse"),
    ]) + PROJECT_STATUS + """
<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Forschungsansatz" data-en="Research approach">Forschungsansatz</div>
    <h2 data-de="Vier Arbeitsschwerpunkte" data-en="Four areas of activity">Vier Arbeitsschwerpunkte</h2>
    <div class="sr"></div>
  </div>
  <div class="approach">
    <div class="stage"><div class="stage-n">01</div>
      <h4 data-de="Forschungsinfrastruktur" data-en="Research infrastructure">Forschungsinfrastruktur</h4>
      <p class="de-block">Instandsetzung, Datenanbindung und Wartungskonzept der f&uuml;nf Schraubsysteme.</p>
      <p class="en-block" style="display:none">Refurbishment, data connectivity and maintenance concept for the five screwdriving systems.</p></div>
    <div class="stage"><div class="stage-n">02</div>
      <h4 data-de="Experimentelle Untersuchungen" data-en="Experimental investigations">Experimentelle Untersuchungen</h4>
      <p class="de-block">Versuchsreihen mit fehlerfreien und gezielt abweichenden Schraubprozessen.</p>
      <p class="en-block" style="display:none">Series of trials with fault-free and deliberately deviating screwdriving processes.</p></div>
    <div class="stage"><div class="stage-n">03</div>
      <h4 data-de="Datengetriebene Qualit&auml;tssicherung" data-en="Data-driven quality assurance">Datengetriebene Qualit&auml;tssicherung</h4>
      <p class="de-block">Anomalieerkennung, Fehlerklassifikation und &Uuml;bertragbarkeit zwischen Schraubsystemen.</p>
      <p class="en-block" style="display:none">Anomaly detection, fault classification and transferability across screwdriving systems.</p></div>
    <div class="stage"><div class="stage-n">04</div>
      <h4 data-de="Offene Forschung &amp; Transfer" data-en="Open research &amp; transfer">Offene Forschung &amp; Transfer</h4>
      <p class="de-block">Ver&ouml;ffentlichung von Daten und Software, Schulungen und Netzwerkarbeit.</p>
      <p class="en-block" style="display:none">Publication of data and software, training measures and network activities.</p></div>
  </div>

  <div style="max-width:760px;margin:3.2rem auto 0">
    <div class="skk" style="display:block;width:fit-content;margin:0 auto 1.2rem" data-de="Arbeitspakete" data-en="Work packages">Arbeitspakete</div>
    <div class="wp">
      <div><code>AP 1</code><span class="de-block">Anforderungen und Erfolgskriterien definieren</span><span class="en-block" style="display:none">Define requirements and success criteria</span></div>
      <div><code>AP 2</code><span class="de-block">Digitale Bef&auml;higung der Schraubsysteme</span><span class="en-block" style="display:none">Digital enablement of the screwdriving systems</span></div>
      <div><code>AP 3</code><span class="de-block">Durchf&uuml;hrung der Versuche und Aufzeichnung der Schraubprozesse</span><span class="en-block" style="display:none">Conducting the trials and recording the screwdriving processes</span></div>
      <div><code>AP 4</code><span class="de-block">Aufbereitung und Bereitstellung der Prozessdaten</span><span class="en-block" style="display:none">Preparation and provision of the process data</span></div>
      <div><code>AP 5</code><span class="de-block">Projektbegleitende Ma&szlig;nahmen, Schulung und Transfer</span><span class="en-block" style="display:none">Accompanying measures, training and transfer</span></div>
    </div>
  </div>
</div></div>

<div class="sec sec-a"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Projektteam" data-en="Project team">Projektteam</div>
    <h2 data-de="Projektteam" data-en="Project team">Projektteam</h2>
    <div class="sr"></div>
  </div>
  <div class="cards">
    <div class="card" style="border-top:3px solid var(--gd3)">
      <img src="assets/team-henkies.jpg" alt="Michelle Henkies" style="width:100%;height:220px;object-fit:cover;object-position:center top;border-radius:8px;margin-bottom:1rem;display:block">
      <h3>Michelle Henkies, M.Sc.</h3>
      <div style="font-size:.78rem;color:var(--gd2);font-weight:700;margin:.25rem 0 .7rem">Projektleitung &middot; RIF Institut</div>
      <p style="font-size:.875rem" class="de-block">Leitet das Forschungsvorhaben INNO-SCREW am RIF Institut. Ihre Arbeit umfasst die Koordination des Projekts, die Anbindung der Schraubsysteme sowie die Zusammenarbeit mit Industriepartnern und dem Projekttr&auml;ger.</p>
      <p style="font-size:.875rem;display:none" class="en-block">Leads the INNO-SCREW research project at RIF Institut. Her work covers project coordination, integration of the screwdriving systems and collaboration with industrial partners and the project sponsor.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1rem">
        <a href="mailto:michelle.henkies@rif-ev.de" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">&#9993; michelle.henkies@rif-ev.de</a>
        <a href="https://ips.mb.tu-dortmund.de/ueber-uns/team/michelle-henkies/" target="_blank" rel="noopener" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">IPS-Profil</a>
        <a href="https://orcid.org/0000-0002-5095-5141" target="_blank" rel="noopener" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">ORCID</a>
      </div>
    </div>
    <div class="card" style="border-top:3px solid var(--bl2)">
      <img src="assets/team-mura.jpg" alt="Robert Mura" style="width:100%;height:220px;object-fit:cover;object-position:center top;border-radius:8px;margin-bottom:1rem;display:block">
      <h3>Robert Mura, M.Sc.</h3>
      <div style="font-size:.78rem;color:var(--bl2);font-weight:700;margin:.25rem 0 .7rem">Projektbearbeitung &middot; RIF Institut</div>
      <p style="font-size:.875rem" class="de-block">Bearbeitet das Vorhaben INNO-SCREW am RIF Institut. Schwerpunkt sind die Durchf&uuml;hrung der Schraubversuche, die Datenerfassung an den Schraubsystemen sowie die Aufbereitung der Messdaten f&uuml;r die Forschungsgemeinschaft.</p>
      <p style="font-size:.875rem;display:none" class="en-block">Works on the INNO-SCREW project at RIF Institut. His focus is the execution of screwdriving trials, data acquisition at the screwdriving systems and preparation of the measurement data for the research community.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1rem">
        <a href="mailto:robert.mura@rif-ev.de" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">&#9993; robert.mura@rif-ev.de</a>
        <a href="https://ips.mb.tu-dortmund.de/ueber-uns/team/robert-mura/" target="_blank" rel="noopener" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">IPS-Profil</a>
        <a href="https://orcid.org/0009-0003-6032-6556" target="_blank" rel="noopener" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">ORCID</a>
      </div>
    </div>
    <div class="card">
      <img src="assets/team-deuse.jpg" alt="Univ.-Prof. Dr.-Ing. Jochen Deuse" style="width:100%;height:220px;object-fit:cover;object-position:center top;border-radius:8px;margin-bottom:1rem;display:block">
      <h3>Univ.-Prof. Dr.-Ing. Jochen Deuse</h3>
      <div style="font-size:.78rem;color:var(--bl2);font-weight:700;margin:.25rem 0 .7rem">Institutsleitung &middot; IPS TU Dortmund</div>
      <p style="font-size:.875rem" class="de-block">Leitet das Institut f&uuml;r Produktionssysteme (IPS) der TU Dortmund. Forschungsschwerpunkte: Industrial Data Science, Lean Management, Produktionssystemgestaltung und Smart Quality. Wissenschaftliche Betreuung von INNO-SCREW.</p>
      <p style="font-size:.875rem;display:none" class="en-block">Heads the Institute of Production Systems (IPS) at TU Dortmund. Research focus: Industrial Data Science, Lean Management, production system design and Smart Quality. Scientific supervisor of INNO-SCREW.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1rem">
        <a href="mailto:sekretariat.ips.mb@tu-dortmund.de" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">&#9993; Sekretariat IPS</a>
        <a href="https://ips.mb.tu-dortmund.de/en/about-us/team/jochen-deuse/" target="_blank" rel="noopener" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">IPS-Profil</a>
        <a href="https://orcid.org/0000-0003-4066-4357" target="_blank" rel="noopener" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">ORCID</a>
        <a href="https://dblp.uni-trier.de/pid/01/3551.html" target="_blank" rel="noopener" style="background:var(--bg2);color:var(--mu);padding:.22rem .58rem;border-radius:5px;font-size:.77rem;text-decoration:none;border:1px solid var(--bd)">DBLP</a>
      </div>
    </div>
  </div>
</div></div>

<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Einrichtungen" data-en="Institutions">Einrichtungen</div>
    <h2 data-de="Durchf&uuml;hrende Einrichtungen" data-en="Executing institutions">Durchf&uuml;hrende Einrichtungen</h2>
    <div class="sr"></div>
  </div>
  <div class="cards" style="max-width:820px;margin:0 auto">
    <div class="card">
      <div class="cico">&#127970;</div>
      <h3>RIF Institut f&uuml;r Forschung und Transfer e.V.</h3>
      <p class="de-block">Abteilung Produktionssysteme, Dortmund. Gemeinn&uuml;tzige Forschungseinrichtung und Zuwendungsempf&auml;nger im Programm INNO-KOM.</p>
      <p class="en-block" style="display:none">Production Systems Department, Dortmund. Non-profit research institute and recipient of funding under the INNO-KOM programme.</p>
    </div>
    <div class="card">
      <div class="cico">&#127979;</div>
      <h3>Institut f&uuml;r Produktionssysteme (IPS), TU Dortmund</h3>
      <p class="de-block">Fakult&auml;t Maschinenbau. Wissenschaftlicher Kooperationspartner mit Schwerpunkt Industrial Data Science und Smart Quality.</p>
      <p class="en-block" style="display:none">Faculty of Mechanical Engineering. Scientific cooperation partner focusing on Industrial Data Science and Smart Quality.</p>
    </div>
  </div>
</div></div>
"""

page("project.html", "Projekt &mdash; INNO-SCREW",
     "Forschungsteam, Foerderung, Arbeitsschwerpunkte und Arbeitspakete des Projekts INNO-SCREW.",
     project)

# --------------------------------------------------------------------------
# RESEARCH INFRASTRUCTURE  (5 screwdriving systems)
# --------------------------------------------------------------------------

SYSTEMS = [
    {
        "id": "ass", "code": "ASS", "icon": "&#128297;", "img": "assets/station-ass.webp",
        "name_de": "Automatische Schraubstation",
        "name_en": "Automatic screwdriving station",
        "short_de": "Vollautomatische, NC-gesteuerte Station",
        "short_en": "Fully automatic, NC-controlled station",
        "teaser_de": "Vollautomatische, NC-gesteuerte Schraubstation (Bosch Rexroth CS351) mit einer Spindel und zwei Verschraubungen je Zyklus.",
        "teaser_en": "Fully automatic, NC-controlled screwdriving station (Bosch Rexroth CS351) with one spindle and two fastenings per cycle.",
        "desc_de": "Die Automatische Schraubstation (ASS) wurde urspr&uuml;nglich f&uuml;r die Verschraubung von Motorgeh&auml;useteilen bei Bosch Ungarn ausgelegt. Sie f&uuml;hrt zwei Verschraubungen mit einer Spindel durch, vollautomatisch und NC-gesteuert &uuml;ber ein CS351-Einkanalsystem von Bosch Rexroth. Die ASS war zu Projektbeginn die einzige vollst&auml;ndig einsatzf&auml;hige Station der Forschungsinfrastruktur. Die Prozessdaten werden als JSON &uuml;ber einen FTP-Server abgelegt; erfasst werden Drehmoment, Drehwinkel, Zeit und Gradient.",
        "desc_en": "The automatic screwdriving station (ASS) was originally designed for fastening motor housing components at Bosch Hungary. It performs two fastenings with a single spindle, fully automatic and NC-controlled via a Bosch Rexroth CS351 single-channel system. At the start of the project the ASS was the only fully operational station in the research infrastructure. Process data are written as JSON to an FTP server; torque, angle, time and gradient are recorded.",
        "chips": ["Bosch Rexroth CS351", "0,5 &ndash; 5,6 Nm", "780 U/min", "JSON / FTP"],
        "specs": [
            ("Hersteller", "Manufacturer", "Bosch Rexroth"),
            ("Steuerung", "Control system", "NC &mdash; CS351 Einkanalsystem"),
            ("Drehmomentbereich", "Torque range", "0,5 &ndash; 5,6 Nm"),
            ("Max. Drehzahl", "Max. speed", "780 U/min"),
            ("Spindeln", "Spindles", "1"),
            ("Datenanbindung", "Connectivity", "JSON &uuml;ber FTP-Server"),
            ("Messgr&ouml;&szlig;en", "Measured variables", "Drehmoment, Drehwinkel, Zeit, Gradient"),
            ("Herkunft", "Origin", "Motorgeh&auml;usemontage, Bosch Ungarn"),
            ("Status", "Status", "Einsatzf&auml;hig"),
        ],
        "scenarios": ["S01"],
    },
    {
        "id": "rss", "code": "RSS", "icon": "&#129302;", "img": "assets/station-rss.webp",
        "name_de": "Roboterbasierte Schraubstation",
        "name_en": "Robot-based screwdriving station",
        "short_de": "Cobot mit Schraubaktor und Zuf&uuml;hrung",
        "short_en": "Cobot with screwdriving actuator and feed",
        "teaser_de": "Robotergest&uuml;tzte Durchf&uuml;hrung automatisierter und reproduzierbarer Versuchsabl&auml;ufe auf einem mobilen Montagesockel.",
        "teaser_en": "Robot-assisted execution of automated and reproducible experimental runs on a mobile assembly base.",
        "desc_de": "Die Roboterbasierte Schraubstation (RSS) besteht aus einem Hanwha-Cobot auf einem mobilen Montagesockel mit einem multifunktionalen Schraubaktor von OnRobot inklusive Schraubenzuf&uuml;hrung. Sie erlaubt die robotergest&uuml;tzte Durchf&uuml;hrung automatisierter und reproduzierbarer Versuchsabl&auml;ufe. Das System wurde im Rahmen des BMWi-Projekts SUPPLy beschafft und erprobt. Die Datenanbindung erfolgt &uuml;ber Modbus (TCP) und Ethernet/IP f&uuml;r den Schrauber sowie Modbus f&uuml;r den Roboter.",
        "desc_en": "The robot-based screwdriving station (RSS) consists of a Hanwha cobot on a mobile assembly base with a multi-functional OnRobot screwdriving actuator including automatic screw feed. It allows automated and reproducible experimental runs to be carried out under robot control. The system was procured and tested in the BMWi project SUPPLy. Connectivity is via Modbus (TCP) and Ethernet/IP for the screwdriver and Modbus for the robot.",
        "chips": ["Hanwha Cobot", "OnRobot", "0,15 &ndash; 5,0 Nm", "Modbus TCP"],
        "specs": [
            ("Roboter", "Robot", "Hanwha Cobot, mobiler Montagesockel"),
            ("Schraubaktor", "Actuator", "OnRobot, multifunktional mit Zuf&uuml;hrung"),
            ("Drehmomentbereich", "Torque range", "0,15 &ndash; 5,0 Nm"),
            ("Max. Drehzahl", "Max. speed", "340 U/min"),
            ("Datenanbindung", "Connectivity", "Modbus TCP / Ethernet/IP"),
            ("Messgr&ouml;&szlig;en", "Measured variables", "Drehmoment, Vorschub, Vorschubkraft, Achsdaten"),
            ("Herkunft", "Origin", "Projekt SUPPLy (BMWi)"),
            ("Status", "Status", "Bedingt einsatzf&auml;hig"),
        ],
        "scenarios": ["S02"],
    },
    {
        "id": "mss", "code": "MSS", "icon": "&#128400;&#65039;", "img": "assets/station-mss.webp",
        "name_de": "Manuelle Schraubstation",
        "name_en": "Manual screwdriving station",
        "short_de": "Montagearbeitsplatz mit manuellem Vorschub",
        "short_en": "Assembly workstation with manual feed",
        "teaser_de": "Klassischer Montagearbeitsplatz mit manuellem Vorschub zur Untersuchung bedienerabh&auml;ngiger Prozessstreuung.",
        "teaser_en": "Classic assembly workstation with manual feed for investigating operator-dependent process variation.",
        "desc_de": "Die Manuelle Schraubstation (MSS) entspricht einem klassischen Montagearbeitsplatz und stammt aus derselben dekommissionierten Fertigungslinie wie die ASS. Sie enth&auml;lt dieselbe Schraubeinheit wie die ASS (0,5 &ndash; 5,6 Nm, max. 780 U/min), der Vorschub erfolgt jedoch manuell durch eine Bedienperson. Damit eignet sie sich zur Untersuchung bedienerabh&auml;ngiger Prozessstreuung. F&uuml;r die Inbetriebnahme sind Schulungen von Bosch Rexroth erforderlich. Datenanbindung: FTP (ohne CF350-Karte) beziehungsweise Open Protocol, XML Protocol, Rexroth IPM Protocol oder HTTP (mit CF350-Karte).",
        "desc_en": "The manual screwdriving station (MSS) mirrors a classic assembly workstation and comes from the same decommissioned production line as the ASS. It uses the same screwdriving unit as the ASS (0.5 &ndash; 5.6 Nm, max. 780 rpm), but the feed is performed manually by an operator. This makes it suitable for investigating operator-dependent process variation. Bosch Rexroth training is required before commissioning. Connectivity: FTP (without CF350 card) or Open Protocol, XML Protocol, Rexroth IPM Protocol or HTTP (with CF350 card).",
        "chips": ["Bosch Rexroth", "Manueller Vorschub", "0,5 &ndash; 5,6 Nm", "Open Protocol"],
        "specs": [
            ("Hersteller", "Manufacturer", "Bosch Rexroth"),
            ("Vorschub", "Feed", "Manuell, handgef&uuml;hrt"),
            ("Drehmomentbereich", "Torque range", "0,5 &ndash; 5,6 Nm"),
            ("Max. Drehzahl", "Max. speed", "780 U/min"),
            ("Datenanbindung", "Connectivity", "FTP / Open Protocol / XML / HTTP"),
            ("Messgr&ouml;&szlig;en", "Measured variables", "Drehmoment, Drehwinkel, Zeit, Gradient"),
            ("Herkunft", "Origin", "Dekommissionierte ASS-Linie"),
            ("Status", "Status", "Funktionsf&auml;hig, nicht einsatzf&auml;hig"),
        ],
        "scenarios": ["S03"],
    },
    {
        "id": "dss", "code": "DSS", "icon": "&#9881;&#65039;", "img": "assets/station-dss.webp",
        "name_de": "Doppelspindel-Schraubstation",
        "name_en": "Dual-spindle screwdriving station",
        "short_de": "Zweispindliges System bis 180 Nm",
        "short_en": "Dual-spindle system up to 180 Nm",
        "teaser_de": "Zweispindliges Schraubsystem zur Untersuchung simultaner Schraubprozesse im h&ouml;heren Drehmomentbereich.",
        "teaser_en": "Dual-spindle screwdriving system for investigating simultaneous fastening processes at higher torque levels.",
        "desc_de": "Die Doppelspindel-Schraubstation (DSS) stammt aus dem Demonstrations- und Forschungsbereich von BMW und wurde dort f&uuml;r Versuche und Schulungen eingesetzt. Die etwa vier Meter hohe Anlage f&uuml;hrt zwei Verschraubungen gleichzeitig aus; der hydraulische Schraubausleger wird dabei von einer Bedienperson gef&uuml;hrt. Mit einem Drehmomentbereich bis 180 Nm deckt sie schwere industrielle Schraubf&auml;lle ab. Die Datenanbindung erfolgt &uuml;ber PROFINET.",
        "desc_en": "The dual-spindle screwdriving station (DSS) originates from BMW's demonstration and research area, where it was used for trials and training. The roughly four-metre installation performs two fastenings simultaneously; the hydraulic boom is guided by an operator. With a torque range up to 180 Nm it covers heavy industrial fastening cases. Connectivity is via PROFINET.",
        "chips": ["Desoutter / IHF Vector 180", "2 Spindeln", "bis 180 Nm", "PROFINET"],
        "specs": [
            ("Hersteller", "Manufacturer", "Desoutter / IHF Vector 180"),
            ("Spindeln", "Spindles", "2 (simultan)"),
            ("Drehmomentbereich", "Torque range", "bis 180 Nm"),
            ("Max. Drehzahl", "Max. speed", "500 U/min"),
            ("Vorschub", "Feed", "Hydraulisch, handgef&uuml;hrt"),
            ("Datenanbindung", "Connectivity", "PROFINET"),
            ("Messgr&ouml;&szlig;en", "Measured variables", "Drehmoment, Drehwinkel"),
            ("Herkunft", "Origin", "BMW Demonstrations- und Forschungsbereich"),
            ("Status", "Status", "Funktionsf&auml;hig, nicht einsatzf&auml;hig"),
        ],
        "scenarios": ["S04"],
    },
    {
        "id": "kss", "code": "KSS", "icon": "&#128295;", "img": "assets/station-kss.webp",
        "name_de": "Kabellose Schraubsysteme",
        "name_en": "Cordless screwdriving systems",
        "short_de": "Handgef&uuml;hrte Akkuschrauber, drei Varianten",
        "short_en": "Hand-held cordless tools, three variants",
        "teaser_de": "Handgef&uuml;hrte Schraubsysteme mit integrierter Prozess&uuml;berwachung auf Basis von Drehmoment- und Winkeldaten.",
        "teaser_en": "Hand-held screwdriving systems with integrated process monitoring based on torque and angle data.",
        "desc_de": "Die kabellosen Schraubsysteme (KSS) decken freie, handgef&uuml;hrte Schraubprozesse ab &mdash; einen der verbreitetsten Anwendungsf&auml;lle in der industriellen Montage. Beschafft wurden zwei Systemtypen: ein Ingersoll Rand MH-TEC (gro&szlig;: 2,4 &ndash; 12,0 Nm bei 750 U/min; klein: 0,8 &ndash; 4,0 Nm bei 1500 U/min) sowie zwei Handschrauber von Atlas Copco (ITB-P: 1 &ndash; 6 Nm bei 2000 U/min; ITB-A: 10 &ndash; 55 Nm bei 590 U/min). Beide Systeme &uuml;bertragen Drehmoment- und Drehwinkelkurven &uuml;ber das Open Protocol und erm&ouml;glichen damit eine integrierte Prozess&uuml;berwachung auf Basis von Drehmoment- und Winkeldaten.",
        "desc_en": "The cordless screwdriving systems (KSS) cover free-form, hand-guided fastening &mdash; one of the most widespread use cases in industrial assembly. Two system types were procured: an Ingersoll Rand MH-TEC (large: 2.4 &ndash; 12.0 Nm at 750 rpm; small: 0.8 &ndash; 4.0 Nm at 1500 rpm) and two Atlas Copco hand tools (ITB-P: 1 &ndash; 6 Nm at 2000 rpm; ITB-A: 10 &ndash; 55 Nm at 590 rpm). Both transmit torque and angle curves via the Open Protocol, enabling integrated process monitoring based on torque and angle data.",
        "chips": ["Ingersoll Rand MH-TEC", "Atlas Copco ITB-P / ITB-A", "0,8 &ndash; 55 Nm", "Open Protocol"],
        "specs": [
            ("System 1", "System 1", "Ingersoll Rand MH-TEC (2,4 &ndash; 12,0 Nm / 750 U/min)"),
            ("System 2", "System 2", "Ingersoll Rand MH-TEC (0,8 &ndash; 4,0 Nm / 1500 U/min)"),
            ("System 3", "System 3", "Atlas Copco ITB-P (1 &ndash; 6 Nm / 2000 U/min)"),
            ("System 4", "System 4", "Atlas Copco ITB-A (10 &ndash; 55 Nm / 590 U/min)"),
            ("Datenanbindung", "Connectivity", "Open Protocol"),
            ("Messgr&ouml;&szlig;en", "Measured variables", "Drehmoment- und Drehwinkelkurve"),
            ("Anwendungsfall", "Use case", "Freie, handgef&uuml;hrte Schraubprozesse"),
            ("Herkunft", "Origin", "Beschafft &uuml;ber INNO-SCREW"),
            ("Status", "Status", "Beschafft und in Betrieb"),
        ],
        "scenarios": ["S05", "S06"],
    },
]

SCENARIOS = {
    "S01": dict(de="Gewindesch&auml;digung", en="Thread degradation", n="5.000", cls="2 (OK / NOK)",
                clsen="2 (OK / NOK)", ds="DS-2025-01", station="ASS"),
    "S02": dict(de="Oberfl&auml;chenreibung", en="Surface friction", n="12.500", cls="8",
                clsen="8", ds="DS-2025-02", station="RSS"),
    "S03": dict(de="Montagebedingungen 1", en="Assembly conditions 1", n="1.700", cls="26",
                clsen="26", ds="DS-2025-03", station="MSS"),
    "S04": dict(de="Montagebedingungen 2", en="Assembly conditions 2", n="5.000", cls="25",
                clsen="25", ds="DS-2025-04", station="DSS"),
    "S05": dict(de="Oberes Werkst&uuml;ck", en="Upper workpiece", n="2.400", cls="42",
                clsen="42", ds="DS-2025-05", station="KSS"),
    "S06": dict(de="Unteres Werkst&uuml;ck", en="Lower workpiece", n="7.482", cls="44",
                clsen="44", ds="DS-2025-06", station="KSS"),
}


def spec_table(specs):
    rows = []
    for de, en, val in specs:
        rows.append(
            '          <div class="spec-row"><span class="spec-key" data-de="%s" data-en="%s">%s</span>'
            '<span class="spec-val">%s</span></div>' % (de, en, de, val)
        )
    return "\n".join(rows)


def scenario_rows(codes):
    out = []
    for c in codes:
        s = SCENARIOS[c]
        out.append(
            '        <div class="dsrow"><span class="k">%s</span><span class="v">'
            '<span class="de-block">%s &mdash; %s Schraubvorg&auml;nge, %s Klassen</span>'
            '<span class="en-block" style="display:none">%s &mdash; %s process recordings, %s classes</span>'
            ' &middot; <code>%s</code></span></div>'
            % (c, s["de"], s["n"], s["cls"], s["en"], s["n"].replace(".", ","), s["clsen"], s["ds"])
        )
    return "\n".join(out)

# --- infrastructure.html -------------------------------------------------

tabs = ['    <a href="#" class="active" data-panel="overview" onclick="switchSystem(event,\'overview\')">'
        '&#128451;&#65039; <span class="de-block">&Uuml;bersicht</span>'
        '<span class="en-block" style="display:none">Overview</span></a>']
for s in SYSTEMS:
    tabs.append(
        '    <a href="#" data-panel="%s" onclick="switchSystem(event,\'%s\')">%s '
        '<span class="badge">%s</span> <span class="de-block">%s</span>'
        '<span class="en-block" style="display:none">%s</span></a>'
        % (s["id"], s["id"], s["icon"], s["code"], s["short_de"], s["short_en"]))

cards = []
for s in SYSTEMS:
    cards.append("""      <a class="st-card" href="#" onclick="switchSystem(event,'%s')">
        <span class="st-card-icon">%s</span><span class="st-card-code">%s</span>
        <h3 data-de="%s" data-en="%s">%s</h3>
        <p class="de-block">%s</p>
        <p class="en-block" style="display:none">%s</p>
        <div class="st-card-link"><span class="de-block">Details</span><span class="en-block" style="display:none">Details</span></div>
      </a>""" % (s["id"], s["icon"], s["code"], s["name_de"], s["name_en"], s["name_de"],
                 s["teaser_de"], s["teaser_en"]))

panels = []
for s in SYSTEMS:
    panels.append("""
<div class="station-panel" id="panel-%(id)s">
  <div class="st-hero">
    <div class="st-hero-inner">
      <div>
        <div class="st-badge">%(code)s &middot; <span class="de-block">Schraubsystem</span><span class="en-block" style="display:none">Screwdriving system</span></div>
        <h1 data-de="%(name_de)s" data-en="%(name_en)s">%(name_de)s</h1>
        <p class="de-block">%(teaser_de)s</p>
        <p class="en-block" style="display:none">%(teaser_en)s</p>
        <div class="st-chips">%(chips)s</div>
      </div>
      <div class="st-icon-big">%(icon)s</div>
    </div>
  </div>
  <div class="sec"><div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;align-items:start">
      <div>
        <div class="skk" style="margin-bottom:1rem" data-de="Beschreibung" data-en="Description">Beschreibung</div>
        <p class="de-block" style="color:var(--mu);line-height:1.9;font-size:.95rem">%(desc_de)s</p>
        <p class="en-block" style="display:none;color:var(--mu);line-height:1.9;font-size:.95rem">%(desc_en)s</p>
        <div style="margin-top:1.6rem;display:flex;gap:.6rem;flex-wrap:wrap">
          <a href="station-%(id)s.html" class="btn btn-b btn-sm" data-de="Systemseite" data-en="System page">Systemseite</a>
          <a href="data.html#datensaetze" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)" data-de="Zugeh&ouml;rige Datens&auml;tze" data-en="Related datasets">Zugeh&ouml;rige Datens&auml;tze</a>
        </div>
      </div>
      <div>
        <img src="%(img)s" alt="%(name_de)s" style="width:100%%;border-radius:8px;display:block;margin-bottom:1.2rem;object-fit:cover;max-height:250px">
        <div class="spec-label" data-de="Technische Daten" data-en="Technical data">Technische Daten</div>
        <div class="spec-table">
%(specs)s
        </div>
      </div>
    </div>
  </div></div>
</div>""" % dict(s,
                 chips="".join('<span class="chip">%s</span>' % c for c in s["chips"]),
                 specs=spec_table(s["specs"])))

sc_rows = []
for code in ["S01", "S02", "S03", "S04", "S05", "S06"]:
    sc = SCENARIOS[code]
    sc_rows.append(
        "      <tr><td><code>%s</code></td><td><strong><span class=\"de-block\">%s</span>"
        "<span class=\"en-block\" style=\"display:none\">%s</span></strong></td>"
        "<td><code>%s</code></td><td>%s</td><td>%s</td><td><code>%s</code></td></tr>"
        % (code, sc["de"], sc["en"], sc["station"], sc["n"], sc["cls"], sc["ds"]))

infra = """
<nav class="stnav" id="stnav">
  <div class="stnav-inner">
%s
  </div>
</nav>

<div class="station-panel active" id="panel-overview">
  <div class="st-hero">
    <div class="st-hero-inner">
      <div>
        <div class="st-badge">INNO-SCREW &middot; <span class="de-block">Forschungsinfrastruktur</span><span class="en-block" style="display:none">Research infrastructure</span></div>
        <h1 data-de="Forschungsinfrastruktur" data-en="Research infrastructure">Forschungsinfrastruktur</h1>
        <p class="de-block">F&uuml;nf Schraubsysteme unterschiedlicher Bauart mit einheitlicher Messdatenerfassung. Sie bilden die Grundlage aller experimentellen Untersuchungen im Projekt.</p>
        <p class="en-block" style="display:none">Five screwdriving systems of different designs with a uniform data acquisition setup. They form the basis of all experimental investigations in the project.</p>
        <div class="st-chips"><span class="chip">ASS</span><span class="chip">RSS</span><span class="chip">MSS</span><span class="chip">DSS</span><span class="chip">KSS</span><span class="chip">Drehmoment &middot; Winkel &middot; Zeit</span></div>
      </div>
      <div class="st-icon-big">&#127981;</div>
    </div>
  </div>

  <div class="sec"><div class="wrap">
    <div class="sh">
      <div class="skk" data-de="Kennzeichnung" data-en="Identifiers">Kennzeichnung</div>
      <h2 data-de="Systeme, Szenarien und Datens&auml;tze" data-en="Systems, scenarios and datasets">Systeme, Szenarien und Datens&auml;tze</h2>
      <div class="sr"></div>
      <p class="de-block">Das Projekt unterscheidet drei Ebenen von Kennungen. Sie werden auf der gesamten Website getrennt gef&uuml;hrt.</p>
      <p class="en-block" style="display:none">The project distinguishes three levels of identifier. They are kept separate throughout this site.</p>
    </div>
%s
    <div class="tscroll" style="max-width:940px;margin:0 auto">
      <table class="dtable">
        <thead><tr>
          <th data-de="Szenario" data-en="Scenario">Szenario</th>
          <th data-de="Untersuchungsgegenstand" data-en="Subject of study">Untersuchungsgegenstand</th>
          <th data-de="System" data-en="System">System</th>
          <th data-de="Schraubvorg&auml;nge" data-en="Recordings">Schraubvorg&auml;nge</th>
          <th data-de="Klassen" data-en="Classes">Klassen</th>
          <th data-de="Datensatz" data-en="Dataset">Datensatz</th>
        </tr></thead>
        <tbody>
%s
        </tbody>
      </table>
    </div>
    <div class="note" style="max-width:940px;margin:1.6rem auto 0">
      <span class="de-block">Die Szenarien S01 bis S06 stammen aus der ver&ouml;ffentlichten Datensatzsammlung und wurden teilweise in Vorarbeiten aufgezeichnet. Laufende Messkampagnen aus INNO-SCREW werden unter eigenen Datensatzkennungen gef&uuml;hrt (siehe <a href="data.html" style="color:var(--bl2)">Forschungsdaten</a>).</span>
      <span class="en-block" style="display:none">Scenarios S01 to S06 come from the published dataset collection and were in part recorded in preliminary work. Ongoing measurement campaigns within INNO-SCREW are tracked under their own dataset identifiers (see <a href="data.html" style="color:var(--bl2)">Research Data</a>).</span>
    </div>
  </div></div>

  <div class="sec sec-a"><div class="wrap">
    <div class="sh">
      <div class="skk" data-de="Schraubsysteme" data-en="Screwdriving systems">Schraubsysteme</div>
      <h2 data-de="F&uuml;nf Systeme im &Uuml;berblick" data-en="Five systems at a glance">F&uuml;nf Systeme im &Uuml;berblick</h2>
      <div class="sr"></div>
    </div>
    <div class="st-overview-grid">
%s
    </div>
  </div></div>
</div>
%s
""" % ("\n".join(tabs), ID_SCHEME, "\n".join(sc_rows), "\n".join(cards), "\n".join(panels))

page("infrastructure.html", "Forschungsinfrastruktur &mdash; INNO-SCREW",
     "Fuenf Schraubsysteme der INNO-SCREW-Forschungsinfrastruktur: ASS, RSS, MSS, DSS und KSS mit technischen Daten und Datenanbindung.",
     infra)


# --- individual system pages ---------------------------------------------

for i, s in enumerate(SYSTEMS):
    prev_s = SYSTEMS[i - 1] if i > 0 else SYSTEMS[-1]
    next_s = SYSTEMS[(i + 1) % len(SYSTEMS)]
    body = phdr(s["name_de"], s["name_en"],
                "Schraubsystem %s &middot; Technische Daten und zugeh&ouml;rige Versuchsszenarien" % s["code"],
                "Screwdriving system %s &middot; technical data and related experimental scenarios" % s["code"])
    body += """
<div class="sec"><div class="wrap">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;align-items:start">
    <div>
      <div class="skk" style="margin-bottom:.9rem">%(code)s &mdash; INNO-SCREW</div>
      <h2 style="font-family:'Lora',serif;font-size:1.4rem;margin-bottom:.9rem;color:var(--tk)" data-de="%(name_de)s (%(code)s)" data-en="%(name_en)s (%(code)s)">%(name_de)s (%(code)s)</h2>
      <p class="de-block" style="color:var(--mu);line-height:1.9;font-size:.95rem">%(desc_de)s</p>
      <p class="en-block" style="display:none;color:var(--mu);line-height:1.9;font-size:.95rem">%(desc_en)s</p>
      <div style="margin-top:1.6rem;display:flex;gap:.6rem;flex-wrap:wrap">
        <a href="infrastructure.html#%(id)s" class="btn btn-b btn-sm" data-de="Zur Infrastruktur&uuml;bersicht" data-en="Back to infrastructure">Zur Infrastruktur&uuml;bersicht</a>
        <a href="data.html#datensaetze" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)" data-de="Forschungsdaten" data-en="Research data">Forschungsdaten</a>
      </div>
    </div>
    <div>
      <div style="background:var(--cd);border:1px solid var(--bd);border-radius:10px;padding:1.5rem;box-shadow:var(--sh)">
        <img src="%(img)s" alt="%(name_de)s" style="width:100%%;border-radius:8px;display:block;margin-bottom:1.1rem;object-fit:cover;max-height:260px">
        <div class="spec-label" data-de="Technische Daten" data-en="Technical data">Technische Daten</div>
        <div class="spec-table">
%(specs)s
        </div>
      </div>
    </div>
  </div>
</div></div>

<div class="sec sec-a"><div class="wrap" style="max-width:760px">
  <div class="sh">
    <div class="skk" data-de="Versuchsszenarien" data-en="Experimental scenarios">Versuchsszenarien</div>
    <h2 data-de="Szenarien auf diesem System" data-en="Scenarios recorded on this system">Szenarien auf diesem System</h2>
    <div class="sr"></div>
  </div>
  <div class="dscard">
    <div class="dsmeta" style="grid-template-columns:1fr">
%(scen)s
    </div>
    <div class="dsfoot">
      <a href="data.html#datensaetze" class="btn btn-b btn-sm" data-de="Datensatz-Metadaten" data-en="Dataset metadata">Datensatz-Metadaten</a>
      <a href="https://doi.org/10.5281/zenodo.16031381" target="_blank" rel="noopener" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)">Zenodo</a>
    </div>
  </div>
  <div style="display:flex;justify-content:space-between;gap:1rem;margin-top:2.4rem;flex-wrap:wrap">
    <a href="station-%(prev_id)s.html" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)">&larr; %(prev_code)s</a>
    <a href="station-%(next_id)s.html" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)">%(next_code)s &rarr;</a>
  </div>
</div></div>
""" % dict(s, specs=spec_table(s["specs"]), scen=scenario_rows(s["scenarios"]),
           prev_id=prev_s["id"], prev_code=prev_s["code"],
           next_id=next_s["id"], next_code=next_s["code"])
    page("station-%s.html" % s["id"],
         "%s (%s) &mdash; INNO-SCREW" % (s["name_de"], s["code"]),
         "Technische Daten des Schraubsystems %s in der INNO-SCREW-Forschungsinfrastruktur." % s["code"],
         body)

# --------------------------------------------------------------------------
# RESEARCH DATA
# --------------------------------------------------------------------------

ZEN = "https://doi.org/10.5281/zenodo.16031381"

DATASETS = [
    dict(ds="DS-2025-01", scen="S01", station="ASS",
         title_de="Gewindesch&auml;digung", title_en="Thread degradation",
         n="5.000", nen="5,000",
         faults_de="Fortschreitende Gewindesch&auml;digung durch wiederholtes Verschrauben derselben Bohrung",
         faults_en="Progressive thread degradation caused by repeatedly fastening the same hole",
         classes_de="2 Klassen: OK / NOK", classes_en="2 classes: OK / NOK",
         status="pub"),
    dict(ds="DS-2025-02", scen="S02", station="RSS",
         title_de="Oberfl&auml;chenreibung", title_en="Surface friction",
         n="12.500", nen="12,500",
         faults_de="Sieben reibungsbeeinflussende Oberfl&auml;chenzust&auml;nde der Kunststoffgeh&auml;use",
         faults_en="Seven surface conditions of the plastic housings that influence friction",
         classes_de="8 Klassen: OK und sieben Abweichungen", classes_en="8 classes: OK plus seven deviations",
         status="pub"),
    dict(ds="DS-2025-03", scen="S03", station="MSS",
         title_de="Montagebedingungen 1", title_en="Assembly conditions 1",
         n="1.700", nen="1,700",
         faults_de="Variation der Montagebedingungen, u.&nbsp;a. Cross-threading, Thread deformation und erh&ouml;htes Anziehdrehmoment",
         faults_en="Variation of assembly conditions, including cross-threading, thread deformation and increased tightening torque",
         classes_de="26 Klassen", classes_en="26 classes",
         status="pub"),
    dict(ds="DS-2025-04", scen="S04", station="DSS",
         title_de="Montagebedingungen 2", title_en="Assembly conditions 2",
         n="5.000", nen="5,000",
         faults_de="Erweiterte Variation der Montagebedingungen mit 25 unterscheidbaren Fehlerbildern",
         faults_en="Extended variation of assembly conditions with 25 distinguishable fault patterns",
         classes_de="25 Klassen", classes_en="25 classes",
         status="pub"),
    dict(ds="DS-2025-05", scen="S05", station="KSS",
         title_de="Oberes Werkst&uuml;ck", title_en="Upper workpiece",
         n="2.400", nen="2,400",
         faults_de="Fertigungsbedingte Varianz des oberen Werkst&uuml;cks",
         faults_en="Manufacturing-related variation of the upper workpiece",
         classes_de="42 Klassen", classes_en="42 classes",
         status="pub"),
    dict(ds="DS-2025-06", scen="S06", station="KSS",
         title_de="Unteres Werkst&uuml;ck", title_en="Lower workpiece",
         n="7.482", nen="7,482",
         faults_de="Fertigungsbedingte Varianz des unteren Werkst&uuml;cks",
         faults_en="Manufacturing-related variation of the lower workpiece",
         classes_de="44 Klassen", classes_en="44 classes",
         status="pub"),
]

PILL = {
    "pub": ('pill-pub', 'Ver&ouml;ffentlicht', 'Published'),
    "req": ('pill-req', 'Auf Anfrage verf&uuml;gbar', 'Available on request'),
    "prep": ('pill-prep', 'In Vorbereitung', 'In preparation'),
    "run": ('pill-run', 'Messkampagne l&auml;uft', 'Experimental campaign ongoing'),
}


def meta_row(k_de, k_en, v_de, v_en=None):
    if v_en is None:
        val = v_de
    else:
        val = ('<span class="de-block">%s</span><span class="en-block" style="display:none">%s</span>'
               % (v_de, v_en))
    return ('        <div class="dsrow"><span class="k" data-de="%s" data-en="%s">%s</span>'
            '<span class="v">%s</span></div>' % (k_de, k_en, k_de, val))


ds_cards = []
for d in DATASETS:
    cls, pde, pen = PILL[d["status"]]
    rows_left = "\n".join([
        meta_row("Datensatz-ID", "Dataset ID", "<code>%s</code>" % d["ds"]),
        meta_row("Schraubsystem", "Screwdriving system",
                 '<a href="station-%s.html"><code>%s</code></a>'
                 % (d["station"].lower(), d["station"])),
        meta_row("Versuchsszenario", "Experimental scenario", "<code>%s</code>" % d["scen"]),
        meta_row("Stichprobenumfang", "Number of samples",
                 "%s Schraubvorg&auml;nge" % d["n"], "%s process recordings" % d["nen"]),
        meta_row("Abweichungsarten", "Process deviation types", d["faults_de"], d["faults_en"]),
        meta_row("Labels", "Labels", d["classes_de"], d["classes_en"]),
        meta_row("Versuchsaufbau", "Experimental setup",
                 "Selbstfurchende Schrauben in Kunststoffgeh&auml;usen, zweiteiliger Werkst&uuml;ckaufbau",
                 "Self-tapping screws in plastic housings, two-part workpiece assembly"),
    ])
    rows_right = "\n".join([
        meta_row("Signale", "Available signals",
                 "Drehmoment, Drehwinkel, Zeit, Gradient &middot; 833,33 Hz",
                 "Torque, angle, time, gradient &middot; 833.33 Hz"),
        meta_row("Werkstoffe", "Materials",
                 "Kunststoffgeh&auml;use, selbstfurchende Stahlschrauben",
                 "Plastic housings, self-tapping steel screws"),
        meta_row("Prozessparameter", "Process parameters",
                 "Drehmoment- und Winkelvorgaben je Szenario, siehe Datensatzdokumentation",
                 "Torque and angle set points per scenario, see dataset documentation"),
        meta_row("Datenformat", "Data format", "JSON / CSV &middot; <code>pyscrew</code>"),
        meta_row("Lizenz", "Licence", "CC BY 4.0"),
        meta_row("DOI", "DOI",
                 '<a href="%s" target="_blank" rel="noopener">10.5281/zenodo.16031381</a>' % ZEN),
        meta_row("Zugeh&ouml;rige Publikation", "Related publication",
                 'West &amp; Deuse (2025), <a href="publications.html">PyScrew</a>'),
    ])
    ds_cards.append("""  <div class="dscard" id="%s">
    <div class="dshead">
      <span class="dsid">%s</span>
      <h3 data-de="%s" data-en="%s">%s</h3>
      <span class="pill %s" data-de="%s" data-en="%s">%s</span>
    </div>
    <div class="dsmeta">
      <div>
%s
      </div>
      <div>
%s
      </div>
    </div>
    <div class="dsfoot">
      <a href="%s" target="_blank" rel="noopener" class="btn btn-b btn-sm">Zenodo</a>
      <a href="https://github.com/nikolaiwest/pyscrew" target="_blank" rel="noopener" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)">PyScrew</a>
      <a href="station-%s.html" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)" data-de="Schraubsystem" data-en="Screwdriving system">Schraubsystem</a>
    </div>
  </div>""" % (d["ds"].lower(), d["ds"], d["title_de"], d["title_en"], d["title_de"],
               cls, pde, pen, pde, rows_left, rows_right, ZEN, d["station"].lower()))

data_page = phdr("Forschungsdaten", "Research data",
                 "Offene Datens&auml;tze aus industriellen Schraubprozessen mit standardisierten Metadaten",
                 "Open datasets from industrial screwdriving processes with standardised metadata") + """
<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Kennzeichnung" data-en="Identifiers">Kennzeichnung</div>
    <h2 data-de="Systeme, Szenarien und Datens&auml;tze" data-en="Systems, scenarios and datasets">Systeme, Szenarien und Datens&auml;tze</h2>
    <div class="sr"></div>
    <p class="de-block">Jeder Datensatz ist einem Schraubsystem und einem Versuchsszenario zugeordnet. Die drei Kennungsebenen werden getrennt gef&uuml;hrt.</p>
    <p class="en-block" style="display:none">Every dataset is assigned to a screwdriving system and an experimental scenario. The three levels of identifier are kept separate.</p>
  </div>
""" + ID_SCHEME + """
  <div class="sh" style="margin-top:3rem;margin-bottom:2rem">
    <div class="skk" data-de="Verf&uuml;gbarkeit" data-en="Availability">Verf&uuml;gbarkeit</div>
    <h2 data-de="Status der Datens&auml;tze" data-en="Dataset status">Status der Datens&auml;tze</h2>
    <div class="sr"></div>
    <p class="de-block">Jeder Datensatz tr&auml;gt einen von vier Status. Nur als <em>ver&ouml;ffentlicht</em> gekennzeichnete Daten sind &ouml;ffentlich abrufbar.</p>
    <p class="en-block" style="display:none">Every dataset carries one of four statuses. Only data marked as <em>published</em> are publicly available.</p>
  </div>
  <div style="display:flex;gap:.7rem;flex-wrap:wrap;justify-content:center;margin-bottom:1rem">
    <span class="pill pill-pub" data-de="Ver&ouml;ffentlicht" data-en="Published">Ver&ouml;ffentlicht</span>
    <span class="pill pill-req" data-de="Auf Anfrage verf&uuml;gbar" data-en="Available on request">Auf Anfrage verf&uuml;gbar</span>
    <span class="pill pill-prep" data-de="In Vorbereitung" data-en="In preparation">In Vorbereitung</span>
    <span class="pill pill-run" data-de="Messkampagne l&auml;uft" data-en="Experimental campaign ongoing">Messkampagne l&auml;uft</span>
  </div>
</div></div>

<div class="sec sec-a" id="datensaetze"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Datens&auml;tze" data-en="Datasets">Datens&auml;tze</div>
    <h2 data-de="Ver&ouml;ffentlichte Datens&auml;tze" data-en="Published datasets">Ver&ouml;ffentlichte Datens&auml;tze</h2>
    <div class="sr"></div>
    <p class="de-block">Sechs Versuchsszenarien mit insgesamt 34.082 Schraubvorg&auml;ngen, ver&ouml;ffentlicht als Sammlung auf Zenodo (v1.2.3, Juli 2025) unter CC BY 4.0.</p>
    <p class="en-block" style="display:none">Six experimental scenarios with a total of 34,082 process recordings, published as a collection on Zenodo (v1.2.3, July 2025) under CC BY 4.0.</p>
  </div>
""" + "\n".join(ds_cards) + """

  <div class="dscard" id="ds-2026-01">
    <div class="dshead">
      <span class="dsid">DS-2026-01</span>
      <h3 data-de="INNO-SCREW Messkampagne 2026" data-en="INNO-SCREW measurement campaign 2026">INNO-SCREW Messkampagne 2026</h3>
      <span class="pill pill-run" data-de="Messkampagne l&auml;uft" data-en="Experimental campaign ongoing">Messkampagne l&auml;uft</span>
    </div>
    <div class="dsmeta">
      <div>
""" + "\n".join([
    meta_row("Datensatz-ID", "Dataset ID", "<code>DS-2026-01</code>"),
    meta_row("Schraubsysteme", "Screwdriving systems", "<code>ASS</code>, <code>RSS</code>, <code>KSS</code>"),
    meta_row("Versuchsszenario", "Experimental scenario", "In Definition", "Being defined"),
    meta_row("Stichprobenumfang", "Number of samples", "Laufend", "Ongoing"),
    meta_row("Abweichungsarten", "Process deviation types",
             "Cross-threading, Thread deformation, erh&ouml;htes Anziehdrehmoment, weitere in Abstimmung",
             "Cross-threading, thread deformation, increased tightening torque, further types under discussion"),
]) + """
      </div>
      <div>
""" + "\n".join([
    meta_row("Signale", "Available signals",
             "Drehmoment, Drehwinkel, Zeit", "Torque, angle, time"),
    meta_row("Datenformat", "Data format", "JSON / CSV"),
    meta_row("Lizenz", "Licence", "Vorgesehen: CC BY 4.0", "Planned: CC BY 4.0"),
    meta_row("DOI", "DOI", "Noch nicht vergeben", "Not yet assigned"),
    meta_row("Verf&uuml;gbarkeit", "Availability",
             "Noch nicht ver&ouml;ffentlicht &mdash; Anfragen &uuml;ber das Projektteam",
             "Not yet published &mdash; enquiries via the project team"),
]) + """
      </div>
    </div>
    <div class="dsfoot">
      <a href="contact.html" class="btn btn-b btn-sm" data-de="Anfrage stellen" data-en="Make an enquiry">Anfrage stellen</a>
    </div>
  </div>

  <div class="note" style="max-width:940px;margin:2rem auto 0">
    <span class="de-block">Daten, die hier nicht als <em>ver&ouml;ffentlicht</em> gekennzeichnet sind, stehen noch nicht zum Download bereit. Zwischenst&auml;nde k&ouml;nnen auf Anfrage und im Rahmen von Forschungskooperationen zug&auml;nglich gemacht werden.</span>
    <span class="en-block" style="display:none">Data not marked as <em>published</em> here are not yet available for download. Interim results can be made accessible on request and within research collaborations.</span>
  </div>
</div></div>

<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Terminologie" data-en="Terminology">Terminologie</div>
    <h2 data-de="Abweichungsarten" data-en="Process deviation types">Abweichungsarten</h2>
    <div class="sr"></div>
    <p class="de-block">In den Datens&auml;tzen und Publikationen werden durchgehend die folgenden Bezeichnungen verwendet.</p>
    <p class="en-block" style="display:none">The following designations are used consistently across datasets and publications.</p>
  </div>
  <div class="tscroll" style="max-width:820px;margin:0 auto">
    <table class="dtable">
      <thead><tr>
        <th data-de="Bezeichnung" data-en="Term">Bezeichnung</th>
        <th data-de="Deutsch" data-en="German">Deutsch</th>
        <th data-de="Beschreibung" data-en="Description">Beschreibung</th>
      </tr></thead>
      <tbody>
        <tr><td><strong>Cross-threading</strong></td><td>Schr&auml;geinschraubung</td>
          <td><span class="de-block">Schraube wird nicht achsparallel angesetzt und schneidet ein zweites Gewinde.</span><span class="en-block" style="display:none">The screw is not started coaxially and cuts a second thread.</span></td></tr>
        <tr><td><strong>Thread deformation</strong></td><td>Gewindeverformung</td>
          <td><span class="de-block">Bleibende Verformung des Gewindes, meist durch wiederholtes Verschrauben.</span><span class="en-block" style="display:none">Permanent deformation of the thread, usually caused by repeated fastening.</span></td></tr>
        <tr><td><strong>Increased tightening torque</strong></td><td>Erh&ouml;htes Anziehdrehmoment</td>
          <td><span class="de-block">Abschaltdrehmoment oberhalb der Sollvorgabe.</span><span class="en-block" style="display:none">Shut-off torque above the specified set point.</span></td></tr>
        <tr><td><strong>OK / NOK</strong></td><td>OK / NOK</td>
          <td><span class="de-block">Einheitliche Bewertung eines Schraubvorgangs. Die Bezeichnungen IO/NIO werden nicht mehr verwendet.</span><span class="en-block" style="display:none">Uniform assessment of a screwdriving process. The designations IO/NIO are no longer used.</span></td></tr>
      </tbody>
    </table>
  </div>
</div></div>

<div class="sec sec-a"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Zugang" data-en="Access">Zugang</div>
    <h2 data-de="Datenzugriff" data-en="Accessing the data">Datenzugriff</h2>
    <div class="sr"></div>
  </div>
  <div class="cards" style="max-width:900px;margin:0 auto">
    <div class="card">
      <div class="cico">&#128202;</div>
      <h3>Zenodo</h3>
      <p class="de-block">Direkter Download der vollst&auml;ndigen Datensatzsammlung mit Dokumentation, Version v1.2.3 (Juli 2025), Lizenz CC BY 4.0.</p>
      <p class="en-block" style="display:none">Direct download of the complete dataset collection including documentation, version v1.2.3 (July 2025), licence CC BY 4.0.</p>
      <div style="margin-top:1rem"><a href="%s" target="_blank" rel="noopener" class="btn btn-b btn-sm">10.5281/zenodo.16031381</a></div>
    </div>
    <div class="card">
      <div class="cico">&#128187;</div>
      <h3>PyScrew</h3>
      <p class="de-block">Python-Bibliothek f&uuml;r den strukturierten Zugriff auf die Datens&auml;tze, inklusive Download, Vorverarbeitung und Anbindung an g&auml;ngige ML-Frameworks.</p>
      <p class="en-block" style="display:none">Python library for structured access to the datasets, including download, preprocessing and integration with common ML frameworks.</p>
      <div style="margin-top:.7rem"><code style="background:var(--bg2);padding:.2rem .5rem;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:.78rem">pip install pyscrew</code></div>
      <div style="margin-top:1rem;display:flex;gap:.5rem;flex-wrap:wrap">
        <a href="https://github.com/nikolaiwest/pyscrew" target="_blank" rel="noopener" class="btn btn-b btn-sm">GitHub</a>
        <a href="https://pypi.org/project/pyscrew/" target="_blank" rel="noopener" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)">PyPI</a>
      </div>
    </div>
    <div class="card">
      <div class="cico">&#9993;&#65039;</div>
      <h3 data-de="Anfrage" data-en="Enquiry">Anfrage</h3>
      <p class="de-block">F&uuml;r noch nicht ver&ouml;ffentlichte Messkampagnen und f&uuml;r Forschungskooperationen wenden Sie sich bitte an das Projektteam.</p>
      <p class="en-block" style="display:none">For measurement campaigns that are not yet published and for research collaborations, please contact the project team.</p>
      <div style="margin-top:1rem"><a href="contact.html" class="btn btn-b btn-sm" data-de="Kontakt" data-en="Contact">Kontakt</a></div>
    </div>
  </div>
  <div class="note" style="max-width:900px;margin:2rem auto 0">
    <span class="de-block"><strong>Zitierhinweis:</strong> West, N.; Deuse, J. (2025): <em>Industrial screw driving dataset collection &mdash; time series data for process monitoring and anomaly detection.</em> Zenodo, v1.2.3. DOI: 10.5281/zenodo.16031381</span>
    <span class="en-block" style="display:none"><strong>How to cite:</strong> West, N.; Deuse, J. (2025): <em>Industrial screw driving dataset collection &mdash; time series data for process monitoring and anomaly detection.</em> Zenodo, v1.2.3. DOI: 10.5281/zenodo.16031381</span>
  </div>
</div></div>
""" % ZEN

page("data.html", "Forschungsdaten &mdash; INNO-SCREW",
     "Offene Forschungsdaten von INNO-SCREW: Datensatz-IDs, Szenarien, Metadaten, Lizenz, DOI und Verfuegbarkeitsstatus.",
     data_page)

# --------------------------------------------------------------------------
# PUBLICATIONS
# --------------------------------------------------------------------------

PUBS = [
    dict(key="p1", year="2025",
         title="Multi-Class Error Detection in Industrial Screw Driving Operations Using Machine Learning",
         authors="West, N.; Schlegl, T.; Deuse, J.",
         venue="Engineering Proceedings, 101(1), 15 &mdash; ITISE 2025",
         tags=["Multi-class classification", "Anomaly detection", "S04"],
         links=[("DOI", "https://doi.org/10.3390/engproc2025101015")],
         bib="@article{west2025multiclass,\\n  title   = {Multi-Class Error Detection in Industrial Screw Driving Operations Using Machine Learning},\\n  author  = {West, Nikolai and Schlegl, Thomas and Deuse, Jochen},\\n  journal = {Engineering Proceedings},\\n  volume  = {101},\\n  number  = {1},\\n  pages   = {15},\\n  year    = {2025},\\n  doi     = {10.3390/engproc2025101015}\\n}"),
    dict(key="p2", year="2025",
         title="PyScrew: A Comprehensive Dataset Collection from Industrial Screw Driving Experiments",
         authors="West, N.; Deuse, J.",
         venue="arXiv preprint arXiv:2505.11925 [cs.LG], Mai 2025",
         tags=["Open data", "S01 &ndash; S06", "PyScrew"],
         links=[("PDF", "https://arxiv.org/pdf/2505.11925"),
                ("DOI", "https://doi.org/10.48550/arXiv.2505.11925")],
         bib="@misc{west2025pyscrew,\\n  title         = {PyScrew: A Comprehensive Dataset Collection from Industrial Screw Driving Experiments},\\n  author        = {West, Nikolai and Deuse, Jochen},\\n  year          = {2025},\\n  eprint        = {2505.11925},\\n  archivePrefix = {arXiv},\\n  primaryClass  = {cs.LG},\\n  doi           = {10.48550/arXiv.2505.11925}\\n}"),
    dict(key="p3", year="2024",
         title="Detection of Surface-Based Anomalies for Self-Tapping Screws in Plastic Housings Using Supervised Machine Learning",
         authors="West, N.; Trianni, A.; Deuse, J.",
         venue="51st International Conference on Computers and Industrial Engineering (CIE51), S. 1&ndash;10, Dez. 2024",
         tags=["Surface friction", "Supervised ML", "S02"],
         links=[],
         bib="@inproceedings{west2024surface,\\n  title     = {Detection of Surface-Based Anomalies for Self-Tapping Screws in Plastic Housings Using Supervised Machine Learning},\\n  author    = {West, Nikolai and Trianni, Andrea and Deuse, Jochen},\\n  booktitle = {Proceedings of the 51st International Conference on Computers and Industrial Engineering (CIE51)},\\n  pages     = {1--10},\\n  year      = {2024}\\n}"),
    dict(key="p4", year="2024",
         title="A Comparative Study of Machine Learning Approaches for Anomaly Detection in Industrial Screw Driving Data",
         authors="West, N.; Deuse, J.",
         venue="57th Hawaii International Conference on System Sciences (HICSS 2024), S. 1050&ndash;1059",
         tags=["Unsupervised ML", "DBSCAN", "Random Forest"],
         links=[("PDF", "https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1568&context=hicss-57"),
                ("DOI", "https://hdl.handle.net/10125/106504")],
         bib="@inproceedings{west2024comparative,\\n  title     = {A Comparative Study of Machine Learning Approaches for Anomaly Detection in Industrial Screw Driving Data},\\n  author    = {West, Nikolai and Deuse, Jochen},\\n  booktitle = {Proceedings of the 57th Hawaii International Conference on System Sciences (HICSS)},\\n  pages     = {1050--1059},\\n  year      = {2024},\\n  url       = {https://hdl.handle.net/10125/106504}\\n}"),
    dict(key="p5", year="2023",
         title="Unsupervised Anomaly Detection in Unbalanced Time Series Data from Screw Driving Processes Using k-Means Clustering",
         authors="West, N.; Schlegl, T.; Deuse, J.",
         venue="Procedia CIRP &mdash; CIRP CMS 2023",
         tags=["k-Means", "Unsupervised", "Time series"],
         links=[("DOI", "https://doi.org/10.1016/j.procir.2023.08.878")],
         bib="@article{west2023kmeans,\\n  title   = {Unsupervised Anomaly Detection in Unbalanced Time Series Data from Screw Driving Processes Using k-Means Clustering},\\n  author  = {West, Nikolai and Schlegl, Thomas and Deuse, Jochen},\\n  journal = {Procedia CIRP},\\n  year    = {2023},\\n  doi     = {10.1016/j.procir.2023.08.878}\\n}"),
]

pub_items = []
for p in PUBS:
    acts = "".join(
        '<a class="pbtn" href="%s" target="_blank" rel="noopener">%s</a>' % (url, label)
        for label, url in p["links"])
    acts += '<button class="pbtn" onclick="dlBib(\'%s\')">BibTeX</button>' % p["key"]
    tags = "".join('<span class="tag">%s</span>' % t for t in p["tags"])
    pub_items.append("""    <div class="pi">
      <div class="py">%s</div>
      <div class="pm">
        <h4>%s</h4>
        <div class="pau">%s</div>
        <div class="pve">%s</div>
        <div class="ptags">%s</div>
      </div>
      <div class="pact">%s</div>
    </div>""" % (p["year"], p["title"], p["authors"], p["venue"], tags, acts))

bib_js = "var BIB={%s};" % ",".join('"%s":"%s"' % (p["key"], p["bib"]) for p in PUBS)

pubs_page = phdr("Publikationen", "Publications",
                 "Wissenschaftliche Ver&ouml;ffentlichungen, Vorarbeiten und Open-Source-Software",
                 "Scientific publications, preliminary work and open-source software") + """
<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk">INNO-SCREW</div>
    <h2 data-de="Publikationen aus dem Projekt" data-en="Publications from the project">Publikationen aus dem Projekt</h2>
    <div class="sr"></div>
    <p class="de-block">Ver&ouml;ffentlichungen, die unmittelbar aus INNO-SCREW hervorgehen.</p>
    <p class="en-block" style="display:none">Publications resulting directly from INNO-SCREW.</p>
  </div>
  <div style="background:var(--cd);border:1px solid var(--bd);border-radius:var(--r);padding:2.2rem;box-shadow:var(--sh);text-align:center;max-width:680px;margin:0 auto">
    <span class="pill pill-prep" data-de="In Vorbereitung" data-en="In preparation">In Vorbereitung</span>
    <p class="de-block" style="color:var(--mu);font-size:.93rem;line-height:1.8;margin:1rem 0 0">
      Publikationen aus dem Projekt INNO-SCREW befinden sich derzeit in Vorbereitung. Sie werden hier
      erg&auml;nzt, sobald sie ver&ouml;ffentlicht sind.</p>
    <p class="en-block" style="display:none;color:var(--mu);font-size:.93rem;line-height:1.8;margin:1rem 0 0">
      Publications from the INNO-SCREW project are currently in preparation. They will be added here
      once they have appeared.</p>
  </div>
</div></div>

<div class="sec sec-a"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Vorarbeiten" data-en="Related research">Vorarbeiten</div>
    <h2 data-de="Vorarbeiten und verwandte Forschung" data-en="Preliminary and related research">Vorarbeiten und verwandte Forschung</h2>
    <div class="sr"></div>
    <p class="de-block">Peer-reviewed Ver&ouml;ffentlichungen und Preprints aus Vorprojekten, die die methodische Grundlage von INNO-SCREW bilden.</p>
    <p class="en-block" style="display:none">Peer-reviewed publications and preprints from predecessor projects that form the methodological foundation of INNO-SCREW.</p>
  </div>
  <div class="plist">
""" + "\n".join(pub_items) + """
  </div>
</div></div>

<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Software" data-en="Software">Software</div>
    <h2 data-de="Open-Source-Software" data-en="Open-source software">Open-Source-Software</h2>
    <div class="sr"></div>
  </div>
  <div class="cards" style="max-width:820px;margin:0 auto">
    <div class="card">
      <div class="cico">&#128187;</div>
      <h3>PyScrew</h3>
      <p class="de-block">Python-Bibliothek f&uuml;r den strukturierten Zugriff auf die Datens&auml;tze des Projekts: automatisiertes Laden, Vorverarbeitung und Anbindung an g&auml;ngige ML-Frameworks.</p>
      <p class="en-block" style="display:none">Python library for structured access to the project datasets: automated download, preprocessing and integration with common ML frameworks.</p>
      <div style="margin-top:.7rem"><code style="background:var(--bg2);padding:.2rem .5rem;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:.78rem">pip install pyscrew</code></div>
      <div style="margin-top:1rem;display:flex;gap:.5rem;flex-wrap:wrap">
        <a href="https://github.com/nikolaiwest/pyscrew" target="_blank" rel="noopener" class="btn btn-b btn-sm">GitHub</a>
        <a href="https://pypi.org/project/pyscrew/" target="_blank" rel="noopener" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)">PyPI</a>
      </div>
    </div>
    <div class="card">
      <div class="cico">&#128451;&#65039;</div>
      <h3 data-de="Forschungsdaten" data-en="Research data">Forschungsdaten</h3>
      <p class="de-block">Die Datens&auml;tze des Projekts werden mit vollst&auml;ndigen Metadaten, Lizenz-, DOI- und Statusangaben auf einer eigenen Seite gef&uuml;hrt.</p>
      <p class="en-block" style="display:none">The project datasets are documented on a dedicated page with full metadata, licence, DOI and availability status.</p>
      <div style="margin-top:1rem"><a href="data.html" class="btn btn-b btn-sm" data-de="Zu den Forschungsdaten" data-en="Go to research data">Zu den Forschungsdaten</a></div>
    </div>
  </div>
</div></div>

<script>
""" + bib_js + """
function dlBib(key){
  var bib = BIB[key];
  if(!bib) return;
  var a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([bib], {type:"text/plain"}));
  a.download = "INNO-SCREW_" + key + ".bib";
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
}
</script>
"""

page("publications.html", "Publikationen &mdash; INNO-SCREW",
     "Publikationen aus INNO-SCREW, Vorarbeiten zur Anomalieerkennung in Schraubprozessen und die Open-Source-Bibliothek PyScrew.",
     pubs_page)

# --------------------------------------------------------------------------
# NEWS  (chronological, categorised)
# --------------------------------------------------------------------------

CATS = [
    ("all", "Alle", "All"),
    ("update", "Projektupdate", "Project Update"),
    ("dataset", "Datenver&ouml;ffentlichung", "Dataset Release"),
    ("publication", "Publikation", "Publication"),
    ("conference", "Konferenz", "Conference"),
    ("transfer", "Industrietransfer", "Industry Transfer"),
    ("infrastructure", "Infrastruktur", "Infrastructure"),
]

CATLABEL = {c[0]: (c[1], c[2]) for c in CATS}

NEWS = [
    dict(id="ein-jahr-inno-screw", cat="update", date_de="01. Dezember 2025", date_en="1 December 2025",
         title_de="Ein Jahr INNO-SCREW", title_en="One year of INNO-SCREW",
         body_de="""<p>Nach einem Jahr Projektlaufzeit ist die experimentelle Infrastruktur f&uuml;r alle f&uuml;nf
         Schraubsysteme aufgebaut. Die ersten Versuchsszenarien wurden auf Zenodo ver&ouml;ffentlicht und
         stehen der Forschungsgemeinschaft offen zur Verf&uuml;gung.</p>
         <p>Zu den Zwischenergebnissen z&auml;hlen die Ver&ouml;ffentlichung der Datenbibliothek PyScrew auf
         GitHub und PyPI, die Einreichung von zwei Konferenzbeitr&auml;gen sowie die Vorstellung des
         Vorhabens auf der SchraubTec Landshut. Die Datenbasis umfasst 34.082 aufgezeichnete
         Schraubvorg&auml;nge aus sechs Versuchsszenarien.</p>
         <p>Im zweiten Projektjahr liegt der Schwerpunkt auf der Entwicklung und Bewertung
         machine-learning-basierter Erkennungsverfahren sowie auf einem einheitlichen
         Benchmark-Protokoll f&uuml;r die Forschungsgemeinschaft.</p>""",
         body_en="""<p>After one year, the experimental infrastructure for all five screwdriving systems
         is in place. The first experimental scenarios have been published on Zenodo and are openly
         available to the research community.</p>
         <p>Interim results include the release of the PyScrew data library on GitHub and PyPI, the
         submission of two conference papers, and the presentation of the project at SchraubTec
         Landshut. The data basis comprises 34,082 recorded screwdriving processes across six
         experimental scenarios.</p>
         <p>In the second project year the focus lies on developing and evaluating machine-learning-based
         detection methods and on a uniform benchmark protocol for the research community.</p>""",
         links=[("publications.html", "Publikationen", "Publications"),
                ("data.html", "Forschungsdaten", "Research data")]),
    dict(id="dataset-v123", cat="dataset", date_de="Juli 2025", date_en="July 2025",
         title_de="Datensatzsammlung v1.2.3 auf Zenodo ver&ouml;ffentlicht",
         title_en="Dataset collection v1.2.3 released on Zenodo",
         body_de="""<p>Die Sammlung <em>Industrial Screw Driving Dataset Collection</em> ist in der Version
         v1.2.3 auf Zenodo verf&uuml;gbar. Sie umfasst sechs Versuchsszenarien (S01 bis S06) mit
         insgesamt 34.082 Schraubvorg&auml;ngen, aufgezeichnet mit 833,33 Hz.</p>
         <p>Die Daten enthalten Drehmoment-, Drehwinkel- und Zeitverl&auml;ufe sowie OK/NOK-Labels und
         Metadaten zu den Versuchsbedingungen. Die Ver&ouml;ffentlichung steht unter CC BY 4.0 und ist
         &uuml;ber den DOI 10.5281/zenodo.16031381 zitierbar.</p>""",
         body_en="""<p>The <em>Industrial Screw Driving Dataset Collection</em> is available on Zenodo in
         version v1.2.3. It comprises six experimental scenarios (S01 to S06) with a total of 34,082
         process recordings, sampled at 833.33 Hz.</p>
         <p>The data contain torque, angle and time curves as well as OK/NOK labels and metadata on the
         experimental conditions. The release is licensed under CC BY 4.0 and citable via the DOI
         10.5281/zenodo.16031381.</p>""",
         links=[("data.html#datensaetze", "Datensatz-Metadaten", "Dataset metadata"),
                ("https://doi.org/10.5281/zenodo.16031381", "Zenodo", "Zenodo")]),
    dict(id="pyscrew-preprint", cat="publication", date_de="Mai 2025", date_en="May 2025",
         title_de="Preprint zur Datensatzsammlung PyScrew erschienen",
         title_en="Preprint on the PyScrew dataset collection published",
         body_de="""<p>Der Preprint <em>PyScrew: A Comprehensive Dataset Collection from Industrial Screw
         Driving Experiments</em> von West und Deuse beschreibt Aufbau, Versuchsbedingungen und
         Struktur der ver&ouml;ffentlichten Datens&auml;tze.</p>
         <p>Beschrieben werden sechs Szenarien zu Gewindesch&auml;digung, Oberfl&auml;chenreibung,
         Montagebedingungen sowie fertigungsbedingter Bauteilvarianz. Der Preprint ist &uuml;ber arXiv
         frei zug&auml;nglich.</p>""",
         body_en="""<p>The preprint <em>PyScrew: A Comprehensive Dataset Collection from Industrial Screw
         Driving Experiments</em> by West and Deuse describes the setup, experimental conditions and
         structure of the published datasets.</p>
         <p>It covers six scenarios on thread degradation, surface friction, assembly conditions and
         manufacturing-related workpiece variation. The preprint is openly available via arXiv.</p>""",
         links=[("https://arxiv.org/abs/2505.11925", "arXiv 2505.11925", "arXiv 2505.11925"),
                ("publications.html", "Publikationen", "Publications")]),
    dict(id="schraubtec-2025", cat="conference", date_de="16. Mai 2025", date_en="16 May 2025",
         title_de="SchraubTec Landshut 2025", title_en="SchraubTec Landshut 2025",
         body_de="""<p>Das Projektteam war mit einem Beitrag auf der SchraubTec Landshut 2025 vertreten,
         einer Fachveranstaltung f&uuml;r Schraubtechnik im deutschsprachigen Raum. Die Veranstaltung
         bot die Gelegenheit, Projektziele und Zwischenergebnisse einem Fachpublikum aus der Industrie
         vorzustellen.</p>
         <p>Im Mittelpunkt der Gespr&auml;che standen die offenen Schraubdatens&auml;tze sowie der Ansatz,
         datengetriebene Qualit&auml;tssicherung in industriellen Produktionsumgebungen einzusetzen.
         Mehrere Kontakte zu Industriepartnern wurden f&uuml;r die praxisnahe Validierung der Verfahren
         angekn&uuml;pft.</p>""",
         body_en="""<p>The project team presented at SchraubTec Landshut 2025, a specialist event for screw
         fastening technology in the German-speaking region. The event provided an opportunity to
         present the project objectives and interim results to a specialist industrial audience.</p>
         <p>Discussions centred on the open screwdriving datasets and on the approach of applying
         data-driven quality assurance in industrial production environments. Several contacts with
         industrial partners were established for practical validation of the methods.</p>""",
         links=[("infrastructure.html", "Forschungsinfrastruktur", "Research infrastructure")]),
    dict(id="projektstart", cat="update", date_de="01. Januar 2025", date_en="1 January 2025",
         title_de="Projektstart INNO-SCREW", title_en="INNO-SCREW project launch",
         body_de="""<p>Mit dem INNO-KOM-Vorhaben INNO-SCREW beginnt der Aufbau eines Innovationszentrums
         f&uuml;r intelligentes Qualit&auml;tsmanagement in industriellen Schraubprozessen. Das Projekt
         wird am RIF Institut f&uuml;r Forschung und Transfer e.V. in Kooperation mit dem Institut
         f&uuml;r Produktionssysteme der TU Dortmund durchgef&uuml;hrt.</p>
         <p>Die ersten Arbeitspakete umfassen die Definition der Anforderungen, die technische
         Ert&uuml;chtigung der Schraubsysteme sowie den Aufbau der Datenerfassungsinfrastruktur.</p>""",
         body_en="""<p>With the INNO-KOM project INNO-SCREW, work begins on an innovation centre for
         intelligent quality management in industrial screwdriving processes. The project is carried out
         at RIF Institut f&uuml;r Forschung und Transfer e.V. in cooperation with the Institute of
         Production Systems at TU Dortmund.</p>
         <p>The first work packages cover the definition of requirements, the technical refurbishment of
         the screwdriving systems and the setup of the data acquisition infrastructure.</p>""",
         links=[("project.html", "Zum Projekt", "About the project")]),
]

filters = "\n".join(
    '    <button class="nfbtn%s" data-cat="%s" data-de="%s" data-en="%s">%s</button>'
    % (" on" if c[0] == "all" else "", c[0], c[1], c[2], c[1]) for c in CATS)

entries = []
for n in NEWS:
    cde, cen = CATLABEL[n["cat"]]
    btns = "".join(
        '<a href="%s" class="btn btn-sm" style="background:var(--bg2);border:1px solid var(--bd);color:var(--mu)" data-de="%s" data-en="%s"%s>%s</a>'
        % (href, lde, len_, ' target="_blank" rel="noopener"' if href.startswith("http") else "", lde)
        for href, lde, len_ in n["links"])
    entries.append("""  <article class="nentry" id="%s" data-cat="%s">
    <div class="nm"><span>%s</span><span class="en-block" style="display:none">%s</span> &middot; RIF e.V. &middot; <span class="ncat" data-de="%s" data-en="%s">%s</span></div>
    <h2 data-de="%s" data-en="%s">%s</h2>
    <div class="prose de-block">%s</div>
    <div class="prose en-block" style="display:none">%s</div>
    <div style="margin-top:1.4rem;display:flex;gap:.6rem;flex-wrap:wrap">%s</div>
  </article>""" % (n["id"], n["cat"],
                   '<span class="de-block">%s</span>' % n["date_de"], n["date_en"],
                   cde, cen, cde,
                   n["title_de"], n["title_en"], n["title_de"],
                   n["body_de"], n["body_en"], btns))

news_page = phdr("Aktuelles", "News",
                 "Chronologischer &Uuml;berblick &uuml;ber den Projektfortschritt von INNO-SCREW",
                 "Chronological overview of progress in the INNO-SCREW project") + """
<div class="sec"><div class="wrap" style="max-width:840px">
  <div class="nfilter">
%s
  </div>
%s
  <div class="note" style="margin-top:2.5rem">
    <span class="de-block">Der Projektfortschritt wird hier fortlaufend dokumentiert. Eine kompakte
    Zusammenfassung des aktuellen Stands findet sich im <a href="index.html#status" style="color:var(--bl2)">Projektstatus</a>.</span>
    <span class="en-block" style="display:none">Project progress is documented here on an ongoing basis.
    A compact summary of the current state is available under <a href="index.html#status" style="color:var(--bl2)">project status</a>.</span>
  </div>
</div></div>
""" % (filters, "\n".join(entries))

page("news.html", "Aktuelles &mdash; INNO-SCREW",
     "Chronologischer Ueberblick ueber Projektfortschritt, Datenveroeffentlichungen, Publikationen und Konferenzbeitraege von INNO-SCREW.",
     news_page)

# --------------------------------------------------------------------------
# CONTACT
# --------------------------------------------------------------------------

contact = phdr("Kontakt", "Contact",
               "Ansprechpartner und Kontaktdaten des Projekts INNO-SCREW",
               "Contact persons and details for the INNO-SCREW project") + """
<div class="sec"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="Ansprechpartner" data-en="Contacts">Ansprechpartner</div>
    <h2 data-de="Projektteam" data-en="Project team">Projektteam</h2>
    <div class="sr"></div>
  </div>
  <div class="cards">
    <div class="card" style="border-top:3px solid var(--gd3)">
      <img src="assets/team-henkies.jpg" alt="Michelle Henkies" style="width:100%;height:200px;object-fit:cover;object-position:center top;border-radius:8px;margin-bottom:1rem;display:block">
      <h3>Michelle Henkies, M.Sc.</h3>
      <div style="font-size:.78rem;color:var(--gd2);font-weight:700;margin:.25rem 0 .7rem">Projektleitung &middot; RIF Institut</div>
      <p style="font-size:.875rem" class="de-block">Erste Ansprechpartnerin f&uuml;r inhaltliche Fragen zu INNO-SCREW, zur Forschungsinfrastruktur und zu Kooperationsanfragen.</p>
      <p style="font-size:.875rem;display:none" class="en-block">Primary contact for scientific enquiries about INNO-SCREW, the research infrastructure and collaboration requests.</p>
      <div style="display:flex;flex-direction:column;gap:.5rem;margin-top:1.1rem;font-size:.86rem">
        <a href="mailto:michelle.henkies@rif-ev.de" style="color:var(--bl2);text-decoration:none">&#9993; michelle.henkies@rif-ev.de</a>
        <a href="https://orcid.org/0000-0002-5095-5141" target="_blank" rel="noopener" style="color:var(--bl2);text-decoration:none">ORCID 0000-0002-5095-5141</a>
        <a href="https://ips.mb.tu-dortmund.de/ueber-uns/team/michelle-henkies/" target="_blank" rel="noopener" style="color:var(--bl2);text-decoration:none">IPS-Profil</a>
      </div>
    </div>
    <div class="card" style="border-top:3px solid var(--bl2)">
      <img src="assets/team-mura.jpg" alt="Robert Mura" style="width:100%;height:200px;object-fit:cover;object-position:center top;border-radius:8px;margin-bottom:1rem;display:block">
      <h3>Robert Mura, M.Sc.</h3>
      <div style="font-size:.78rem;color:var(--bl2);font-weight:700;margin:.25rem 0 .7rem">Projektbearbeitung &middot; RIF Institut</div>
      <p style="font-size:.875rem" class="de-block">Ansprechpartner f&uuml;r die Versuchsdurchf&uuml;hrung, die Datenerfassung an den Schraubsystemen und die Aufbereitung der Messdaten.</p>
      <p style="font-size:.875rem;display:none" class="en-block">Contact for the execution of trials, data acquisition at the screwdriving systems and preparation of the measurement data.</p>
      <div style="display:flex;flex-direction:column;gap:.5rem;margin-top:1.1rem;font-size:.86rem">
        <a href="mailto:robert.mura@rif-ev.de" style="color:var(--bl2);text-decoration:none">&#9993; robert.mura@rif-ev.de</a>
        <a href="https://orcid.org/0009-0003-6032-6556" target="_blank" rel="noopener" style="color:var(--bl2);text-decoration:none">ORCID 0009-0003-6032-6556</a>
        <a href="https://ips.mb.tu-dortmund.de/ueber-uns/team/robert-mura/" target="_blank" rel="noopener" style="color:var(--bl2);text-decoration:none">IPS-Profil</a>
      </div>
    </div>
    <div class="card">
      <img src="assets/team-deuse.jpg" alt="Univ.-Prof. Dr.-Ing. Jochen Deuse" style="width:100%;height:200px;object-fit:cover;object-position:center top;border-radius:8px;margin-bottom:1rem;display:block">
      <h3>Univ.-Prof. Dr.-Ing. Jochen Deuse</h3>
      <div style="font-size:.78rem;color:var(--bl2);font-weight:700;margin:.25rem 0 .7rem">Institutsleitung &middot; IPS TU Dortmund</div>
      <p style="font-size:.875rem" class="de-block">Wissenschaftliche Gesamtverantwortung f&uuml;r INNO-SCREW. Forschungsschwerpunkte: Industrial Data Science, Smart Quality, Produktionssystemgestaltung.</p>
      <p style="font-size:.875rem;display:none" class="en-block">Overall scientific responsibility for INNO-SCREW. Research focus: Industrial Data Science, Smart Quality, production system design.</p>
      <div style="display:flex;flex-direction:column;gap:.5rem;margin-top:1.1rem;font-size:.86rem">
        <a href="mailto:sekretariat.ips.mb@tu-dortmund.de" style="color:var(--bl2);text-decoration:none">&#9993; sekretariat.ips.mb@tu-dortmund.de</a>
        <a href="https://ips.mb.tu-dortmund.de/en/about-us/team/jochen-deuse/" target="_blank" rel="noopener" style="color:var(--bl2);text-decoration:none">IPS-Profil</a>
        <a href="https://orcid.org/0000-0003-4066-4357" target="_blank" rel="noopener" style="color:var(--bl2);text-decoration:none">ORCID 0000-0003-4066-4357</a>
      </div>
    </div>
    <div class="card">
      <div class="cico">&#127968;</div>
      <h3 data-de="Institutskontakt" data-en="Institute contact">Institutskontakt</h3>
      <div style="font-size:.78rem;color:var(--bl2);font-weight:700;margin:.25rem 0 .7rem">RIF e.V. &middot; IPS TU Dortmund</div>
      <div style="display:flex;flex-direction:column;gap:.7rem;font-size:.875rem;color:var(--mu)">
        <div>
          <div style="font-weight:600;color:var(--tk);margin-bottom:.15rem">RIF Institut f&uuml;r Forschung und Transfer e.V.</div>
          Joseph-von-Fraunhofer-Str. 20<br>44227 Dortmund, Deutschland
        </div>
        <div>
          <div style="font-weight:600;color:var(--tk);margin-bottom:.15rem">Institut f&uuml;r Produktionssysteme (IPS)</div>
          Leonhard-Euler-Str. 5, 2. Etage (Einfahrt 4&ndash;7)<br>44227 Dortmund, Deutschland
        </div>
        <a href="mailto:inno-screw@rif-ev.de" style="color:var(--bl2);text-decoration:none">&#9993; inno-screw@rif-ev.de</a>
        <a href="https://ips.mb.tu-dortmund.de" target="_blank" rel="noopener" style="color:var(--bl2);text-decoration:none">ips.mb.tu-dortmund.de</a>
      </div>
    </div>
  </div>
</div></div>

<div class="sec sec-a"><div class="wrap">
  <div class="sh">
    <div class="skk" data-de="F&ouml;rderung" data-en="Funding">F&ouml;rderung</div>
    <h2 data-de="Projektdaten" data-en="Project details">Projektdaten</h2>
    <div class="sr"></div>
  </div>
  <div class="cards" style="max-width:940px;margin:0 auto">
    <div class="card">
      <div class="cico">&#128197;</div>
      <h3 data-de="Laufzeit" data-en="Duration">Laufzeit</h3>
      <p class="de-block">01. Dezember 2024 &ndash; 31. Mai 2027<br><span style="color:var(--fa);font-size:.83rem">30 Monate</span></p>
      <p class="en-block" style="display:none">1 December 2024 &ndash; 31 May 2027<br><span style="color:var(--fa);font-size:.83rem">30 months</span></p>
    </div>
    <div class="card">
      <div class="cico">&#127963;&#65039;</div>
      <h3 data-de="F&ouml;rderprogramm" data-en="Funding programme">F&ouml;rderprogramm</h3>
      <p class="de-block">Innovationskompetenz INNO-KOM<br><span style="color:var(--fa);font-size:.83rem">Bundesministerium f&uuml;r Wirtschaft und Energie (BMWE)<br>Projekttr&auml;ger: EURONORM GmbH, Berlin</span></p>
      <p class="en-block" style="display:none">Innovation Competence INNO-KOM<br><span style="color:var(--fa);font-size:.83rem">Federal Ministry for Economic Affairs and Energy (BMWE)<br>Project sponsor: EURONORM GmbH, Berlin</span></p>
    </div>
    <div class="card">
      <div class="cico">&#128101;</div>
      <h3 data-de="Durchf&uuml;hrende Einrichtungen" data-en="Executing institutions">Durchf&uuml;hrende Einrichtungen</h3>
      <p style="font-size:.875rem">RIF Institut f&uuml;r Forschung und Transfer e.V.<br><span style="color:var(--fa);font-size:.83rem">Abteilung Produktionssysteme, Dortmund</span></p>
      <p style="font-size:.875rem;margin-top:.55rem">TU Dortmund &mdash; Institut f&uuml;r Produktionssysteme (IPS)<br><span style="color:var(--fa);font-size:.83rem">Fakult&auml;t Maschinenbau</span></p>
      <div style="margin-top:.9rem"><a href="https://ips.mb.tu-dortmund.de/en/research-consult/research-projects/" target="_blank" rel="noopener" class="btn btn-b btn-sm">IPS-Projektseite</a></div>
    </div>
  </div>
</div></div>

<div class="sec"><div class="wrap" style="max-width:700px">
  <div class="sh">
    <div class="skk" data-de="Anfrage" data-en="Enquiry">Anfrage</div>
    <h2 data-de="Kontakt aufnehmen" data-en="Get in touch">Kontakt aufnehmen</h2>
    <div class="sr"></div>
    <p class="de-block">F&uuml;r Kooperationsanfragen, Datensatzanfragen oder technische R&uuml;ckfragen wenden Sie sich bitte an
    <a href="mailto:inno-screw@rif-ev.de" style="color:var(--bl2)">inno-screw@rif-ev.de</a> oder direkt an die oben genannten Ansprechpartner.</p>
    <p class="en-block" style="display:none">For collaboration requests, dataset enquiries or technical questions, please write to
    <a href="mailto:inno-screw@rif-ev.de" style="color:var(--bl2)">inno-screw@rif-ev.de</a> or contact the people listed above directly.</p>
  </div>
  <div style="text-align:center">
    <a href="mailto:inno-screw@rif-ev.de" class="btn btn-g" data-de="E-Mail schreiben" data-en="Send an e-mail">E-Mail schreiben</a>
  </div>
</div></div>

<div class="sec sec-a"><div class="wrap" style="max-width:780px">
  <div class="sh">
    <div class="skk" data-de="Rechtliches" data-en="Legal">Rechtliches</div>
    <h2 data-de="Impressum und Datenschutz" data-en="Legal notice and privacy">Impressum und Datenschutz</h2>
    <div class="sr"></div>
  </div>
  <div class="legal">
    <h3 id="impressum" data-de="Impressum" data-en="Legal notice">Impressum</h3>
    <p class="de-block"><strong>Verantwortlich f&uuml;r diese Website:</strong><br>
      RIF Institut f&uuml;r Forschung und Transfer e.V.<br>
      Joseph-von-Fraunhofer-Str. 20 &middot; 44227 Dortmund &middot; Deutschland<br>
      in Kooperation mit dem Institut f&uuml;r Produktionssysteme (IPS), TU Dortmund<br>
      Leonhard-Euler-Str. 5 &middot; 44227 Dortmund</p>
    <p class="en-block" style="display:none"><strong>Responsible for this website:</strong><br>
      RIF Institut f&uuml;r Forschung und Transfer e.V.<br>
      Joseph-von-Fraunhofer-Str. 20 &middot; 44227 Dortmund &middot; Germany<br>
      in cooperation with the Institute of Production Systems (IPS), TU Dortmund<br>
      Leonhard-Euler-Str. 5 &middot; 44227 Dortmund</p>
    <h3 id="datenschutz" data-de="Datenschutzhinweis" data-en="Privacy notice">Datenschutzhinweis</h3>
    <p class="de-block">Diese Website erhebt keine personenbezogenen Daten und setzt keine Cookies zu
      Analyse- oder Werbezwecken ein. Sprach- und Darstellungseinstellungen werden ausschlie&szlig;lich
      lokal im Browser gespeichert. Schriftarten werden von Google Fonts geladen; dabei wird die
      IP-Adresse an Google &uuml;bertragen. F&uuml;r Anfragen nutzen Sie bitte die angegebenen
      E-Mail-Adressen.</p>
    <p class="en-block" style="display:none">This website does not collect personal data and does not use
      cookies for analytics or advertising. Language and display settings are stored locally in the
      browser only. Fonts are loaded from Google Fonts, which transmits your IP address to Google. For
      enquiries, please use the e-mail addresses provided.</p>
    <h3 data-de="Haftungsausschluss" data-en="Disclaimer">Haftungsausschluss</h3>
    <p class="de-block">Trotz sorgf&auml;ltiger inhaltlicher Kontrolle &uuml;bernehmen wir keine Haftung
      f&uuml;r die Inhalte externer Links. F&uuml;r den Inhalt verlinkter Seiten sind ausschlie&szlig;lich
      deren Betreiber verantwortlich.</p>
    <p class="en-block" style="display:none">Despite careful review, we accept no liability for the content
      of external links. The operators of linked pages are solely responsible for their content.</p>
  </div>
</div></div>
"""

page("contact.html", "Kontakt &mdash; INNO-SCREW",
     "Ansprechpartner, Anschrift, Foerderdaten, Impressum und Datenschutzhinweis des Projekts INNO-SCREW.",
     contact)


# --------------------------------------------------------------------------
# Redirect stubs for the old URLs
# --------------------------------------------------------------------------

REDIRECTS = {
    "about.html": "project.html",
    "stations.html": "infrastructure.html",
    "station-s1.html": "station-ass.html",
    "station-s2.html": "station-rss.html",
    "station-s3.html": "station-mss.html",
    "station-s4.html": "station-dss.html",
    "station-s5.html": "station-kss.html",
    "demo.html": "index.html",
    "ap01.html": "project.html",
    "ap02.html": "project.html",
    "ap03.html": "project.html",
    "ap04.html": "project.html",
}

STUB = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="0; url=%(target)s">
<link rel="canonical" href="%(target)s">
<meta name="robots" content="noindex">
<title>INNO-SCREW</title>
</head>
<body style="font-family:system-ui,sans-serif;padding:3rem;text-align:center">
<p>Diese Seite wurde verschoben. / This page has moved.</p>
<p><a href="%(target)s">%(target)s</a></p>
<script>location.replace("%(target)s");</script>
</body>
</html>
"""

for old, new in REDIRECTS.items():
    with open(OUT + old, "w", encoding="utf-8") as fh:
        fh.write(STUB % {"target": new})
print("wrote %d redirect stubs" % len(REDIRECTS))
