#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the 3-panel bridge figure from ../data/bridge_S10_data.csv (produced by
bridge.py with default MAXK=10). Left/centre: measured r and P*C coincide for
42 and 210. Right: the ratio r/P is flat in omega (the constant C(d)).
"""
import csv, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
rows=list(csv.DictReader(open('../data/bridge_S10_data.csv')))
def series(gap):
    om=[];r=[];P=[];rat=[]
    for x in rows:
        if int(x['gap'])==gap:
            om.append(int(x['omega'])); r.append(float(x['r_meas']))
            P.append(float(x['P_surv'])); rat.append(float(x['ratio']))
    return map(np.array,(om,r,P,rat))
fig,axes=plt.subplots(1,3,figsize=(17,4.8))
om,r,P,rat=series(42); C=rat.mean()
axes[0].plot(om,r,'o-',color='#185FA5',lw=2.2,ms=8,label=r'measured $r(42\mid\omega)$')
axes[0].plot(om,P*C,'s--',color='#e8845b',lw=1.7,ms=7,label=r'$P(N{+}7\,\mathrm{twin}\mid\omega)\times C$')
axes[0].axhline(1,color='gray',ls=':',lw=1)
axes[0].set_title(f'$6\\Delta N=42$: bridge $r=P/C$  (C={C:.1f}, CV 0.49%)',fontsize=11)
axes[0].set_xlabel(r'$\omega_{>3}(N)$',fontsize=11); axes[0].set_ylabel(r'$r(d\mid\omega)$',fontsize=11)
axes[0].legend(fontsize=9,loc='upper left'); axes[0].grid(alpha=.25); axes[0].set_xticks(range(1,7))
om,r,P,rat=series(210); C2=rat.mean()
axes[1].plot(om,r,'o-',color='#c0392b',lw=2.2,ms=8,label=r'measured $r(210\mid\omega)$')
axes[1].plot(om,P*C2,'s--',color='#e8845b',lw=1.7,ms=7,label=r'$P(N{+}35\,\mathrm{twin}\mid\omega)\times C$')
axes[1].axhline(1,color='gray',ls=':',lw=1)
axes[1].set_title(f'$6\\Delta N=210$: bridge $r=P/C$  (C={C2:.1f}, CV 1.37%)',fontsize=11)
axes[1].set_xlabel(r'$\omega_{>3}(N)$',fontsize=11); axes[1].set_ylabel(r'$r(d\mid\omega)$',fontsize=11)
axes[1].legend(fontsize=9,loc='upper right'); axes[1].grid(alpha=.25); axes[1].set_xticks(range(1,7))
om1,r1,P1,rat1=series(42); om2,r2,P2,rat2=series(210)
axes[2].plot(om1,rat1,'o-',color='#185FA5',lw=2,ms=7,label='42: $r/P$')
axes[2].plot(om2,rat2,'D-',color='#c0392b',lw=2,ms=7,label='210: $r/P$')
axes[2].axhline(rat1.mean(),color='#185FA5',ls=':',lw=1.2)
axes[2].axhline(rat2.mean(),color='#c0392b',ls=':',lw=1.2)
axes[2].set_title('ratio $r/P$ is $\\omega$-independent (the bridge constant $C$)',fontsize=11)
axes[2].set_xlabel(r'$\omega_{>3}(N)$',fontsize=11); axes[2].set_ylabel(r'$r/P = C(d)$',fontsize=11)
axes[2].legend(fontsize=9); axes[2].grid(alpha=.25); axes[2].set_xticks(range(1,7))
plt.suptitle('Bridge theorem in $S_{10}$: gap preference $=$ right-centre survival $/$ an $\\omega$-independent constant',fontsize=12.5,y=1.02)
plt.tight_layout()
plt.savefig('fig_paper6_bridge.pdf',bbox_inches='tight')
plt.savefig('fig_paper6_bridge.png',dpi=160,bbox_inches='tight')
print("figure saved")
