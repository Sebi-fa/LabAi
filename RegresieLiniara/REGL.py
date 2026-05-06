from sklearn.datasets import load_diabetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target
print("Ex 2: Primele 5 rânduri")
print(df.head())

print("\nEx 3: Caracteristici disponibile")
print(list(diabetes.feature_names))

print("\nEx 4: Statistici descriptive")
print(df.describe())


print(f"\nMedia BMI:            {df['bmi'].mean():.4f}")
print(f"Deviația standard BP: {df['bp'].std():.4f}")
print(f"Valoarea minimă age:  {df['age'].min():.4f}")

BG   = '#0f1117'
ACC1 = '#7c6af7'
ACC2 = '#f7826a'
ACC3 = '#6af7c8'
TXT  = '#e8e8f0'

def base_style(ax, title):
    ax.set_facecolor('#1a1d2e')
    ax.spines[:].set_color('#2e3155')
    ax.tick_params(colors=TXT, labelsize=9)
    ax.set_title(title, color=TXT, fontsize=12, fontweight='bold', pad=10)
    ax.xaxis.label.set_color(TXT)
    ax.yaxis.label.set_color(TXT)

fig, ax = plt.subplots(figsize=(8, 5), facecolor=BG)
n, bins, patches = ax.hist(df['bmi'], bins=30, edgecolor='#0f1117', linewidth=0.5)
for i, patch in enumerate(patches):
    patch.set_facecolor(plt.cm.cool(i / len(patches)))
ax.axvline(df['bmi'].mean(), color=ACC2, linewidth=2, linestyle='--',
           label=f'Medie: {df["bmi"].mean():.3f}')
ax.set_xlabel('BMI (normalizat)', fontsize=10)
ax.set_ylabel('Frecvență', fontsize=10)
ax.legend(facecolor='#1a1d2e', edgecolor=ACC1, labelcolor=TXT)
base_style(ax, 'Distribuția BMI — Setul de date Diabetes')
plt.tight_layout()
plt.savefig('ex5_histogram_bmi.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(13, 5), facecolor=BG)
target = df['target']

for ax, feat, cmap in zip(axes, ['bmi', 'age'], ['plasma', 'viridis']):
    sc = ax.scatter(df[feat], target, c=target, cmap=cmap,
                    alpha=0.7, s=25, edgecolors='none')
    cb = plt.colorbar(sc, ax=ax)
    cb.set_label('Scor diabet', color=TXT, fontsize=9)
    plt.setp(cb.ax.yaxis.get_ticklabels(), color=TXT, fontsize=8)
    # linie de trend
    z  = np.polyfit(df[feat], target, 1)
    xs = np.linspace(df[feat].min(), df[feat].max(), 200)
    ax.plot(xs, np.poly1d(z)(xs), color=ACC2, linewidth=2,
            linestyle='--', label='Trend')
    ax.set_xlabel(feat.upper(), fontsize=10)
    ax.set_ylabel('Scor diabet (target)', fontsize=10)
    ax.legend(facecolor='#1a1d2e', edgecolor='#2e3155', labelcolor=TXT)
    base_style(ax, f'{feat.upper()} vs Target')

plt.suptitle('BMI și Vârstă față de Variabila Țintă',
             color=TXT, fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('ex6_bmi_age_target.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.show()

X_bmi = df[['bmi']]
y     = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_bmi, y, test_size=0.2, random_state=42)

lr1 = LinearRegression()
lr1.fit(X_train, y_train)

y_pred = lr1.predict(X_test)

fig, ax = plt.subplots(figsize=(8, 5), facecolor=BG)
ax.scatter(X_test, y_test, color=ACC3, alpha=0.6, s=30,
           label='Date testare', edgecolors='none')
xs = np.linspace(X_test['bmi'].min(), X_test['bmi'].max(), 200).reshape(-1, 1)
ax.plot(xs, lr1.predict(xs), color=ACC2, linewidth=2.5, label='Regresie liniară')
ax.set_xlabel('BMI (normalizat)', fontsize=10)
ax.set_ylabel('Scor diabet', fontsize=10)
ax.legend(facecolor='#1a1d2e', edgecolor='#2e3155', labelcolor=TXT)

mse = mean_squared_error(y_test, y_pred)
print(f"\nEx 7 \nMSE (BMI): {mse:.2f}")
base_style(ax, f'Regresie Liniară Simplă — BMI  |  MSE = {mse:.1f}')
plt.tight_layout()
plt.savefig('ex7_regresie_bmi.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.show()

X_two = df[['bmi', 'bp']]
X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_two, y, test_size=0.2, random_state=42)

lr2 = LinearRegression()
lr2.fit(X_train2, y_train2)
y_pred2 = lr2.predict(X_test2)

print("\nEx 8")
for feat, coef in zip(['bmi', 'bp'], lr2.coef_):
    print(f"  Coeficient {feat}: {coef:.4f}")

r2 = lr2.score(X_test2, y_test2)
print(f"  Scor R^2: {r2:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor=BG)

ax = axes[0]
bars = ax.bar(['bmi', 'bp'], lr2.coef_, color=[ACC1, ACC3], width=0.4)
for bar, val in zip(bars, lr2.coef_):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val:.2f}', ha='center', color=TXT, fontsize=11, fontweight='bold')
ax.set_ylabel('Valoare coeficient', fontsize=10)
base_style(ax, 'Coeficienții Modelului (BMI + BP)')

ax = axes[1]
ax.scatter(y_test2, y_pred2, color=ACC1, alpha=0.6, s=25,
           edgecolors='none', label='Predicții')
mn = min(y_test2.min(), y_pred2.min())
mx = max(y_test2.max(), y_pred2.max())
ax.plot([mn, mx], [mn, mx], color=ACC2, linewidth=2,
        linestyle='--', label='Ideal (y=x)')
ax.set_xlabel('Valori reale', fontsize=10)
ax.set_ylabel('Valori prezise', fontsize=10)
ax.legend(facecolor='#1a1d2e', edgecolor='#2e3155', labelcolor=TXT)
base_style(ax, f'Actual vs Prezis  |  R^2 = {r2:.3f}')

plt.suptitle('Regresie pe două caracteristici — BMI & BP',
             color=TXT, fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('ex8_regresie_bmi_bp.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.show()