import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score

class AnomalyScoreDetection:
    def __init__(self, logs):
        self.df = pd.DataFrame(logs)
        
    def _score(self, row):
        score = 0
        if row["latency"] > 1000: score += 1
        if row["priv"] == 1: score += 1
        if row["time"] in ["01:00", "02:00", "03:00"]: score += 1
        return score
    
    def calculate_scores(self):
        self.df["anomaly_score"] = self.df.apply(self._score, axis=1)
        self.df["refined_flag"] = self.df["anomaly_score"].apply(lambda x: 1 if x >= 2 else 0)
    
    def evaluate(self):
        cm = confusion_matrix(self.df["actual"], self.df["refined_flag"])
        precision = precision_score(self.df["actual"], self.df["refined_flag"])
        return cm, precision
    
    def run(self):
        self.calculate_scores()
        cm, precision = self.evaluate()
        print("Confusion Matrix:\n", cm)
        print(f"Precision: {precision:.2f}")

if __name__ == "__main__":
    logs = [
        {"query": "SELECT", "latency": 120, "priv": 0, "time": "02:00", "flagged": 1, "actual": 0},
        {"query": "DROP TABLE", "latency": 80, "priv": 1, "time": "03:00", "flagged": 1, "actual": 0},
        {"query": "INSERT", "latency": 300, "priv": 0, "time": "11:00", "flagged": 0, "actual": 0},
        {"query": "SELECT + SLEEP(5)", "latency": 5000, "priv": 1, "time": "01:00", "flagged": 1, "actual": 1},
        {"query": "SELECT", "latency": 100, "priv": 0, "time": "02:00", "flagged": 1, "actual": 0},
    ]
    detector = AnomalyScoreDetection(logs)
    detector.run()
