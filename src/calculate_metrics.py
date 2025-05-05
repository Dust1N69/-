def calculate_metrics(tp, fn, fp, tn):
    accuracy = (tp + tn) / (tp + fn + fp + tn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return accuracy, precision, recall, f1_score

# Model A
metrics_a = calculate_metrics(853, 576, 341, 7230)
# Model B
metrics_b = calculate_metrics(846, 583, 316, 7255)

print("Model A Metrics: Accuracy = {:.4f}, Precision = {:.4f}, Recall = {:.4f}, F1-Score = {:.4f}".format(*metrics_a))
print("Model B Metrics: Accuracy = {:.4f}, Precision = {:.4f}, Recall = {:.4f}, F1-Score = {:.4f}".format(*metrics_b))