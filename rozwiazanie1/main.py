import pandas as pd
import numpy as np
import json
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score


#klasa węzła: potrzebna do tworzenia drzewa i serializacji
class Node:
    def __init__(self, attribute=None, split_value=None, children=None, class_label=None):
        self.attribute = attribute
        self.split_value = split_value
        self.children = children
        self.class_label = class_label


#index gini
def gini_index(data, attribute):
    class_counts = data[attribute].value_counts()
    class_probabilities = class_counts / len(data)
    gini = 1 - np.sum(class_probabilities ** 2)
    return gini

def gini_gain(data, attribute, split_value):
    subset1 = data[data[attribute] <= split_value]
    subset2 = data[data[attribute] > split_value]
    
    gini1 = gini_index(subset1, attribute)
    gini2 = gini_index(subset2, attribute)
    
    weighted_gini = (len(subset1) / len(data) * gini1) + (len(subset2) / len(data) * gini2)
    
    gini_gain = gini_index(data, attribute) - weighted_gini
    
    return gini_gain

# obliczenie najleprzego podziału
def best_split_point(data, attribute):
    unique_values = data[attribute].astype(float).unique()
    unique_values.sort()
    
    split_points = []
    for i in range(len(unique_values) - 1):
        split_value = (unique_values[i] + unique_values[i+1]) / 2
        split_points.append(split_value)
    
    return split_points


# korzeń algorytmu: tworzenie drzewa: rekursja
def build_decision_tree(data, max_depth=2, level=0):
    if level >= max_depth:
        class_label = data['class'].mode()[0]
        return Node(class_label=class_label)
    
    best_attribute = None
    best_split_value = None
    best_gini_gain = 0
    
    for attribute in data.columns[:-1]:
        split_values = best_split_point(data, attribute)
        
        for split_value in split_values:
            gini_gain_value = gini_gain(data, attribute, split_value)
            
            if gini_gain_value > best_gini_gain:
                best_gini_gain = gini_gain_value
                best_attribute = attribute
                best_split_value = split_value
    
    if best_attribute is None:
        class_label = data['class'].mode()[0]
        return Node(class_label=class_label)
    
    subset1 = data[data[best_attribute] <= best_split_value]
    subset2 = data[data[best_attribute] > best_split_value]
    
    children = []
    children.append(build_decision_tree(subset1, max_depth, level + 1))
    children.append(build_decision_tree(subset2, max_depth, level + 1))
    
    return Node(attribute=best_attribute, split_value=best_split_value, children=children)

# serializacja drzewa
def serialize_decision_tree(node):
    serialized_node = {}
    
    if node.attribute is not None:
        serialized_node['attribute'] = node.attribute
        serialized_node['split_value'] = node.split_value
        serialized_node['children'] = [serialize_decision_tree(child) for child in node.children]
    else:
        serialized_node['class_label'] = node.class_label
    
    return serialized_node


# funkcja dla predykcji
def prediction(node, data_point):
    if node.class_label is not None:
        return node.class_label
    
    attribute = node.attribute
    split_value = node.split_value
    
    if data_point[attribute] <= split_value:
        return prediction(node.children[0], data_point)
    else:
        return prediction(node.children[1], data_point)


df = pd.read_excel('result_uma.xlsx')
#zmiana typów
df['kable'] = df['kable'].astype(float)
df['protokol'] = df['protokol'].astype(float)
df['hopes'] = df['hopes'].astype(float)
df['class'] = df['class'].astype(str)


decision_tree = build_decision_tree(df, max_depth=4) ##pomyśleć odnośnie 3-5

serialized_tree = serialize_decision_tree(decision_tree)

json_tree = json.dumps(serialized_tree, indent=2)
print(" ")
print("drzewo decyzyjne zapisane w pliku json")
print(json_tree)


#dane testowe dla predykcji
dfp = pd.read_excel('predict100.xlsx')

df_copy = dfp.copy()
df_copy = df_copy.drop(df_copy.columns[-1], axis=1)

df_result = dfp.iloc[:, -1]

l = 0
num_rows = df_result.shape[0]
for i in range(len(df_copy)):
    row = df_copy.iloc[i]
    predicted_class = prediction(decision_tree, row)
  #  print(i, " ", predicted_class, " ", df_result.iloc[i])   funkcja porównuje resultaty
    df_result = df_result.astype(int)
    predicted_class = int(predicted_class)
    
    if predicted_class == df_result.iloc[i]:  
        l = l + 1
    
procent = l / len(df_copy)
print("")
print( "Accuracy: ", procent)



predicted_classes = []

for i in range(len(df_copy)):
    row = df_copy.iloc[i]
    predicted_class = prediction(decision_tree, row)
    predicted_class = int(predicted_class)
    predicted_classes.append(predicted_class)

predicted_classes = np.array(predicted_classes)


expected_classes =df_result.values

###############################################


# (Confusion Matrix)
confusion = confusion_matrix(expected_classes, predicted_classes)
print("Confusion Matrix:")
print(confusion)

#  (Classification Report)
classification_report = classification_report(expected_classes, predicted_classes)
print("Classification Report:")
print(classification_report)



