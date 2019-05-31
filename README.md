# Outstanding challenges in sentiment analysis

Jeremy Barnes [jeremycb@ifi.uio.no]

The idea is to find a subset of errors that all sentiment classifiers
still make and identify common characteristics, if there are any.

## Models
1. [Bag-of-Words + L2 regularized Logistic Regression](https://aclanthology.info/papers/W17-5202/w17-5202)
2. [BiLSTM](https://aclanthology.info/papers/W17-5202/w17-5202)
3. [ELMo](https://aclanthology.coli.uni-saarland.de/papers/N18-1202/n18-1202)
4. [BERT](https://arxiv.org/abs/1810.04805)

## Datasets
1. [MPQA polarity](http://aclweb.org/anthology/N15-1146)
2. [OpeNER](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/4891)
3. [SemEval 2013 Task 2](https://www.cs.york.ac.uk/semeval-2013/task2.html)
4. [Stanford Sentiment Treebank](http://aclweb.org/anthology/D/D13/D13-1170.pdf)
5. [Täckström Dataset](https://github.com/oscartackstrom/sentence-sentiment-data)
6. [Thelwall Datasets](http://sentistrength.wlv.ac.uk/)


### Requirements

1. Python 3
2. sklearn  ```pip install -U scikit-learn```
3. Keras ```pip install keras```
4. Pytorch ```pip install torch torchvision```
5. [H5py](http://docs.h5py.org/en/latest/build.html) ```pip install h5py```


