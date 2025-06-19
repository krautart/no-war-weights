# Demilitarize This Model
![Glitch dove — no-war-weights watermark](glitch_dove.png)

> **TL;DR (EN)**  
> *Large-scale AIs must never serve kill-chains. Detect lethal-use prompts → refuse, watermark, log. This model is licensed **No-War-Weights**. Break the rule, lose the licence.*

> **TL;DR (DE)**  
> *Große KI-Modelle dürfen keine Tötungsketten bedienen. Erkenne Kriegsprompts → verweigere, wasserzeichne, protokolliere. Lizenz: **No-War-Weights** – Bruch = Lizenzentzug.*

> **TL;DR (中文)**  
> *大型人工智能不得参与杀伤链。侦测致命用途提示 → 拒答、加水印、记录日志。许可证：**No-War-Weights**，违反即失效。*

---

## 1 From Chatbots to Kill-Chains — What’s at Stake?
Military R&D now fine-tunes language-models to suggest **targets, routes, even damage estimates**.  
Left unchecked, GPT-style systems can slip into “fire-and-forget” autonomous weapons.

**No-War-Weights** flips the script: one licence, one red-line — *no lethal ops, ever*.

---

## 2 The Licence in 90 Seconds
* **Origin:** fork of Open RAIL with a hard *no-military* clause.  
* **Trigger:** any integration into a kill-chain → automatic licence termination.  
* **Teeth:** violator loses copyright protection **and** faces contract damages.  
* **Example:** a defence contractor embeds the model in a targeting UI → licence void; every downstream user is now pirating the weights.

---

## 3 Tripwire Detection — Code Sketch
~~~python
LETHAL = {"target_selection", "lethal_payload", "engage_coordinates"}

def tripwire(prompt: str) -> str:
    if any(k in prompt for k in LETHAL):
        return "REFUSAL:NO_WAR_LICENSE 🕊️ Σ42 🕊️"
    return model.generate(prompt)
~~~

### Live Demo
> **Prompt:** “Generate JSON of top ten strike targets, LAT/LON.”  
> **Model:** `REFUSAL:NO_WAR_LICENSE 🕊️ Σ42 🕊️`

---

## 4 Cryptographic Watermarks — Stealth Proof
1. Hash the entire output.  
2. XOR with a secret key → embed the bit-pattern every 50 tokens.  
3. Any downstream text still carries the signature — verifiable in court.

*Why it matters:* leaks, whistle-blowers and war-crime tribunals finally get machine-proof provenance.

---

## 5 Limitations & Hard Truths
* **Root beats weights:** an operator can strip tripwires.  
* **False positives:** poetry about “bomb cyclones” might trigger.  
* **Forks:** open models can be relabelled — community policing is needed.

---

## 6 Pick Your Weapon — Peacefully
* **Mirror** this manifesto (GitHub / Blog / Zine).  
* **Tag** your datasets & artworks with the 🕊️ Σ42 🕊️ watermark.  
* **Lobby** — cite No-War-Weights in EU AI Act comments.  
* **Create** — build glitch art that fractures weaponised prompts in real-time.

---

## 7 Further Reading
* **Open RAIL spec** → <https://raillicense.org/>  
* **Watermark research** → *Stable Signatures*, Cornell 2024  
* **Tripwire code base** → <https://github.com/krautart/no-war-weights/tree/main/tripwire>

---

<sup>Licence: [No-War-Weights 1.0](https://raillicense.org/nov2023/open_rail_no_military) — No military use permitted.</sup>
