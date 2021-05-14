class Perceptron:
  def __init__ (self):
    self.w = None
    self.b = None

  def model(self, x):
    return 1 if (np.dot(self.w, x) >= self.b) else 0

  def predict(self, X):
    Y = []
    for x in X:
      result = self.model(x)
      Y.append(result)
    return np.array(Y)

  def fit(self, X, Y, epoc, learning_rate = 1):
    self.w = np.ones(X.shape[1])
    self.b = 0
    accuracy = []
    max_accuracy = 0
    max_accuracy_point = 0

    for i in range(epoc):
      for x, y in zip(X, Y):
        y_pred = self.model(x)
        if y == 1 and y_pred == 0:
          self.w = self.w + learning_rate * x
          self.b = self.b + learning_rate * 1
        elif y == 0 and y_pred == 1:
          self.w = self.w - learning_rate * x
          self.b = self.b - learning_rate * 1
      accuracy.append(accuracy_score(self.predict(X),  Y))
      if (accuracy[i] > max_accuracy):
        max_accuracy = accuracy[i]
        max_accuracy_point = i
        checkw = self.w
        checkb = self.b

    self.w = checkw
    self.b = checkb
    plt.plot(accuracy)
    plt.show()
    print("Max accuracy = ",max_accuracy)
    print("Max accuracy point = ",max_accuracy_point)
