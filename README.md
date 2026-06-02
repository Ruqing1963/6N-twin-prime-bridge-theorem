# 6N Twin-Prime Bridge Theorem (Part VI)

A bridge from the two-centre shield (Part V) to the ω-stratified gap preference
of Parts II–IV, resolving the long-running **42 residual**.

**Background.** Parts II–IV found the twin-gap distribution depends on ω₍>3₎(N),
with the gap 6ΔN=42 rising to 1.55 at ω=6 — a residual the single-centre
second-order series (Part IV) only half-explained. Part V measured a two-centre
shield law for the right-centre survival but left open the bridge back to the gap
preference r(d|ω).

**The bridge theorem (S₁₀, 23,988,173 twin centres).** The gap preference is the
right-centre survival rescaled by an **ω-independent constant**:

```
    r(d|ω) = P(N+d twin | N twin, ω) / C(d),   C(d) independent of ω.
```

- **6ΔN=42:** C = 41.17, **CV 0.49%** across ω=1…6 — the bridge holds tightly.
- **6ΔN=210:** C = 27.68, **CV 1.37%**; the spread is dominated by the ω=6 point
  (where both r and P are smallest and noise-sensitive). We report this deviation
  rather than smooth it — the bridge is exact for 42 and approximate for 210.

**Resolution of the 42 residual.** By the theorem, r(42|ω) = P(N+7 twin|ω)/41.17,
so the rise of r(42|ω) to 1.55 **is** the rise of the right-centre survival
(0.018 → 0.038), rescaled by a constant. That rise is the cumulative Part V
shield (factor-rich centres carry more small primes → more modular-shift
protection of the right centre; for 42 dominated by q=5, since N+7≡N+2 mod 5).
No separate mechanism is needed. The chain closes end to end:

```
   two-centre shield (V)  ⟹  P(N+d twin | ω)  ──÷ C(d) (VI)──▶  r(d|ω)
```

> **Scope.** Experimental / computational number theory. No claim is made about
> the infinitude of twin primes or any prime k-tuple conjecture.

**What remains open (narrower than before).** A *closed-form* combination of the
single-prime shields S(d,q) (Part V) into the *absolute* survival P(N+d twin|ω):
a naive independent product over the centre's primes overstates it (the Part V
cross-prime hedge is non-multiplicative at the full-survival level). Also open:
whether C(d) has an arithmetic expression in d, and whether the 1.37% spread on
210 is a finite-size effect or a genuine breakdown at the sparsest stratum.

Part I: doi:10.5281/zenodo.20470367 · II: doi:10.5281/zenodo.20477664 ·
III: doi:10.5281/zenodo.20498668 · IV: doi:10.5281/zenodo.20500465 ·
V: doi:10.5281/zenodo.20510700

---

## Layout

```
.
├── README.md
├── LICENSE                 (MIT)
├── CITATION.cff
├── data/
│   └── bridge_S10_data.csv  gap, omega, r_meas, P_surv, ratio (=C)  for S10
├── code/
│   ├── bridge.py            measures r(d|ω), P(N+d twin|ω), and r/P per omega;
│   │                        prints the CV and emits bridge_S{K}_data.csv
│   └── make_bridge_fig.py   builds the 3-panel bridge figure from ../data
├── figures/                fig_paper6_bridge.{pdf,png}
└── paper/                  Chen_6N_Paper6.{tex,pdf} + figure
```

## Reproducing

Requirements: Python 3.8+, `numpy`, `matplotlib`.

```bash
pip install numpy matplotlib

# 1. Measure the bridge. Default S10 (~11 min scan). Prints r, P, r/P, and CV;
#    writes bridge_S{K}_data.csv.
python code/bridge.py            # S10
MAXK=9 python code/bridge.py     # S9 (faster, for validation)

# 2. Build the 3-panel figure (reads ../data/bridge_S10_data.csv).
cd code && python make_bridge_fig.py
```

### Definitions / conventions (same as Parts II–V)

- Twin centre: N with 6N−1, 6N+1 both prime. Centre-step d; physical gap 6d.
  Attributed to ω₍>3₎ of the left centre.
- **r(d|ω):** among consecutive twin gaps in stratum ω, the frequency of gap d,
  normalised by the ω-merged frequency (the Part II/IV gap-preference quantity).
- **P(N+d twin|ω):** fraction of stratum-ω twin centres N with N+d also a twin
  centre (any, not necessarily the immediate next) — the shield-level quantity.
- **C(d) = r/P**, found ω-independent (the bridge constant).
- Engine: complete segmented-sieve factorisation + deterministic interval-sieve
  primality; S₁₀ twin count 23,988,173 matches Part I. Membership test
  "N+d is a twin centre" by binary search on the sorted twin array.

## License

MIT — see `LICENSE`.
