## Outstanding challenges in sentiment analysis

Jeremy Barnes [jeremycb@ifi.uio.no]

This repo contains a challenging dataset for sentiment analysis, as well as a python script to calculate per class results presented in at BlackboxNLP 2019.


Jeremy Barnes, Lilja Øvrelid, and Erik Velldal. 2019. [**Sentiment analysis is not solved!: Assessing and probing sentiment classification**](https://jbarnesspain.github.io/downloads/challenges.pdf). In *Proceedings of the 2019 {ACL} Workshop {B}lackbox{NLP}: Analyzing and Interpreting Neural Networks for {NLP}*. To appear.


If you use the code for academic research, please cite the paper in question:
```
@inproceedings{barnes-etal2019-challenges,
  author =  "Barnes, Jeremy
        and {\O}vrelid, Lilja
        and Velldal, Erik",
  title =   Sentiment analysis is not solved!: Assessing and probing sentiment classification",
  booktitle =   "Proceedings of the 2019 {ACL} Workshop {B}lackbox{NLP}: Analyzing and Interpreting Neural Networks for {NLP}",
  year =    "2019",
  publisher =   "Association for Computational Linguistics",
  pages =   "To Appear",
  location =    "Florence, Italy",
  url =     "To Appear"
}
```




It was created by finding the subset of instances from six sentence-level sentiment datasets ([MPQA polarity](http://aclweb.org/anthology/N15-1146), [OpeNER](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/4891), [SemEval 2013 Task 2](https://www.cs.york.ac.uk/semeval-2013/task2.html), [Stanford Sentiment Treebank](http://aclweb.org/anthology/D/D13/D13-1170.pdf), [Täckström Dataset](https://github.com/oscartackstrom/sentence-sentiment-data), [Thelwall Datasets](http://sentistrength.wlv.ac.uk/)) that an oracle ensemble of models ([Bag-of-Words + L2 regularized Logistic Regression](https://aclanthology.info/papers/W17-5202/w17-5202), [BiLSTM](https://aclanthology.info/papers/W17-5202/w17-5202), [ELMo](https://aclanthology.coli.uni-saarland.de/papers/N18-1202/n18-1202), [BERT](https://arxiv.org/abs/1810.04805)).

We performed a thorough error analysis of the data by annotating each sentence for 19 linguistic and paralinguistic categories. Sentences may contain more than a single category.

## Dataset

The dataset contains 836 sentences in a tab separated format:

sentence index -- dataset it comes from -- index within that dataset -- gold label -- text -- error annotations

The gold labels range from 0 (Strong Negative) to 5 (Strong Positive).


## Use

First, use your favorite models to get predictions for the test.txt data. Each prediction file should contain an integer prediction (0-5) for each sentence in test.txt (one per line). See example_pred_file.txt to ensure your file is similar.



```
python3 analyze_predictions.py [prediction_files]
```

Challenge dataset file: annotated.txt
Testing predictions from example_pred.txt/
model               pos    neg    mixed    no-sent    spelling    desirable    idioms    strong    negated    w-know    amp.    comp.    irony    shift    emoji    modal    morph.    red.    vocab
----------------  -----  -----  -------  ---------  ----------  -----------  --------  --------  ---------  --------  ------  -------  -------  -------  -------  -------  --------  ------  -------
example_pred.txt   16.0   55.4     14.6        1.0        53.1         44.9      18.8      18.6       30.7      32.4    33.3     33.3     45.8     62.2     72.2     45.7       7.4    15.4     12.7



