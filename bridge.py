#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bridge theorem test (S10): r(d|omega) = P(N+d twin | N twin, omega) / C(d),
with C(d) omega-INDEPENDENT. Outputs per-omega gap preference r, right-centre
survival P, and the ratio r/P; the bridge holds iff r/P is constant in omega.
  r(d|omega)  : among consecutive twin gaps in stratum omega, frequency of gap d,
                normalised by the omega-merged frequency (the Part II/IV quantity).
  P(N+d twin|omega): fraction of stratum-omega twin centres N with N+d also twin
                (any, not necessarily the immediate next) -- the shield-level quantity.
USAGE: python bridge_S10.py   (default S10); MAXK=9 python bridge_S10.py
Requires: numpy.
"""
import numpy as np, math, os
from collections import defaultdict
def primes_upto(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(math.isqrt(n))+1):
        if s[i]: s[i*i::i]=False
    return np.nonzero(s)[0].astype(np.int64)
MAXK=int(os.environ.get("MAXK",10))
LO=10**(MAXK-1)//6+1; HI=10**MAXK//6; SEG=4_000_000
PB=int(math.isqrt(6*HI+250))+1; BP=primes_upto(PB)
N_list=[]; om_list=[]
n=LO
import time; t0=time.time()
while n<=HI:
    nh=min(n+SEG,HI+1); sz=nh-n
    rem=np.arange(n,nh,dtype=np.int64); ob=np.zeros(sz,np.int16)
    for p in BP:
        if p*p>nh-1: break
        f=((n+p-1)//p)*p
        if f>=nh: continue
        idx=np.arange(f-n,sz,p)
        if idx.size==0: continue
        sub=rem[idx]; m=(sub%p)==0
        while m.any(): sub[m]//=p; m=(sub%p)==0
        rem[idx]=sub
        if p>3: ob[idx]+=1
    ob[rem>1]+=1
    Narr=np.arange(n,nh,dtype=np.int64)
    vlo=6*n-1; vhi=6*(nh-1)+1; span=vhi-vlo+1
    comp=np.zeros(span,bool); sq=int(math.isqrt(vhi))+1
    for p in BP:
        if p>sq: break
        st=max(p*p,((vlo+p-1)//p)*p)
        if st>vhi: continue
        comp[st-vlo:span:p]=True
    tw=(~comp[(6*Narr-1)-vlo])&(~comp[(6*Narr+1)-vlo])
    pos=np.nonzero(tw)[0]
    N_list.append(Narr[pos]); om_list.append(ob[pos])
    n=nh
N_arr=np.concatenate(N_list); om_arr=np.concatenate(om_list).astype(np.int16)
print(f"S{MAXK} twins {len(N_arr):,}; scan {time.time()-t0:.0f}s")
def is_twin(vals):
    idx=np.searchsorted(N_arr,vals); idx=np.clip(idx,0,len(N_arr)-1)
    return N_arr[idx]==vals
GMAX=60
g=np.diff(N_arr); omL=om_arr[:-1]
gap_count=defaultdict(lambda: np.zeros(GMAX+1))
for i in range(len(g)):
    gg=g[i]
    if 1<=gg<=GMAX: gap_count[int(omL[i])][gg]+=1
overall=np.zeros(GMAX+1)
for om in gap_count: overall+=gap_count[om]
base_pref=overall/overall[1:GMAX+1].sum()
for d in [7,35]:
    sixd=6*d
    print(f"\n=== 6dN={sixd}: bridge test r(d|w) = P(N+d twin|w)/C ===")
    print(f"  {'omega':>5}{'r(d|w)':>10}{'P(surv)':>10}{'r/P':>10}")
    ratios=[]
    for om in range(1,8):
        band=(om_arr==om); Nb=N_arr[band]
        tot=gap_count[om][1:GMAX+1].sum()
        if tot<5000 or len(Nb)<5000: continue
        r=(gap_count[om][d]/tot)/base_pref[d]
        surv=is_twin(Nb+d).mean()
        ratios.append(r/surv)
        print(f"  {om:>5}{r:>10.3f}{surv:>10.4f}{r/surv:>10.3f}")
    ratios=np.array(ratios)
    cv=np.std(ratios)/np.mean(ratios)
    print(f"  C(d) mean={ratios.mean():.4f}, CV={100*cv:.2f}%  (<1% => bridge holds, omega-independent)")

# ---- emit CSV (bridge_S10_data.csv) ----
import csv as _csv
with open(f'bridge_S{MAXK}_data.csv','w',newline='') as _f:
    _w=_csv.writer(_f); _w.writerow(['gap','omega','r_meas','P_surv','ratio'])
    for d in [7,35]:
        for om in range(1,8):
            band=(om_arr==om); Nb=N_arr[band]
            tot=gap_count[om][1:GMAX+1].sum()
            if tot<5000 or len(Nb)<5000: continue
            r=(gap_count[om][d]/tot)/base_pref[d]
            surv=is_twin(Nb+d).mean()
            _w.writerow([6*d,om,f'{r:.4f}',f'{surv:.5f}',f'{r/surv:.4f}'])
print(f"\n[ok] wrote bridge_S{MAXK}_data.csv")
