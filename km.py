import numpy as np
from sklearn.datasets import load_iris
import time

class KMeans:
    def __init__(self, k, max_iter=100):
        self.k = k#số cụm
        self.max_iter = max_iter#số lần lặp max
        self.centroids = None#toạ độ
        self.labels = None#nhãn cụm
    def fit(self, data):
        self.centroids = self.init_centroids(data)#khởi tạo tâm cụm ngẫu nhiên từ dl
        for _ in range(self.max_iter):
            self.labels = self.assign_labels(data)#gán nhãn cho mỗi điểm dl
            new_centroids = self.update_centroids(data)#update tâm cụm
            self.centroids = new_centroids
    #chọn ngẫu nhiên k điểm để làm tâm cụm ban đầu 
    def init_centroids(self, data):
        np.random.seed(0)
        random_indices = np.random.choice(data.shape[0], self.k, replace=False)
        return data[random_indices]
    def assign_labels(self, data):#gán nhãn
        labels = []
        for point in data:#kc ơ cờ lít giữa các điểm và tâm cụm
            distances = np.linalg.norm(point - self.centroids, axis=1)
            labels.append(np.argmin(distances))#chọn tâm cụm
        return np.array(labels)
    def update_centroids(self, data):#cập nhật kiểm tra lại tâm cụm
        new_centroids = np.zeros((self.k, data.shape[1]))
        for i in range(self.k):
            points_in_cluster = data[self.labels == i]
            new_centroids[i] = points_in_cluster.mean(axis=0)#cập nhật bằng cách tính tbc các điểm 1 cụm
        return new_centroids
    def get_centroids(self):
        return self.centroids#lấy tâm cụm hiện tại
    def get_labels(self):
        return self.labels#lấy nhãn hiện tại
start_time=time.time()#tg bắt đầu
if __name__ == "__main__":
    iris = load_iris()
    data = iris.data
    labels = iris.target
    kmeans = KMeans(k=3)
    kmeans.fit(data)
    print("Centroids(tọa độ tâm cụm):")
    print(kmeans.get_centroids())
    print("\nPhân cụm 150 điểm dữ liệu:")
    print(kmeans.get_labels())
    end_time=time.time()#tg kết thúc
    print(f'Time run: {end_time - start_time:.5f}s')
