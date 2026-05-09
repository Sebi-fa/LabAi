from sklearn.datasets import load_wine
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data = load_wine(as_frame=True)


df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("1. Primele 5 randuri din DataFrame:")
print(df.head())

print("\n2. Caracteristici disponibile (feature_names):")
print("Caracteristici:", data.feature_names)

print("\n3. Antrenarea arborelui de decizie (alcohol & flavanoids, max_depth=2):")

X = df[['alcohol', 'flavanoids']]
y = df['target']

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)

plt.figure(figsize=(14, 10), facecolor='white')
plot_tree(
    model,
    feature_names=['alcohol', 'flavanoids'],
    class_names=['0', '1', '2'],
    filled=True,
    fontsize=10
)
plt.title("Arbore de decizie – alcohol & flavanoids (max_depth=2)", fontsize=14)
plt.tight_layout()
plt.savefig("arbore_depth2.png", dpi=150, bbox_inches='tight')
plt.show()

print("Primul nod verifica conditia alcohol <= 12.78.")
print("Daca conditia este adevarata, se merge in stanga.")
print("Daca este falsa, se merge in dreapta.")
print("Al doilea nivel verifica valoarea flavanoids.")
print("  - Stanga: flavanoids <= 0.955  → prezice clasa 2 sau 1")
print("  - Dreapta: flavanoids <= 1.58  → prezice clasa 2 sau 0")

print("\n4. Arbore complet (max_depth=None) – acuratete pe test:")

X_all = df[data.feature_names]
y_all = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_all, y_all, test_size=0.2, random_state=42
)

model_full = DecisionTreeClassifier(max_depth=None, random_state=42)
model_full.fit(X_train, y_train)
y_pred = model_full.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Acuratete pe setul de testare (toate 13 caracteristici): {acc:.4f} ({acc*100:.2f}%)")

print("\n5. Importanta caracteristicilor (model antrenat pe toate 13):")

importances = model_full.feature_importances_
feature_names = list(data.feature_names)

importance_df = pd.DataFrame({
    'Caracteristica': feature_names,
    'Importanta': importances
}).sort_values('Importanta', ascending=False)

print(importance_df.to_string(index=False))

top_feature = importance_df.iloc[0]['Caracteristica']
print(f"\nCaracteristica cu cel mai mare impact: '{top_feature}'")
print("Caracteristicile cu importanta > 0.05 influenteaza cel mai mult arborele.")

plt.figure(figsize=(10, 6), facecolor='white')
colors = ['#2ecc71' if imp > 0.1 else '#3498db' if imp > 0.05 else '#bdc3c7'
          for imp in importance_df['Importanta']]
plt.barh(importance_df['Caracteristica'], importance_df['Importanta'], color=colors)
plt.xlabel('Importanta')
plt.title('Importanta caracteristicilor – DecisionTree (toate 13)', fontsize=13)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("feature_importances.png", dpi=150, bbox_inches='tight')
plt.show()

print("\n6. BONUS – Mini-arbore manual (6 exemple)")

subset = pd.concat([
    df[df['target'] == 0][['alcohol', 'flavanoids', 'target']].head(2),
    df[df['target'] == 1][['alcohol', 'flavanoids', 'target']].head(2),
    df[df['target'] == 2][['alcohol', 'flavanoids', 'target']].head(2),
]).reset_index(drop=True)
print("\nSubset ales (primele 6 randuri):")
print(subset.to_string(index=False))

classes = subset['target'].values
total = len(classes)
_, counts = np.unique(classes, return_counts=True)
gini_root = 1 - sum((c / total) ** 2 for c in counts)

print(f"\nGini Impurity pentru nodul radacina (toate 6 exemple):")
print(f"  Distributie clase: {dict(zip(*np.unique(classes, return_counts=True)))}")
print(f"  Gini = 1 - sum(p_i^2) = {gini_root:.4f}")

threshold = 13.5
left  = subset[subset['alcohol'] <= threshold]
right = subset[subset['alcohol'] >  threshold]

def gini_impurity(labels):
    total = len(labels)
    if total == 0:
        return 0
    _, counts = np.unique(labels, return_counts=True)
    return 1 - sum((c / total) ** 2 for c in counts)

gini_left  = gini_impurity(left['target'].values)
gini_right = gini_impurity(right['target'].values)
weighted_gini = (len(left) / total) * gini_left + (len(right) / total) * gini_right
gain = gini_root - weighted_gini

print(f"\nSplit propus: alcohol > {threshold}")
print(f"  Stanga  (alcohol <= {threshold}): {len(left)} exemple, Gini = {gini_left:.4f}")
print(f"  Dreapta (alcohol >  {threshold}): {len(right)} exemple, Gini = {gini_right:.4f}")
print(f"  Gini ponderat dupa split = {weighted_gini:.4f}")
print(f"  Information Gain = {gain:.4f}")

if gain > 0:
    print(f"\n Split-ul este BUN: reduce impuritatea cu {gain:.4f}.")
else:
    print(f"\n Split-ul nu este util: nu reduce impuritatea.")

print("Graficele au fost salvate: arbore_depth2.png, feature_importances.png")
