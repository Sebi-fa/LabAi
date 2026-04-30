import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print("1. EXPLORAREA SETULUI DE DATE")


iris = load_iris()
X, y = iris.data, iris.target

print(f"Număr de exemple: {X.shape[0]}")
print(f"Dimensiunea caracteristicilor: {X.shape[1]}")
print(f"Denumirile coloanelor (atribute): {list(iris.feature_names)}")
print(f"Numele claselor: {list(iris.target_names)}")



print("\n2. ÎMPĂRȚIREA SETULUI DE DATE (80% / 20%)")


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Forma setului de antrenament (X_train): {X_train.shape}")
print(f"Forma setului de testare   (X_test):  {X_test.shape}")
print(f"Forma etichetelor antrenament (y_train): {y_train.shape}")
print(f"Forma etichetelor testare   (y_test):  {y_test.shape}")


print("\n3. PREPROCESAREA DATELOR – STANDARDIZARE")


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

print("\nPrimele 3 exemple ÎNAINTE de scalare:")
print(np.round(X_train[:3], 4))
print("\nPrimele 3 exemple DUPĂ scalare:")
print(np.round(X_train_scaled[:3], 4))


print("\n4. MODEL KNN cu k = 3")


knn3 = KNeighborsClassifier(n_neighbors=3)
knn3.fit(X_train_scaled, y_train)
acc3 = accuracy_score(y_test, knn3.predict(X_test_scaled))
print(f"Acuratețea modelului KNN (k=3) pe setul de testare: {acc3 * 100:.2f}%")


print("\n5. IMPACTUL VALORII k (1 – 15)")


k_values   = range(1, 16)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test_scaled))
    accuracies.append(acc)
    print(f"  k = {k:2d}  →  Acuratețe: {acc * 100:.2f}%")

best_k   = k_values[np.argmax(accuracies)]
best_acc = max(accuracies)
print(f"\n Valoarea optimă: k = {best_k}  (acuratețe: {best_acc * 100:.2f}%)")
print(
    f"  Justificare: k = {best_k} oferă cel mai bun echilibru între bias și varianță "
    "pe acest set de date. Valori prea mici (k=1) sunt sensibile la zgomot, "
    "iar valori prea mari pot generaliza greșit."
)

plt.figure(figsize=(9, 4))
plt.plot(k_values, [a * 100 for a in accuracies], marker="o", color="#4C72B0", linewidth=2)
plt.axvline(best_k, color="red", linestyle="--", label=f"k optim = {best_k}")
plt.title("Acuratețea KNN în funcție de valoarea lui k")
plt.xlabel("Valoarea lui k")
plt.ylabel("Acuratețe (%)")
plt.xticks(k_values)
plt.legend()
plt.tight_layout()
plt.savefig("knn_acuratete_vs_k.png", dpi=150)
plt.show()
print("\n  Graficul a fost salvat: knn_acuratete_vs_k.png")


print("\n6. EVALUAREA MODELULUI")


knn_best = KNeighborsClassifier(n_neighbors=best_k)
knn_best.fit(X_train_scaled, y_train)
y_pred = knn_best.predict(X_test_scaled)

# 6.1 Matricea de confuzie
cm = confusion_matrix(y_test, y_pred)
print("\n6.1 Matricea de confuzie:")
print(cm)

fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
plt.colorbar(im, ax=ax)
ax.set(
    xticks=np.arange(3),
    yticks=np.arange(3),
    xticklabels=iris.target_names,
    yticklabels=iris.target_names,
    xlabel="Clasă prezisă",
    ylabel="Clasă reală",
    title=f"Matricea de confuzie (k={best_k})",
)
for i in range(3):
    for j in range(3):
        ax.text(j, i, cm[i, j], ha="center", va="center",
                color="white" if cm[i, j] > cm.max() / 2 else "black")
plt.tight_layout()
plt.savefig("knn_confusion_matrix.png", dpi=150)
plt.show()
print("  Graficul matricei de confuzie a fost salvat: knn_confusion_matrix.png")

# 6.2 Raport complet de clasificare
print("\n6.2 Raport complet de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))


print("7. VIZUALIZAREA DISTRIBUȚIEI FLORILOR IRIS")
print("   (după lungime și lățime petală)")

# Extragem doar coloanele 2 și 3: lungime petală și lățime petală
X_plot = X[:, [2, 3]]

plt.figure(figsize=(7, 5))

scatter = plt.scatter(
    X_plot[:, 0],
    X_plot[:, 1],
    c=y,
    cmap="viridis",       # paletă de culori clară pentru 3 clase
    edgecolors="k",       # contur negru pentru lizibilitate
    linewidths=0.4,
    alpha=0.85,
    s=60
)

plt.xlabel("Lungime petală (cm)")
plt.ylabel("Lățime petală (cm)")
plt.title("Distribuția florilor Iris după dimensiunile petalei")

handles, _ = scatter.legend_elements()
plt.legend(handles, iris.target_names, title="Clase")

plt.tight_layout()
plt.savefig("knn_distributie_iris.png", dpi=150)
plt.show()
print("  Graficul distribuției a fost salvat: knn_distributie_iris.png")