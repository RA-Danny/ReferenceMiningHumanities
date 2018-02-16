# Deep reference mining from humanities pubications

> Master semester project <br/>
> Digital Humanities Laboratory<br/>
> EPFL Fall 2017<br/>


> Student: **Rodrigues Alves Danny**<br/>
> Supervisor: Giovanni Colavizza

<br/>

## Repository organisation
- **BiLSTM**: Python scripts for a Bidirectional LSTM neural network. 
	- code/models.py: Script building the Keras model. Parameters allow network to use - or not - word embeddings, character-level featurs (CNN or BiLSTM) and a softmax or CRF prediction layer.
	- code/utils.py: Scripts containing helper functions for the models and main scripts.
	- main_modelComparison.py: Script to fine-tune parameters
	- main_multiTaskLearning.py: Script for a multi-task learning approach.
	- main_multiTaskLearning_finetune.py: Script to fine-tune parameters of a multi-task learning model.
	- main_threeTasks.py: Script launching three models, one per task
- **CRF**: Python code for the CRF baseline model.
- **Project Notebooks**: Jupyter Notebooks use through the entire project.
- **EPFL_MS_PROJECT_RodriguesDanny.pdf**: Project report

<br/>

 Note that the **data/** folder isn't present in this repository. The *data* folder must contain:
:	- test.txt
	- train.txt
	- valid.txt
	- pretrained_vectors/
		- vecs_100.txt
		- vecs_300.txt


<br/>

## Paper Abstract
This project considers the task of reference mining: the detection, extraction and classification of references within a plain text from humanities publications. Despite its similarities to Named Entity Recognition, reference mining applied to the field of arts and humanities brings forward specific difficulties, mainly the need to capture the richness of referencing styles,  referred objects, references locations and the morphology of highly abbreviated words. 

A deep learning approach requiring no explicit feature engineering is proposed, outperforming a Conditional Random Field model based on hand-crafted features. Several architectures and components are explored and discussed: word and character embeddings, hidden recurrent layers and their directionality, prediction layers (Softmax and CRF), single and multi-task learning. The results highlight the importance of character-level embeddings, which allow to learn word-level encoding styles and be more robust against OCR issues, and of the CRF prediction layer, convenient to consider the structural dependence among predictions. The BiLSTM-CRF neural network with both word and character features learns the compositionality of reference styles, from the encoding of its components at word level to their ordering at the reference level. Trained and tested on an annotated dataset of references from the historiography of Venice, the best model reaches a validation F1 score of  89.13% for reference components, 79.78% for generic tags and  94.34% for begin-end tags.\newline


**KEYWORDS**: Reference mining, Bibliometrics, NLP, Deep Learning, BiLSTM-CRF, Embeddings
