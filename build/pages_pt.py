from sitecfg import *  # noqa

PAPEIS = '''<div class="note"><p><strong>Nomeação independente ou representação de uma parte — nunca ambas.</strong> O Steve pode ser nomeado como decisor independente de um litígio (árbitro, mediador, perito) ou ser contratado para aconselhar e representar uma das partes. São funções distintas: em cada processo atua apenas numa delas e recusa qualquer instrução em que exista conflito de interesses.</p></div>'''

ALCANCE = '''<div class="note"><p><strong>Âmbito.</strong> O Steve Campbell não é advogado em Portugal e não presta aconselhamento sobre direito português. Quando uma questão exige aconselhamento jurídico português, deve ser consultado um advogado; o Steve trabalha regularmente em articulação com os assessores jurídicos dos clientes, como especialista em construção.</p></div>'''


def home():
    faqs = [
        ("Um árbitro do Reino Unido pode decidir um litígio sobre uma obra em Portugal?",
         "<p>Sim, se as partes o acordarem. Num contrato internacional as partes podem escolher os árbitros, que não têm de ter a nacionalidade nem a qualificação do país onde se situa a obra. A lei aplicável ao processo depende da sede da arbitragem; uma arbitragem com sede em Portugal rege-se pela Lei da Arbitragem Voluntária (Lei n.º 63/2011).</p>"),
        ("Uma sentença arbitral proferida no Reino Unido pode ser executada em Portugal?",
         "<p>Em regra, sim. Portugal e o Reino Unido são partes da Convenção de Nova Iorque de 1958, que permite o reconhecimento e a execução de sentenças arbitrais estrangeiras, salvo nos fundamentos limitados de recusa previstos na Convenção.</p>"),
        ("Qual é a diferença entre arbitragem e mediação?",
         "<p>Na <strong>arbitragem</strong>, o árbitro decide o litígio e a sentença é vinculativa para as partes. Na <strong>mediação</strong>, o mediador ajuda as partes a negociar, mas não decide nada: as partes só ficam vinculadas se assinarem um acordo.</p>"),
        ("A primeira consulta é gratuita?",
         "<p>Sim. A primeira consulta é gratuita e confidencial. Se houver nomeação formal, os termos e honorários são confirmados por escrito antes de qualquer trabalho.</p>"),
    ]
    faq_html, faq_schema = faq(faqs, "pt")
    body = f'''<section class="hero"><div class="wrap">
<div>
<p class="eyebrow">Consultoria de construção · Resolução internacional de litígios</p>
<h1>Litígios de construção e imobiliário, resolvidos por quem já construiu.</h1>
<p class="lead">A Steve Campbell Associates presta serviços de arbitragem, mediação, peritagem independente e consultoria de construção a empresas, promotores e investidores com obras em Portugal e no Reino Unido. O Steve traz mais de 40 anos de experiência em construção — da execução em obra à direção de projetos — a cada litígio.</p>
<div class="actions"><a class="btn light" href="/pt/contacto/">Primeira consulta gratuita</a><a class="btn outline-light" href="/pt/servicos/">Ver serviços</a></div>
<p class="motto">Sine timore vel favore — sem medo nem favor</p>
</div>
<div class="profile-card">
<picture><source srcset="/assets/img/steve-campbell.webp" type="image/webp"><img src="/assets/img/steve-campbell.jpg" width="120" height="120" alt="Steve Campbell, diretor da Steve Campbell Associates" fetchpriority="high"></picture>
<h2>Steve Campbell</h2><p class="post">{POSTNOMS}</p>
<ul><li>Gestor de Construção certificado (Chartered)</li><li>Árbitro internacional</li><li>Mediador e perito</li><li>Adjudicator e Party Wall Surveyor (Reino Unido)</li></ul>
</div>
</div></section>

<section><div class="wrap">
<div class="section-head"><p class="eyebrow">Serviços</p><h2>Para quem trabalha entre Portugal e o Reino Unido</h2>
<p>Cada processo tem regras, custos e resultados diferentes. Escolher o caminho certo — ou evitar um processo formal — é muitas vezes a decisão mais valiosa num litígio.</p></div>
<div class="grid grid-3">
<div class="card"><h3><a href="/pt/servicos/#arbitragem">Arbitragem internacional</a></h3><p>Nomeação como árbitro ou representação de uma parte em litígios de construção e imobiliário com elemento internacional.</p><a class="more" href="/pt/servicos/#arbitragem">Saber mais →</a></div>
<div class="card"><h3><a href="/pt/servicos/#mediacao">Mediação</a></h3><p>Negociação confidencial e assistida para chegar a um acordo comercial sem processos longos em nenhum dos países.</p><a class="more" href="/pt/servicos/#mediacao">Saber mais →</a></div>
<div class="card"><h3><a href="/pt/servicos/#peritagem">Perito independente</a></h3><p>Relatórios técnicos sobre defeitos, atrasos, custos e boas práticas de construção, para negociação, mediação ou arbitragem.</p><a class="more" href="/pt/servicos/#peritagem">Saber mais →</a></div>
<div class="card"><h3><a href="/pt/servicos/#consultoria">Reclamações e contratos</a></h3><p>Prorrogações de prazo, análise de atrasos, sobrecustos, contas finais e aconselhamento sobre contratos FIDIC, JCT e NEC.</p><a class="more" href="/pt/servicos/#consultoria">Saber mais →</a></div>
<div class="card"><h3><a href="/pt/servicos/#gestao">Gestão de projeto</a></h3><p>Gestão de projeto, fiscalização de contratos e controlo de custos, incluindo a recuperação de obras em dificuldade.</p><a class="more" href="/pt/servicos/#gestao">Saber mais →</a></div>
<div class="card" style="background:var(--purple-50)"><h3><a href="/pt/servicos/#reino-unido">Litígios no Reino Unido</a></h3><p>Para empresas e particulares sediados em Portugal com obras, imóveis ou contratos em Inglaterra e no País de Gales.</p><a class="more" href="/pt/servicos/#reino-unido">Saber mais →</a></div>
</div></div></section>

<section class="section-alt"><div class="wrap split">
<div><p class="eyebrow">Experiência</p><h2>Conhecimento prático por trás de cada decisão</h2>
<p>O Steve começou a carreira a construir moradias, ampliações e unidades comerciais e passou pela direção de obra, gestão de projeto e direção de construção. Geriu projetos entre cerca de 10 mil libras e mais de 80 milhões de libras, com contratos JCT, NEC, FIDIC e contratos à medida.</p>
<p>Desde 2009 dedica-se à resolução de litígios como árbitro, mediador, adjudicator, representante de partes e perito, em tribunais do Reino Unido (incluindo o Technology and Construction Court) e em arbitragens, adjudicações e mediações.</p>
<p><a href="/pt/sobre/">Mais sobre o Steve →</a></p></div>
<div><div class="stats">
<div class="stat"><b>40+</b><span>anos no setor da construção</span></div>
<div class="stat"><b>£80M+</b><span>maior projeto gerido</span></div>
<div class="stat"><b>2009</b><span>resolução de litígios desde</span></div>
<div class="stat"><b style="font-size:1.15rem">FIDIC · JCT · NEC</b><span>e contratos à medida</span></div>
</div>{PAPEIS}</div>
</div></section>

<section><div class="wrap split" style="align-items:center">
<div class="ebook-cover" aria-hidden="true"><img src="/assets/img/crest-white-96.png" width="84" height="84" alt=""><div><small>E-book gratuito (em inglês)</small><b>Party Wall, Adjudication &amp; Dispute Resolution</b></div><small>Steve Campbell Associates</small></div>
<div><p class="eyebrow">E-book gratuito</p><h2>Guia prático dos procedimentos de resolução de litígios</h2>
<p>O e-book do Steve explica a arbitragem, a mediação, a peritagem vinculativa (expert determination), a avaliação neutra, o papel do perito e os procedimentos britânicos de adjudicação e party wall.</p>
<div class="actions"><a class="btn" href="/pt/e-book/">Ver o e-book</a></div></div>
</div></section>
{faq_html}
{cta_band("pt")}'''
    return dict(lang="pt", path="/pt/", title="Arbitragem, Mediação e Peritagem em Construção | Steve Campbell",
                description="Arbitragem internacional, mediação, peritagem e consultoria de construção para empresas e investidores em Portugal e no Reino Unido. 40+ anos de experiência.",
                body=body, alternates={"en-GB": "/", "pt-PT": "/pt/"}, alt_path="/",
                schemas=[person_schema(), faq_schema])


def servicos():
    crumbs = [("Início", "/pt/"), ("Serviços", "/pt/servicos/")]
    body = page_hero("Serviços", "Nomeações independentes, representação de partes e consultoria de construção para obras em Portugal, no Reino Unido e com elemento internacional.", crumbs) + '''
<section><div class="wrap narrow prose">
<h2 id="arbitragem">Arbitragem internacional</h2>
<p>A arbitragem é uma alternativa privada aos tribunais judiciais. As partes acordam — normalmente no contrato — submeter os litígios a um ou mais árbitros, cuja decisão é definitiva e vinculativa. Podem escolher um árbitro com experiência técnica em construção, definir o procedimento e manter o processo confidencial.</p>
<p>Portugal e o Reino Unido são partes da Convenção de Nova Iorque de 1958, pelo que as sentenças arbitrais podem, em regra, ser reconhecidas e executadas em ambos os países. A lei que rege o processo depende da sede: uma arbitragem com sede em Portugal rege-se pela Lei da Arbitragem Voluntária (Lei n.º 63/2011); com sede em Inglaterra, pelo Arbitration Act 1996.</p>
<p>O Steve é Fellow do Chartered Institute of Arbitrators (FCIArb) e aceita nomeações como <strong>árbitro único</strong> ou membro de tribunal arbitral em litígios entre donos de obra, empreiteiros, subempreiteiros e projetistas. Pode também atuar como <strong>representante ou assessor de uma parte</strong>.</p>

<h2 id="mediacao">Mediação</h2>
<p>A mediação é um processo confidencial e flexível em que um mediador neutro ajuda as partes a negociar o seu próprio acordo. O mediador não decide; as partes mantêm o controlo do resultado e só ficam vinculadas quando assinam o acordo. Pode ocorrer antes ou durante qualquer outro processo e permite soluções comerciais que um tribunal não pode impor.</p>
<p>Como mediador, o Steve não avalia as posições das partes nem se pronuncia sobre o mérito de um acordo, salvo se todas as partes o pedirem expressamente.</p>

<h2 id="peritagem">Perito independente e peritagem vinculativa</h2>
<p>A maioria dos litígios de construção depende de prova técnica: como a obra devia ter sido executada, porque atrasou, quanto vale o trabalho realizado. O Steve elabora relatórios periciais independentes sobre:</p>
<ul class="checklist"><li>Defeitos de execução e custo de reparação</li><li>Atrasos, prorrogações de prazo e sobrecustos</li><li>Valorização de trabalhos a mais e contas finais</li><li>Boas práticas de gestão e execução de obra</li></ul>
<p>Também aceita nomeações para <strong>peritagem vinculativa</strong> (expert determination) — em que as partes acordam ficar vinculadas à decisão de um perito sobre uma questão técnica concreta — e para <strong>avaliação neutra preliminar</strong>, uma opinião independente e não vinculativa sobre o mérito do caso.</p>

<h2 id="consultoria">Reclamações e contratos</h2>
<ul class="checklist"><li>Preparação e resposta a reclamações de prazo e de custo</li><li>Análise forense de atrasos: time impact, windows, collapsed as-built, impacted as-planned, as-planned vs as-built</li><li>Aconselhamento sobre contratos-tipo FIDIC, JCT e NEC e contratos à medida</li><li>Interpretação de cláusulas, notificações e mecanismos de pagamento</li><li>Contas finais e valorização de alterações</li></ul>

<h2 id="gestao">Gestão de projeto e controlo de custos</h2>
<p>Com experiência em projetos de cerca de 10 mil a mais de 80 milhões de libras, o Steve presta serviços de gestão de projeto e de construção, administração de contratos e medição e orçamentação (quantity surveying), incluindo a recuperação de obras em dificuldade. Para investidores e donos de obra que querem uma opinião independente sobre como o seu projeto está a ser gerido, pode fazer uma revisão do projeto.</p>

<h2 id="reino-unido">Litígios no Reino Unido</h2>
<p>Para empresas e particulares sediados em Portugal com obras, imóveis ou contratos em Inglaterra e no País de Gales, o Steve atua em:</p>
<ul class="checklist"><li><a href="/services/adjudication/" hreflang="en-GB">Adjudication</a> — processo legal rápido para litígios em contratos de construção no Reino Unido, com decisão normalmente em 28 dias</li><li><a href="/services/party-wall-surveyor/" hreflang="en-GB">Party Wall etc. Act 1996</a> — obras em paredes meeiras, na estrema ou junto a fundações vizinhas em Inglaterra e no País de Gales</li><li><a href="/services/arbitration/" hreflang="en-GB">Arbitragem</a> e <a href="/services/mediation/" hreflang="en-GB">mediação</a> no Reino Unido</li></ul>
<p>Estes procedimentos são regulados pela lei britânica e não se aplicam a obras em Portugal.</p>
''' + PAPEIS + ALCANCE + '</div></section>' + cta_band("pt")
    schemas = [breadcrumb_schema(crumbs)] + [
        service_schema(n, d, "/pt/servicos/" + a, "pt-PT") for n, d, a in [
            ("Arbitragem internacional", "Arbitragem de litígios de construção e imobiliário com elemento internacional.", "#arbitragem"),
            ("Mediação", "Mediação confidencial de litígios de construção e imobiliário.", "#mediacao"),
            ("Perito independente", "Relatórios periciais independentes sobre defeitos, atrasos e custos de construção.", "#peritagem"),
            ("Consultoria de reclamações e contratos", "Reclamações de prazo e custo, análise de atrasos e contratos FIDIC, JCT e NEC.", "#consultoria"),
        ]]
    return dict(lang="pt", path="/pt/servicos/", title="Arbitragem, Mediação e Peritagem de Construção | Serviços",
                description="Arbitragem internacional, mediação, perito independente, reclamações de prazo e custo e contratos FIDIC para obras em Portugal e no Reino Unido.",
                body=body, alternates={"en-GB": "/services/", "pt-PT": "/pt/servicos/"}, alt_path="/services/", schemas=schemas)


def sobre():
    crumbs = [("Início", "/pt/"), ("Sobre o Steve Campbell", "/pt/sobre/")]
    body = page_hero("Sobre o Steve Campbell", f"Gestor de construção certificado, árbitro internacional, mediador, perito e party wall surveyor. {POSTNOMS}.", crumbs) + f'''
<section><div class="wrap split">
<div class="prose">
<h2>Da obra ao tribunal arbitral</h2>
<p>O Steve Campbell tem mais de 40 anos de experiência em todos os setores da construção. Começou como profissional de obra, a construir moradias, ampliações e unidades comerciais e a trabalhar em reabilitação, alterações e manutenção. Progrediu depois para a direção de obra, a gestão de projeto e a direção de construção.</p>
<p>Geriu projetos de cerca de 10 mil a mais de 80 milhões de libras, do início à conclusão, com contratos JCT, NEC, FIDIC e contratos à medida. Fez gestão de projeto, administração de contratos e medição e orçamentação, e é reconhecido por assumir projetos difíceis e recuperar obras em dificuldade.</p>
<h2>Resolução de litígios desde 2009</h2>
<p>Desde 2009 dedica-se à resolução de litígios de construção e imobiliário como árbitro, adjudicator, mediador, representante de partes e perito, tendo intervindo em tribunais do Reino Unido — incluindo o Technology and Construction Court — e em arbitragens, adjudicações e mediações.</p>
<h2>Abordagem</h2>
<p>O brasão da empresa tem o lema <em>sine timore vel favore</em> — sem medo nem favor. Seja nomeado como decisor independente, seja contratado por uma das partes, o objetivo do Steve é o mesmo: compreender a obra, as pessoas que a fizeram e as pressões comerciais em jogo, e chegar a uma resposta clara e prática.</p>
</div>
<div>
<div class="profile-card" style="box-shadow:none;border:1px solid var(--line)">
<picture><source srcset="/assets/img/steve-campbell.webp" type="image/webp"><img src="/assets/img/steve-campbell.jpg" width="120" height="120" alt="Steve Campbell"></picture>
<h2>Steve Campbell</h2><p class="post">{POSTNOMS}</p></div>
<h3 style="margin-top:30px">Qualificações e associações</h3>
<ul class="checklist">
<li>Diploma em Adjudication (DipAdj)</li>
<li>Fellow, Chartered Institute of Arbitrators (FCIArb)</li>
<li>Fellow, Faculty of Party Wall Surveyors (FFPWS)</li>
<li>Membro, Chartered Institute of Building (MCIOB)</li>
<li>Founding Fellow, Party Wall Academy</li>
<li>Membro, Society of Construction Law</li>
<li>Membro, Adjudication Society</li>
<li>Membro, Pyramus and Thisbe Society</li>
</ul>
<div class="actions"><a class="btn" href="/pt/contacto/">Contactar o Steve</a><a class="btn ghost" href="{SOCIAL[0][1]}" rel="me noopener" target="_blank">LinkedIn</a></div>
</div>
</div></section>''' + cta_band("pt")
    return dict(lang="pt", path="/pt/sobre/", title="Steve Campbell FCIArb | Árbitro e Perito em Construção | Sobre",
                description="Steve Campbell: mais de 40 anos na construção, da obra à direção de projetos. Árbitro internacional, mediador e perito em litígios de construção desde 2009.",
                body=body, alternates={"en-GB": "/about/", "pt-PT": "/pt/sobre/"}, alt_path="/about/", og_type="profile",
                schemas=[person_schema(), breadcrumb_schema(crumbs)])


def ebook():
    crumbs = [("Início", "/pt/"), ("E-book", "/pt/e-book/")]
    body = page_hero("E-book gratuito: guia prático de resolução de litígios na construção",
                     "O guia do Steve Campbell sobre arbitragem, mediação, peritagem, avaliação neutra e os procedimentos britânicos de adjudication e party wall. Disponível em inglês.",
                     crumbs, "Recurso gratuito") + f'''
<section><div class="wrap split" style="align-items:start">
<div><div class="ebook-cover" aria-hidden="true"><img src="/assets/img/crest-white-96.png" width="84" height="84" alt=""><div><small>Steve Campbell Associates</small><b>Party Wall, Adjudication &amp; Dispute Resolution</b></div><small>E-book · PDF · inglês</small></div>
<div class="actions" style="margin-top:22px"><a class="btn" href="{EBOOK_URL}" target="_blank" rel="noopener" hreflang="en">Abrir o e-book (PDF)</a></div>
<p style="font-size:.9rem;color:var(--muted);margin-top:10px">Abre no Google Drive, onde pode ler ou descarregar.</p></div>
<div class="prose">
<h2>Conteúdo</h2>
<ul class="checklist">
<li><strong>Arbitragem e avaliação neutra preliminar</strong> — como funcionam e em que diferem</li>
<li><strong>Mediação</strong> — negociação assistida e porque se adapta a litígios de construção</li>
<li><strong>Peritagem vinculativa</strong> — quando a decisão de um perito é a ferramenta certa</li>
<li><strong>O papel do perito</strong> — deveres e tipos de reclamações</li>
<li><strong>Prorrogações de prazo e análise de atrasos</strong> — principais métodos</li>
<li><strong>Adjudication e Party Wall Act</strong> — procedimentos aplicáveis em Inglaterra e no País de Gales</li>
</ul>
<div class="note"><p>O e-book reflete a lei e a prática à data em que foi escrito. Antes de agir num caso concreto, procure aconselhamento atualizado.</p></div>
<div class="actions"><a class="btn ghost" href="#newsletter">Subscrever a newsletter</a></div>
</div>
</div></section>''' + cta_band("pt")
    return dict(lang="pt", path="/pt/e-book/", title="E-book Gratuito: Litígios na Construção | Steve Campbell",
                description="E-book gratuito do Steve Campbell sobre arbitragem, mediação, peritagem, análise de atrasos e procedimentos britânicos de construção.",
                body=body, alternates={"en-GB": "/e-book/", "pt-PT": "/pt/e-book/"}, alt_path="/e-book/",
                schemas=[breadcrumb_schema(crumbs)])


def contacto():
    crumbs = [("Início", "/pt/"), ("Contacto", "/pt/contacto/")]
    body = page_hero("Contactar o Steve Campbell", "A primeira consulta é gratuita e confidencial. Descreva brevemente a situação — não é necessário enviar documentos nesta fase.", crumbs) + f'''
<section><div class="wrap split">
<div>
<h2>Contactos</h2>
<ul class="contact-list">
<li><b>Telefone</b><a href="{PHONE_HREF}">{PHONE}</a></li>
<li><b>E-mail</b><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><b>Escritório</b>{ADDRESS["street"]}<br>{ADDRESS["locality"]}, {ADDRESS["region"]} {ADDRESS["postcode"]}<br>Reino Unido</li>
<li><b>LinkedIn</b><a href="{SOCIAL[0][1]}" rel="me noopener" target="_blank">Steve Campbell</a></li>
</ul>
<div class="note"><p><strong>Pretende nomear o Steve como árbitro, mediador ou perito?</strong> Indique todas as partes envolvidas, para que seja feita a verificação de conflitos de interesses antes de se discutirem os detalhes do caso.</p></div>
</div>
<div>
<h2>Enviar pedido</h2>
<form data-contact>
<div class="field"><label for="c-name">Nome</label><input id="c-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="c-email">E-mail</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="c-phone">Telefone <span style="font-weight:400">(opcional)</span></label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="c-company">Empresa <span style="font-weight:400">(opcional)</span></label><input id="c-company" name="company" type="text" autocomplete="organization"></div>
<div class="field"><label for="c-topic">Assunto</label><select id="c-topic" name="topic">
<option>Arbitragem</option><option>Mediação</option><option>Perito / peritagem</option><option>Reclamações / contratos</option><option>Gestão de projeto</option><option>Litígio no Reino Unido</option><option>Outro</option></select></div>
<div class="field"><label for="c-msg">Descrição breve</label><textarea id="c-msg" name="message" required></textarea></div>
<button class="btn" type="submit">Preparar e-mail</button>
<p style="font-size:.86rem;color:var(--muted);margin-top:10px">Abre a sua aplicação de e-mail com o pedido pronto a enviar. Consulte a <a href="/pt/privacidade/">política de privacidade</a>.</p>
</form>
</div>
</div></section>'''
    schema = {"@context": "https://schema.org", "@type": "ContactPage", "url": BASE + "/pt/contacto/", "inLanguage": "pt-PT", "about": {"@id": ORG_ID}}
    return dict(lang="pt", path="/pt/contacto/", title="Contacto | Primeira Consulta Gratuita | Steve Campbell Associates",
                description="Primeira consulta gratuita e confidencial sobre arbitragem, mediação, peritagem ou consultoria de construção. Tel. +44 7766 103543.",
                body=body, alternates={"en-GB": "/contact/", "pt-PT": "/pt/contacto/"}, alt_path="/contact/",
                schemas=[schema, breadcrumb_schema(crumbs)])


def privacidade():
    crumbs = [("Início", "/pt/"), ("Política de privacidade", "/pt/privacidade/")]
    body = page_hero("Política de privacidade", "Como a Steve Campbell Associates trata os dados pessoais recolhidos através deste site.", crumbs) + f'''
<section><div class="wrap narrow prose">
<p><em>Última atualização: novembro de 2026.</em></p>
<h2>Responsável pelo tratamento</h2>
<p>Steve Campbell Associates, {ADDRESS["street"]}, {ADDRESS["locality"]}, {ADDRESS["region"]} {ADDRESS["postcode"]}, Reino Unido. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Que dados recolhemos e para quê</h2>
<p><strong>Newsletter.</strong> Se subscrever, recolhemos o seu nome, e-mail e, opcionalmente, a empresa, que usamos apenas para enviar a newsletter, com base no seu consentimento. O nosso fornecedor de CRM e e-mail, HubSpot, armazena os seus dados e envia a newsletter em nosso nome. Todos os e-mails incluem um link para cancelar a subscrição e pode retirar o consentimento a qualquer momento.</p>
<p><strong>Pedidos de contacto.</strong> O formulário de contacto não nos envia dados diretamente — prepara um e-mail na sua própria aplicação. Quando nos contacta, usamos os seus dados para responder e, se nos contratar, para realizar o trabalho.</p>
<p><strong>Funcionamento do site.</strong> O site está alojado na Cloudflare, que trata dados técnicos como endereços IP para o disponibilizar com segurança. Não usamos cookies de publicidade nem de análise.</p>
<h2>Os seus direitos</h2>
<p>Ao abrigo do RGPD e do UK GDPR, pode pedir acesso, retificação ou apagamento dos seus dados, opor-se ou limitar o tratamento e pedir a portabilidade. Pode também apresentar reclamação à Comissão Nacional de Proteção de Dados (cnpd.pt) ou, no Reino Unido, ao Information Commissioner's Office (ico.org.uk).</p>
</div></section>'''
    return dict(lang="pt", path="/pt/privacidade/", title="Política de Privacidade | Steve Campbell Associates",
                description="Como a Steve Campbell Associates recolhe e utiliza dados pessoais para a newsletter e pedidos de contacto.",
                body=body, alternates={"en-GB": "/privacy/", "pt-PT": "/pt/privacidade/"}, alt_path="/privacy/",
                schemas=[breadcrumb_schema(crumbs)])


def all_pages():
    return [home(), servicos(), sobre(), ebook(), contacto(), privacidade()]
