import random
import numpy as np
import tensorflow
random.seed(42)
np.random.seed(42)
tensorflow.set_random_seed(42)

# Models and Utils scripts
from code.models import *
from code.utils import *


# Load entire data
train_w, train_t1, train_t2, train_t3, train_t4 = load_data("data/train.txt")
test_w, test_t1, test_t2, test_t3, test_t4 = load_data("data/test.txt")
validation_w, validation_t1, validation_t2, validation_t3, validation_t4 = load_data("data/valid.txt")

# Training data
X_train_w  = train_w
y_train1_w = train_t1
y_train2_w = train_t3
y_train3_w = train_t4

# Testing data
X_test_w  = test_w
y_test1_w = test_t1
y_test2_w = test_t3
y_test3_w = test_t4


# Validation data
X_valid_w  = validation_w
y_valid1_w = validation_t1
y_valid2_w = validation_t3
y_valid3_w = validation_t4



# Merge digits under the same word
digits_word = "$NUM$" 
X_train_w, X_test_w, X_valid_w = mergeDigits([X_train_w, X_test_w, X_valid_w], digits_word)

# Compute indexes for words+labels in the training data
ukn_words = "out-of-vocabulary"   # Out-of-vocabulary words entry in the "words to index" dictionary
word2ind,   ind2word   =  indexData_x(X_train_w, ukn_words)
label2ind1, ind2label1 =  indexData_y(y_train1_w)
label2ind2, ind2label2 =  indexData_y(y_train2_w)
label2ind3, ind2label3 =  indexData_y(y_train3_w)

print(ind2label1)
print(ind2label2)
print(ind2label3)



# Convert data into indexes data
maxlen  = max([len(xx) for xx in X_train_w])
padding_style   = 'pre'                 # 'pre' or 'post': Style of the padding, in order to have sequence of the same size
X_train   = encodePadData_x(X_train_w,  word2ind,   maxlen, ukn_words, padding_style)
X_test    = encodePadData_x(X_test_w,   word2ind,   maxlen, ukn_words, padding_style)
X_valid   = encodePadData_x(X_valid_w,  word2ind,   maxlen, ukn_words, padding_style)

y_train1  = encodePadData_y(y_train1_w, label2ind1, maxlen, padding_style)
y_test1   = encodePadData_y(y_test1_w,  label2ind1, maxlen, padding_style)
y_valid1  = encodePadData_y(y_valid1_w, label2ind1, maxlen, padding_style)

y_train2  = encodePadData_y(y_train2_w, label2ind2, maxlen, padding_style)
y_test2   = encodePadData_y(y_test2_w,  label2ind2, maxlen, padding_style)
y_valid2  = encodePadData_y(y_valid2_w, label2ind2, maxlen, padding_style)

y_train3  = encodePadData_y(y_train3_w, label2ind3, maxlen, padding_style)
y_test3   = encodePadData_y(y_test3_w,  label2ind3, maxlen, padding_style)
y_valid3  = encodePadData_y(y_valid3_w, label2ind3, maxlen, padding_style)



# Create the character level data
char2ind, maxWords, maxChar = characterLevelIndex(X_train_w, digits_word)
X_train_char = characterLevelData(X_train_w, char2ind, maxWords, maxChar, digits_word, padding_style)
X_test_char  = characterLevelData(X_test_w,  char2ind, maxWords, maxChar, digits_word, padding_style)
X_valid_char = characterLevelData(X_valid_w, char2ind, maxWords, maxChar, digits_word, padding_style)






y_train = [y_train1, y_train2, y_train3]
y_test  = [y_test1,  y_test2,  y_test3] 
y_valid = [y_valid1, y_valid2, y_valid3]
ind2label = [ind2label1, ind2label2, ind2label3]



# MODEL PARAMETERS

"""
	BATCH:   	 [100, 70, 30]
	DROPOUT:  	 [0.7, 0.5, 0.2]
	LSTM SIZE:   [200, 100, 40]
"""

models = []
models.append({"name":"multi_task_b100_d7_lstm200",   "batch":100, "dropout":0.7, "lstm_size":200})
models.append({"name":"multi_task_b100_d7_lstm100",   "batch":100, "dropout":0.7, "lstm_size":100})
models.append({"name":"multi_task_b100_d7_lstm40",    "batch":100, "dropout":0.7, "lstm_size":40})
models.append({"name":"multi_task_b100_d5_lstm200",   "batch":100, "dropout":0.5, "lstm_size":200})
models.append({"name":"multi_task_b100_d5_lstm100",   "batch":100, "dropout":0.5, "lstm_size":100})
models.append({"name":"multi_task_b100_d5_lstm40",    "batch":100, "dropout":0.5, "lstm_size":40})
models.append({"name":"multi_task_b100_d2_lstm200",   "batch":100, "dropout":0.2, "lstm_size":200})
models.append({"name":"multi_task_b100_d2_lstm100",   "batch":100, "dropout":0.2, "lstm_size":100})
models.append({"name":"multi_task_b100_d2_lstm40",    "batch":100, "dropout":0.2, "lstm_size":40})

models.append({"name":"multi_task_b70_d7_lstm200",    "batch":70, "dropout":0.7, "lstm_size":200})
models.append({"name":"multi_task_b70_d7_lstm100",    "batch":70, "dropout":0.7, "lstm_size":100})
models.append({"name":"multi_task_b70_d7_lstm40",     "batch":70, "dropout":0.7, "lstm_size":40})
models.append({"name":"multi_task_b70_d5_lstm200",    "batch":70, "dropout":0.5, "lstm_size":200})
models.append({"name":"multi_task_b70_d5_lstm100",    "batch":70, "dropout":0.5, "lstm_size":100})
models.append({"name":"multi_task_b70_d5_lstm40",     "batch":70, "dropout":0.5, "lstm_size":40})
models.append({"name":"multi_task_b70_d2_lstm200",    "batch":70, "dropout":0.2, "lstm_size":200})
models.append({"name":"multi_task_b70_d2_lstm100",    "batch":70, "dropout":0.2, "lstm_size":100})
models.append({"name":"multi_task_b70_d2_lstm40",     "batch":70, "dropout":0.2, "lstm_size":40})

models.append({"name":"multi_task_b30_d7_lstm200",    "batch":30, "dropout":0.7, "lstm_size":200})
models.append({"name":"multi_task_b30_d7_lstm100",    "batch":30, "dropout":0.7, "lstm_size":100})
models.append({"name":"multi_task_b30_d7_lstm40",     "batch":30, "dropout":0.7, "lstm_size":40})
models.append({"name":"multi_task_b30_d5_lstm200",    "batch":30, "dropout":0.5, "lstm_size":200})
models.append({"name":"multi_task_b30_d5_lstm100",    "batch":30, "dropout":0.5, "lstm_size":100})
models.append({"name":"multi_task_b30_d5_lstm40",     "batch":30, "dropout":0.5, "lstm_size":40})
models.append({"name":"multi_task_b30_d2_lstm200",    "batch":30, "dropout":0.2, "lstm_size":200})
models.append({"name":"multi_task_b30_d2_lstm100",    "batch":30, "dropout":0.2, "lstm_size":100})
models.append({"name":"multi_task_b30_d2_lstm40",     "batch":30, "dropout":0.2, "lstm_size":40})


# Run models
models_results = {}
for model in models:
	models_results[model['name']] = BiLSTM_model( model['name'], True, "crf",
												  [X_train, X_train_char], [X_test, X_test_char], word2ind, maxWords,
												  y_train, y_test, ind2label,
												  validation=False,
												  pretrained_embedding=True word_embedding_size=300,
												  maxChar=maxChar, char_embedding_type="BILSTM", char2ind=char2ind, char_embedding_size=100,
												  lstm_hidden=model["lstm_size"], batch_size=model["batch"], dropout=model["dropout"],
												  nbr_epochs=25, gen_confusion_matrix=True, early_stopping_patience=5
												)


# Report each model's best score in a csv file
model_columns = ["Model", "Best epoch", "Training Accuracy", "Training Recall", "Training F1", "Testing Accuracy", "Testing Recall", "Testing F1"]
write_to_csv("model_results/model_scores", model_columns, [[k]+v for k,v in models_results.items()])

print("FINITO")