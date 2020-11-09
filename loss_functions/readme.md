# Loss functions

Various built-in loss functions and their usage. Also documents the process of creating a user-defined loss function.

---

## Importing them

All loss functions are in ```torch.nn```. So, import using

```python
import torch.nn as nn
```

---

## Regression losses

The output is a continuous variable with no bounds.

### L1 loss

Mean absolute loss. i.e, sum of absolute errors between the prediction and the actual output.

```python
loss = nn.L1Loss(reduction = 'mean')
loss_val = loss(prediction, label)
```

- reduction specifies how the losses of individual elements in a mini-batch is reduced.
  - ```none``` : No reduction - each element has its own loss
  - ```sum``` : Sums the losses of individual elements
  - ```mean``` : Averages the losses of individual elements

### MSE loss

**Mean square error loss**. i.e, the mean of the square of error between prediction and actual output. It is the squared L2 norm.

```python
loss = nn.MSE(reduction = 'mean')
loss_val = loss(prediction, label)
```

### 

---

## Classification losses

The output is a continous variable between two bounds, and the labelleed data is a discrete variable that can take value of one of these two bounds.

---

## References

 1. [pytorch official documentation](https://pytorch.org/docs/stable/nn.html#loss-functions)