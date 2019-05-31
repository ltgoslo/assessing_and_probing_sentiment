import argparse
from sklearn.metrics import accuracy_score
import numpy as np
from tabulate import tabulate

def import_challenge_dataset(dataset_file):
    idxs = []
    datasets = []
    original_idxs = []
    golds = []
    texts = []
    annotations = []

    for i, line in enumerate(open(dataset_file)):
        idx, dataset, original_idx, gold, text, ann = line.split("\t")
        idxs.append(int(idx))
        datasets.append(dataset)
        original_idxs.append(int(original_idx))
        golds.append(int(gold))
        texts.append(text)
        annotations.append(ann)

    # create annotation dictionary where keys are annotation labels
    # and values are a set of the indexes where this annotation occurs
    annotation_dict = {}
    for i, annotation in enumerate(annotations):
        for ann in annotation.split("::"):
            ann = ann.strip()
            if ann not in annotation_dict:
                # each label in the annotation dictionary is a set
                annotation_dict[ann] = set()
            # for each label, keep a set of the indexes where it occurs
            annotation_dict[ann].update([i])

    return (idxs, datasets, original_idxs, golds,
            texts, annotations, annotation_dict)

def import_prediction(prediction_file):
    return [int(l.strip()) for l in open(prediction_file)]

def main():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-challenge_dataset", default="challenge_dataset.txt")
    parser.add_argument("predictions", nargs="+")
    args = parser.parse_args()


    print("Challenge dataset file: {0}".format(args.challenge_dataset))

    print("Testing predictions from ", end="")
    for i in args.predictions:
        print(i, end="/ ")
    print()

    (idxs, datasets, original_idxs, golds,
    texts, annotations, annotation_dict) = import_challenge_dataset(args.challenge_dataset)

    preds = []
    for pred_file in args.predictions:
        preds.append(import_prediction(pred_file))


    # labels = ['amplified', 'comparative', 'desirable-element', 'difficult-vocab', 'emoji', 'mixed', 'morphology', 'negated', 'negative', 'no-sentiment', 'non-factual speech', 'positive', 'reduced', 'sarcasm/irony', 'set-phrase', 'shifted', 'spelling', 'strong', 'world-knowledge']

    labels = ['positive', 'negative', 'mixed', 'no-sentiment', 'spelling', 'desirable-element', 'set-phrase', 'strong', 'negated', 'world-knowledge', 'amplified', 'comparative', 'sarcasm/irony', 'shifted', 'emoji', 'non-factual speech', 'morphology', 'reduced', 'difficult-vocab']

    short_labels = ['model', 'pos', 'neg', 'mixed', 'no-sent', 'spelling', 'desirable', 'set-phr.', 'strong', 'negated', 'w-know', 'amp.', 'comp.', 'irony', 'shift', 'emoji', 'modal', 'morph.', 'reduced', 'vocab']



    results = []
    for i, model in enumerate(preds):
        model_results = []
        model_results.append(args.predictions[i])
        for label in labels:
            idxs = sorted(annotation_dict[label])
            #print(idxs)
            gold = np.array(golds)[idxs]
            pred = np.array(model)[idxs]
            acc = accuracy_score(gold, pred)
            model_results.append(acc * 100)
        results.append(model_results)

    print(tabulate(results, headers=short_labels, floatfmt=".1f"))


        #results.append([ model_results])




   # main()
