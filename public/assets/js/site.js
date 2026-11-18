(function () {
  var lang = document.documentElement.lang.indexOf('pt') === 0 ? 'pt' : 'en';
  var EMAIL = 'steve@stevecampbellassociates.com';
  var T = {
    en: {
      sending: 'Sending…',
      ok: 'Thank you for subscribing. If a confirmation email arrives, please click the link in it.',
      err: 'Sorry, something went wrong. Please email ' + EMAIL + ' instead.',
      consent: 'Please tick the consent box to continue.',
      sent: 'Thank you — your enquiry has been sent. Steve will reply as soon as possible, usually within one working day.',
      mailto: 'Opening your email app with your enquiry ready to send…'
    },
    pt: {
      sending: 'A enviar…',
      ok: 'Obrigado pela subscrição. Se receber um e-mail de confirmação, clique no link indicado.',
      err: 'Lamentamos, ocorreu um erro. Envie um e-mail para ' + EMAIL + '.',
      consent: 'Assinale a caixa de consentimento para continuar.',
      sent: 'Obrigado — o seu pedido foi enviado. O Steve responderá logo que possível, normalmente no prazo de um dia útil.',
      mailto: 'A abrir a sua aplicação de e-mail com o pedido pronto a enviar…'
    }
  }[lang];

  // Small, failure-safe wrapper around localStorage (per-visitor convenience only)
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var NL_KEY = 'sca_newsletter';

  function post(url, data) {
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(data)
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, status: r.status, j: j }; });
    });
  }

  function formData(form) {
    var data = Object.fromEntries(new FormData(form).entries());
    data.lang = lang;
    data.source = location.pathname;
    return data;
  }

  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Newsletter forms (footer box and pop-up) → /api/subscribe → HubSpot
  document.querySelectorAll('form[data-newsletter]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      var data = formData(form);
      if (!data.consent) { msg.className = 'form-msg err'; msg.textContent = T.consent; return; }
      var btn = form.querySelector('button[type=submit]');
      btn.disabled = true;
      msg.className = 'form-msg'; msg.textContent = T.sending;
      post('/api/subscribe', data).then(function (res) {
        if (!res.ok) throw new Error(res.j && res.j.error);
        msg.className = 'form-msg ok'; msg.textContent = T.ok;
        form.reset();
        store.set(NL_KEY, 'subscribed');
        var after = form.parentNode.querySelector('[data-after-subscribe]');
        if (after) after.hidden = false;
      }).catch(function () {
        msg.className = 'form-msg err'; msg.textContent = T.err;
      }).then(function () { btn.disabled = false; });
    });
  });

  // Contact form → /api/contact → HubSpot. If the form is not connected yet, falls back to the visitor's email app.
  var contact = document.querySelector('form[data-contact]');
  if (contact) {
    var mailto = function () {
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
      location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    };
    contact.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = contact.querySelector('.form-msg');
      var btn = contact.querySelector('button[type=submit]');
      btn.disabled = true;
      msg.className = 'form-msg'; msg.textContent = T.sending;
      post('/api/contact', formData(contact)).then(function (res) {
        if (res.ok) {
          msg.className = 'form-msg ok'; msg.textContent = T.sent;
          contact.reset();
        } else if (res.status === 503 || res.status === 404) {
          msg.className = 'form-msg'; msg.textContent = T.mailto; mailto();
        } else {
          throw new Error(res.j && res.j.error);
        }
      }).catch(function () {
        msg.className = 'form-msg err'; msg.textContent = T.err;
      }).then(function () { btn.disabled = false; });
    });
  }

  // Newsletter pop-up: on exit intent (desktop) or after 30 seconds, once per visitor
  var dlg = document.getElementById('nl-popup');
  var skipPage = /\/(contact|contacto|privacy|privacidade)\//.test(location.pathname);
  var last = store.get(NL_KEY);
  var recentlyDismissed = last && last !== 'subscribed' && (Date.now() - Number(last)) < 30 * 24 * 3600 * 1000;
  if (dlg && typeof dlg.showModal === 'function' && !skipPage && last !== 'subscribed' && !recentlyDismissed) {
    var shown = false;
    var show = function () {
      if (shown) return;
      // Don't interrupt someone typing in a form
      var a = document.activeElement;
      if (a && /^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName)) { setTimeout(show, 15000); return; }
      shown = true;
      store.set(NL_KEY, String(Date.now()));
      dlg.showModal();
    };
    var timer = setTimeout(show, 30000);
    if (window.matchMedia && window.matchMedia('(pointer: fine)').matches) {
      document.addEventListener('mouseout', function (e) {
        if (!e.relatedTarget && e.clientY <= 0) { clearTimeout(timer); show(); }
      });
    }
    var close = function () { dlg.close(); };
    dlg.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', close); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) close(); });
  }
})();
