# -*- coding: utf-8 -*-
"""Untitled45.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qj3aNonFX7Br-RCyAGpiD25wNLy48o5r
"""

import pandas as pd
import numpy as np

import pandas as pd
dataset=pd.read_csv("/content/DFU121 - Copy.csv")

print(dataset)

dataset.shape

from sklearn.utils import shuffle
data=shuffle(dataset)

print(data)

from collections import Counter

print(sorted(Counter(data['Label']).items()))

diab=data[data['Label']==1]
non_daib=data[data['Label']==0]

print(diab.shape)
print(non_daib.shape)

p=data
q=data['Label']

from imblearn import under_sampling,over_sampling

from imblearn.over_sampling import RandomOverSampler
ros=RandomOverSampler(random_state=0)
X_resampled,y_resampled=ros.fit_resample(p,q)
print(sorted(Counter(y_resampled.items())),y_resampled.shape)

print(X_resampled)

X_resampled.shape

print(sorted(Counter(X_resampled['Label']).items()))

dataset = pd.DataFrame(X_resampled,
				columns = ['Subject','Gender', 'Age','General','LCA','LPA','MCA','MPA',
							'TCI','Label'])

n = 1
X = X_resampled.iloc[:, :-n].values
y = X_resampled.iloc[:, -n].values

print(X.shape)

print(X)

df1 = pd.DataFrame(X,
				columns = ['Subject','Gender', 'Age','General','LCA','LPA','MCA','MPA',
							'TCI'])
df1

df2 = pd.DataFrame(y,
				columns = ['Label'])

df3 = pd.DataFrame(X,
				columns = ['Subject','Gender', 'Age','General','LCA','LPA','MCA','MPA',
							'TCI'])

df3.drop('Subject',axis=1,inplace=True)

df3.shape

print(df2.shape)

print(df2)

df=df1.join(df2)

print(df)

print(df1)

print(df2)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = pd.DataFrame(le.fit_transform(df1.Gender))

print(y)

y = y.rename({0: 'Gender'}, axis=1)

print(y)

df1.drop('Gender', axis=1, inplace=True)

print(df1)

df1 = df1.join(y)

print(df1)

print(df2)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y1 = pd.DataFrame(le.fit_transform(df1.Subject))

print(y1)

df1.drop('Subject', axis=1, inplace=True)

print(df1)

y1 = y1.rename({0: 'Subject'}, axis=1)

df1 = df1.join(y1)

print(df1)

print(df2)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df1, df2, test_size = 0.2, random_state = 1)

temp_X_test = X_test.copy()
temp_y_test = y_test.copy()
temp_X_train = X_train.copy()
temp_y_train = y_train.copy()

X_train.shape

print(X_train)

X_test.shape

y_train.shape

print(y_train)

y_test.shape

print(X_train)

p_train=X_train
p_train.drop('Subject',axis=1,inplace=True)

p_train

p_test=X_test
p_test.drop('Subject',axis=1,inplace=True)

p_test

X_train

print(y_train)

print(y_test)

print(X_test)

import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import collections
import csv

import os
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class_values = sorted(df["Subject"].unique())
class_idx = {name: id for id, name in enumerate(class_values)}

print(df.sample(5).T)

print(df.Subject.value_counts())

plt.figure(figsize=(10, 10))
colors = df["Subject"].tolist()

class_values = sorted(df["Label"].unique())

print(class_values)

class_idx = {name: id for id, name in enumerate(class_values)}

p_train

feature_names = set(p_train.columns)
num_features = len(feature_names)
num_classes = 2
feature=set(df2.columns)
len_feature=len(feature)

print(len_feature)
len(feature_names)

df3.to_numpy()

x_train =   p_train[feature_names].to_numpy()
x_test =   p_test[feature_names].to_numpy()
y_train = y_train[feature].to_numpy()
y_test = y_test[feature].to_numpy()

print(x_test)

print(x_train)
len(x_train)
x_train.shape

import os
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

data.shape
hidden_units = [32, 32]
learning_rate = 0.001
dropout_rate = 0.1
num_epochs = 1000
batch_size = 5

def run_experiment(model, x_train, y_train):
    # Compile the model.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate),
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[keras.metrics.SparseCategoricalAccuracy(name="acc")],
    )
    # Create an early stopping callback.
    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_acc", patience=50, restore_best_weights=True
    )
    # Fit the model.
    history = model.fit(
        x=x_train,
        y=y_train,
        epochs=num_epochs,
        batch_size=batch_size,
        validation_split=0.20,
        callbacks=[early_stopping],
    )

    return history

def display_learning_curves(history):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    ax1.plot(history.history["loss"])
    ax1.plot(history.history["val_loss"])
    ax1.legend(["train", "test"], loc="upper right")
    ax1.set_xlabel("Epochs")
    ax1.set_ylabel("Loss")

    ax2.plot(history.history["acc"])
    ax2.plot(history.history["val_acc"])
    ax2.legend(["train", "test"], loc="upper right")
    ax2.set_xlabel("Epochs")
    ax2.set_ylabel("Accuracy")
    plt.show()

def create_ffn(hidden_units, dropout_rate, name=None):
    fnn_layers = []

    for units in hidden_units:
        fnn_layers.append(layers.BatchNormalization())
        fnn_layers.append(layers.Dropout(dropout_rate))
        fnn_layers.append(layers.Dense(units, activation=tf.nn.gelu))

    return keras.Sequential(fnn_layers, name=name)

feature_names = set(df1.columns)
num_features = len(feature_names)
num_classes = 2

import tensorflow
X_train = np.asarray(x_train).astype(np.float32)
y_train = np.asarray(y_train).astype(np.float32)

print(X_train)

import tensorflow
X_test = np.asarray(X_test).astype(np.float32)
y_test = np.asarray(y_test).astype(np.float32)
print(X_test)

edges = df[["Subject", "Label"]].to_numpy().T
edge_weights = tf.ones(shape=edges.shape[1])

from keras.models import Sequential
from keras import applications

import tensorflow as tf

edges = df[["Subject", "Label"]].to_numpy().T
# Create an edge weights array of ones.
edge_weights = tf.ones(shape=edges.shape[1])
# Create a node features array of shape [num_nodes, num_features].

node_features = tf.cast(
    df1.sort_values("Subject")[feature_names].to_numpy().astype(np.float32),
    dtype=tf.dtypes.float32
)

# Create graph info tuple with node_features, edges, and edge_weights.
graph_info = (node_features, edges, edge_weights)

print("Edges shape:", edges.shape)
print("Nodes shape:", node_features.shape)

print("Edges shape:", edges.shape)

def create_baseline_model(hidden_units, num_classes, dropout_rate=0.2):
    inputs = layers.Input(shape=(num_features,), name="input_features")
    x = create_ffn(hidden_units, dropout_rate, name=f"ffn_block1")(inputs)
    for block_idx in range(4):
        # Create an FFN block.
        x1 = create_ffn(hidden_units, dropout_rate, name=f"ffn_block{block_idx + 2}")(x)
        # Add skip connection.
        x = layers.Add(name=f"skip_connection{block_idx + 2}")([x, x1])
    # Compute logits.
    logits = layers.Dense(num_classes, name="logits")(x)
    # Create the model.
    return keras.Model(inputs=inputs, outputs=logits, name="baseline")


baseline_model = create_baseline_model(hidden_units, num_classes, dropout_rate)
baseline_model.summary()

history = run_experiment(baseline_model, X_train, y_train)

class GraphConvLayer(layers.Layer):
    def __init__(
        self,
        hidden_units,
        dropout_rate=0.15,
        aggregation_type="mean",
        combination_type="concat",
        normalize=False,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self.aggregation_type = aggregation_type
        self.combination_type = combination_type
        self.normalize = normalize

        self.ffn_prepare = create_ffn(hidden_units, dropout_rate)
        if self.combination_type == "gated":
            self.update_fn = layers.GRU(
                units=hidden_units,
                activation="tanh",
                recurrent_activation="sigmoid",
                dropout=dropout_rate,
                return_state=True,
                recurrent_dropout=dropout_rate,
            )
        else:
            self.update_fn = create_ffn(hidden_units, dropout_rate)

    def prepare(self, node_repesentations, weights=None):
        # node_repesentations shape is [num_edges, embedding_dim].
        messages = self.ffn_prepare(node_repesentations)
        if weights is not None:
            messages = messages * tf.expand_dims(weights, -1)
        return messages

    def aggregate(self, node_indices, neighbour_messages, node_repesentations):
        # node_indices shape is [num_edges].
        # neighbour_messages shape: [num_edges, representation_dim].
        # node_repesentations shape is [num_nodes, representation_dim]
        num_nodes = node_repesentations.shape[0]
        print(node_repesentations.shape,node_indices.shape)
        if self.aggregation_type == "sum":
            aggregated_message = tf.math.unsorted_segment_sum(
                neighbour_messages, node_indices-1, num_segments=num_nodes
            )
        elif self.aggregation_type == "mean":
            aggregated_message = tf.math.unsorted_segment_mean(
                neighbour_messages, node_indices, num_segments=num_nodes
            )
        elif self.aggregation_type == "max":
            aggregated_message = tf.math.unsorted_segment_max(
                neighbour_messages, node_indices, num_segments=num_nodes
            )
        else:
            raise ValueError(f"Invalid aggregation type: {self.aggregation_type}.")

        return aggregated_message

    def update(self, node_repesentations, aggregated_messages):
        # node_repesentations shape is [num_nodes, representation_dim].
        # aggregated_messages shape is [num_nodes, representation_dim].
        if self.combination_type == "gru":
            # Create a sequence of two elements for the GRU layer.
            h = tf.stack([node_repesentations, aggregated_messages], axis=1)
        elif self.combination_type == "concat":
            # Concatenate the node_repesentations and aggregated_messages.
            h = tf.concat([node_repesentations, aggregated_messages], axis=1)
        elif self.combination_type == "add":
            # Add node_repesentations and aggregated_messages.
            h = node_repesentations + aggregated_messages
        else:
            raise ValueError(f"Invalid combination type: {self.combination_type}.")

        # Apply the processing function.
        node_embeddings = self.update_fn(h)
        if self.combination_type == "gru":
            node_embeddings = tf.unstack(node_embeddings, axis=1)[-1]

        if self.normalize:
            node_embeddings = tf.nn.l2_normalize(node_embeddings, axis=-1)
        return node_embeddings

    def call(self, inputs):
        """Process the inputs to produce the node_embeddings.

        inputs: a tuple of three elements: node_repesentations, edges, edge_weights.
        Returns: node_embeddings of shape [num_nodes, representation_dim].
        """

        node_repesentations, edges, edge_weights = inputs
        # Get node_indices (source) and neighbour_indices (target) from edges.
        node_indices, neighbour_indices = edges[0], edges[1]
        # neighbour_repesentations shape is [num_edges, representation_dim].
        neighbour_repesentations = tf.gather(node_repesentations, tf.cast(neighbour_indices, tf.int32)
)

        # Prepare the messages of the neighbours.
        neighbour_messages = self.prepare(neighbour_repesentations, edge_weights)
        # Aggregate the neighbour messages.
        aggregated_messages = self.aggregate(
           tf.cast(node_indices, tf.int32), neighbour_messages, node_repesentations
        )
        # Update the node embedding with the neighbour messages.
        return self.update(node_repesentations, aggregated_messages)

class GNNNodeClassifier(tf.keras.Model):
    def __init__(
        self,
        graph_info,
        num_classes,
        hidden_units,
        aggregation_type="sum",
        combination_type="concat",
        dropout_rate=0.1,
        normalize=True,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        # Unpack graph_info to three elements: node_features, edges, and edge_weight.
        node_features, edges, edge_weights = graph_info
        self.node_features = node_features
        self.edges = edges
        self.edge_weights = edge_weights
        # Set edge_weights to ones if not provided.
        if self.edge_weights is None:
            self.edge_weights = tf.ones(shape=edges.shape[1])
        # Scale edge_weights to sum to 1.
        self.edge_weights = self.edge_weights / tf.math.reduce_sum(self.edge_weights)

        # Create a process layer.
        self.preprocess = create_ffn(hidden_units, dropout_rate, name="preprocess")
        # Create the first GraphConv layer.
        self.conv1 = GraphConvLayer(
            hidden_units,
            dropout_rate,
            aggregation_type,
            combination_type,
            normalize,
            name="graph_conv1",
        )
        # Create the second GraphConv layer.
        self.conv2 = GraphConvLayer(
            hidden_units,
            dropout_rate,
            aggregation_type,
            combination_type,
            normalize,
            name="graph_conv2",
        )

        # Create a postprocess layer.
        self.postprocess = create_ffn(hidden_units, dropout_rate, name="postprocess")
        # Create a compute logits layer.
        self.compute_logits = layers.Dense(units=num_classes, name="logits")

    def call(self, input_node_indices):
        print(input_node_indices)

        # Preprocess the node_features to produce node representations.
        x = self.preprocess(self.node_features)
        # Apply the first graph conv layer.
        x1 = self.conv1((x, tf.convert_to_tensor(self.edges, dtype=tf.float32), self.edge_weights))
        # Skip connection.
        x = x1 + x
        # Apply the second graph conv layer.
        x2 = self.conv2((x, tf.convert_to_tensor(self.edges, dtype=tf.float32), self.edge_weights))
        # Skip connection.
        x = x2 + x
        #x3 = self.conv3((x, tf.convert_to_tensor(self.edges, dtype=tf.float32), self.edge_weights))
        # Skip connection.
        #x = x3 + x
        #x4 = self.conv4((x, tf.convert_to_tensor(self.edges, dtype=tf.float32), self.edge_weights))
        # Skip connection.
        #x = x4 + x
        # Postprocess node embedding.
        x = self.postprocess(x)
        # Fetch node embeddings for the input node_indices.
        node_embeddings = tf.gather(x, input_node_indices)
        # Compute logits
        return self.compute_logits(node_embeddings)

from tensorflow import keras
from keras.models import Sequential
import tensorflow as tf

gnn_model = GNNNodeClassifier(
    graph_info=graph_info,
    num_classes=num_classes,
    hidden_units=hidden_units,
    dropout_rate=dropout_rate,
    name="gnn_model",
)

print("GNN output shape:", gnn_model([1, 10, 100]))

gnn_model.summary()

X_train = temp_X_train.Subject.to_numpy()
y_train=temp_y_train.Label.to_numpy()
# history = run_experiment(gnn_model, X_train, df2.Label.y_train)

print(X_train)

#x_train = train_data.paper_id.to_numpy()
history = run_experiment(gnn_model, X_train, y_train)

history.history['acc']

from tensorflow.python.ops.math_ops import mean
import statistics
from statistics import mean


mean(history.history['acc'])

fig, ax1 = plt.subplots(1, figsize=(8, 4))

ax1.plot(history.history["loss"])
ax1.plot(history.history["val_loss"])
ax1.legend(["Train", "Test"],fontsize="20", loc="upper right")
ax1.set_xlabel("Epochs",fontsize=16)
ax1.set_ylabel("Loss",fontsize=16)

fig, ax2 = plt.subplots(1, figsize=(8, 4))
ax2.plot(history.history["acc"])
ax2.plot(history.history["val_acc"])
ax2.legend(["Train", "Test"],fontsize="20", loc="upper right")
ax2.set_xlabel("Epochs",fontsize=16)
ax2.set_ylabel("Accuracy",fontsize=16)
plt.show()

X_test = temp_X_test.Subject.to_numpy()
y_test=temp_y_test.Label.to_numpy()
# history = run_experiment(gnn_model, X_train, df2.Label.y_train)

_, test_accuracy = gnn_model.evaluate(X_test,y_test, verbose=0)
print(test_accuracy)
print(f"Test accuracy: {round(test_accuracy * 100, 2)}%")

import tensorflow as tf
x = tf.constant([44,33.61,33.38,33.82,33.43,33.66,33.57,0,11])
x = tf.cast(x, tf.int32)
p=gnn_model.predict(x)
print(p)

y_pred=gnn_model.predict(X_test)
print(y_pred)
len(y_pred)

rounded_predictions=np.argmax(y_pred,axis=-1)
len(rounded_predictions)

for i in rounded_predictions:
  print(i)

from sklearn.metrics import classification_report
print(classification_report(y_test,rounded_predictions))

plt.savefig('destination_pathclass_report.eps', format='eps')

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt

cm=confusion_matrix(y_true=y_test,y_pred=rounded_predictions)

def plot_confusion_matrix(cm,classes,normalize=False,title='Confusion_matrix,cmap=plt.cm.blues'):
  plt.imshow(cm,interpolation='nearest',cmap=cmap)
  plot.title(title)
  plt.colorbar()
  tick_marks=np.arrange(len(classes))
  plt.xticks(tick_marks,classes,rotation=45)
  plt.ytick(tick_marks,classes)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

cnf_matrix = confusion_matrix(y_test, rounded_predictions, labels=[0,1])
np.set_printoptions(precision=2)

# Plot confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=['Infected_Foot','Healthy_Foot'],normalize= False,  title='Confusion matrix')

plt.savefig('destination_pathconfusionmatrix.eps', format='eps')

sensitivity = cm[0,0]/(cm[0,0]+cm[0,1])
print(sensitivity)

specificity = cm[1,1]/(cm[1,0]+cm[1,1])
print('Specificity : ', specificity)