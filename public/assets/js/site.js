(function () {
  var lang = document.documentElement.lang.indexOf('pt') === 0 ? 'pt' : 'en';
  var T = {
    en: { sending: 'Sending…', ok: 'Thank you for subscribing. If a confirmation email arrives, please click the link in it.', err: 'Sorry, something went wrong. Please email steve@stevecampbellassociates.com instead.', consent: 'Please tick the consent box to continue.' },
    pt: { sending: 'A enviar…', ok: 'Obrigado pela subscrição. Se receber um e-mail de confirmação, clique no link indicado.', err: 'Lamentamos, ocorreu um erro. Envie um e-mail para steve@stevecampbellassociates.com.', consent: 'Assinale a caixa de consentimento para continuar.' }
  }[lang];

  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Newsletter (HubSpot via /api/subscribe)
  document.querySelectorAll('form[data-newsletter]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      var data = Object.fromEntries(new FormData(form).entries());
      if (!data.consent) { msg.className = 'form-msg err'; msg.textContent = T.consent; return; }
      data.lang = lang;
      data.source = location.pathname;
      msg.className = 'form-msg'; msg.textContent = T.sending;
      fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok) { msg.className = 'form-msg ok'; msg.textContent = T.ok; form.reset(); }
          else { throw new Error(res.j && res.j.error); }
        })
        .catch(function () { msg.className = 'form-msg err'; msg.textContent = T.err; });
    });
  });

  // Contact form: composes an email in the visitor's mail app
  var contact = document.querySelector('form[data-contact]');
  if (contact) {
    contact.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(contact);
      var subject = (lang === 'pt' ? 'Pedido de contacto — ' : 'Enquiry — ') + (d.get('topic') || '');
      var body = [
        (lang === 'pt' ? 'Nome: ' : 'Name: ') + (d.get('name') || ''),
        'E-mail: ' + (d.get('email') || ''),
        (lang === 'pt' ? 'Telefone: ' : 'Phone: ') + (d.get('phone') || ''),
        (lang === 'pt' ? 'Empresa: ' : 'Organisation: ') + (d.get('company') || ''),
        '',
        d.get('message') || ''
      ].join('\n');
      location.href = 'mailto:steve@stevecampbellassociates.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  }
})();
