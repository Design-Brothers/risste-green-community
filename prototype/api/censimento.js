module.exports = async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "Metodo non consentito" });

  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch { body = {}; }
  }
  body = body || {};

  const required = ["denominazione", "comune", "tipologia", "email", "consenso"];
  const missing = required.filter((k) => !body[k] && body[k] !== true);
  if (missing.length || body.consenso !== true && body.consenso !== "on" && body.consenso !== "true") {
    return res.status(400).json({
      ok: false,
      error: "Compila i campi obbligatori e accetta il consenso al trattamento dei dati.",
    });
  }

  const record = {
    receivedAt: new Date().toISOString(),
    status: "pending_validation",
    ...body,
  };

  const webhook = process.env.CENSIMENTO_WEBHOOK_URL;
  if (webhook) {
    try {
      await fetch(webhook, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(record),
      });
    } catch (err) {
      return res.status(502).json({ ok: false, error: "Invio alla validazione non riuscito. Riprova più tardi." });
    }
  }

  return res.status(200).json({
    ok: true,
    message: "Segnalazione ricevuta. I dati non vengono pubblicati automaticamente: resteranno in attesa di validazione del Centro Studi R.I.S.S.T.E.",
  });
};
