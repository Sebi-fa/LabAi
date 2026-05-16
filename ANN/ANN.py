import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist, fashion_mnist

tf.random.set_seed(42)
np.random.seed(42)


def build_model(hidden_units=128, activation='relu'):
    model = keras.Sequential([
        keras.Input(shape=(28, 28)),
        layers.Flatten(),
        layers.Dense(hidden_units, activation=activation),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model


print("EXERCITIUL 1: Incarcarea si normalizarea datelor MNIST")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f"Forma datelor de antrenament: {x_train.shape}")
print(f"Forma etichetelor de antrenament: {y_train.shape}")
print(f"Forma datelor de test: {x_test.shape}")
print(f"Forma etichetelor de test: {y_test.shape}")
print(f"Valoarea minima a unui pixel (inainte de normalizare): {x_train.min()}")
print(f"Valoarea maxima a unui pixel (inainte de normalizare): {x_train.max()}")

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

print(f"Valoarea minima dupa normalizare: {x_train.min()}")
print(f"Valoarea maxima dupa normalizare: {x_train.max()}")
print()


print("EXERCITIUL 2: Crearea modelului Sequential")

model = build_model(hidden_units=128, activation='relu')
model.summary()
print()


print("EXERCITIUL 3: Antrenarea si evaluarea modelului")

history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\nLoss pe setul de test: {test_loss:.4f}")
print(f"Acuratete pe setul de test: {test_acc:.4f} ({test_acc*100:.2f}%)")
print()


print("EXERCITIUL 4: Afisarea unei imagini si a predictiei")

index = 0
test_image = x_test[index]
true_label = y_test[index]

predictions = model.predict(np.expand_dims(test_image, axis=0), verbose=0)
predicted_label = np.argmax(predictions[0])
confidence = predictions[0][predicted_label] * 100

print(f"Eticheta reala: {true_label}")
print(f"Eticheta prezisa: {predicted_label}")
print(f"Incredere: {confidence:.2f}%")

plt.figure(figsize=(6, 6))
plt.imshow(test_image, cmap='gray')
plt.title(f"Real: {true_label} | Prezis: {predicted_label} ({confidence:.1f}%)")
plt.axis('off')
plt.savefig('ex4_predictie_mnist.png', dpi=100, bbox_inches='tight')
plt.show()
print("Imaginea a fost salvata in 'ex4_predictie_mnist.png'")
print()


print("EXERCITIUL 5: Variatia numarului de neuroni din stratul ascuns")

neuroni_de_testat = [32, 128, 512]
rezultate_neuroni = {}

for nr_neuroni in neuroni_de_testat:
    print(f"\n--- Antrenare model cu {nr_neuroni} neuroni in stratul ascuns ---")
    model_temp = build_model(hidden_units=nr_neuroni, activation='relu')
    model_temp.fit(x_train, y_train, epochs=3, batch_size=32, verbose=0)
    _, acc = model_temp.evaluate(x_test, y_test, verbose=0)
    rezultate_neuroni[nr_neuroni] = acc
    print(f"Acuratete cu {nr_neuroni} neuroni: {acc*100:.2f}%")

print("\nObservatie:")
print("  - Putini neuroni (32):  modelul este simplu, poate sa nu invete suficient")
print("                          (underfitting - acuratete mica).")
print("  - Mediu (128):          echilibru bun intre complexitate si performanta.")
print("  - Multi neuroni (512):  modelul este complex, invata mai bine,")
print("                          dar e mai lent si poate face overfitting.")
print()


print("EXERCITIUL 6: Variatia numarului de epoci")

epoci_de_testat = [1, 5, 10]
rezultate_epoci = {}

for nr_epoci in epoci_de_testat:
    print(f"\n--- Antrenare cu {nr_epoci} epoci ---")
    model_temp = build_model(hidden_units=128, activation='relu')
    model_temp.fit(x_train, y_train, epochs=nr_epoci, batch_size=32, verbose=0)
    _, acc = model_temp.evaluate(x_test, y_test, verbose=0)
    rezultate_epoci[nr_epoci] = acc
    print(f"Acuratete dupa {nr_epoci} epoci: {acc*100:.2f}%")

print("\nObservatie:")
print("  - 1 epoca:    modelul invata doar partial, acuratete mai mica.")
print("  - 5 epoci:    acuratetea creste, modelul invata bine.")
print("  - 10+ epoci:  cresterea acuratetii incetineste, risc de overfitting.")
print()


print("EXERCITIUL 7: Compararea functiilor de activare ReLU vs tanh")

functii_activare = ['relu', 'tanh']
rezultate_activare = {}

for activare in functii_activare:
    print(f"\n--- Antrenare cu activare: {activare} ---")
    model_temp = build_model(hidden_units=128, activation=activare)
    model_temp.fit(x_train, y_train, epochs=3, batch_size=32, verbose=0)
    _, acc = model_temp.evaluate(x_test, y_test, verbose=0)
    rezultate_activare[activare] = acc
    print(f"Acuratete cu {activare}: {acc*100:.2f}%")

print("\nObservatie:")
print("  - ReLU: f(x) = max(0, x).")
print("          Rapida, evita problema gradientilor dispari, dominanta in DL modern.")
print("  - tanh: f(x) intre -1 si 1.")
print("          Mai lenta, poate avea gradient mic la extreme (vanishing gradient).")
print("  - In general, ReLU performeaza mai bine in straturile ascunse moderne.")
print()


print("EXERCITIUL 8: Aplicarea modelului pe Fashion-MNIST")

(x_train_f, y_train_f), (x_test_f, y_test_f) = fashion_mnist.load_data()

nume_clase_fashion = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

x_train_f = x_train_f.astype("float32") / 255.0
x_test_f = x_test_f.astype("float32") / 255.0

print(f"Forma datelor de antrenament: {x_train_f.shape}")
print(f"Clase: {nume_clase_fashion}")

model_fashion = build_model(hidden_units=128, activation='relu')

print("\nAntrenare model pe Fashion-MNIST...")
model_fashion.fit(x_train_f, y_train_f, epochs=5, batch_size=32, verbose=1)

test_loss_f, test_acc_f = model_fashion.evaluate(x_test_f, y_test_f, verbose=0)
print(f"\nAcuratete pe Fashion-MNIST: {test_acc_f*100:.2f}%")
print(f"(comparativ cu MNIST: {test_acc*100:.2f}%)")
print("\nObservatie:")
print("  - Fashion-MNIST este mai dificil decat MNIST.")
print("  - Cifrele scrise de mana sunt mai simplu de distins decat hainele,")
print("    care au texturi si forme mai variate.")
print("  - Acuratetea pe Fashion-MNIST este de obicei cu ~5-10% mai mica.")

index_f = 0
test_image_f = x_test_f[index_f]
true_label_f = y_test_f[index_f]
predictions_f = model_fashion.predict(np.expand_dims(test_image_f, axis=0), verbose=0)
predicted_label_f = np.argmax(predictions_f[0])
confidence_f = predictions_f[0][predicted_label_f] * 100

plt.figure(figsize=(6, 6))
plt.imshow(test_image_f, cmap='gray')
plt.title(
    f"Real: {nume_clase_fashion[true_label_f]} | "
    f"Prezis: {nume_clase_fashion[predicted_label_f]} ({confidence_f:.1f}%)"
)
plt.axis('off')
plt.savefig('ex8_predictie_fashion.png', dpi=100, bbox_inches='tight')
plt.show()
print(f"\nPredictie pentru o imagine din Fashion-MNIST:")
print(f"  Real:   {nume_clase_fashion[true_label_f]}")
print(f"  Prezis: {nume_clase_fashion[predicted_label_f]} ({confidence_f:.1f}%)")
print()

print("Toate exercitiile rezolvate cu succes!")