from sitecfg import *  # noqa


def aside(current):
    links = "".join(
        f'<li><a href="/services/{s}/"{" aria-current=page" if s == current else ""}>{n}</a></li>'
        for s, n, _ in SERVICES_EN
    )
    return f'''<aside class="aside">
<div class="card"><h3 style="font-size:1.05rem">Services</h3><ul>{links}</ul></div>
<div class="card" style="background:var(--purple-50)"><h3 style="font-size:1.05rem">Speak to Steve</h3>
<p style="font-size:.93rem">Free initial consultation. Every enquiry is treated in confidence.</p>
<p style="margin:0"><a href="{PHONE_HREF}"><strong>{PHONE}</strong></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="card"><h3 style="font-size:1.05rem">Free e-book</h3><p style="font-size:.93rem">Steve's guide to party wall procedure, adjudication, mediation, arbitration and expert evidence.</p><a class="more" href="/e-book/">Read and download →</a></div>
</aside>'''


def service_page(slug, title, meta_title, meta_desc, lead, body_html, faqs):
    path = f"/services/{slug}/"
    crumbs = [("Home", "/"), ("Services", "/services/"), (title, path)]
    faq_html, faq_schema = faq(faqs)
    body = (page_hero(title, lead, crumbs, "Services")
            + f'<section><div class="wrap layout"><article class="prose">{body_html}</article>{aside(slug)}</div></section>'
            + faq_html + cta_band())
    return dict(lang="en", path=path, title=meta_title, description=meta_desc, body=body,
                alternates={"en-GB": path}, alt_path="/pt/servicos/",
                schemas=[service_schema(title, meta_desc, path), breadcrumb_schema(crumbs), faq_schema])


ROLES_NOTE = '''<div class="note"><p><strong>Independent appointment or party representation — never both.</strong> Steve may be appointed as the independent decision-maker in a dispute, or instructed to advise and represent one party. These are distinct roles. On any one matter he acts in one capacity only, and he will decline an instruction where there is a conflict of interest.</p></div>'''


def home():
    cards = "".join(
        f'<div class="card"><h3><a href="/services/{s}/">{n}</a></h3><p>{d}</p><a class="more" href="/services/{s}/" aria-label="More about {n}">Learn more →</a></div>'
        for s, n, d in SERVICES_EN
    )
    cards += '<div class="card" style="background:var(--purple-50)"><h3><a href="/portugal/">Projects in Portugal</a></h3><p>International arbitration, mediation and independent construction expertise for owners, investors and contractors with projects in Portugal.</p><a class="more" href="/portugal/">Learn more →</a></div>'
    faqs = [
        ("What is the difference between adjudication, arbitration and mediation?",
         "<p><strong>Adjudication</strong> is a fast statutory process for construction contracts: an adjudicator decides the dispute, usually within 28 days of referral, and the decision is binding until finally resolved by litigation, arbitration or agreement. <strong>Arbitration</strong> is a private alternative to court, based on an agreement to arbitrate; the arbitrator's award is final and binding, with very limited rights of challenge. <strong>Mediation</strong> is a confidential, facilitated negotiation — the mediator does not decide anything, and the parties are only bound if they sign a settlement.</p>"),
        ("Does Steve act as adjudicator and arbitrator, or does he represent parties?",
         "<p>Both, but never on the same matter. Steve accepts independent appointments as adjudicator, arbitrator, mediator, expert determiner and third surveyor, and he also advises and represents parties in adjudication, arbitration and mediation. The role is agreed at the outset of every instruction.</p>"),
        ("Who does Steve Campbell Associates act for?",
         "<p>Main contractors, subcontractors, house builders, developers and property owners, as well as construction professionals — architects, engineers, surveyors — and the solicitors, barristers and insurers who instruct them.</p>"),
        ("Do you work with clients outside the UK?",
         "<p>Yes. Steve is an international arbitrator (FCIArb) and accepts instructions from clients in Portugal and elsewhere, particularly on arbitration, mediation, expert evidence and construction consultancy. UK statutory procedures such as the Party Wall etc. Act 1996 and statutory adjudication apply only to work and contracts within their scope in the UK.</p>"),
        ("Is the first consultation free?",
         "<p>Yes. The initial consultation is free and confidential. If a formal appointment follows, terms and fees are confirmed in writing before any work begins.</p>"),
    ]
    faq_html, faq_schema = faq(faqs)
    body = f'''<section class="hero"><div class="wrap">
<div>
<p class="eyebrow">Chartered building consultancy · International dispute resolution</p>
<h1>Construction and property disputes, resolved by someone who has built.</h1>
<p class="lead">Steve Campbell Associates provides arbitration, adjudication, party wall surveying, mediation and expert witness services across England and Wales, with international arbitration and consultancy for clients in Portugal and beyond. Steve brings more than 40 years of construction experience — from the trades to site, project and construction management — to every dispute.</p>
<div class="actions"><a class="btn light" href="/contact/">Free initial consultation</a><a class="btn outline-light" href="/services/">View services</a></div>
<p class="motto">Sine timore vel favore — without fear or favour</p>
</div>
<div class="profile-card">
<picture><source srcset="/assets/img/steve-campbell.webp" type="image/webp"><img src="/assets/img/steve-campbell.jpg" width="120" height="120" alt="Steve Campbell, principal of Steve Campbell Associates" fetchpriority="high"></picture>
<h2>Steve Campbell</h2><p class="post">{POSTNOMS}</p>
<ul><li>Chartered Construction Manager</li><li>International Arbitrator &amp; Construction Adjudicator</li><li>Party Wall Surveyor &amp; Third Surveyor</li><li>Mediator &amp; Expert Witness</li></ul>
</div>
</div></section>

<section><div class="wrap">
<div class="section-head"><p class="eyebrow">Services</p><h2>Dispute resolution and consultancy for the construction and property sectors</h2>
<p>Each process has different rules, costs and outcomes. Choosing the right one — or avoiding a formal process altogether — is often the most valuable decision in a dispute.</p></div>
<div class="grid grid-3">{cards}</div>
</div></section>

<section class="section-alt"><div class="wrap split">
<div><p class="eyebrow">Experience</p><h2>Practical construction knowledge behind every decision</h2>
<p>Steve began his career building houses, extensions and commercial units, then progressed through site management, project management and construction direction. He has managed projects from around £10,000 to more than £80 million, under JCT, NEC, FIDIC and bespoke contracts, and is known for taking on difficult and distressed projects.</p>
<p>Since 2009 he has worked in dispute resolution as an adjudicator, arbitrator, mediator, party representative and expert witness, in the county court, the Technology and Construction Court, and in arbitrations, adjudications and mediations. He is regularly appointed as a third surveyor in party wall matters.</p>
<p><a href="/about/">More about Steve →</a></p></div>
<div><div class="stats">
<div class="stat"><b>40+</b><span>years in the construction industry</span></div>
<div class="stat"><b>£80m+</b><span>largest project managed</span></div>
<div class="stat"><b>2009</b><span>dispute resolution practice since</span></div>
<div class="stat"><b style="font-size:1.15rem">JCT · NEC · FIDIC</b><span>and bespoke contracts</span></div>
</div>
<h3 style="margin-top:34px">Professional bodies</h3>
<ul class="checklist"><li>Fellow, Chartered Institute of Arbitrators (FCIArb)</li><li>Fellow, Faculty of Party Wall Surveyors (FFPWS)</li><li>Member, Chartered Institute of Building (MCIOB)</li><li>Founding Fellow, Party Wall Academy</li><li>Member, Society of Construction Law</li><li>Member, Adjudication Society</li><li>Member, Pyramus and Thisbe Society</li></ul>
</div></div></section>

<section><div class="wrap split">
<div><p class="eyebrow">Who we act for</p><h2>Clients across the construction supply chain</h2>
<ul class="checklist"><li>Main contractors, subcontractors and specialist trades</li><li>Developers, house builders and commercial property owners</li><li>Building owners and adjoining owners under the Party Wall Act</li><li>Architects, engineers, quantity surveyors and project managers</li><li>Solicitors, barristers and insurers requiring independent expertise</li><li>Owners, investors and contractors with projects in Portugal</li></ul></div>
<div>{ROLES_NOTE}<p>Every instruction starts with the same question: what outcome does the client actually need, and what is the most proportionate route to it? Sometimes that is a formal process; often it is a well-prepared negotiation.</p></div>
</div></section>

<section class="section-alt"><div class="wrap split" style="align-items:center">
<div class="ebook-cover" aria-hidden="true"><img src="/assets/img/crest-white-96.png" width="84" height="84" alt=""><div><small>Free e-book</small><b>Party Wall, Adjudication &amp; Dispute Resolution</b></div><small>Steve Campbell Associates</small></div>
<div><p class="eyebrow">Free e-book</p><h2>A practical guide to construction dispute procedures</h2>
<p>Steve's e-book explains the Party Wall etc. Act 1996, construction adjudication, mediation, expert determination, arbitration, early neutral evaluation and the role of the expert witness — in plain terms, for owners and industry professionals.</p>
<div class="actions"><a class="btn" href="/e-book/">Read and download the e-book</a></div></div>
</div></section>
{faq_html}
{cta_band()}'''
    return dict(lang="en", path="/", title="Construction Arbitrator, Adjudicator & Party Wall Surveyor | SCA",
                description="Construction dispute resolution in the UK and internationally: arbitration, adjudication, party wall, mediation and expert witness. Steve Campbell FCIArb.",
                body=body, alternates={"en-GB": "/", "pt-PT": "/pt/"}, alt_path="/pt/",
                schemas=[person_schema(), faq_schema])


def services_index():
    crumbs = [("Home", "/"), ("Services", "/services/")]
    cards = "".join(
        f'<div class="card"><h2 style="font-size:1.3rem"><a href="/services/{s}/" style="text-decoration:none;color:var(--ink)">{n}</a></h2><p>{d}</p><a class="more" href="/services/{s}/">Learn more →</a></div>'
        for s, n, d in SERVICES_EN
    )
    body = (page_hero("Services", "Independent appointments, party representation and construction consultancy. Each service below explains how the process works, when it is appropriate and what Steve's role would be.", crumbs)
            + f'<section><div class="wrap"><div class="grid grid-3">{cards}</div>{ROLES_NOTE}</div></section>'
            + '''<section class="section-alt"><div class="wrap narrow prose"><h2>Choosing the right process</h2>
<p><strong>Need a quick, enforceable decision on a construction contract — usually about money?</strong> Statutory <a href="/services/adjudication/">adjudication</a> is designed for this. Decisions are usually given within 28 days of referral and are binding in the meantime.</p>
<p><strong>Need a final, private decision, possibly with an international element?</strong> <a href="/services/arbitration/">Arbitration</a> is available where the parties have agreed to it, and awards can be enforced internationally under the New York Convention.</p>
<p><strong>Want to preserve the commercial relationship and control the outcome?</strong> <a href="/services/mediation/">Mediation</a> is confidential and flexible, and can take place before or during formal proceedings.</p>
<p><strong>Is the dispute a narrow technical or valuation question?</strong> <a href="/services/expert-determination-and-early-neutral-evaluation/">Expert determination</a> can resolve it quickly; early neutral evaluation gives a non-binding view of the merits.</p>
<p><strong>Planning work to a shared wall, on a boundary or near a neighbour's foundations in England or Wales?</strong> The <a href="/services/party-wall-surveyor/">Party Wall etc. Act 1996</a> may require formal notice and, if there is a dispute, the appointment of surveyors.</p>
</div></section>''' + cta_band())
    return dict(lang="en", path="/services/", title="Construction Dispute Resolution Services | Steve Campbell",
                description="Adjudication, arbitration, party wall, mediation, expert determination, expert witness and claims consultancy — how each works and when to use it.",
                body=body, alternates={"en-GB": "/services/", "pt-PT": "/pt/servicos/"}, alt_path="/pt/servicos/",
                schemas=[breadcrumb_schema(crumbs)])


def adjudication():
    body = '''<h2>What is construction adjudication?</h2>
<p>Adjudication is a statutory dispute resolution procedure for construction contracts in the UK. It was introduced by Part II of the Housing Grants, Construction and Regeneration Act 1996 (the "Construction Act"), which came into force on 1 May 1998, and was amended in England and Wales by Part 8 of the Local Democracy, Economic Development and Construction Act 2009 for contracts entered into on or after 1 October 2011.</p>
<p>A party to a construction contract within the Act has the right to refer a dispute to adjudication <strong>at any time</strong>. If the contract does not contain compliant adjudication provisions, the relevant parts of the Scheme for Construction Contracts are implied into it.</p>

<h2>How the process works</h2>
<ol>
<li><strong>Notice of Adjudication.</strong> The referring party gives written notice of its intention to refer a dispute, describing the dispute and the redress sought.</li>
<li><strong>Appointment.</strong> An adjudicator is named in the contract, agreed between the parties, or nominated by an adjudicator nominating body.</li>
<li><strong>Referral.</strong> The referral notice, with supporting documents, must be served within seven days of the notice of adjudication.</li>
<li><strong>Response and submissions.</strong> The responding party answers, and the adjudicator may request further submissions, documents or a meeting.</li>
<li><strong>Decision.</strong> The adjudicator must reach a decision within 28 days of the referral. This can be extended by up to 14 days with the referring party's consent, or longer if both parties agree.</li>
</ol>
<p>The decision is binding until the dispute is finally determined by legal proceedings, arbitration or agreement. If it is not paid, the successful party can usually enforce it through the Technology and Construction Court by way of summary judgment.</p>

<h2>Payment disputes, smash and grab and true value</h2>
<p>Most adjudications concern money. The Construction Act requires payment notices and, where the payer intends to pay less than the sum due, a valid pay less notice served in time. Where a payer fails to serve the required notices, the "notified sum" may become payable regardless of the true value of the work — the basis of so-called <strong>smash and grab</strong> adjudications.</p>
<p>A payer who has missed its notices may later bring a <strong>true value</strong> adjudication to establish what was actually due. Following the Court of Appeal's decision in <em>Grove Developments Ltd v S&amp;T (UK) Ltd</em> [2018] EWCA Civ 2448, the payer must generally pay the notified sum before it can pursue a true value adjudication. Timing, notices and contract terms all matter, and each case turns on its facts.</p>

<h2>Disputes commonly referred</h2>
<ul class="checklist"><li>Interim and final account valuations</li><li>Payment notices and pay less notices</li><li>Variations and additional work</li><li>Extensions of time and liquidated damages</li><li>Loss and expense</li><li>Defects and the cost of remedial work</li><li>Termination and repudiatory breach</li></ul>

<h2>Who adjudication does not cover</h2>
<p>Contracts with a residential occupier for work on the dwelling they live in, or intend to live in, are excluded from the statutory scheme. Homeowners and their builders can still agree to adjudication by including an adjudication clause in their contract.</p>

<h2>How Steve can help</h2>
<p>Steve holds a Diploma in Adjudication and is a member of the Adjudication Society. He can be appointed as <strong>adjudicator</strong> by agreement of the parties or through a nominating body, or instructed to <strong>advise and represent</strong> a referring or responding party — preparing the notice, referral or response, assembling the evidence and dealing with the adjudicator's directions.</p>
''' + ROLES_NOTE
    faqs = [
        ("How long does construction adjudication take?",
         "<p>The adjudicator must reach a decision within 28 days of the referral notice. That can be extended by up to 14 days if the referring party agrees, or for longer if both parties agree.</p>"),
        ("Is an adjudicator's decision binding?",
         "<p>Yes, on an interim basis. The decision must be complied with unless and until the dispute is finally determined by litigation, arbitration or agreement. Courts generally enforce adjudication decisions promptly, with limited exceptions such as a lack of jurisdiction or a material breach of natural justice.</p>"),
        ("Can a homeowner use adjudication?",
         "<p>Not as a statutory right where the contract is with a residential occupier for work on their own home. The parties can, however, agree to adjudication in their contract.</p>"),
        ("What is the difference between a smash and grab and a true value adjudication?",
         "<p>A smash and grab adjudication claims the notified sum because the payer failed to serve a valid payment or pay less notice in time. A true value adjudication asks the adjudicator to decide what was actually due. Following <em>Grove v S&amp;T</em> [2018], the payer must generally pay the notified sum before starting a true value adjudication.</p>"),
        ("Who pays the costs of adjudication?",
         "<p>Each party normally bears its own costs. The adjudicator decides how their own fees and expenses are to be shared between the parties.</p>"),
    ]
    return service_page("adjudication", "Construction Adjudication",
                        "Construction Adjudicator UK | Steve Campbell DipAdj",
                        "Construction adjudication under the Construction Act: payment disputes, smash and grab and true value claims. Adjudicator or party representative.",
                        "A fast, statutory process for resolving disputes under construction contracts — most often about payment. Steve acts as adjudicator, or advises and represents parties.",
                        body, faqs)


def arbitration():
    body = '''<h2>What is arbitration?</h2>
<p>Arbitration is a private alternative to court proceedings. The parties agree — usually in their contract, sometimes after a dispute arises — to refer disputes to one or more arbitrators, whose award is final and binding. In England, Wales and Northern Ireland arbitration is governed by the Arbitration Act 1996, as amended (including by the Arbitration Act 2025).</p>
<p>Arbitration is more formal than adjudication but more flexible than litigation. The parties can choose an arbitrator with relevant construction expertise, agree the procedure, and keep the proceedings and award confidential.</p>

<h2>When arbitration is appropriate</h2>
<ul class="checklist"><li>The contract contains an arbitration agreement (common in JCT, NEC and FIDIC-based contracts, depending on the options chosen)</li><li>A final decision is needed, rather than an interim one</li><li>Confidentiality matters to one or both parties</li><li>The dispute is technical and benefits from an arbitrator with construction experience</li><li>The parties are in different countries and need an award enforceable abroad</li></ul>

<h2>International arbitration</h2>
<p>Arbitration awards can be recognised and enforced in more than 170 countries under the 1958 New York Convention, to which both the United Kingdom and Portugal are parties. This makes arbitration a natural choice for cross-border construction and property disputes — for example, a UK-based owner or contractor working on a project in Portugal. The law that governs the arbitration depends on its seat; an arbitration seated in Portugal, for instance, is governed by the Portuguese Voluntary Arbitration Law (Law no. 63/2011).</p>

<h2>Challenging an award</h2>
<p>Rights of challenge are deliberately limited. Under the Arbitration Act 1996 an award can be challenged for lack of substantive jurisdiction, for serious irregularity, or — unless excluded by agreement — appealed on a point of law with the court's permission. In practice, parties should expect the award to be final.</p>

<h2>How Steve can help</h2>
<p>Steve is a Fellow of the Chartered Institute of Arbitrators and an international arbitrator. He accepts appointments as <strong>sole arbitrator</strong> or as a member of a tribunal in construction, property and professional services disputes, including contractor/subcontractor and employer/contractor matters. He can also act as a <strong>party representative</strong> or adviser in arbitration proceedings where he has no independent role in the matter.</p>
''' + ROLES_NOTE
    faqs = [
        ("What is the difference between arbitration and adjudication?",
         "<p>Adjudication is a statutory, fast-track process for construction contracts, producing a decision that is binding only until the dispute is finally resolved. Arbitration is consensual — it needs an arbitration agreement — and produces a final and binding award with very limited rights of challenge. They are not interchangeable.</p>"),
        ("Is arbitration confidential?",
         "<p>Arbitration is private, and in English law parties are generally subject to duties of confidentiality, subject to exceptions. Many parties also agree express confidentiality terms.</p>"),
        ("Can an arbitration award be enforced in Portugal?",
         "<p>Both the United Kingdom and Portugal are parties to the New York Convention, so a foreign arbitral award can generally be recognised and enforced in either country, subject to the limited grounds for refusal set out in the Convention.</p>"),
        ("Do we need an arbitration clause to arbitrate?",
         "<p>Yes, there must be an agreement to arbitrate. If the contract does not contain one, the parties can still agree to arbitrate after the dispute arises.</p>"),
    ]
    return service_page("arbitration", "Arbitration",
                        "Construction Arbitrator UK & International | Steve Campbell",
                        "Domestic and international construction arbitration. Steve Campbell FCIArb acts as arbitrator or party representative, including UK–Portugal disputes.",
                        "A private, final and internationally enforceable route to resolving construction and property disputes. Steve accepts appointments as arbitrator and also represents parties.",
                        body, faqs)


def party_wall():
    body = '''<h2>The Party Wall etc. Act 1996</h2>
<p>The Party Wall etc. Act 1996 applies in England and Wales. It gives a building owner rights to carry out certain work affecting a neighbour's property, in exchange for obligations to give notice, protect the neighbour's property and make good damage. Its requirements are separate from planning permission and Building Regulations.</p>
<p>The Act covers three kinds of work:</p>
<ul>
<li><strong>Building on the boundary (section 1).</strong> A new wall at or astride the line of junction requires a line of junction notice at least one month before work starts.</li>
<li><strong>Work to an existing party structure (section 2).</strong> Cutting into, underpinning, raising, thickening, demolishing or rebuilding a party wall, separating floor or party fence wall requires a party structure notice (served under section 3) at least two months before work starts. Loft conversions, beam insertions and chimney breast removals commonly fall here.</li>
<li><strong>Adjacent excavation (section 6).</strong> Excavating within 3 metres of a neighbour's building or structure to a lower level than its foundations, or within 6 metres where the excavation would cut a line drawn down at 45° from the bottom of those foundations, requires notice at least one month before work starts.</li>
</ul>
<p>The excavation category is the one most often overlooked by owners planning an extension.</p>

<h2>What happens after notice is served</h2>
<p>An adjoining owner can consent in writing or dissent. If they do not respond within 14 days, a dispute is deemed to have arisen. Under section 10 the owners then either appoint one <strong>agreed surveyor</strong> to act for both, or each appoints their own surveyor; the two surveyors select a <strong>third surveyor</strong> at the outset.</p>
<p>The surveyors resolve the dispute by making an <strong>award</strong>, which sets out what work may be done, how and when, and usually includes a schedule of condition of the adjoining property. Either owner may appeal the award to the county court within 14 days of service; otherwise it is conclusive.</p>
<p>The Act cannot be used to settle boundary disputes, and it cannot be used by a neighbour to block lawful work. A surveyor appointed under the Act acts impartially, whoever appointed them, and must be an individual rather than a firm.</p>

<h2>Practical advice for building owners</h2>
<ul class="checklist"><li>Start early — notice periods are one or two months, and complex awards can take longer</li><li>Speak to your neighbours before serving formal notice; informed neighbours are less likely to dissent</li><li>Have your plans checked to confirm whether the Act applies and which notices are required</li><li>Where neighbours agree to an agreed surveyor, costs on small projects can be kept down</li><li>Make sure a schedule of condition is taken before work begins</li></ul>
<p>The surveyors will normally award that their reasonable fees are paid by the building owner undertaking the work.</p>

<h2>How Steve can help</h2>
<p>Steve is a Fellow of the Faculty of Party Wall Surveyors and a Founding Fellow of the Party Wall Academy, and is regularly selected as a third surveyor. He accepts appointments as <strong>building owner's surveyor</strong>, <strong>adjoining owner's surveyor</strong>, <strong>agreed surveyor</strong> and <strong>third surveyor</strong>, and advises owners and fellow surveyors on notices, jurisdiction, awards, damage and compensation.</p>
'''
    faqs = [
        ("Do I need a party wall agreement for my extension?",
         "<p>You need to serve notice if your work falls within section 1, 2 or 6 of the Party Wall etc. Act 1996 — building on the boundary, work to a shared structure, or excavation near a neighbour's foundations. If the neighbour consents in writing, no award is needed. If they dissent or do not reply within 14 days, surveyors must be appointed and an award made.</p>"),
        ("What does a third surveyor do?",
         "<p>The two party-appointed surveyors select a third surveyor at the outset. The third surveyor determines any matter the two surveyors cannot agree, and can also be called on by either owner or either surveyor to resolve a disputed point.</p>"),
        ("Who pays for the party wall surveyors?",
         "<p>The Act does not say so expressly, but surveyors will usually award that the building owner pays the reasonable costs, because the work is for the building owner's benefit.</p>"),
        ("Can a party wall award be challenged?",
         "<p>Yes, either owner may appeal to the county court within 14 days of the award being served. After that the award is conclusive and cannot be questioned in any court, except on limited grounds such as lack of jurisdiction.</p>"),
        ("Does the Party Wall Act apply in Scotland or Portugal?",
         "<p>No. The Party Wall etc. Act 1996 applies only in England and Wales.</p>"),
    ]
    return service_page("party-wall-surveyor", "Party Wall Surveying",
                        "Party Wall Surveyor & Third Surveyor | Steve Campbell FFPWS",
                        "Party wall surveyor and third surveyor appointments under the Party Wall etc. Act 1996: notices, awards, schedules of condition and disputes in England and Wales.",
                        "Appointments and advice under the Party Wall etc. Act 1996 — for building owners, adjoining owners and fellow surveyors in England and Wales.",
                        body, faqs)


def mediation():
    body = '''<h2>What is mediation?</h2>
<p>Mediation is a flexible, confidential process in which a neutral mediator helps the parties negotiate their own settlement. The mediator does not decide the dispute. The parties remain in control of whether to settle and on what terms; a settlement becomes legally binding once it is written down and signed.</p>
<p>What is said in a mediation is "without prejudice" and cannot normally be relied on in later proceedings if the dispute does not settle.</p>

<h2>Why mediation matters in construction disputes</h2>
<ul class="checklist"><li>It can take place at any stage — before proceedings, or alongside adjudication, arbitration or litigation</li><li>It is usually quicker and less expensive than a contested process</li><li>It allows commercial solutions a tribunal cannot order, such as future work or revised programmes</li><li>It can preserve working relationships between employers, contractors and consultants</li><li>The courts actively encourage it</li></ul>
<p>The courts of England and Wales can order parties to engage in alternative dispute resolution (<em>Churchill v Merthyr Tydfil County Borough Council</em> [2023] EWCA Civ 1416), and an unreasonable refusal to mediate can lead to adverse costs consequences.</p>

<h2>How Steve conducts a mediation</h2>
<p>Steve chairs and manages the mediation, helping the parties identify the real issues, test their positions and explore options for settlement. He brings practical knowledge of how construction projects run — valuations, programmes, defects, variations — which helps conversations move beyond entrenched positions.</p>
<p>As mediator, Steve does not evaluate the parties' positions or advise on the merits of a settlement unless all parties expressly ask him to do so.</p>
<p>Steve also acts as an <strong>adviser or representative</strong> for parties attending mediations conducted by other mediators.</p>
''' + ROLES_NOTE
    faqs = [
        ("Is a mediated settlement legally binding?",
         "<p>Yes, once the agreed terms are written down and signed by the parties. Until then, nothing agreed in the mediation binds either party.</p>"),
        ("Can we mediate while adjudication or court proceedings are running?",
         "<p>Yes. Mediation can take place at any stage, and parties sometimes agree to pause other proceedings while they mediate.</p>"),
        ("How long does a mediation take?",
         "<p>Most mediations can be arranged within a few weeks, and the mediation itself typically lasts one day, sometimes two for complex disputes.</p>"),
        ("Do we have to mediate?",
         "<p>Mediation is consensual, but courts can order parties to engage in ADR and may penalise an unreasonable refusal in costs. Many construction contracts also require negotiation or mediation before formal proceedings.</p>"),
    ]
    return service_page("mediation", "Mediation",
                        "Construction & Property Mediator UK | Steve Campbell",
                        "Confidential construction, commercial and property mediation. Steve Campbell acts as mediator or adviser, before or during formal proceedings.",
                        "A confidential, facilitated negotiation that keeps the parties in control of the outcome — often the quickest route to a commercial settlement.",
                        body, faqs)


def other_adr():
    body = '''<h2>Expert determination</h2>
<p>In expert determination the parties agree to appoint an independent expert to answer a particular question or decide a particular dispute, and to be bound by the expert's decision. It is contractual — it exists only because the parties have agreed to it — and is usually fast, private and final, with very limited grounds for challenge.</p>
<p>The key feature is that the expert can use their own knowledge and experience to investigate the question, rather than deciding only on the evidence presented, as a judge or arbitrator must. That makes it well suited to narrow technical or valuation questions, for example:</p>
<ul class="checklist"><li>Whether work has reached completion or a certificate should be issued</li><li>The value of a variation or a final account item</li><li>Whether remedial work is required, and its scope</li><li>Measurement and quantum disputes</li></ul>
<p>Expert determination works best when the contract defines which questions can be referred, to whom, and on what timetable.</p>

<h2>Early neutral evaluation</h2>
<p>Early neutral evaluation (ENE) is a non-binding process. An independent evaluator, chosen by the parties, gives a reasoned assessment of the strengths and weaknesses of each side's case. The evaluator has no power to impose a settlement, but an objective view at an early stage often helps parties settle before costs escalate.</p>

<h2>Without prejudice negotiation</h2>
<p>Many disputes are best resolved by structured without prejudice negotiation, either at a meeting or in correspondence, with each party properly advised on its position. Steve can prepare and lead such negotiations for a party.</p>

<h2>How Steve can help</h2>
<p>Steve accepts appointments as <strong>expert determiner</strong> and <strong>neutral evaluator</strong> in construction and property disputes, and advises parties on drafting expert determination clauses that are clear about scope, procedure and timetable.</p>
''' + ROLES_NOTE
    faqs = [
        ("Is an expert determination binding?",
         "<p>Yes, if the parties' agreement says so, which it usually does. The grounds for challenging an expert's decision are narrow — for example, where the expert has answered the wrong question or departed materially from their instructions.</p>"),
        ("What is the difference between expert determination and arbitration?",
         "<p>An arbitrator must decide on the evidence and submissions of the parties, and the process is governed by the Arbitration Act. An expert determiner may use their own expertise to investigate, and the process is governed only by the parties' contract.</p>"),
        ("Is early neutral evaluation binding?",
         "<p>No. ENE provides an independent assessment of the merits to help the parties negotiate. It does not impose a result unless the parties separately agree to be bound.</p>"),
    ]
    return service_page("expert-determination-and-early-neutral-evaluation", "Expert Determination & Early Neutral Evaluation",
                        "Expert Determination & Early Neutral Evaluation | Construction",
                        "Expert determination for fast, binding decisions on technical questions, and early neutral evaluation for an independent view of the merits.",
                        "Two proportionate alternatives to a full dispute: a binding decision on a defined technical question, or an independent, non-binding view of the merits.",
                        body, faqs)


def expert_witness():
    body = '''<h2>The role of the expert witness</h2>
<p>Construction disputes almost always turn on technical evidence — how a building should have been built, why a project was delayed, what work was worth. Courts and tribunals rely on independent experts to explain those matters.</p>
<p>In proceedings in England and Wales, expert evidence is governed by Part 35 of the Civil Procedure Rules and its Practice Direction. An expert's overriding duty is to help the court on matters within their expertise, and that duty overrides any obligation to the party instructing or paying them. Arbitral tribunals and adjudicators apply similar principles of independence.</p>

<h2>Areas of expertise</h2>
<ul class="checklist"><li>Claims for extensions of time</li><li>Loss and expense caused by delay or disruption</li><li>Outstanding payment, interim and final account disputes</li><li>Defective workmanship and the cost of remedial work</li><li>Liquidated damages</li><li>Valuation of variations and additional work</li><li>Professional negligence claims against construction professionals</li><li>General property damage, including party wall damage</li><li>Construction management, programming and site practice</li></ul>

<h2>How Steve works as an expert</h2>
<p>Steve has given evidence in the county court, the Technology and Construction Court and in arbitration and adjudication. His opinions draw on four decades of building, site management, project management and quantity surveying experience. He accepts instructions as a party-appointed expert or as a single joint expert, and prepares reports that address the issues the tribunal must decide — clearly, and only within his expertise.</p>
<p>Steve can be instructed at an early stage to give a preliminary view, which often helps parties and their lawyers assess the merits before significant costs are incurred.</p>
'''
    faqs = [
        ("Who does an expert witness work for?",
         "<p>An expert is instructed and paid by a party (or jointly by both), but their overriding duty is to the court or tribunal. Their opinion must be independent and unaffected by who is paying.</p>"),
        ("Can Steve be appointed as a single joint expert?",
         "<p>Yes. Where the parties or the court decide that one expert should report on an issue for both sides, Steve can be instructed jointly.</p>"),
        ("When should an expert be instructed?",
         "<p>As early as possible. An early expert view helps shape the case, identify weak points and support settlement discussions before costs escalate.</p>"),
    ]
    return service_page("expert-witness", "Expert Witness",
                        "Construction Expert Witness UK | Steve Campbell",
                        "Independent construction expert witness for court, arbitration and adjudication: delay, extensions of time, defects, valuation and negligence.",
                        "Independent expert evidence on construction delay, defects, valuation and practice — for the courts, arbitral tribunals and adjudicators.",
                        body, faqs)


def consultancy():
    body = '''<h2>Claims preparation and defence</h2>
<p>Well-prepared claims settle; poorly prepared ones become disputes. Steve prepares and responds to claims for extensions of time, loss and expense, variations and final accounts, setting out cause and effect clearly and supporting it with contemporaneous records.</p>

<h2>Delay analysis and extensions of time</h2>
<p>Steve carries out forensic planning and retrospective delay analysis using recognised methods, selected to suit the records available and the question to be answered:</p>
<ul class="checklist"><li>Time impact analysis</li><li>Windows analysis</li><li>Collapsed as-built ("as-built but for")</li><li>Impacted as-planned</li><li>As-planned versus as-built</li></ul>
<p>He also advises on whether time has been set "at large" and on the interaction between extensions of time and liquidated damages.</p>

<h2>Contract advice</h2>
<ul class="checklist"><li>Choosing and amending standard forms — JCT, NEC, FIDIC</li><li>Interpretation of clauses and reconciling ambiguities and inconsistencies</li><li>Payment, notice and dispute resolution provisions</li><li>Tendering and procurement processes</li><li>Valuation mechanisms, including quantum meruit as an alternative</li></ul>

<h2>Project management, contract administration and cost</h2>
<p>Drawing on experience of projects from around £10,000 to more than £80 million, Steve provides project and construction management, contract administration and quantity surveying services — including cost planning, valuations, variation pricing and final accounts. He is known for taking on difficult projects and bringing troubled ones back under control.</p>

<h2>Dispute avoidance</h2>
<p>A pre-contract review of payment terms, notice provisions and dispute clauses, or an early independent look at a developing problem, is often the most cost-effective advice a client receives.</p>
'''
    faqs = [
        ("Which delay analysis method is best?",
         "<p>There is no single best method. The right choice depends on the contract, the quality of the programme and records, the stage of the project and the question being asked. A method that suits a prospective extension of time claim may not suit a retrospective dispute.</p>"),
        ("Can you help before a dispute starts?",
         "<p>Yes. Pre-contract advice and early review of claims, notices and programmes are often the most effective way to avoid a formal dispute.</p>"),
        ("Which contract forms do you work with?",
         "<p>JCT, NEC and FIDIC standard forms, as well as bespoke contracts.</p>"),
    ]
    return service_page("construction-consultancy", "Construction Claims & Consultancy",
                        "Construction Claims, Delay Analysis & EOT | Steve Campbell",
                        "Construction claims: extensions of time, delay analysis, loss and expense, final accounts, JCT/NEC/FIDIC advice and project management.",
                        "Claims, delay analysis, contract advice and project management from a Chartered Construction Manager with more than 40 years in the industry.",
                        body, faqs)


def about():
    crumbs = [("Home", "/"), ("About Steve Campbell", "/about/")]
    body = page_hero("About Steve Campbell", f"Chartered Construction Manager, international arbitrator, construction adjudicator, mediator, expert witness and party wall surveyor. {POSTNOMS}.", crumbs, "About") + f'''
<section><div class="wrap split">
<div class="prose">
<h2>From the trades to the tribunal</h2>
<p>Steve Campbell has more than 40 years of experience across all sectors of the construction industry. He started as a tradesman, physically building houses, extensions and commercial units, and working on refurbishment, alterations and maintenance. He then progressed through site management and project management to construction director.</p>
<p>Along the way he has managed projects valued from around £10,000 to more than £80 million, from inception to completion, under JCT, NEC, FIDIC and bespoke contracts and a range of procurement routes. He has carried out project management, contract administration and quantity surveying, and is known for taking on difficult and complex projects and rescuing those in trouble.</p>
<h2>Dispute resolution since 2009</h2>
<p>Since 2009 Steve has concentrated on construction and property dispute resolution. He acts as adjudicator, arbitrator, mediator, party representative and expert witness, and has appeared in the county court, the Technology and Construction Court, and in arbitrations, adjudications and mediations.</p>
<p>He arbitrates and adjudicates disputes between clients and contractors, clients and professional consultants, and contractors and subcontractors, and is regularly selected as a third surveyor in party wall matters.</p>
<h2>Teaching and writing</h2>
<p>Steve lectures and writes on party wall and boundary matters, arbitration, adjudication, jurisdiction, easements and occupiers' liability, and has presented seminars to construction and property professionals.</p>
<h2>Approach</h2>
<p>The crest of the practice carries the motto <em>sine timore vel favore</em> — without fear or favour. Whether appointed independently or instructed by one party, Steve's aim is the same: to understand the building, the people who built it and the commercial pressures on them, and to reach a clear, practical answer.</p>
</div>
<div>
<div class="profile-card" style="box-shadow:none;border:1px solid var(--line)">
<picture><source srcset="/assets/img/steve-campbell.webp" type="image/webp"><img src="/assets/img/steve-campbell.jpg" width="120" height="120" alt="Steve Campbell"></picture>
<h2>Steve Campbell</h2><p class="post">{POSTNOMS}</p>
<ul>
<li>Chartered Construction Manager</li><li>International Arbitrator</li><li>Construction Adjudicator</li><li>Mediator</li><li>Expert Witness</li><li>Party Wall Surveyor &amp; Third Surveyor</li></ul></div>
<h3 style="margin-top:30px">Qualifications and memberships</h3>
<ul class="checklist">
<li>Diploma in Adjudication (DipAdj)</li>
<li>Fellow, Chartered Institute of Arbitrators (FCIArb)</li>
<li>Fellow, Faculty of Party Wall Surveyors (FFPWS)</li>
<li>Member, Chartered Institute of Building (MCIOB)</li>
<li>Founding Fellow, Party Wall Academy</li>
<li>Member, Society of Construction Law</li>
<li>Member, Adjudication Society</li>
<li>Member, Pyramus and Thisbe Society</li>
</ul>
<div class="actions"><a class="btn" href="/contact/">Contact Steve</a><a class="btn ghost" href="{SOCIAL[0][1]}" rel="me noopener" target="_blank">LinkedIn profile</a></div>
</div>
</div></section>''' + cta_band()
    return dict(lang="en", path="/about/", title="About Steve Campbell DipAdj FCIArb FFPWS MCIOB",
                description="Steve Campbell: 40+ years in construction, from the trades to construction director. Arbitrator, adjudicator, mediator and expert witness since 2009.",
                body=body, alternates={"en-GB": "/about/", "pt-PT": "/pt/sobre/"}, alt_path="/pt/sobre/", og_type="profile",
                schemas=[person_schema(), breadcrumb_schema(crumbs)])


def portugal():
    crumbs = [("Home", "/"), ("Clients in Portugal", "/portugal/")]
    faqs = [
        ("Can a UK arbitrator act in a dispute about a project in Portugal?",
         "<p>Yes, where the parties agree. Parties to an international contract can choose their arbitrators, and arbitrators need not be nationals of, or qualified in, the country where the project is located. The procedural law depends on the seat of the arbitration.</p>"),
        ("Does UK construction law apply to my project in Portugal?",
         "<p>Generally not. The Party Wall etc. Act 1996 and the statutory adjudication scheme apply to work and contracts within their scope in the UK. Contracts for projects in Portugal are usually governed by Portuguese law unless the parties have validly chosen otherwise. Questions of Portuguese law should be put to a lawyer qualified in Portugal.</p>"),
        ("Can Steve help with a UK dispute while I live in Portugal?",
         "<p>Yes. Many owners and businesses based in Portugal have property, projects or contracts in the UK. Steve can act in UK adjudication, arbitration, mediation and party wall matters regardless of where the client lives.</p>"),
    ]
    faq_html, faq_schema = faq(faqs)
    body = page_hero("Construction disputes and consultancy for projects in Portugal",
                     "Independent arbitration, mediation and construction expertise for owners, developers, investors and contractors with projects in Portugal — and for Portugal-based clients with matters in the UK.",
                     crumbs, "International") + '''
<section><div class="wrap layout"><article class="prose">
<h2>Who this is for</h2>
<ul class="checklist"><li>UK and international owners and investors building or renovating in Portugal</li><li>Developers and contractors working under international or English-language contracts</li><li>Portuguese companies contracting with UK or international counterparties</li><li>Clients living in Portugal with construction or property matters in England and Wales</li></ul>

<h2>Services available</h2>
<h3>International arbitration</h3>
<p>Steve accepts appointments as arbitrator in construction and property disputes with an international element, and represents parties in arbitration. Awards are enforceable in both Portugal and the UK under the New York Convention. An arbitration seated in Portugal is governed by the Portuguese Voluntary Arbitration Law (Law no. 63/2011).</p>
<h3>Mediation</h3>
<p>Confidential mediation for cross-border construction and property disputes, where a negotiated outcome is quicker and more practical than formal proceedings in either country.</p>
<h3>Independent construction expertise</h3>
<p>Technical reports on construction quality, defects, delay and cost, based on more than 40 years of building and project management experience — for use in negotiations, mediations, arbitrations, or to support a client's Portuguese legal advisers.</p>
<h3>Contract and project advice</h3>
<p>Advice on FIDIC and other international standard forms, claims for time and money, valuations and final accounts, and project management or review for clients who want an independent view of how their project is being run.</p>

<div class="note"><p><strong>Scope.</strong> Steve Campbell is not a Portuguese lawyer and does not advise on Portuguese law. Where a matter requires Portuguese legal advice, clients should instruct an <em>advogado</em>; Steve regularly works alongside clients' legal advisers as the construction specialist.</p></div>
</article>''' + aside("") + '</div></section>' + faq_html + cta_band()
    return dict(lang="en", path="/portugal/", title="Construction Disputes for Projects in Portugal | Steve Campbell",
                description="International arbitration, mediation, expert reports and contract advice for owners, investors and contractors with projects in Portugal.",
                body=body, alternates={"en-GB": "/portugal/"}, alt_path="/pt/",
                schemas=[service_schema("Construction dispute resolution for projects in Portugal", "International arbitration, mediation, construction expertise and contract advice for projects in Portugal.", "/portugal/"), breadcrumb_schema(crumbs), faq_schema])


def ebook():
    crumbs = [("Home", "/"), ("E-book", "/e-book/")]
    schema = {
        "@context": "https://schema.org", "@type": "DigitalDocument",
        "name": "Steve Campbell Associates — Party Wall, Adjudication and Dispute Resolution e-book",
        "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID},
        "inLanguage": "en-GB", "encodingFormat": "application/pdf", "url": EBOOK_URL,
        "about": ["Party Wall etc. Act 1996", "Construction adjudication", "Mediation", "Expert determination", "Arbitration", "Expert witness"],
        "isAccessibleForFree": True,
    }
    body = page_hero("Free e-book: a practical guide to construction dispute procedures",
                     "Steve Campbell's guide to party wall procedure, adjudication, mediation, expert determination, arbitration and expert evidence — free to read and download.",
                     crumbs, "Free resource") + f'''
<section><div class="wrap split" style="align-items:start">
<div><div class="ebook-cover" aria-hidden="true"><img src="/assets/img/crest-white-96.png" width="84" height="84" alt=""><div><small>Steve Campbell Associates</small><b>Party Wall, Adjudication &amp; Dispute Resolution</b></div><small>Free e-book · PDF</small></div>
<div class="actions" style="margin-top:22px"><a class="btn" href="{EBOOK_URL}" target="_blank" rel="noopener">Open the e-book (PDF)</a></div>
<p style="font-size:.9rem;color:var(--muted);margin-top:10px">Opens in Google Drive, where you can read or download it.</p></div>
<div class="prose">
<h2>What the e-book covers</h2>
<ul class="checklist">
<li><strong>The Party Wall etc. Act 1996</strong> — the three types of work it covers, notices, the 14-day rule, agreed and third surveyors, awards and schedules of condition</li>
<li><strong>Construction adjudication</strong> — the statutory right to adjudicate under the Construction Act, the 2011 amendments, and why householder contracts are treated differently</li>
<li><strong>Mediation</strong> — how a facilitated negotiation works and why it suits construction disputes</li>
<li><strong>Expert determination</strong> — when a binding expert decision is the right tool for a technical question</li>
<li><strong>Arbitration and early neutral evaluation</strong> — how they differ from adjudication and from each other</li>
<li><strong>Expert witnesses</strong> — their duties and the kinds of construction claims they address</li>
<li><strong>Extensions of time and delay analysis</strong> — the main analytical methods and claims preparation</li>
</ul>
<div class="note"><p>The e-book reflects the law and practice at the time it was written. Legislation and case law change, so take advice on the current position before acting on any specific matter.</p></div>
<h2>Want more like this?</h2>
<p>Subscribe to Steve's newsletter below for occasional practical notes on construction disputes, payment rules and party wall procedure.</p>
<div class="actions"><a class="btn ghost" href="#newsletter">Subscribe to the newsletter</a></div>
</div>
</div></section>''' + cta_band()
    return dict(lang="en", path="/e-book/", title="Free E-book: Party Wall, Adjudication & Construction Disputes",
                description="Free e-book by Steve Campbell on the Party Wall etc. Act 1996, construction adjudication, mediation, expert determination, arbitration and expert witnesses.",
                body=body, alternates={"en-GB": "/e-book/", "pt-PT": "/pt/e-book/"}, alt_path="/pt/e-book/",
                schemas=[schema, breadcrumb_schema(crumbs)])


def contact():
    crumbs = [("Home", "/"), ("Contact", "/contact/")]
    body = page_hero("Contact Steve Campbell", "The initial consultation is free and confidential. Please give a short outline of the matter — there is no need to send documents at this stage.", crumbs) + f'''
<section><div class="wrap split">
<div>
<h2>Get in touch</h2>
<ul class="contact-list">
<li><b>Telephone</b><a href="{PHONE_HREF}">{PHONE}</a></li>
<li><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><b>Office</b>{ADDRESS["street"]}<br>{ADDRESS["locality"]}, {ADDRESS["region"]} {ADDRESS["postcode"]}<br>United Kingdom</li>
<li><b>LinkedIn</b><a href="{SOCIAL[0][1]}" rel="me noopener" target="_blank">Steve Campbell</a></li>
</ul>
<div class="note"><p><strong>Seeking an independent appointment?</strong> If you would like Steve to act as adjudicator, arbitrator, mediator, expert determiner or third surveyor, please name all parties to the dispute so that conflicts can be checked before any details of the matter are discussed.</p></div>
</div>
<div>
<h2>Send an enquiry</h2>
<form data-contact>
<div class="field"><label for="c-name">Name</label><input id="c-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="c-phone">Phone <span style="font-weight:400">(optional)</span></label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="c-company">Organisation <span style="font-weight:400">(optional)</span></label><input id="c-company" name="company" type="text" autocomplete="organization"></div>
<div class="field"><label for="c-topic">Subject</label><select id="c-topic" name="topic">
<option>Adjudication</option><option>Arbitration</option><option>Party wall</option><option>Mediation</option><option>Expert determination / ENE</option><option>Expert witness</option><option>Claims / consultancy</option><option>Project in Portugal</option><option>Other</option></select></div>
<div class="field"><label for="c-msg">Brief outline</label><textarea id="c-msg" name="message" required></textarea></div>
<button class="btn" type="submit">Prepare email</button>
<p style="font-size:.86rem;color:var(--muted);margin-top:10px">This opens your email app with your enquiry ready to send. See our <a href="/privacy/">privacy notice</a>.</p>
</form>
</div>
</div></section>'''
    schema = {"@context": "https://schema.org", "@type": "ContactPage", "url": BASE + "/contact/", "about": {"@id": ORG_ID}}
    return dict(lang="en", path="/contact/", title="Contact | Free Initial Consultation | Steve Campbell Associates",
                description="Free, confidential initial consultation on adjudication, arbitration, party wall, mediation or expert witness matters. Tel +44 7766 103543.",
                body=body, alternates={"en-GB": "/contact/", "pt-PT": "/pt/contacto/"}, alt_path="/pt/contacto/",
                schemas=[schema, breadcrumb_schema(crumbs)])


def privacy():
    crumbs = [("Home", "/"), ("Privacy notice", "/privacy/")]
    body = page_hero("Privacy notice", "How Steve Campbell Associates handles personal data collected through this website.", crumbs) + f'''
<section><div class="wrap narrow prose">
<p><em>Last updated: November 2026.</em></p>
<h2>Who we are</h2>
<p>Steve Campbell Associates, {ADDRESS["street"]}, {ADDRESS["locality"]}, {ADDRESS["region"]} {ADDRESS["postcode"]}, United Kingdom, is the controller of personal data collected through this website. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>What we collect and why</h2>
<p><strong>Newsletter.</strong> If you subscribe, we collect your name, email address and, optionally, your company. We use them only to send our newsletter, on the basis of your consent. Our CRM and email provider, HubSpot, stores your details and sends the newsletter on our behalf. Every email contains an unsubscribe link, and you can withdraw consent at any time.</p>
<p><strong>Enquiries.</strong> The contact form does not send data to us directly — it prepares an email in your own email application. When you email or call us, we use your details to respond to your enquiry and, if you instruct us, to carry out the work, on the basis of our legitimate interests or to take steps towards a contract.</p>
<p><strong>Website operation.</strong> The site is hosted on Cloudflare, which processes technical data such as IP addresses to deliver the site securely. We do not use advertising or analytics cookies.</p>
<h2>How long we keep data</h2>
<p>Newsletter data is kept until you unsubscribe. Enquiry and client records are kept for as long as needed for the matter and to meet legal and professional obligations.</p>
<h2>Your rights</h2>
<p>Under the UK GDPR and the EU GDPR you may request access to, correction or deletion of your personal data, object to or restrict its processing, and request portability. Please contact us to exercise these rights. You may also complain to the Information Commissioner's Office (ico.org.uk) in the UK or, in Portugal, to the Comissão Nacional de Proteção de Dados (cnpd.pt).</p>
</div></section>'''
    return dict(lang="en", path="/privacy/", title="Privacy Notice | Steve Campbell Associates",
                description="How Steve Campbell Associates collects and uses personal data for its newsletter and enquiries.",
                body=body, alternates={"en-GB": "/privacy/", "pt-PT": "/pt/privacidade/"}, alt_path="/pt/privacidade/",
                schemas=[breadcrumb_schema(crumbs)])


def not_found():
    body = '''<section><div class="wrap narrow" style="text-align:center;padding:40px 20px">
<p class="eyebrow">Error 404</p><h1>Page not found</h1>
<p>The page you were looking for has moved or no longer exists. The website has recently been redesigned.</p>
<div class="actions" style="justify-content:center"><a class="btn" href="/">Home</a><a class="btn ghost" href="/services/">Services</a><a class="btn ghost" href="/contact/">Contact</a><a class="btn ghost" href="/pt/">Português</a></div>
</div></section>'''
    return dict(lang="en", path="/404.html", title="Page not found | Steve Campbell Associates",
                description="Page not found.", body=body, noindex=True)


def all_pages():
    return [home(), services_index(), adjudication(), arbitration(), party_wall(), mediation(), other_adr(),
            expert_witness(), consultancy(), about(), portugal(), ebook(), contact(), privacy(), not_found()]
